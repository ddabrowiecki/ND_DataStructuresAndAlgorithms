class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = set()
        self.users = set()

    def add_group(self, group):
        self.groups.add(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

# Inspired to use sets due to this mentor help post https://knowledge.udacity.com/questions/224129
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    for group in group.get_groups():
        if user in group.get_users():
            return True
        else:
            return False


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

fishing = Group("fishing")
trout_fishing = Group("trout fishing")

tf_1 = "Mark Johns"
trout_fishing.add_user(tf_1)

fishing.add_group(trout_fishing)

assert is_user_in_group(tf_1, fishing) == True

# Test Case 2

sf_1 = "David Jacobs"
salmon_fishing = Group("salmon fishing")
salmon_fishing.add_user(sf_1)

assert is_user_in_group(sf_1, fishing) == False

# Test Case 3
sea_fishing = Group("sea_fishing")
sea_fishing.add_user("Martin Michaels")
fishing.add_group(sea_fishing)

assert is_user_in_group("Martin Michaels", fishing) == True