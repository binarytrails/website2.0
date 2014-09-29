from frontend.models import User, Skill

kedfilmsFounder = User.objects.get(nick = "kedfilms-founder")

"""
Delete all records
"""
Skill.objects.all().delete()

"""
Programming
"""
skill = Skill(
        title = "Python",
        category = "CS",
        subcategory = "P",
        owner = kedfilmsFounder,
        rating_on_five = 4,
        description = "Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C."
)
skill.save()
skill = Skill(
        title = "Java",
        category = "CS",
        subcategory = "P",
        owner = kedfilmsFounder,
        rating_on_five = 4,
        description = "It is intended to let application developers 'write once, run anywhere' (WORA), meaning that code that runs on one platform does not need to be recompiled to run on another."
)
skill.save()
skill = Skill(
        title = "C++",
        category = "CS",
        subcategory = "P",
        owner = kedfilmsFounder,
        rating_on_five = 3,
        description = ""
)
skill.save()
skill = Skill(
        title = "VB",
        category = "CS",
        subcategory = "P",
        owner = kedfilmsFounder,
        rating_on_five = 4,
        description = ""
)
skill.save()
skill = Skill(
        title = "Masm32",
        category = "CS",
        subcategory = "P",
        owner = kedfilmsFounder,
        rating_on_five = 2,
        description = ""
)
skill.save()

"""
Databases
"""
skill = Skill(
        title = "MySQL",
        category = "CS",
        subcategory = "DB",
        owner = kedfilmsFounder,
        rating_on_five = 4,
	    description = "MySQL was created by a Swedish company, MySQL AB, founded by David Axmark, Allan Larsson and Michael 'Monty' Widenius."
)
skill.save()

"""
Operative systems
"""
skill = Skill(
    title = "Debian",
    category = "CS",
    subcategory = "OS",
    owner = kedfilmsFounder,
    rating_on_five = 4,
    description = "Debian is an operating system which is composed primarily of free and open-source software, most of which is under the GNU General Public License, and developed by a group of individuals known as the Debian project."
)
skill.save()
