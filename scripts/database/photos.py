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
    title = "Béate",
    description = "Camera: Canon EOS REBEL T3i",
    category = Photo.GN,
    author = "Seva Ivanov",
    date_created = date(2014, 8, 15),
    owner = KEDFILMS_FOUNDER
)
photo.save()

