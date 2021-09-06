# Exercise 1 = Family

class Family:
    def __init__(self, last_name: str, members=None):
        if members is None:
            members = [{"name": "", "age": 0, "gender": "Female", "is_child": True}]
        self.last_name = last_name
        self.members = [
            {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
            {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
        ]

    def born(self, **kwargs):
        print("Congratulations!")
        self.members.append(kwargs)

    def is_18(self, name):
        for i in self.members:
            if name in i["name"] and i["age"] > 18:
                return True
            else:
                return False

    def show_family(self):
        print(f"Printing all members of the {self.last_name} Family:")
        for i in self.members:
            print(i["name"])


jones = Family("Jones")
jones.born(name="Rick", age=1, gender="Male", is_child=True)
jones.show_family()


# Exercise 2 - TheIncredibles Family

class TheIncredibles(Family):
    def __init__(self, last_name: str, members=None):
        super().__init__(last_name, members)
        if members is None:
            members = [{"name": "", "age": 0, "gender": "Female", "is_child": True, "power": "", "incredible_name": ""}]

    def use_power(self, name):
        for item in self.members:
            if name in item["name"]:
                if not self.is_18(name):
                    raise Exception(f"{name} is not above 18 years old yet!")
                else:
                    print(f"{name}'s power is: {item['power']}")

    def incredible_presentation(self):
        print("The incredible names with their powers are:")
        for item in self.members:
            print(f"{item['incredible_name']}: {item['power']}")


the_incredibles = TheIncredibles("Incredibles", [{"name":"Incredible", "age": 30, "gender": "Male", "is_child": False, "power": "super-strength", "incredible_name": "Incredible"},
                                                 {"name":"Elastigirl", "age": 30, "gender": "Female", "is_child": False, "power": "Elasticity", "incredible_name": "Elastigirl"},
                                                 {"name":"Violet", "age": 30, "gender": "Female", "is_child": False, "power": "Invisibility", "incredible_name": "Invisible girl"}])
the_incredibles.use_power("Elastigirl")

