from frontend.models import User, Skill

kedfilmsFounder = User.objects.get(nick = "kedfilms-founder")

"""
Delete all records
"""
Skill.objects.all().delete()

"""
MD Methods of development
"""
skill = Skill(
        title = "Agile",
        category = Skill.MD,
        owner = kedfilmsFounder,
        rating_on_five = 5,
        description = ""
)
skill.save()
skill = Skill(
        title = "Object-oriented",
        category = Skill.MD,
        owner = kedfilmsFounder,
        rating_on_five = 5,
        description = ""
)
skill.save()

"""
PR Programming
"""
skill = Skill(
        title = "Python",
        category = Skill.PR,
        owner = kedfilmsFounder,
        rating_on_five = 5,
        description = "Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C."
)
skill.save()
skill = Skill(
        title = "Java",
        category = Skill.PR,
        owner = kedfilmsFounder,
        rating_on_five = 5,
        description = "It is intended to let application developers 'write once, run anywhere' (WORA), meaning that code that runs on one platform does not need to be recompiled to run on another."
)
skill.save()
skill = Skill(
        title = "C++",
        category = Skill.PR,
        owner = kedfilmsFounder,
        rating_on_five = 3,
        description = ""
)
skill.save()
skill = Skill(
        title = "VB",
        category = Skill.PR,
        owner = kedfilmsFounder,
        rating_on_five = 4,
        description = ""
)
skill.save()
skill = Skill(
        title = "C#",
        category = Skill.PR,
        owner = kedfilmsFounder,
        rating_on_five = 4,
        description = ""
)
skill.save()

"""
Databases
"""
skill = Skill(
        title = "MySQL",
        category = Skill.DB,
        owner = kedfilmsFounder,
        rating_on_five = 4,
	    description = "MySQL was created by a Swedish company, MySQL AB, founded by David Axmark, Allan Larsson and Michael 'Monty' Widenius."
)
skill.save()
skill = Skill(
        title = "PostgreSQL",
        category = Skill.DB,
        owner = kedfilmsFounder,
        rating_on_five = 4,
        description = ""
)
skill.save()
skill = Skill(
        title = "Oracle",
        category = Skill.DB,
        owner = kedfilmsFounder,
        rating_on_five = 4,
        description = ""
)
skill.save()
"""
ML Markup language
"""
skill = Skill(
        title = "HTML",
        category = Skill.ML,
        owner = kedfilmsFounder,
        rating_on_five = 5,
        description = ""
)
skill.save()
skill = Skill(
        title = "CSS",
        category = Skill.ML,
        owner = kedfilmsFounder,
        rating_on_five = 5,
        description = ""
)
skill.save()

"""
RC Revision control
"""
skill = Skill(
        title = "Git Hub",
        category = Skill.RC,
        owner = kedfilmsFounder,
        rating_on_five = 4,
        description = ""
)
skill.save()
skill = Skill(
        title = "SVN",
        category = Skill.RC,
        owner = kedfilmsFounder,
        rating_on_five = 3,
        description = ""
)
skill.save()

"""
FR Framework
"""
skill = Skill(
        title = "Django",
        category = Skill.FR,
        owner = kedfilmsFounder,
        rating_on_five = 4,
        description = ""
)
skill.save()
skill = Skill(
        title = "MVC .NET",
        category = Skill.FR,
        owner = kedfilmsFounder,
        rating_on_five = 4,
        description = ""
)
skill.save()

"""
SR Server
"""
skill = Skill(
        title = "Apache",
        category = Skill.SR,
        owner = kedfilmsFounder,
        rating_on_five = 4,
        description = ""
)
skill.save()
skill = Skill(
        title = "Nginx",
        category = Skill.SR,
        owner = kedfilmsFounder,
        rating_on_five = 4,
        description = ""
)
skill.save()
skill = Skill(
        title = "IIS",
        category = Skill.SR,
        owner = kedfilmsFounder,
        rating_on_five = 3,
        description = ""
)
skill.save()

"""
OS Operative systems
"""
skill = Skill(
    title = "Debian",
    category = Skill.OS,
    owner = kedfilmsFounder,
    rating_on_five = 5,
    description = "Debian is an operating system which is composed primarily of free and open-source software, most of which is under the GNU General Public License, and developed by a group of individuals known as the Debian project."
)
skill.save()
skill = Skill(
        title = "Ubuntu",
        category = Skill.OS,
        owner = kedfilmsFounder,
        rating_on_five = 4,
        description = ""
)
skill.save()
skill = Skill(
        title = "Arch Linux",
        category = Skill.OS,
        owner = kedfilmsFounder,
        rating_on_five = 3,
        description = ""
)
skill.save()
skill = Skill(
        title = "Windows 7",
        category = Skill.OS,
        owner = kedfilmsFounder,
        rating_on_five = 4,
        description = ""
)
skill.save()

"""
VA Visual arts
"""
skill = Skill(
        title = "Adobe after effect",
        category = Skill.VA,
        owner = kedfilmsFounder,
        rating_on_five = 5,
        description = ""
)
skill.save()
skill = Skill(
        title = "GIMP",
        category = Skill.VA,
        owner = kedfilmsFounder,
        rating_on_five = 3,
        description = ""
)
skill.save()
