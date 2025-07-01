class Requirments:
    def __init__(self, word):
        self.word = word
        self.upper_case = {"check": False, "message": "at least 1 uppercase letter"}
        self.lower_case = {"check": False, "message": "at least 1 lowercase letter"}
        self.character_count = {"check": False, "message": "at least 8 characters"}
        self.special_character = {"check": False, "message": "at least 1 special character"}
        self.strength = 0
        self.failed_tests = []

    def upper_case_check(self):
        if any(letter.isupper() for letter in self.word):
            self.upper_case["check"] = True
            self.strength += 1
        else:
            self.failed_tests.append(self.upper_case["message"])

    def lower_case_check(self):
        if any(letter.islower() for letter in self.word):
            self.lower_case["check"] = True
            self.strength += 1
        else:
            self.failed_tests.append(self.lower_case["message"])

    def character_count_check(self):
        if len(self.word) >= 8:
            self.character_count["check"] = True
            self.strength += 1
        else:
            self.failed_tests.append(self.character_count["message"])

    def special_character_check(self):
        if any(not char.isalnum() for char in self.word):
            self.special_character["check"] = True
            self.strength += 1
        else:
            self.failed_tests.append(self.special_character["message"])

    def run_all_tests(self):
        self.lower_case_check()
        self.upper_case_check()
        self.character_count_check()
        self.special_character_check()

        print(f"\nPassword strength: {self.strength}/4")

        if self.failed_tests:
            print("Missing:")
            for test in self.failed_tests:
                print(f"- {test}")
        else:
            print("Password meets all requirements!")


password = input("Enter your password: ")
requirements = Requirments(password)
requirements.run_all_tests()
