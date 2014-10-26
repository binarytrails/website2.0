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
    filename = "skyline-moq.jpg",
    fragment_identifier = "skyline",
    title = "Skyline demonstration image",
    author = "Internet",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "Adobe After Effect",
    date_created = date(2099, 9, 06),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "stars-moq.jpg",
    fragment_identifier = "stars",
    title = "Stars demonstration image",
    author = "Internet",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "Adobe After Effect",
    date_created = date(2099, 9, 06),
    owner = KEDFILMS_FOUNDER
)
photo.save()
"""
GN General
"""
photo = Photo(
    filename = "jaded-moq.jpg",
    fragment_identifier = "jaded",
    title = "Jaded - demonstration image",
    author = "Internet",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "Adobe After Effect",
    date_created = date(2099, 9, 06),
    owner = KEDFILMS_FOUNDER
)
photo.save()
