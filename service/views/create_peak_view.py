from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from service.controllers.peak_controller import PeakController


class CreatePeakView(generics.GenericAPIView):

    @staticmethod
    def post(request):
        print(request.data)
        PeakController.create_peak(request.data)
        return render(request, 'index.html', {'peaks': PeakController.get_peaks()})
