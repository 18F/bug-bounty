import os
import markdown
from django.conf import settings
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from .forms import ReportForm

def index(request):
    context = {slug: _load_content(slug) for slug in ('rules', 'scope', 'faq')}
    return render(request, "bugbounty/index.html", context)

def _load_content(slug):
    content_file = os.path.join(settings.BASE_DIR, 'content', slug+'.md')
    with open(content_file) as fp:
        html = markdown.markdown(fp.read(), otuput_format='html5')
    return mark_safe(html)

def submit(request):
    form = ReportForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(thanks)
    return render(request, "bugbounty/submit.html", {'form': form})

def thanks(request):
    return render(request, "bugbounty/thanks.html")

def page(request, slug, template="bugbounty/page.html"):
    return render(request, template, {
        'content': _load_content(slug)
    })