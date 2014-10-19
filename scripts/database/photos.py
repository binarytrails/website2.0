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
    staticfilepath = "img/portfolio/russian_standard.jpg",
    fragment_identifier = "russian_standard",
    title = "Russian standard",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2012, 12, 23),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/mindseption.jpg",
    fragment_identifier = "mindseption",
    title = "Mindseption",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "Adobe After Effect",
    date_created = date(2013, 6, 19),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/electric_teeth.jpg",
    fragment_identifier = "electric_teeth",
    title = "Electric teeth",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2014, 8, 15),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/dj.jpg",
    fragment_identifier = "street_vibes",
    title = "Street vibes",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "Adobe After Effect",
    date_created = date(2013, 9, 13),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/barman.jpg",
    fragment_identifier = "absinthe_elegance",
    title = "Absinthe elegance",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "Adobe After Effect",
    date_created = date(2012, 3, 15),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/gandalf.jpg",
    fragment_identifier = "gandalf",
    title = "Gandalf",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "Adobe After Effect",
    date_created = date(2012, 3, 16),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/infected.jpg",
    fragment_identifier = "infected",
    title = "Infected",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "Adobe After Effect",
    date_created = date(2012, 9, 22),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/melo_two_faces.jpg",
    fragment_identifier = "how_you_feel",
    title = "How you feel",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "Adobe After Effect",
    date_created = date(2013, 12, 24),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/zoomout.jpg",
    fragment_identifier = "enter_the_void",
    title = "If I... enter the void.",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2013, 9, 22),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/fake_fisheye.jpg",
    fragment_identifier = "wide_look",
    title = "Wide look",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "Adobe After Effect",
    date_created = date(2012, 9, 13),
    owner = KEDFILMS_FOUNDER
)
photo.save()

"""
GN General
"""
photo = Photo(
    staticfilepath = "img/general/beate.jpg",
    fragment_identifier = "beate",
    title = "Béate",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2014, 8, 15),
    owner = KEDFILMS_FOUNDER
)
photo.save()

