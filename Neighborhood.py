from House import House

def get_neighbor(x, y):
    adjacent_houses = []
    if (x > 0):
        adjacent_houses.append((x - 1, y))
        print("1: " + str(adjacent_houses))
    if (x + 1) < 5:
        adjacent_houses.append((x + 1, y))
        print("2: " + str(adjacent_houses))
    if (y > 0):
        adjacent_houses.append((x, y - 1))
        print("3: " + str(adjacent_houses))
    if (y + 1) < 5:
        adjacent_houses.append((x, y + 1))
        print("4: " + str(adjacent_houses))
    return adjacent_houses


def average(x):
    return "The average candy of our neighbor: " + str(x / 25)


def get_location(l):
    m = -10000
    location = []
    for x in range(len(l)):
        for y in range(len(l[x])):
            if l[x][y].get_candy() > m:
                m = l[x][y].get_candy()
                location = (x, y)
    return location


def most_candy(l):
    m = -10000
    for x in range(len(l)):
        for y in range(len(l[x])):
            if l[x][y].get_candy() > m:
                m = l[x][y].get_candy()
    return m


def main():
    total_path = []
    total_candy = []

    matrix = [[], [], [], [], []]
    for h in matrix:
        for i in range(5):
            h.append(House())
    for l in matrix:
        print("[", end="")
        for house in l:
            print(house, end=",")
        print("]")
    print("\n")

    # highest candy of one house
    candy = most_candy(matrix)
    print("The highest candy can collected at 1 house is " + str(candy))
    total_candy.append(candy)
    x, y = get_location(matrix)
    sp = x, y  # location of house with most candy
    print("starting house is " + str(sp) + "\n")
    total_path.append(sp)

    n = int(input("How many houses you want to go through "))
    
    if n <= 25:
        for i in range(n-1):
            if n-1 < 25:
                candy_val = []
                neighbor_location = []
                your_neighbor = get_neighbor(x, y)  # list location of neighbors
                print("AAA " + str(your_neighbor))
                for i in range(len(your_neighbor)):
                    neighbor = your_neighbor[i]  # [(x, y), (x, y), (x, y)]
                    # print("n " + str(neighbor))
                    candy_val.append(matrix[neighbor[0]][neighbor[1]].get_candy())  # access the value of each location
                print("C " + str(candy_val))
                print("Path " + str(total_path))
                for i in range(len(your_neighbor)):
                    for i in your_neighbor:
                        if i in total_path:
                            your_neighbor.remove(i)
                            if len(your_neighbor) == 0:
                                print(your_neighbor)
                                print("stuck")
                                
                            if len(your_neighbor) > 0:
                                candy_val = []
                                for i in range(len(your_neighbor)):
                                    neighbor = your_neighbor[i]  # [(x, y), (x, y), (x, y)]
                                    candy_val.append(matrix[neighbor[0]][neighbor[1]].get_candy())  # access the value of each location
            
                            

            if len(your_neighbor) > 0:
                print("BBB " + str(your_neighbor))
                print("C " + str(candy_val))
                print("\n")
                
                highest_candy = max(candy_val)
                nei_location = (-1, -1)
                for i in range(len(your_neighbor)):
                    if candy_val[i] == highest_candy:
                        nei_location = your_neighbor[i]
                total_candy.append(highest_candy)
                x, y = nei_location
                new_location = (x, y)
                total_path.append(new_location)
                                  
                print("New location: " + str(new_location))
                print("Total path: " + str(total_path))
                print("Most candy = " + str(highest_candy))
                print("total candy: " + str(sum(total_candy)))
                print("\n")
                
                # calculate average candy of neighbor
                neighbor_average = 0
                for i in matrix:
                    for j in i:
                        neighbor_average += j.get_candy()

                # average candy of the neighborhood
                print(average(neighbor_average))
                print("Your average: " + str((sum(total_candy)) / (n)))
            else:
                print("stuck")
                break
    
        else:
            
              print("Our neighborhood do not have enough houses you want to go")


if __name__ == "__main__":
    main()
