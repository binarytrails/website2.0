from datetime import date
from frontend.models import User, Photo

KEDFILMS_FOUNDER = User.objects.get(nick = "kedfilms-founder")

"""
Delete all records
"""
Photo.objects.all().delete()

"""
PF Portfolio
"""
photo = Photo(
    staticfilepath = "img/portfolio/skyline-moq.jpg",
    title = "Skyline demonstration image",
    description = "Demonstration image",
    category = Photo.PF,
    author = "Internet",
    date_created = date(2099, 9, 06),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/stars-moq.jpg",
    title = "Stars demonstration image",
    description = "Demonstration image",
    category = Photo.PF,
    author = "Internet",
    date_created = date(2099, 9, 06),
    owner = KEDFILMS_FOUNDER
)
photo.save()
"""
GN General
"""
photo = Photo(
    staticfilepath = "img/general/jaded-moq.jpg",
    title = "Jaded - demonstration image",
    description = "Demonstration image",
    category = Photo.GN,
    author = "Internet",
    date_created = date(2099, 9, 06),
    owner = KEDFILMS_FOUNDER
)
photo.save()
