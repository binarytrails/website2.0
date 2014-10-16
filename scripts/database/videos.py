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
	staticfilepath = "vid/intro/camera_intro.ogv",
	staticposterpath = "img/video-poster/camera_intro.jpg",
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
	staticfilepath = "vid/intro/industrial.ogv",
	staticposterpath = "img/video-poster/industrial.jpg",
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
	staticfilepath = "vid/intro/qc_timelapse.ogv",
	staticposterpath = "img/video-poster/qc_timelapse.jpg",
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
	staticfilepath = "vid/intro/kedproduction.ogv",
	staticposterpath = "img/video-poster/kedproduction.jpg",
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
	staticfilepath = "vid/favorite/flying_car.ogv",
	staticposterpath = "img/video-poster/flying_car.jpg",
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
	staticfilepath = "vid/favorite/gta5.ogv",
	staticposterpath = "img/video-poster/gta5.jpg",
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
	staticfilepath = "vid/favorite/spring_recap.ogv",
	staticposterpath = "img/video-poster/spring_recap.jpg",
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
	staticfilepath = "vid/favorite/daveland.ogv",
	staticposterpath = "img/video-poster/daveland.jpg",
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
	staticfilepath = "vid/favorite/tv_flowmo.ogv",
	staticposterpath = "img/video-poster/tv_flowmo.jpg",
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
	staticfilepath = "vid/favorite/beard_on_fire.ogv",
	staticposterpath = "img/video-poster/beard_on_fire.jpg",
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
	staticfilepath = "vid/favorite/gta_intro_clothing.ogv",
	staticposterpath = "img/video-poster/gta_intro_clothing.jpg",
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
	staticfilepath = "vid/event/afternoon-jam.ogv",
	staticposterpath = "img/video-poster/afternoon-jam.jpg",
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
	staticfilepath = "vid/event/braggin-rites-8.ogv",
	staticposterpath = "img/video-poster/braggin-rites-8.jpg",
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
	staticfilepath = "vid/event/old_to_the_new.ogv",
	staticposterpath = "img/video-poster/old_to_the_new.jpg",
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
	staticfilepath = "vid/event/openwood.ogv",
	staticposterpath = "img/video-poster/openwood.jpg",
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
	staticfilepath = "vid/event/qcroc.ogv",
	staticposterpath = "img/video-poster/qcroc.jpg",
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
	staticfilepath = "vid/dancer/bboyseva.ogv",
	staticposterpath = "img/video-poster/bboyseva.jpg",
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
	staticfilepath = "vid/dancer/spike.ogv",
	staticposterpath = "img/video-poster/spike.jpg",
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