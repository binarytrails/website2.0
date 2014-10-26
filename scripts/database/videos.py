from datetime import date
from frontend.models import User, Video

KEDFILMS_FOUNDER = User.objects.get(nick = "kedfilms-founder")

"""
Delete all records
"""
Video.objects.all().delete()

"""
I Intro
"""
video = Video(
	filename = "camera_intro.ogv",
	posterfile = "camera_intro.jpg",
	title = "Preparations",
	director = "Seva Ivanov",
	description = "",
	category = Video.IN,
    hardware = "Canon EOS REBEL T3i",
	application = "Adobe After Effect",
	date_created = date(2012, 07, 17),
	owner = KEDFILMS_FOUNDER
)
video.save()
video = Video(
	filename = "industrial.ogv",
	posterfile = "industrial.jpg",
	title = "Montréal",
	director = "Seva Ivanov",
	description = "Unique picture animation",
	category = Video.IN,
	application = "Adobe After Effect",
	date_created = date(2012, 04, 22),
	owner = KEDFILMS_FOUNDER
)
video.save()
video = Video(
	filename = "qc_timelapse.ogv",
	posterfile = "qc_timelapse.jpg",
	title = "Quebec city",
	director = "Seva Ivanov",
	description = "Timelapse",
	category = Video.IN,
    hardware = "Canon EOS REBEL T3i",
	application = "Adobe After Effect",
	date_created = date(2012, 12, 23),
	owner = KEDFILMS_FOUNDER
)
video.save()
video = Video(
	filename = "kedproduction.ogv",
	posterfile = "kedproduction.jpg",
	title = "Ked production",
	director = "Seva Ivanov",
	description = "Pure animation",
	category = Video.IN,
    hardware = "",
	application = "Adobe After Effect",
	date_created = date(2011, 01, 22),
	owner = KEDFILMS_FOUNDER
)
video.save()

"""
FV Favorite
"""
video = Video(
	filename = "flying_car.ogv",
	posterfile = "flying_car.jpg",
	title = "Back in the forest",
	director = "Seva Ivanov",
	description = "",
	category = Video.FV,
    hardware = "Canon EOS REBEL T3i",
	application = "Adobe After Effect",
	date_created = date(2011, 10, 12),
	owner = KEDFILMS_FOUNDER
)
video.save()
video = Video(
	filename = "gta5.ogv",
	posterfile = "gta5.jpg",
	title = "Gta V - Away from the keyboard",
	director = "Seva Ivanov",
	description = "Three hours of improvisation.",
	category = Video.FV,
    hardware = "Canon EOS REBEL T3i",
	application = "Adobe After Effect",
	date_created = date(2011, 11, 02),
	owner = KEDFILMS_FOUNDER
)
video.save()
video = Video(
	filename = "spring_recap.ogv",
	posterfile = "spring_recap.jpg",
	title = "Spring",
	director = "Seva Ivanov",
	description = "Pictures in motion",
	category = Video.FV,
    hardware = "Canon EOS REBEL T3i",
	application = "Adobe After Effect",
	date_created = date(2012, 06, 24),
	owner = KEDFILMS_FOUNDER
)
video.save()
video = Video(
	filename = "daveland.ogv",
	posterfile = "daveland.jpg",
	title = "Daveland",
	director = "Seva Ivanov & Guillaume Bonneau",
	description = "High school project",
	category = Video.FV,
    hardware = "Sony Bloggie MHS-FV5",
	application = "Adobe After Effect",
	date_created = date(2011, 05, 15),
	owner = KEDFILMS_FOUNDER
)
video.save()
video = Video(
	filename = "tv_flowmo.ogv",
	posterfile = "tv_flowmo.jpg",
	title = "Television",
	director = "Seva Ivanov",
	description = "AE Flowmo effect",
	category = Video.FV,
    hardware = "",
	application = "Adobe After Effect",
	date_created = date(2012, 9, 13),
	owner = KEDFILMS_FOUNDER
)
video.save()
video = Video(
	filename = "beard_on_fire.ogv",
	posterfile = "beard_on_fire.jpg",
	title = "Beard On Fire",
	director = "Seva Ivanov",
	description = "Short episode",
	category = Video.FV,
    hardware = "Canon EOS REBEL T3i",
	application = "Adobe After Effect",
	date_created = date(2012, 05, 27),
	owner = KEDFILMS_FOUNDER
)
video.save()
video = Video(
	filename = "gta_intro_clothing.ogv",
	posterfile = "gta_intro_clothing.jpg",
	title = "GTA Like Wardrobe",
	director = "Seva Ivanov",
	description = "Masking challenge",
	category = Video.FV,
    hardware = "Canon EOS REBEL T3i",
	application = "Adobe After Effect",
	date_created = date(2011, 9, 30),
	owner = KEDFILMS_FOUNDER
)
video.save()

"""
EV Event
"""
video = Video(
	filename = "afternoon-jam.ogv",
	posterfile = "afternoon-jam.jpg",
	title = "Afternoon Birthday Jam",
	director = "Seva Ivanov",
	description = "Bboying, Hip-Hop culture",
	category = Video.EV,
    hardware = "Canon EOS REBEL T3i",
	application = "Adobe After Effect",
	date_created = date(2012, 05, 23),
	owner = KEDFILMS_FOUNDER
)
video.save()
video = Video(
	filename = "braggin-rites-8.ogv",
	posterfile = "braggin-rites-8.jpg",
	title = "Braggin' Rites 8",
	director = "Seva Ivanov",
	description = "Bboying, Hip-Hop culture",
	category = Video.EV,
    hardware = "",
	application = "Adobe After Effect",
	date_created = date(2012, 01, 29),
	owner = KEDFILMS_FOUNDER
)
video.save()
video = Video(
	filename = "old_to_the_new.ogv",
	posterfile = "old_to_the_new.jpg",
	title = "Old to the new",
	director = "Seva Ivanov",
	description = "Bboying, Hip-Hop culture",
	category = Video.EV,
    hardware = "Canon EOS REBEL T3i",
	application = "Adobe After Effect",
	date_created = date(2012, 03, 06),
	owner = KEDFILMS_FOUNDER
)
video.save()
video = Video(
	filename = "openwood.ogv",
	posterfile = "openwood.jpg",
	title = "Open Wood",
	director = "Seva Ivanov",
	description = "Quebec forest rave",
	category = Video.EV,
    hardware = "Canon EOS REBEL T3i",
	application = "Adobe After Effect",
	date_created = date(2012, 07, 15),
	owner = KEDFILMS_FOUNDER
)
video.save()
video = Video(
	filename = "qcroc.ogv",
	posterfile = "qcroc.jpg",
	title = "Qc Roc 15th Anniversary",
	director = "Seva Ivanov",
	description = "Powemoves battle",
	category = Video.EV,
    hardware = "Sony Bloggie MHS-FV5",
	application = "Adobe After Effect",
	date_created = date(2011, 11, 30),
	owner = KEDFILMS_FOUNDER
)
video.save()

"""
DN Dancer
"""
video = Video(
	filename = "bboyseva.ogv",
	posterfile = "bboyseva.jpg",
	title = "Bboy Seva",
	director = "Seva Ivanov",
	description = "",
	category = Video.DN,
    hardware = "",
	application = "Adobe After Effect",
	date_created = date(2012, 9, 12),
	owner = KEDFILMS_FOUNDER
)
video.save()
video = Video(
	filename = "spike.ogv",
	posterfile = "spike.jpg",
	title = "Spike on the roof",
	director = "Seva Ivanov",
	description = "Old Quebec city",
	category = Video.DN,
    hardware = "",
	application = "Adobe After Effect",
	date_created = date(2011, 9, 10),
	owner = KEDFILMS_FOUNDER
)
video.save()