from rest_framework import generics, status
from rest_framework.response import Response

from service.controllers.peak_controller import PeakController


class SinglePeakView(generics.GenericAPIView):

    @staticmethod
    def get(request, **kwargs):
        return Response(PeakController.get_peak(kwargs['peak_id']),
                        status=status.HTTP_201_CREATED)

    @staticmethod
    def put(request, **kwargs):
        peak = PeakController.update_peak(request.data, kwargs['peak_id'])
        return Response(peak, status=status.HTTP_200_OK)

    @staticmethod
    def delete(request, **kwargs):
        PeakController.delete_peak(kwargs['peak_id'])
        return Response(status=status.HTTP_200_OK)
