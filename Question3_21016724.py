def max_footPath(self, count = 1):

    #Initialise list for all the counts
    counts = []

    #Loop through the tree
    while True:
        
        #If there are two children, add one to the count and go down both paths. 
        # If there is only one child, add one to the count and go down that path. 
        # If there are no children, add the count to the list of counts and break the loop
        if self.left != None and self.right != None:
            count += 1
            max_footPath(self.left, count)
            max_footPath(self.right, count)
        elif self.left != None:
            count += 1
            max_footPath(self.left, count)
        elif self.right != None:
            count += 1
            max_footPath(self.right, count)
        else:
            counts.append(count)
            break

    #Sort the counts
    counts.sort()

    #Return the highest count
    return counts[-1]

