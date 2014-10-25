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
    staticfilepath = "img/portfolio/absinthe.jpg",
    fragment_identifier = "absinthe",
    title = "Absinthe",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2012, 03, 14),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/alien_on_road.jpg",
    fragment_identifier = "alien_on_road",
    title = "Welcome, space being.",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 9, 19),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/autumn.jpg",
    fragment_identifier = "autumn",
    title = "Autumn",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2013, 10, 15),
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
    staticfilepath = "img/portfolio/beate.jpg",
    fragment_identifier = "beate",
    title = "Béate",
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
photo = Photo(
    staticfilepath = "img/portfolio/flying_me.jpg",
    fragment_identifier = "flying_me",
    title = "Flying is a reality",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2014, 03, 15),
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
    staticfilepath = "img/portfolio/hidden_nature.jpg",
    fragment_identifier = "hidden_nature",
    title = "Hidden Nature",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "iPhone",
    application = "Adobe After Effect",
    date_created = date(2013, 6, 12),
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
    staticfilepath = "img/portfolio/led_jump.jpg",
    fragment_identifier = "night_jump",
    title = "Night Jump",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 9, 27),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/led_kitchen.jpg",
    fragment_identifier = "mage_kitchen",
    title = "Mage Kitchen",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 9, 27),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/leg_on_fire.jpg",
    fragment_identifier = "crawling_fire",
    title = "Crawling Fire",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 9, 27),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/long_shoot.jpg",
    fragment_identifier = "frames_evolution",
    title = "Frames Evolution",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "Adobe After Effect",
    date_created = date(2013, 8, 9),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/long_shoot_workspace.jpg",
    fragment_identifier = "virtualisation_creativity",
    title = "Virtualisation Creativity",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "Adobe After Effect",
    date_created = date(2013, 8, 9),
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
    staticfilepath = "img/portfolio/mindception.jpg",
    fragment_identifier = "mindception",
    title = "Mindception",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "Adobe After Effect",
    date_created = date(2013, 6, 19),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/purple_night.jpg",
    fragment_identifier = "purple_night",
    title = "Purple Night",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "Adobe After Effect",
    date_created = date(2013, 9, 18),
    owner = KEDFILMS_FOUNDER
)
photo.save()
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
    staticfilepath = "img/portfolio/sand_winter.jpg",
    fragment_identifier = "sandwinter",
    title = "Sandwinter",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "After Effect",
    date_created = date(2013, 12, 26),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/smoke_simulation.jpg",
    fragment_identifier = "smoke_simulation",
    title = "Smoke Simulation",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2013, 05, 16),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/spirit_driver.jpg",
    fragment_identifier = "spirit_driver",
    title = "Spirit Driver",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "Adobe After Effect",
    date_created = date(2013, 11, 25),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/tv-inception.jpg",
    fragment_identifier = "tv-inception",
    title = "Television Inception",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "Adobe After Effect",
    date_created = date(2012, 10, 13),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/wall_painting.jpg",
    fragment_identifier = "painting",
    title = "The Painting",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2013, 10, 01),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    staticfilepath = "img/portfolio/window_design.jpg",
    fragment_identifier = "window_design",
    title = "Window Design",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 10, 19),
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

"""
GN General
"""
photo = Photo(
    staticfilepath = "img/general/electric_teeth.jpg",
    fragment_identifier = "electric_teeth",
    title = "Electric teeth",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2014, 8, 15),
    owner = KEDFILMS_FOUNDER
)
photo.save()
