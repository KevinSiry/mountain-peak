from common.exceptions import NotFoundException, InvalidParametersException
from service.models import Mountain
from service.tools.serializers.peak_serializer import PeakSerializer
from django.core.exceptions import ObjectDoesNotExist


class DataAccessLayer:

    @staticmethod
    def save(serializer):
        if serializer.is_valid():
            instance = serializer.save()
            return PeakSerializer(instance).data
        else:
            raise InvalidParametersException(serializer.errors)

    def create_peak(self, peak):
        serializer = PeakSerializer(data=peak)
        return self.save(serializer)

    @staticmethod
    def get_peak(peak_id):
        try:
            peak = Mountain.objects.get(id=peak_id)
            return PeakSerializer(instance=peak).data
        except ObjectDoesNotExist as error:
            raise NotFoundException(str(error))

    def update_peak(self, data, peak_id):
        instance = Mountain.objects.get(id=peak_id)
        serializer = PeakSerializer(instance, data=data)
        return self.save(serializer)

    @staticmethod
    def delete_peak(peak_id):
        try:
            Mountain.objects.get(id=peak_id).delete()
        except ObjectDoesNotExist as error:
            raise NotFoundException(str(error))

    @staticmethod
    def get_peaks(sw_long, sw_lat, ne_long, ne_lat):
        peaks = Mountain.objects.filter(longitude__gte=sw_long,
                                        longitude__lte=ne_long,
                                        latitude__gte=sw_lat,
                                        latitude__lte=ne_lat)
        return PeakSerializer(peaks, many=True).data
