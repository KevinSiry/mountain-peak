from rest_framework import generics, status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from service.controllers.peak_controller import PeakController


class GetPeaksView(generics.GenericAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'mountain_detail.html'

    @staticmethod
    def get(request):
        peaks = PeakController.get_peaks(request.GET.get('sw_long'),
                                         request.GET.get('sw_lat'),
                                         request.GET.get('ne_long'),
                                         request.GET.get('ne_lat'))
        return Response({'peaks': peaks}, status=status.HTTP_200_OK)
