from urllib.parse import quote, urljoin

from django.conf import settings
from django.shortcuts import redirect
from django.templatetags.static import get_media_prefix
from django.views.generic.base import TemplateView

from codesamples.models import CodeSample
from downloads.models import Release


class IndexView(TemplateView):
    template_name = "python/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'code_samples': CodeSample.objects.published()[:5],
        })
        return context


class DocumentationIndexView(TemplateView):
    template_name = 'python/documentation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'latest_python2': Release.objects.latest_python2(),
            'latest_python3': Release.objects.latest_python3(),
        })
        return context


def migrate_media_view(request):
    media_file = request.path.lstrip(settings.MEDIA_URL)
    return redirect(urljoin(get_media_prefix(), quote(media_file)))
