task = input ( "Enter your task:" )
priority = input ( "Priority (high/medium/low):" )
time_bound = input ( "Is it time-bound? (yes/no):" )

match priority:
    case "high":
        if time_bound == "yes":
            reminder = (task + " is a high priority task that requires immediate attention today!")
            print('Reminder:',reminder)
        else:
            reminder = (task + " is a high priority task. Consider completing it when you have free time.")
            print('Note:',reminder)

    case "medium":
        if time_bound == "yes":
            reminder = (task + " is a medium priority task that requires immediate attention today!")
            print('Reminder:',reminder)
        else:
            reminder = (task + " is a medium priority task. Consider completing it when you have free time.")
            print('Note:',reminder)

    case "low":
        if time_bound == "yes":
            reminder = (task + " is a low priority task that requires immediate attention today!")
            print('Reminder:',reminder)
        else:
            reminder = (task + " is a low priority task. Consider completing it when you have free time.")
            print('Note:',reminder)

    case _:
        print("Invalid Selection")               
