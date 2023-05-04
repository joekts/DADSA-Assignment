class ClothesPriorityQueue:

    #Constructor
    def __init__(self):
        #Initialise list
        self.queue = []

    #Task 1
    def print_queue(self):
        print('| {:^15} | {:^15} | {:^15} | {:^15} |'.format("Priority", "CustomerName", "Task", "CompletionTime"))
        #Loop through queue
        for clothes in self.queue:
            #Putting the dictionary values in the format placeholders to make a neat table
            print('| {priority_number:^15} | {customer_name:^15} | {task:^15} | {completion_time:^15} |'.format(**clothes))

    #Task 2
    def print_count(self):
        #Initialise count dictionary
        count = {}

        #Loop through queue
        for clothes in self.queue:
            #Assign clothing items priority to variable
            priority = clothes["priority_number"]

            #If priority already exists in count dict, add one to it. If priority doesn't exist in dict default value is zero (+ 1) and priority is then added to dict with count of 1.
            count[priority] = count.get(priority, 0) + 1
        
        for priority in count.keys():
            print(priority, ": ", count[priority])

            
    #Task 3
    def next_task(self):
        #Create new Clothes priority queue
        list = ClothesPriorityQueue()

        #Find the next task and add it to this new queue
        next = self.queue[0]
        list.add_task(next["priority_number"], next["customer_name"], next["task"], next["completion_time"])

        #Use the existing print_queue function
        ClothesPriorityQueue.print_queue(list)

    #Task 4
    def next_tasks(self):
        #Create new Clothes priority queue
        list = ClothesPriorityQueue()

        #Find the next task and get its priority
        next = self.queue[0]
        priority = next["priority_number"]

        #Add every task to the new queue that is the highest priority
        for task in self.queue:
            if task["priority_number"] == priority:
                list.add_task(task["priority_number"], task["customer_name"], task["task"], task["completion_time"])

        #Use the existing print_queue function
        ClothesPriorityQueue.print_queue(list)
        
    #Task 5
    def finish_task(self):
        #Removes first item
        self.queue.pop(0)

    #Task 6
    def add_task(self, priority_number, customer_name, task_desc, completion_time):

        #Initialise pointer
        pointer = 0

        #Loop through list, finding the point of insertion for the new task
        for index, task in enumerate(self.queue):

            if(priority_number < task["priority_number"]):
                break
            elif(priority_number >= task["priority_number"]):
                pointer = index + 1
            
        self.queue.insert(pointer, {"priority_number": priority_number, "customer_name": customer_name, "task": task_desc, "completion_time": completion_time})

    #Task 7
    def change_priority(self, name, new_priority):

        #Initialise pointer
        pointer = None

        #Loop through list and find the index of the customers task
        for index, task in enumerate(self.queue):
            if task["customer_name"].lower() == name.lower():
                pointer = index

        #Validation for if the customer has been found
        if(pointer == None):
            return print("This customer does not exist")

        #Create a placeholder and change its priority to the new priority
        holder = self.queue[pointer]
        holder["priority_number"] = new_priority

        #Remove the task with the old priority
        self.queue.pop(pointer)

        #Add the task with the new priority
        ClothesPriorityQueue.add_task(self, holder["priority_number"], holder["customer_name"], holder["task"], holder["completion_time"])

    #Task 8
    def delete_task(self, name):

        #Initialise pointer
        pointer = None

        #Loop through list and find the index of the customers task
        for index, task in enumerate(self.queue):
            if task["customer_name"].lower() == name.lower():
                pointer = index

        #Validation for if the customer has been found
        if(pointer == None):
            return print("This customer does not exist")

        #Remove task
        self.queue.pop(pointer)

    #Task 9
    def rearrange_priorities(self):
        #Initialise list for all the priorities
        priorities = []

        #Add priority of each task to the list
        for task in self.queue:
            priorities.append(task["priority_number"])

        #Make the list unique, now the index of each priority in the list will be its new priority
        priorities = set(priorities)

        #Loop through priorities keeping track of the index
        for index, priority in enumerate(priorities):

            #Loop through each task
            for task in self.queue:

                #If the task matches the current priority in the priorities list change its priority
                if task["priority_number"] == priority:
                    task["priority_number"] = index



    




    





clothes = ClothesPriorityQueue()

clothes.add_task(3, "Omar", "Hemming Pants", 3)
clothes.add_task(3, "lily", "Shorten dress", 2)
clothes.add_task(1, "Sam", "Fix zipper", 4)
clothes.add_task(1, "Ollie", "Fix zipper", 3)
clothes.add_task(4, "Cunt", "Fix zipper", 4)
clothes.add_task(2, "NIgel", "Fix zipper", 9)
clothes.print_queue()
clothes.change_priority("cunt", 9)
clothes.print_queue()
clothes.rearrange_priorities()
clothes.print_queue()

#print(clothes.highest_priority())




