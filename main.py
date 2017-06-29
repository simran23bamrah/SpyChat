# Written by Simran
# Importing packages

import os
from spy_details import *
from steganography.steganography import Steganography
from datetime import datetime
import ntpath
from termcolor import colored



# Function checking validity of the entered spy name
def name_validation(name):
    name=name.strip()    # Strip space from begining and end of the string
    name1=name.split(" ")  # Spilt the string whenever space is encountered
    a=0
    b=0
    for i in name1: # Checking i in list name1
        if(i.isalpha()):  # Name1 should contain alphabets only
            a +=1
        else:
            b+=1
    if (b>0):
        return False  # False when there is number or any special char in name1
    elif(b==0):
        return True # True means there is no number or special char in name1


# Function checking validity of spy age
def age_validation():
    age = raw_input("Enter your age")
    if  age.isspace()==True and age.isdigit==False and len(age)==0 :
        print colored('Enter valid age','red')
    else:
        return age


# Function checking age of the friend
def friend_age_validation():

    age = raw_input("Enter friend's age")
    if  age.isspace()==True and age.isdigit==False and len(age)==0 :
        print colored('Enter valid age','red')
    else:
        return age     # Return age if no condition satisfied


# Function to check the rating values of the spy
def check_rating_value(rating):
    if (spy.rating) > 5:
        print colored('Enter rating between 1 to 5', 'red')
        return None
    elif (spy.rating) > 4.5 and (spy.rating) <= 5:
        print colored("Great ace!", 'green')
        return rating
    elif (spy.rating) > 3.5 and (spy.rating) <= 4.5:
        print colored("You are one of the good ones.", 'green')
        return rating
    elif (spy.rating) >= 2.5 and (spy.rating) <= 3.5:
        print colored("You can always do better.", 'green')
        return rating
    else:
        print colored("We can always use somebody to help in the office.", 'green')
        return rating


# Function checking the rating of the spy
def spy_rating_check():

    rating = raw_input("Enter Rating")
    if  rating.isspace()==True and rating.isdigit==False and len(rating)==0 :
        print colored("enter valid rating!","red")

    else:
        return rating


# Function to get the details of the new spy
def details():
    spy = Spy('', '', 0, 0.0)       # Object of Spy class created in spy_details.py file
    name = raw_input("Welcome! write your name!")
    spy.name = name
    if name_validation(spy.name):       # Calling name_validation function to check if the entered name is valid or not
        spy.salutation = raw_input("what do we call you 'MS.' or 'MR.' or 'DR.' or 'ER.'or 'MRS.'")

        if spy.salutation.upper() in list:        # Checking if the entered salutation lies in list or not
            spy.name = spy.salutation + " " + spy.name

            age=age_validation()        # Calling age validation function & see if correct age is entered or not
            try:
                spy.age= int(age)
            except ValueError:
                pass
            if spy.age > 12 and spy.age < 50:
                print colored("NOTE :) THE RATING SHOULD BE IN BETWEEN 1-5 ", "blue")
                rate = spy_rating_check()         # Calling spy_rating_check method to see if rating in between 1-5
                try:
                    spy.rating = float(rate)
                except ValueError:
                    pass
                ratee=check_rating_value(spy.rating)
                if ratee == None:                # Rate not valid then print error
                    print colored("Try again!:(","red")
                    start()
                else:
                    spy.is_online = True
                    print colored("Sucessfully registered", "green")
                    start_chat(spy)                      # Authorization complete. Now spy can go to start_chat function
            else:
                print colored("enter valid age","red")
                start()
        else:
            print colored("Enter valid salutation!", 'red')
            start()      # When salutation not valid calling start function n asking if you want to continue with old spy

    else:
        print colored("enter valid name", "red")
        start()      # When name not valid calling start function n asking if you want to continue with old spy


# Function to add a new status or to choose from the existing status
def add_status(current_status_message):

    updated_status_message = None
    if current_status_message != None:
        print colored('Your current status message is %s \n',"green") % (current_status_message)   # If there is current_status_message present then print the status
    else:
        print colored("No current status!","red")       # Print when no current status
    que = raw_input("Do you want to select from the older status (y/n)? ")   # Ask if spy want to update the old status or addd  new status
    if que.upper() == "N":      # Execute if spy entered "N"
        new_status_message = raw_input("What status message do you want to set? ") # Take new status as input from spy
        if len(new_status_message) > 0:     # Check if length of new status is more than 0
            STATUS_MESSAGE.append(new_status_message)
            updated_status_message = new_status_message     # Updating the status message
            print "your new status added is %s"%(updated_status_message)        # Print new status
    elif que.upper() == 'Y':         # Execute if spy enter "Y" that is spy want to get old status as updated current status
        item_position = 1
        for message in STATUS_MESSAGE:  # Checks the message status_message list
            print '%d. %s' % (item_position, message)       # Print old status in list
            item_position = item_position + 1
        message_selection = int(raw_input("\nChoose from the above messages "))
        if len(STATUS_MESSAGE) >= message_selection:        # True if length of list is greater than the mesggae selected by the spy
            updated_status_message = STATUS_MESSAGE[message_selection - 1]
            print colored("current status is %s","green") % updated_status_message  # Status updated
        else:
            print colored("You didn't choose the correct status","red")
    else:
        print colored('The option you chose is not valid! Press either Y or N.',"red")
    if updated_status_message:          # Check if curren message is true
        print colored('Your updated status message is: %s',"green") % (updated_status_message)  # Print updated message
    else:
        print colored('You don\'t have any current status update',"red")
    return updated_status_message     # return updated_status_message



# Function to add new friends to send secret messages
def add_friend():
    new_friend = Spy('','',0,0.0)       # Object of Spy class created in spy_details.py file

    new_friend.name = raw_input("Please add your friend's name: ")
    if name_validation(new_friend.name):        # Calling name_validation function to check if the entered name is valid or not
        new_friend.salutation= raw_input("What are they? MS. or MR. or DR. or ER. or MRS.? ")

        if new_friend.salutation.upper() in list:       # Checking if the entered salutation lies in list or not
            new_friend.name = new_friend.salutation + " " + new_friend.name
            age = friend_age_validation()  # Calling age validation functiion n see if correct age is entered or not
            try:
                new_friend.age = int(age)
            except ValueError:
                pass

            if new_friend.age>12  :   # Calling friend age validation functiion n see if correct age is entered or not
                print colored("NOTE Friend rating should be greater than spy rating","blue")
                rate = spy_rating_check()  # Calling spy_rating_check method to see if rating in between 1-5
                try:
                    new_friend.rating= float(rate)
                except ValueError:
                    pass
                ratee = check_rating_value(new_friend.rating)
                if ratee == None:

                    print colored("Try again!:(","red")
                    start()

                else:
                    if new_friend.rating >= spy.rating :            # If rating of friend added is more than rating of spy only  then the friend should be accepted
                        friends.append(new_friend)      # Append the new friend in friends list created in spy_details
                        print colored('Friend Added!',"green")
                    else:
                        print colored('Sorry! Invalid entry. We can\'t add spy with the details you provided',"red")   # Print when details of friend is not correct

            else:
                print colored("enter valid age of friend","red")   # Print when age of friend is not correct
        else:
            print colored("write salutation of friend","red")        # Print when salutation of friend is not in list
    else:
        print colored("enter valid name of friend!  ","red")         # Print when name of friend is not correct

    return len(friends)         # Returning the no of friends in friend list



# Function to select a friend to send secret message
def select_a_friend():
    item_number = 0
    for friend in friends:      # Fetching friends from friends list created in spy_details
        print '%d. %s aged %d with rating %.2f is online' % (item_number +1, friend.name, friend.age,friend.rating)
        item_number = item_number + 1

    friend_choice =( raw_input("Choose from your friends"))
    if len(friend_choice) >0 and friend_choice.isdigit() :      # Check if the length if friend choosen is greater than zero and it should be digit
        friend_choice=int(friend_choice)            # Converting string to int
        if friend_choice>0 and friend_choice< item_number+1:        # Check if the choosen friend lie in the list
            friend_choice_position = int(friend_choice) - 1         # Index of friend_choice stored in friend_choice_position
            return friend_choice_position       # Returned index
        else:
            print colored("Choose friends between (1 - %d)","red") %item_number # Tells that the friend choosen should be in between range
            return None
    else:
        print colored("Choose number between (1 - %d)","red") % item_number    # Tells that the friend choosen should be in between range
        return None



# Function to encode the secret message in image and send to the selected friend
def send_message():
    friend_choice = select_a_friend()       # Calling the select_a_friend() fucntion and getting the choosen friend
    if friend_choice==None:  # If wrong friend choosen then display try again
        print colored("Try again :(","blue")
    else:       # If correct friend choosen then else part run of this function

        original_image = raw_input("What is the name of the image?")     # Ask name of file
        if os.path.exists(original_image):  # If file exist in os then true
            output_path = "output.jpg"      # Giving the path to encoded image
            text = raw_input("What do you want to say? ")   # Getting msg to be send
            list=['SOS','SAVE ME','HELP ME!']   # Creating list for emergency msgs
            if text in list:    # Check if text entered is in list
                text= colored("Its an emergency.Reach me as soon as possible","red")
                Steganography.encode(original_image, output_path, text)     # Encoding the image with text
            if len(text)>0 and len(text)<100 and text.isspace()==False:  # Check if len of text between 1 to 100 and it shouldnt be only spaces
                Steganography.encode(original_image, output_path, text)  # Encoding the image with text
                new_chat= Chat(text,True)       # Calling Chat class
                friends[friend_choice].chats.append(new_chat)  # Appending in chats in friends list
                print colored("Your secret message image is ready!","green")
            else:
                if len(text)>100:  # Check if spy is talkitive by seeing if he speak more tha 100 words
                    print colored(" You are speaking alot! We are removing you from chat list","red")
                    del(friends[friend_choice])     # Delete the garrulous friend
        else:
            print colored("No such file present!","red")        # Print when file name dont exist



# Function used for reading the received secret message
def read_message():
    sender = select_a_friend()      # Calling the select_a_friend() fucntion and getting the choosen friend
    if sender==None:
        print colored("Try again :(","red")        # If wrong friend choosen then display try again
    else:           # If correct friend choosen then else part run of this function

        output_path = raw_input("What is the name of the file?")     # Ask name of file

        if os.path.isfile(output_path)==1:   # If given name is file in os then true
            secret_text = Steganography.decode(output_path)  # Decode the txt from image
            if len(secret_text)>0:      # If there is secret msg in image only then this if true
                new_chat= Chat(secret_text,False)   # Chat class called and secret text stored
                friends[sender].chats.append(new_chat)      # Append the message
                words = secret_text.split()
                friends[sender].average = (float(friends[sender].average * len(friends[sender].chats) + len(words))) / (len(friends[sender].chats) + 1)
                print colored("Average word count is: %.2f","blue") % (friends[sender].average)
                print colored("Your secret message has been saved!","green")    # Print when msg saved
            else:
                print colored("there is no secret message in this image","red") # Print when len of secret msg < 0
        else :
            print colored("No such file present !","red")   # Print when no file present  by the name given by spy


# Function to read chat history
def read_chat_history():
  read_for = select_a_friend()      # Calling the select_a_friend() fucntion and getting the choosen friend
  if read_for== None:
      print colored("Try again :(","red")          # If wrong friend choosen then display try again
  else:             # If correct friend choosen then else part run of this function
    if len(friends[read_for].chats)>0:      # Will work if there is any message in chats
      for chat in friends[read_for].chats:      # Fetcing chats from friends
        if chat.sent_by_me:         # Check if send_by_me is true
          print colored('[%s] %s %s',"blue") % (chat.time.strftime("%d %B %Y"), colored('You said:','red'), chat.message)     # Printing time and chat emssage send by you
        else:       #check if send_by_me is tru
          print colored('[%s] %s said: %s','blue') % (chat.time.strftime("%d %B %Y"), colored(friends[read_for].name,"red"), chat.message)      # Printing time and chat emssage send by spy



# Function to start the chat. It has menu options in it
def start_chat(spy):
    current_status_message=None
    spy.name= spy.salutation + " " + spy.name  # Concating the name of spy and its salutation into name
      # Age_validation fucntion is called to see id spy age is valid or not
    print "Authentication complete. Welcome " + spy.name + " age: " + str(spy.age) + " and rating of: " + str(spy.rating)  # Printing welcome message
    show_menu = True  # Taking a variable and setting it to true
    while show_menu:
        # Putting the menu item which we want to use in chatApp
        menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n "
        # Letting spy decide which menu item to choose
        menu_choice = raw_input(menu_choices)

        if len(menu_choice) > 0:        # If len of menu choice is greater than 0 then only it will work
            menu_choice = int(menu_choice)      # Converting the menu choice to int

            if menu_choice == 1:        # If menu choice is 1 then spy will be able to add or update status
                current_status_message = add_status(current_status_message)  #calling add_status function and adding or updating a status
            elif menu_choice == 2:            # If menu choice is 2 then spy will be able to add new friends
                number_of_friends = add_friend()       # Calling the add_friend() function and storing the no od freinds returned by function
                print 'Currently You have %d friends' % (number_of_friends)     # Prining no of friends
            elif menu_choice == 3:        # If menu choice is 3 then spy will be able to send encoded message
                send_message()          # Calling send_message() function
            elif menu_choice == 4:    # If menu choice is 4 then spy will be able to decrypt and read the encoded message
                 read_message()     # Calling read_message() function
            elif menu_choice ==5:    # If menu choice is 5 then spy will be able to read chat history
                 read_chat_history()        # Calling read_chat_history() fucntion
            elif menu_choice==6:          # If menu choice is 1 then spy will be able to exit application
                 show_menu = False          # Changing the value of show_menu from True to False
            else:
                print colored("Please enter a valid number from menu!","red")       #  Enter valid choice of menu



# Function to start the chat with the existing spy
def start():
    question = raw_input('do you want to continue as %s %s  ? Y/N' % (spy.salutation, spy.name))  # Asking if spy want to continue or he want to add new spy?
    if question.upper()=='Y':
        start_chat(spy)  # If spy want to continue then start_chat() function will be called to show menu of chatApp

    elif question.upper()=='N':
        details()       # If spy want to add new spy the details() is called and details of new spy is input in that function
    else:
        print colored("enter either Y or N! ","red")  # If spy enter anything except Y or N then it print this



STATUS_MESSAGE=['Available','Busy','At work']      # Listing containing initial status messages
list = ["Dr.", "Mr.", "Ms.","Mrs."]       # Storing salutations for spy in list
print colored('lets get started with the software of hidding text inside an image',"green")
start()  # Calling start function
