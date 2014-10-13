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
	title = "Preparations",
	director = "Seva Ivanov",
	description = "",
	category = Video.IN,
    hardware = "Camera: Canon EOS REBEL T3i",
	application = "SFX: Adobe After Effect",
	date_created = date(2012, 07, 17),
	owner = KEDFILMS_FOUNDER
)
video.save()
video = Video(
	staticfilepath = "vid/intro/industrial.ogv",
	title = "Montréal",
	director = "Seva Ivanov",
	description = "Unique picture animation",
	category = Video.IN,
    hardware = "Camera: Canon EOS REBEL T3i",
	application = "SFX: Adobe After Effect",
	date_created = date(2012, 04, 22),
	owner = KEDFILMS_FOUNDER
)
video.save()
video = Video(
	staticfilepath = "vid/intro/qc_timelapse.ogv",
	title = "Quebec city",
	director = "Seva Ivanov",
	description = "Timelapse",
	category = Video.IN,
    hardware = "Camera: Canon EOS REBEL T3i",
	application = "SFX: Adobe After Effect",
	date_created = date(2012, 12, 23),
	owner = KEDFILMS_FOUNDER
)
video.save()

"""
C complete
"""
video = Video(
	staticfilepath = "vid/complete/flying_car.ogv",
	title = "Back in the forest",
	director = "Seva Ivanov",
	description = "",
	category = Video.CM,
    hardware = "Camera: Canon EOS REBEL T3i",
	application = "SFX: Adobe After Effect",
	date_created = date(2011, 10, 12),
	owner = KEDFILMS_FOUNDER
)
video.save()
video = Video(
	staticfilepath = "vid/complete/gta5.ogv",
	title = "Gta V - Away from the keyboard",
	director = "Seva Ivanov",
	description = "Three hours of improvisation.",
	category = Video.CM,
    hardware = "Camera: Canon EOS REBEL T3i",
	application = "SFX: Adobe After Effect",
	date_created = date(2011, 11, 02),
	owner = KEDFILMS_FOUNDER
)
video.save()
video = Video(
	staticfilepath = "vid/complete/spring_recap.ogv" ,
	title = "Spring",
	director = "Seva Ivanov",
	description = "Pictures in motion",
	category = Video.CM,
    hardware = "Camera: Canon EOS REBEL T3i",
	application = "SFX: Adobe After Effect",
	date_created = date(2012, 06, 24),
	owner = KEDFILMS_FOUNDER
)
video.save()
video = Video(
	staticfilepath = "vid/complete/daveland.ogv" ,
	title = "Daveland",
	director = "Seva Ivanov",
	description = "High school project",
	category = Video.CM,
    hardware = "Camera: Canon EOS REBEL T3i",
	application = "SFX: Adobe After Effect",
	date_created = date(2011, 05, 15),
	owner = KEDFILMS_FOUNDER
)
video.save()
