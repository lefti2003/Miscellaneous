# Looks to see if a user is part of a group or not
# Shows the tree hierarchy

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' '*self.get_level()*3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.name)
        for user in self.users:
            print("User:" + prefix + user)
        if self.groups:
            for group in self.groups:
                group.print_tree()

    def add_group(self, group):
        group.parent = self
        self.groups.append(group)

    def add_user(self, user):
        #user.parent = self
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    if user != ' ':
        if user in group.get_users():
            return True
        else:
            for subgroup in group.get_groups():
                return is_user_in_group(user, subgroup)
        return False
    else:
        print("Not a valid user!")


parent = Group("IT")
desktop_support = Group("Desktop Support")
server_support = Group("Server Support")

parent.add_group(desktop_support)
parent.add_group(server_support)

tier1 = Group("Tier 1")
desktop_support.add_group(tier1)
tier1.add_user("Vinh N")
tier2 = Group("Tier 2")
desktop_support.add_group(tier2)
tier2.add_user("John Smith")
tier3 = Group("Tier 3")
desktop_support.add_group(tier3)


hardware = Group("Hardware")
server_support.add_group(hardware)
software = Group("Software")
server_support.add_group(software)

software_win = Group("Windows")
software_win.add_user("John Smith")
software_win.add_user("Jorge W")
software_win.add_user("El S")
software_linux = Group("Linux")
software_linux.add_user("Ashish P")

software.add_group(software_win)
software.add_group(software_linux)

# Directory tree created
# IT
#    |__Desktop Support
#       |__Tier 1
# User:      |__Vinh N
#       |__Tier 2
# User:      |__John Smith
#       |__Tier 3
#    |__Server Support
#       |__Hardware
#       |__Software
#          |__Windows
# User:         |__John Smith
# User:         |__Jorge W
# User:         |__El S
#          |__Linux
# User:         |__Ashish P
#



parent.print_tree()


possible_users = ["El S", "Alan W", "John Smith", "Vinh N", "Allison M", "Jorge W", "Ashish P"]

# Test 1
print("Test1")
for user in possible_users:
    print(f"Is User:{user} in Software Linux Group")
    if is_user_in_group(user, software_linux):
        print("True")
    else:
        print("False")
print("--"*36)
# Test1
# Is User:El S in Software Linux Group
# False
# Is User:Alan W in Software Linux Group
# False
# Is User:John Smith in Software Linux Group
# False
# Is User:Vinh N in Software Linux Group
# False
# Is User:Allison M in Software Linux Group
# False
# Is User:Jorge W in Software Linux Group
# False
# Is User:Ashish P in Software Linux Group
# True
#




# Test 2
print("Test2")
for user in possible_users:
    print(f"Is User:{user} in Software Windows Group")
    if is_user_in_group(user, software_win):
        print("True")
    else:
        print("False")
print("--"*36)
# Test2
# Is User:El S in Software Windows Group
# True
# Is User:Alan W in Software Windows Group
# False
# Is User:John Smith in Software Windows Group
# True
# Is User:Vinh N in Software Windows Group
# False
# Is User:Allison M in Software Windows Group
# False
# Is User:Jorge W in Software Windows Group
# True
# Is User:Ashish P in Software Windows Group
# False



# Test 3
print("Test3")
for user in possible_users:
    print(f"Is User:{user} in DeskTop Support Group")
    if is_user_in_group(user, desktop_support):
        print("True")
    else:
        print("False")

# Test3
# Is User:El S in DeskTop Support Group
# False
# Is User:Alan W in DeskTop Support Group
# False
# Is User:John Smith in DeskTop Support Group
# False
# Is User:Vinh N in DeskTop Support Group
# True
# Is User:Allison M in DeskTop Support Group
# False
# Is User:Jorge W in DeskTop Support Group
# False
# Is User:Ashish P in DeskTop Support Group
# False

# Test 4
print("Test4")
possible_users = [" "]
for user in possible_users:
    print(f"Is User:{user} in DeskTop Support Group")
    if is_user_in_group(user, desktop_support):
        print("True")
    else:
        print("False")
# Test4
# Is User:  in DeskTop Support Group
# Not a valid user!
# False
#

# Test 5
print("Test5")
possible_users = ["Steve M"]
for user in possible_users:
    print(f"Is User:{user} in Group (IT)")
    if is_user_in_group(user, parent):
        print("True")
    else:
        print("False")
# Test5
# Is User:Steve M in Group (IT)
# False
#


