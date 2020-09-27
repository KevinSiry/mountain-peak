from rest_framework import generics, status
from rest_framework.response import Response

from service.controllers.peak_controller import PeakController


class CreatePeakView(generics.GenericAPIView):

    @staticmethod
    def post(request):
        peak = PeakController.create_peak(request.data)
        return Response(peak, status=status.HTTP_201_CREATED)
