from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Client, Breif, PlanOverViewForm

# Create your views here.
def index(request):
    client = Client.objects.order_by("-created_at")

    return render(request, "mgblog/index.html", {"client": client})


def breif(request, clientId):
    breif = Breif.objects.get(client_id=clientId)
    return render(request, "mgblog/breif.html", {"breif": breif})


def plan_form(request):
    if request.method == "POST":
        form = PlanOverViewForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("/mgblog/", pk=post.pk)
    else:
        form = PlanOverViewForm()
    return render(request, "mgblog/plan_form.html", {"PlanOverViewForm": form})
