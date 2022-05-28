from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import User


@login_required
def profile(request, slug):
    template = "profiles/profile.html"
    user = get_object_or_404(User, slug=slug)

    context = {"u": user}
    return render(request, template, context)
