from django.shortcuts import render

from service.controllers.peak_controller import PeakController


def home(request):
    return render(request, 'index.html', {'peaks': PeakController.get_peaks()})
