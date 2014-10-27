from datetime import date
from frontend.models import User, Photo

KEDFILMS_FOUNDER = User.objects.get(nick = "kedfilms-founder")

"""
Delete all records
"""
Photo.objects.filter(category = Photo.GN).delete()

"""
GN General
"""
photo = Photo(
    filename = "bboy_freeze.jpg",
    fragment_identifier = "creative_concept",
    title = "Creative Concept",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2014, 03, 15),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "bboy_freeze2.jpg",
    fragment_identifier = "hollow_back",
    title = "Hollow Back",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 10, 11),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "bitch_please.jpg",
    fragment_identifier = "honey_please",
    title = "Honey Please",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2012, 9, 22),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "butterfly.jpg",
    fragment_identifier = "green_butterfly",
    title = "Green Butterfly",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2014, 8, 11),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "cancun_cars.jpg",
    fragment_identifier = "cancun_cars",
    title = "Cancun Cars",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2012, 12, 22),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "cancun_escape.jpg",
    fragment_identifier = "mayas_escape",
    title = "The Great Mayas Escape",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2012, 12, 25),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "cancun_market.jpg",
    fragment_identifier = "cacun_market",
    title = "Cancun Street Market",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2012, 12, 25),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "cocacola.jpg",
    fragment_identifier = "retro_cocacola",
    title = "Retro CocaCola",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 10, 10),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "couple_nicefr.png",
    fragment_identifier = "nice_trip",
    title = "That one time at the Nice, France",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2014, 9, 21),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "dinner_in_town.jpg",
    fragment_identifier = "dinner_in_town",
    title = "Dinner In Town",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2013, 9, 18),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "electric_sky.jpg",
    fragment_identifier = "electric_sky",
    title = "Electric Sky",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2012, 03, 13),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "electric_teeth.jpg",
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
photo = Photo(
    filename = "geek_squad.jpg",
    fragment_identifier = "csf_lab",
    title = "CSF Lab",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2013, 06, 15),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "girly_driver.jpg",
    fragment_identifier = "girly_driver",
    title = "Girly Driver",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 11, 17),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "green_lamp.jpg",
    fragment_identifier = "green_lamp",
    title = "Green Lamp",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2014, 8, 11),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "lamp_heart.jpg",
    fragment_identifier = "lamp_heart",
    title = "Lamp Heart",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 8, 27),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "led_robot.jpg",
    fragment_identifier = "bionic_motion",
    title = "Bionic Motion",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 8, 27),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "led_self.jpg",
    fragment_identifier = "bionic_self",
    title = "Bionic Self",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 8, 27),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "led_side.jpg",
    fragment_identifier = "apocalypse_now",
    title = "Apocalypse Now",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 8, 27),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "little_flower.jpg",
    fragment_identifier = "little_flower",
    title = "Little Flower",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2013, 9, 16),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "mayas.jpg",
    fragment_identifier = "mayas_dawn",
    title = "Mayas Dawn",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2012, 12, 25),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "old_quebec_gates.jpg",
    fragment_identifier = "winter_gates",
    title = "Winter Gates",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2012, 01, 02),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "pierced_flower.jpg",
    fragment_identifier = "pierced_flower",
    title = "Pierced Flower",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2013, 9, 16),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "piwi_skate.jpg",
    fragment_identifier = "skate_on_rocks",
    title = "Skate On Rocks",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 10, 11),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "powers_flare.jpg",
    fragment_identifier = "powers_flare",
    title = "Powers Flare",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2012, 03, 03),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "quebec_montreal_3h.jpg",
    fragment_identifier = "winter_road",
    title = "Winter Road",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2012, 03, 13),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "quebec_winter.jpg",
    fragment_identifier = "white_winter",
    title = "White Winter",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2014, 05, 11),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "rocket_to_winterspace.jpg",
    fragment_identifier = "winter_sky_light",
    title = "Winter Sky Light",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2012, 01, 19),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "rocks_skate.jpg",
    fragment_identifier = "skate_on_rocks_2",
    title = "Skate On Rocks 2",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 10, 11),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "sandy_friendly.jpg",
    fragment_identifier = "sandrink_and_20th",
    title = "Sandrink & 20th",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2013, 02, 24),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "sideway.jpg",
    fragment_identifier = "sideway_smile",
    title = "Sideway Smile",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2014, 07, 31),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "snow_electrons.jpg",
    fragment_identifier = "snow_electrons",
    title = "Snow Electrons",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2012, 01, 19),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "south_shore.jpg",
    fragment_identifier = "south_shore",
    title = "South Shore",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 10, 10),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "square_subway.jpg",
    fragment_identifier = "square_subway",
    title = "Square Subway",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2012, 02, 14),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "the_car_jump.jpg",
    fragment_identifier = "skate_on_rocks_3",
    title = "Skate On Rocks 3",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 10, 11),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "theoule_sur_mer.jpg",
    fragment_identifier = "theoule_sur_mer",
    title = "Theoul Sur Mer",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2014, 8, 15),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "the_virus.jpg",
    fragment_identifier = "night_virus",
    title = "Night Virus",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 9, 29),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "tunnel_of_life.jpg",
    fragment_identifier = "tunnel_of_life",
    title = "Tunnel Of Life",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2011, 10, 9),
    owner = KEDFILMS_FOUNDER
)
photo.save()
photo = Photo(
    filename = "waiting_for_train.jpg",
    fragment_identifier = "waiting_for_train",
    title = "Waiting For The Train",
    author = "Seva Ivanov",
    category = Photo.GN,
    hardware = "Canon EOS REBEL T3i",
    application = "",
    date_created = date(2014, 9, 15),
    owner = KEDFILMS_FOUNDER
)
photo.save()