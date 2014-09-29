from frontend.models import User

"""
Users
"""
user = User(
    nick = "kedfilms-founder",
    name = "Seva",
    lastname = "Ivanov",
    email = "m.seva.ivanov@gmail.com",
)
user.save()
