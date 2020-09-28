from rest_framework import generics, status
from rest_framework.response import Response

from common.exceptions import InvalidParametersException
from service.controllers.peak_controller import PeakController


class CreatePeakView(generics.GenericAPIView):

    @staticmethod
    def post(request):
        try:
            peak = PeakController.create_peak(request.data)
            return Response(peak, status=status.HTTP_201_CREATED)
        except InvalidParametersException as error:
            return Response(error.to_dict(), status=status.HTTP_400_BAD_REQUEST)
