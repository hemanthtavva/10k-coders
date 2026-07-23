from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, user_id, name, phone, email, password):
        self.__user_id = user_id
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__password = password

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def set_name(self, name):
        self.__name = name

    def set_phone(self, phone):
        self.__phone = phone

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    def login(self, email, password):
        if self.__email == email and self.__password == password:
            print(f'Welcome {self.__name}')
            return True
        print('Invalid Email or Password')
        return False

    def logout(self):
        print(f'Thank You {self.__name}')

    @abstractmethod
    def display_profile(self):
        pass

class Customer(User):
    def __init__(self, user_id, name, phone, email, password, location):
        super().__init__(user_id, name, phone, email, password)
        self.__location = location


    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    # def display_profile(self):
    #     print("\n===== CUSTOMER PROFILE =====")
    #     print("ID      :", self.get_user_id())
    #     print("Name    :", self.get_name())
    #     print("Phone   :", self.get_phone())
    #     print("Email   :", self.get_email())
    #     print("Location:", self.__location)
    #     print("============================")

class restaurant_owner(User):
    def __init__(self, user_id, name, phone, email, password, restaurant):
        super().__init__(user_id, name, phone, email, password)
        self.__restaurant = restaurant

    def get_restaurant(self):
        return self.__restaurant

    def set_restaurant(self, restaurant):
        self.__restaurant = restaurant

    # def display_profile(self):
    #     print("\n===== RESTAURANT OWNER PROFILE =====")
    #     print("ID         :", self.get_user_id())
    #     print("Name       :", self.get_name())
    #     print("Phone      :", self.get_phone())
    #     print("Email      :", self.get_email())
    #     print("Restaurant :", self.__restaurant.get_name())
    #     print("============================")