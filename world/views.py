from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import WorldBorder, Co_School, State_Bound
from django.shortcuts import redirect
from django.contrib.gis.forms import widgets
from .forms import Co_School
from django.core.serializers import serialize
from django.http import HttpResponse

def index(request):
    form = Co_School()
    context = { 'form': form }
    return render(request, 'world/index.html', context)



###takes objects from Co_School and returns them as a geojson###
def Co_School_view(request):
    points_as_geojson = serialize('geojson', Co_School.objects.all())
    return HttpResponse(points_as_geojson, content_type='json')
