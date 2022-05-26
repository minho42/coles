from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import User


@login_required
def profile(request, slug):
    template = "profiles/profile.html"
    user = get_object_or_404(User, slug=slug)

    # superuser shouldn't be visible to anyone else
    superuser = get_object_or_404(User, is_superuser=True)
    if slug == superuser.slug and request.user.slug != slug:
        raise Http404

    context = {"u": user}
    return render(request, template, context)
