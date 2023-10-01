import random
 
class House:
 
    def __init__(self):
        self.rating = random.randint(1,10)
 
    def getRating(self):
        return self.rating
 
   
def greedyPath(m, num):
    bestHouses = []
    houses = []
    coords = []
    for i in range(5):
        for j in range(5):
            houses.append(m[i][j])
            coords.append([i,j])
    for i in range (25):
        maxHval=0
        maxHcoord=[0,0]
        for pos in range(len(houses)):
            if houses[pos] > maxHval:
                maxHval=houses[pos]
                maxHcoord= coords[pos]
 
 
 
        bestHouses.append(maxHcoord)
        houses.remove(maxHval)
        coords.remove(maxHcoord)
 
 
    for i in range(0, len(bestHouses)):
        p = []
 
 
 
 
        start = bestHouses[i]
        x=start[0]
        y=start[1]
        pVal=m[x][y]
        p.append(start)
       
 
 
        #add neighbors to the path after comparing to see which neighbor is best
        for i in range(num-1):
 
            bad = []
 
            neighbors=[[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
            for n in neighbors:
                if (n[0]>4) or (n[0] < 0):
                    bad.append(n)
                elif (n[1]>4) or (n[1] < 0):
                    bad.append(n)
                if n in p:
                    bad.append(n)
 
                   
            for b in bad:
                neighbors.remove(b)
           
                if len(neighbors) == 0:
                    break
 
            toBreak = False
            for h in bestHouses:
                if toBreak:
                    break
                for n in neighbors:
                    if n == h:
                        nextHouse = n
                        toBreak = True
                        break
           
               
 
           
            
            p.append(nextHouse)
            x=nextHouse[0]
            y=nextHouse[1]
            pVal=pVal+m[x][y]
           
        
 
 
 
        return pVal, p
    return 0, [[0,0]]
 
def randPath(m, num):
    #create an empty path
    p = []
 
    #try to add coordinates to the path
    #if the path were to get stuck or be 'unfinished' in anyway, try again
    #only finish once a fair path is generated
    while (len(p) < num):
        p = []
       
 
        #keep track of the value of the path
        #choose a random coordinate to start at
 
        x = random.randint(0,4)
        y = random.randint(0,4)
        p.append([x,y])
 
           
        pVal=m[x][y]
 
       
 
        #add neighbors to the path at a randomly chosen direction
        #keep track of whether we get stuck. If we get stuck, break
        #print(p)
        for i in range(num - 1):
            bad = []
 
            neighbors=[[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
            for n in neighbors:
                if (n[0]>4) or (n[0] < 0):
                    bad.append(n)
                elif (n[1]>4) or (n[1] < 0):
                    bad.append(n)
                if n in p:
                    bad.append(n)
            #print(bad)
            #print(neighbors)
            for b in bad:
                neighbors.remove(b)
           
                if len(neighbors) == 0:
                    break
 
            for h in bestHouses:
                for n in neighbors:
                    if n == h:
                        nextHouse = n
                        break
           
               
 
           
            
            p.append(nextHouse)
            x=nextHouse[0]
            y=nextHouse[1]
            pVal=pVal+m[x][y]
           
            
                #choose a random direction and attempt to add the neighbor
                #do not add the neighbor to the path if it is outside of the 5x5
                #or if the neighbor is already in the path
                #break the while loop if it was a successful addition or if stuck
               
        return pVal, p
                       
                
  
def main():
    m = [[], [], [], [], []]
    for l in m:
        for i in range(5):
            h = House()
            l.append(h.getRating())
 
    for i in range(5):
        print(m[0][i], m[1][i], m[2][i], m[3][i], m[4][i])
 
 
    num = int(input("How many houses?\n"))
 
 
 
    total=0
    for i in range(5):
        for j in range(5):
            total = total+m[i][j]
    average=total/25
   
    ''' Greedy Path Call '''
    pVal, p = greedyPath(m, num)
 
    print(p)
    print("The average value of the houses is "+str(average))
    print("The average value of your route is "+str(pVal/num))
   
    '''
     Random Path Call
    #calculate the average rating of a house in the neighborhood
    total=0
    for i in range(5):
        for j in range(5):
            total = total+m[i][j]
    average=total/25
    #while the average of value of the house is greater than the
    #average of the path randomly chosen, try getting another random
    #path. stop, once it is better, and print it.
 
    pVal,p = randPath(m,num)
    while (average > pVal/num):
        pVal,p = randPath(m,num)
 
    print(p)
    print("The average value of the houses is "+str(average))
    print("The average value of your route is "+str(pVal/num))
    '''
           
 
       
 
if __name__ == "__main__":
    main()
 
