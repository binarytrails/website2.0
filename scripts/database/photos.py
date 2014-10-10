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
    description = "Camera: Canon EOS REBEL T3i",
    category = Photo.PF,
    author = "Seva Ivanov",
    date_created = date(2012, 12, 23),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/mindseption.jpg",
    fragment_identifier = "mindseption",
    title = "Mindseption",
    description = "Camera: Canon EOS REBEL T3i; SFX: After Effect CS6",
    category = Photo.PF,
    author = "Seva Ivanov",
    date_created = date(2013, 6, 19),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/electric_teeth.jpg",
    fragment_identifier = "electric_teeth",
    title = "Electric teeth",
    description = "Camera: Canon EOS REBEL T3i;",
    category = Photo.PF,
    author = "Seva Ivanov",
    date_created = date(2014, 8, 15),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/dj.jpg",
    fragment_identifier = "street_vibes",
    title = "Street vibes",
    description = "Camera: Canon EOS REBEL T3i; SFX: After Effect CS6",
    category = Photo.PF,
    author = "Seva Ivanov",
    date_created = date(2013, 9, 13),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/barman.jpg",
    fragment_identifier = "absinthe_elegance",
    title = "Absinthe elegance",
    description = "Camera: Canon EOS REBEL T3i; SFX: After Effect CS6",
    category = Photo.PF,
    author = "Seva Ivanov",
    date_created = date(2012, 3, 15),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/gandalf.jpg",
    fragment_identifier = "gandalf",
    title = "Gandalf",
    description = "Camera: Canon EOS REBEL T3i; SFX: After Effect CS6",
    category = Photo.PF,
    author = "Seva Ivanov",
    date_created = date(2012, 3, 16),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/infected.jpg",
    fragment_identifier = "infected",
    title = "Infected",
    description = "Camera: Canon EOS REBEL T3i; SFX: After Effect CS6",
    category = Photo.PF,
    author = "Seva Ivanov",
    date_created = date(2012, 9, 22),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/melo_two_faces.jpg",
    fragment_identifier = "how_you_feel",
    title = "How you feel",
    description = "Camera: Canon EOS REBEL T3i; SFX: After Effect CS6",
    category = Photo.PF,
    author = "Seva Ivanov",
    date_created = date(2013, 12, 24),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/zoomout.jpg",
    fragment_identifier = "enter_the_void",
    title = "If I... enter the void.",
    description = "Camera: Canon EOS REBEL T3i; SFX: After Effect CS6",
    category = Photo.PF,
    author = "Seva Ivanov",
    date_created = date(2013, 9, 22),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/fake_fisheye.jpg",
    fragment_identifier = "wide_look",
    title = "Wide look",
    description = "Camera: Canon EOS REBEL T3i; SFX: After Effect CS6",
    category = Photo.PF,
    author = "Seva Ivanov",
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
    description = "Camera: Canon EOS REBEL T3i",
    category = Photo.GN,
    author = "Seva Ivanov",
    date_created = date(2014, 8, 15),
    owner = KEDFILMS_FOUNDER
)
photo.save()

