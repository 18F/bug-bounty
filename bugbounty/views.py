from django.shortcuts import render, redirect
from .forms import ReportForm

def index(request):
    return render(request, "bugbounty/index.html")

def submit(request):
    form = ReportForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(thanks)
    return render(request, "bugbounty/submit.html", {'form': form})

def thanks(request):
    return render(request, "bugbounty/thanks.html")