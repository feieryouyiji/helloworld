"""
  Multiple return values
"""


def profile():
    global name
    global age
    name = "Danny"
    age = 30


profile()
print(name)
# Output: Danny

print(age)
# Output: 30


"""
  Advanced you should return a tuple
"""


def profile_advanced():
    return ('Danny', 30)