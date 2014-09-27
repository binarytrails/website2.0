from frontend.models import User, Section, Subsection

kedfilmsFounder = User.objects.get(nick = "kedfilms-founder")

"""
Delete all records
"""
Subsection.objects.all().delete()
Section.objects.all().delete()

"""
Section: Home
"""
section = Section(
    name = "Home",
    title = "Yours truly",
    subtitle = """
        I am a humanbeing, an amazing student & a freelancer.</br>
        Art & minutiae are transparent in my projects.</br>
        Opensource is a reality & Linux is a choice.</br>
    """,
    owner = kedfilmsFounder
)
section.save()
home = Section.objects.all().get(name = "Home")
"""
Subsections
"""
subsection = Subsection(
    name = "r&d",
    title = "R & D",
    body = """
        First line</br>
        Second line
    """,
    section = home
)
subsection.save()
subsection = Subsection(
    name = "photos",
    title = "Photography",
    body = """
        First line</br>
        Second line
    """,
    section = home
)
subsection.save()
subsection = Subsection(
    name = "videos",
    title = "Short Films",
    body = """
        First line</br>
        Second line
    """,
    section = home
)
subsection.save()
subsection = Subsection(
    name = "articles",
    title = "Articles",
    body = """
        First line</br>
        Second line
    """,
    section = home
)
subsection.save()
