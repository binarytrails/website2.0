from datetime import date
from frontend.models import User, Photo

KEDFILMS_FOUNDER = User.objects.get(nick = "kedfilms-founder")

"""
Delete all records
"""
Photo.objects.filter(category = Photo.PF).delete()

"""
PF Portfolio
"""
photo = Photo(
    filename = "absinthe.jpg",
    fragment_identifier = "absinthe",
    title = "Absinthe",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "Adobe After Effect",
    date_created = date(2012, 03, 14),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "alien_on_road.jpg",
    fragment_identifier = "alien_on_road",
    title = "Alien On Road",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 9, 19),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "autumn.jpg",
    fragment_identifier = "autumn",
    title = "Autumn",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "Adobe After Effect",
    date_created = date(2013, 9, 15),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "barman.jpg",
    fragment_identifier = "barman",
    title = "Barman",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "Adobe After Effect",
    date_created = date(2012, 3, 15),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "beate.jpg",
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
    filename = "dj.jpg",
    fragment_identifier = "dj_vibes",
    title = "Dj Vibes",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "Adobe After Effect",
    date_created = date(2012, 9, 13),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "fake_fisheye.jpg",
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
    filename = "flying_me.jpg",
    fragment_identifier = "flying_me",
    title = "Flying is a reality",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2014, 03, 15),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "gandalf.jpg",
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
    filename = "hidden_nature.jpg",
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
    filename = "infected.jpg",
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
    filename = "led_jump.jpg",
    fragment_identifier = "night_jump",
    title = "Night Jump",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 8, 27),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "led_kitchen.jpg",
    fragment_identifier = "mage_kitchen",
    title = "Mage Kitchen",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 8, 27),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "leg_on_fire.jpg",
    fragment_identifier = "crawling_fire",
    title = "Crawling Fire",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 8, 27),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "long_shoot.jpg",
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
    filename = "long_shoot_workspace.jpg",
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
    filename = "melo_two_faces.jpg",
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
    filename = "mindception.jpg",
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
    filename = "purple_night.jpg",
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
    filename = "russian_standard.jpg",
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
    filename = "sand_winter.jpg",
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
    filename = "smoke_simulation.jpg",
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
    filename = "spirit_driver.jpg",
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
    filename = "theoule_sur_mer.jpg",
    fragment_identifier = "theoule_sur_mer",
    title = "Theoul Sur Mer",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2014, 8, 15),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "tv-inception.jpg",
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
    filename = "wall_painting.jpg",
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
    filename = "window_design.jpg",
    fragment_identifier = "window_design",
    title = "Window Design",
    author = "Seva Ivanov",
    category = Photo.PF,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 9, 19),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "zoomout.jpg",
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