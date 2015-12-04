
IE_USERAGENT_TAGS = ["msie", "trident"]

def old_browsers(initial_view):
    def wrapped_view(request, *args, **kwargs):
        if any(agent in request.META["HTTP_USER_AGENT"].lower() for agent in IE_USERAGENT_TAGS):
            browsers_suggestion = {"firefox": True, "chrome": True, "safari": True}
            return render(request, "frontend/errors/old-browser.html", browsers_suggestion)

        return initial_view(request, *args, **kwargs)
    return wrapped_view
