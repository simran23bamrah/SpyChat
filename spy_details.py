from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.average = 0
        self.current_status_message = None


class Chat:
    def __init__(self,message,sent_by_me):
        self.message= message
        self.time=datetime.now()
        self.sent_by_me= sent_by_me



spy = Spy('Bond', 'Mr.', 24, 4.7)

friend_one = Spy('Black', 'Mr.',  21,4.9)
friend_two = Spy('Scarlette', 'Ms.', 20,5)
friend_three = Spy('Green', 'Dr.' ,19,5.1)


friends = [friend_one, friend_two, friend_three]