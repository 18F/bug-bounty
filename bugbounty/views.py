import os
import markdown
from django.conf import settings
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from .forms import ReportForm
from .notifications import send_report_notification

def index(request):
    context = {slug: _load_content(slug) for slug in ('rules', 'scope')}
    return render(request, "bugbounty/index.html", context)

def _load_content(slug):
    content_file = os.path.join(settings.BASE_DIR, 'content', '{}.md'.format(slug))
    with open(content_file) as fp:
        html = markdown.markdown(fp.read(), otuput_format='html5')
    return mark_safe(html)  # nosec - we trust content in these files

def submit(request):
    form = ReportForm(request.POST or None)
    if form.is_valid():
        report = form.save()
        send_report_notification(request, report)
        return redirect(thanks)
    return render(request, "bugbounty/submit.html", {'form': form})

def thanks(request):
    return render(request, "bugbounty/thanks.html")

def page(request, slug, template="bugbounty/page.html"):
    return render(request, template, {
        'content': _load_content(slug)
    })
