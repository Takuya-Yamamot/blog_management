from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Client, Breif, PlanOverView, PlanOverViewForm, BreifForm

# Create your views here.
def index(request):
    client = Client.objects.order_by("created_at")
    breif = Breif.objects.all()
    plan_over = PlanOverView.objects.all()

    return render(
        request,
        "mgblog/index.html",
        {"client": client, "breif": breif, "plan_over": plan_over},
    )


def breif(request, clientId):
    breif = Breif.objects.get(client_id=clientId)
    return render(request, "mgblog/breif.html", {"breif": breif})


def plan_list(request, clientId):
    plan_list = PlanOverView.objects.get(client_id=clientId)
    return render(request, "mgblog/plan_list.html", {"plan_list": plan_list})


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


def breif_form(request):
    if request.method == "POST":
        form = BreifForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("/mgblog/", pk=post.pk)
    else:
        form = BreifForm()
    return render(request, "mgblog/breif_form.html", {"BreifForm": form})
