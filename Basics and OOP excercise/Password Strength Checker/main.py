class Requirments:


    def __init__(self,word):
        self.word=word
        self.upper_case = {"check": False, "message": "at least 1 uppercase letter"}
        self.lower_case = {"check": False, "message": "at least 1 lower case letter"}
        self.character_count = {"check": False, "message": "at least 8 characters"}
        self.special_character = {"check": False, "message": "at least 1 special character"}
        self.strength = 0

    def upper_case_check(self):
        for letter in self.word:
            if letter.isupper():
                self.upper_case["check"]=True
                self.strength+=1
                break

    def lower_case_check(self):
        for letter in self.word:
            if letter.islower():
                self.lower_case["check"]=True
                self.strength+=1
                break

    def character_count_check(self):
        if len(self.word)>=8:
            self.character_count["check"]=True
            self.strength+=1

    def special_character_check(self):
        for char in self.word:
            if not char.isalnum():  # Special = not a letter or number
                self.special_character["check"] = True
                self.strength += 1
                break











