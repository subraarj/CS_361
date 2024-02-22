The microservice is named reminder.py. You can run the microservice in the terminal by using the command: python3 reminder.py
You can request data from the microservice once it's run by writing information into the text file "list_of_reminders.txt". You must enter task information in the following format with one task per row: {task name} | {year/month/day task is due}
Here is an example call: write "2/21 | 2024-02-21" into the file "list_of_reminders.txt".
To recieve the data from the microservice simply moniter the file reminder.txt, which will contain the names of the tasks that are due today.

UML Diagram:
Notes:
- The Program must input tasks and date in the format {task name} | {year/month/day task is due} into "list_of_reminders.txt"
- In the Reminder Microservice moniter_file() will both moniter list_of_reminders.txt and write to reminder.txt
- reminder.txt will have due tasks names in the format of one task name per line of the text file

Program making a request                      list_of_reminders.txt                          Reminder Microservice                                reminder.txt 
    ||  write "{task name} | {date}" to file            |                         (loop) moniter_file()  ||  moniter_file() writes "{task name}" to file |                         
    || -------------------------------------------->    |  <-------------------------------------------  ||  ------------------------------------->      |            
    ||                                                  |                                                ||                                              |                     
    ||  (loop) check file for task names                |                                                ||                                              |           
    ||  ------------------------------------------------------------------------------------------------------------------------------------------->     |            
    ||                                                  |                                                ||                                              |                                      
    ||                                                  |                                                ||                                              |   
    ||                                                  |                                                ||                                              |                                      
    ||                                                  |                                                ||                                              |          
    ||                                                  |                                                ||                                              |          
