# Programme Topic: Zoom Application using Python Prototype

# Registering to Zoom

user_name = input("Enter your name: ")
user_password = input("Enter your password: ")
print(f"Your account has been succesfully created! \nYour details are below: \nName: {user_name} \nPassowrd: {user_password}")
user_m_id = 1902372274
user_m_password = user_password
print(f"Your ZOOM MEETING ID is {user_m_id}")
print(f"Your ZOOM MEETING PASSWORD is {user_m_password}")

# Zoom Contacts Database

id_password_set = {
    "190902647": "hello_world",
    "928647393": "bye",
    user_m_id: user_m_password
}


print("\nWelcome to ZOOM")
print("*" * 125)

using = True
while using:
    print("1. Join Meeting \n2. Start Meeting \n3. Exit Application ")
    use = int(input("Enter what you want to use \n"))
    if use == 1:
        meeting_id = input("Enter meeting ID \n")
        if meeting_id in id_password_set.keys():
            meeting_password =  input("Enter meeting password \n")
            if meeting_password == id_password_set[meeting_id]:
                print("Meeting Joined!")
                exit = input("Press e to leave meeting\n").lower()
                if exit == "e":
                    print("Meeting Left!")
                else:
                    continue
            else:
                print("Invalid Meeting Password!")
                continue
        else:
            print("Sorry Invalid Meeting ID")
            continue
    elif use == 2:
        print("Meeting has been Started!")
        print(f"Meeting Details are below: \nMeeting ID: {user_m_id} \nMeeting Password: {user_m_password}")
        end = input("Press e to end the meeting").lower()
        if end == "e":
            print("Meeting has been ended!")
        else:
            continue
    elif use == 3:
        print("Thank You for using Zoom!\n")
        break