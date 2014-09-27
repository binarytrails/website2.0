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
    filename = "russian_standard.jpg",
    title = "Russian standard",
    description = "Camera: Canon EOS REBEL T3i",
    category = "PF",
    author = "Seva Ivanov",
    date_created = date(2012, 12, 23),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "mindseption.jpg",
    title = "Mindseption",
    description = "Camera: Canon EOS REBEL T3i; SFX: After Effect CS6",
    category = "PF",
    author = "Seva Ivanov",
    date_created = date(2013, 6, 19),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "electric_teeth.jpg",
    title = "Electric teeth",
    description = "Camera: Canon EOS REBEL T3i;",
    category = "PF",
    author = "Seva Ivanov",
    date_created = date(2014, 15, 8)
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "dj.jpg",
    title = "Street vibes",
    description = "Camera: Canon EOS REBEL T3i; SFX: After Effect CS6",
    category = "PF",
    author = "Seva Ivanov",
    date_created = date(2013, 13, 9),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "barman.jpg",
    title = "Absinthe elegance",
    description = "Camera: Canon EOS REBEL T3i; SFX: After Effect CS6",
    category = "PF",
    author = "Seva Ivanov",
    date_created = date(2012, 15, 3),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "gandalf.jpg",
    title = "Gandalf",
    description = "Camera: Canon EOS REBEL T3i; SFX: After Effect CS6",
    category = "PF",
    author = "Seva Ivanov",
    date_created = date(2012, 3, 16),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "infected.jpg",
    title = "Infected",
    description = "Camera: Canon EOS REBEL T3i; SFX: After Effect CS6",
    category = "PF",
    author = "Seva Ivanov",
    date_created = date(2012, 9, 22),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "melo_two_faces.jpg",
    title = "How you feel",
    description = "Camera: Canon EOS REBEL T3i; SFX: After Effect CS6",
    category = "PF",
    author = "Seva Ivanov",
    date_created = date(2013, 12, 24),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "zoomout.jpg",
    title = "If I... enter the void.",
    description = "Camera: Canon EOS REBEL T3i; SFX: After Effect CS6",
    category = "PF",
    author = "Seva Ivanov",
    date_created = date(2013, 9, 22),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "fake_fisheye.jpg",
    title = "Wide look",
    description = "Camera: Canon EOS REBEL T3i; SFX: After Effect CS6",
    category = "PF",
    author = "Seva Ivanov",
    date_created = date(2012, 9, 13),
    owner = KEDFILMS_FOUNDER
)
photo.save()

"""
GN General
"""
photo = Photo(
    filename = "beate.jpg",
    title = "Béate",
    description = "Camera: Canon EOS REBEL T3i",
    category = "GN",
    author = "Seva Ivanov",
    date_created = date(2014, 8, 15),
    owner = KEDFILMS_FOUNDER
)
photo.save()

