def max_footPath(binary_tree, count = 1):

    #Initialise list for all the counts
    counts = []

    #Loop through the tree
    while True:
        
        #If there are two children, add one to the count and go down both paths. 
        # If there is only one child, add one to the count and go down that path. 
        # If there are no children, add the count to the list of counts and break the loop
        if binary_tree.left != None and binary_tree.right != None:
            count += 1
            max_footPath(binary_tree.left, count)
            max_footPath(binary_tree.right, count)
        elif binary_tree.left != None:
            count += 1
            max_footPath(binary_tree.left, count)
        elif binary_tree.right != None:
            count += 1
            max_footPath(binary_tree.right, count)
        else:
            counts.append(count)
            break

    #Sort the counts
    counts.sort()

    #Return the highest count
    return counts[-1]

