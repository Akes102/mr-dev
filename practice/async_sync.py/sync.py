import time #import the time module

def task(name): #create a function to capture duration of work
    print(f"Starting task {name}"#display the task start time)
    time.sleep(2)#pause for 2 seconds 
    print(f"Finished task {name}")#say the task ended

start_time = time.time()#
#this is the task that will be done
task("A")
task("B")
task("C")

end_time = time.time()#duration of task
#claculate duration
print("Total time:", end_time - start_time)