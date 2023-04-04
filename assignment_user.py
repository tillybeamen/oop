class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        # default attributes 
        is_rewards_member = False
        gold_card_points = 0


    def display_info(self):
        print(f"{self.first_name}")
        print(f"{self.last_name}")
        print(f"{self.email}")
        print(f"{self.age}")
        print(f"{self.is_rewards_member}")
        print(f"{self.gold_card_points}")
        
    def enroll(self, is_rewards_member, gold_card_points):
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
        if is_rewards_member:
            print("User already a member")
            return False
        else:
            return True

    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
    


tillman = User("Tillman", "Pugh", "till.pugh@gmail.com", 34)
tillman.enroll(True, 200)
tillman.spend_points(50)
tillman.display_info()


class User2:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        # default attributes 
        is_rewards_member = False
        gold_card_points = 0

    def display_info(self):
        print(f"{self.first_name}")
        print(f"{self.last_name}")
        print(f"{self.email}")
        print(f"{self.age}")
        print(f"{self.is_rewards_member}")
        print(f"{self.gold_card_points}")

    def enroll(self, is_rewards_member, gold_card_points):
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
        if is_rewards_member:
            print("User already a member")
            return False
        else:
            print("User has enrolled")
            return True
        
    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
    


tillman = User2("Clyde", "Pine", "clyde.pine@gmail.com", 84)
tillman.enroll(False, 200)
tillman.spend_points(80)
tillman.display_info()


class User3:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        # default attributes 
        is_rewards_member = False
        gold_card_points = 0

    def display_info(self):
        print(f"{self.first_name}")
        print(f"{self.last_name}")
        print(f"{self.email}")
        print(f"{self.age}")
        print(f"{self.is_rewards_member}")
        print(f"{self.gold_card_points}")

    def enroll(self, is_rewards_member, gold_card_points):
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
        if is_rewards_member:
            print("User already a member")
            return False
        else:
            return True
        
    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
    


tillman = User3("Gabe", "Quincy", "gabe.quincy@gmail.com", 14)
tillman.enroll(True, 200)
tillman.spend_points(50)
tillman.display_info()

