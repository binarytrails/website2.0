# Copyright (C) 2016 Seva Ivanov
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import os, random

from django.shortcuts import HttpResponse, render, redirect
from django.core.urlresolvers import reverse
from django.views.decorators.cache import never_cache

from kedfilms.decorators import old_browsers
from frontend import views as frontend

@never_cache
@old_browsers
def project(request, category, title, html_file):
    version = frontend.get_app_version(request)

    if version == "mobile": html_file += "-" + version
    html_file += ".html"
    
    template = os.path.join(category, title, html_file)
    template_abspath = os.path.join(frontend.PROJECT_ROOT, "projects/templates", template)

    if os.path.isfile(template_abspath) == False: return error404(request)

    elif "moodboard" in html_file:
        folder = os.path.join(frontend.STATIC_PROJECTS, "cart/moodboard/images/data")

        return render(request, template, {
            "version": version,
            "files": moodboard(folder)
        })

    return render(request, template, {"version": version})

def moodboard(folder):
    unordered_files = []
    video_formats = ["webm"]
    image_formats = ["jpg", "png", "gif", "svg"]
    supported_formats = image_formats + video_formats

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        if os.path.isfile(filepath):

            extension = os.path.splitext(filename)[1][1:].lower()
            if extension not in supported_formats: continue

            unordered_files.append({
                # wrap with 'time.ctime()' to make readable
                "mtime": os.path.getmtime(filepath),
                "is_video": extension in video_formats,
                "top_shift": random.randint(1, 10),
                "filename": filename
            })

    ordered_files = sorted(unordered_files,
        key=lambda item: item["mtime"], reverse=True)

    return ordered_files
