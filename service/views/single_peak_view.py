from django.shortcuts import render, redirect
from rest_framework import generics, status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from service.controllers.peak_controller import PeakController


class SinglePeakView(generics.GenericAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'mountain_detail.html'

    @staticmethod
    def get(request, **kwargs):
        return Response(PeakController.get_peak(kwargs['peak_id']),
                        status=status.HTTP_201_CREATED)

    @staticmethod
    def put(request, **kwargs):
        peak = PeakController.update_peak(request.data, kwargs['peak_id'])
        return Response(peak, status=status.HTTP_200_OK)

    @staticmethod
    def post(request, **kwargs):
        PeakController.delete_peak(kwargs['peak_id'])
        return render(request, 'index.html', {'peaks': PeakController.get_peaks()})
