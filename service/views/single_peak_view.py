from rest_framework import generics, status
from rest_framework.response import Response

from common.exceptions import NotFoundException, InvalidParametersException
from service.controllers.peak_controller import PeakController


class SinglePeakView(generics.GenericAPIView):

    @staticmethod
    def get(request, **kwargs):
        try:
            peak = PeakController.get_peak(kwargs['peak_id'])
            return Response(peak, status=status.HTTP_201_CREATED)
        except NotFoundException as error:
            return Response(error.to_dict(), status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def put(request, **kwargs):
        try:
            peak = PeakController.update_peak(request.data, kwargs['peak_id'])
            return Response(peak, status=status.HTTP_200_OK)
        except InvalidParametersException as error:
            return Response(error.to_dict(), status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, **kwargs):
        try:
            PeakController.delete_peak(kwargs['peak_id'])
            return Response(status=status.HTTP_200_OK)
        except NotFoundException as error:
            return Response(error.to_dict(), status=status.HTTP_404_NOT_FOUND)
