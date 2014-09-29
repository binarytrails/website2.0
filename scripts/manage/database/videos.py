from frontend.models import Video

video = Video(
	filename = "camera_intro.mov",
	title = "Camera assembly",
	category = "I"
)
video.save()
video = Video(
	filename = "industrial.mov",
	title = "Industrial",
	category = "I"
)
video.save()
video = Video(
	filename = "qc_timelapse.mov",
	title = "Quebec city morning timelapse",
	category = "I"
)
video.save()

video = Video(
	filename = "flying_car.mov",
	title = "Back in the forest",
	category = "C"
)
video.save()
video = Video(
	filename = "gta5.mov",
	title = "Gta V - Away from the keyboard",
	category = "C"
)
video.save()
video = Video(
	filename = "spring_recap.mov" ,
	title = "Just relax - Spring Recap",
	category = "C"
)
video.save()

