from service.models import Mountain
from service.tools.serializers.peak_serializer import PeakSerializer


class DataAccessLayer:

    @staticmethod
    def save(serializer):
        if serializer.is_valid():
            instance = serializer.save()
            return PeakSerializer(instance).data
        else:
            raise Exception(serializer.errors)

    def create_peak(self, peak):
        serializer = PeakSerializer(data=peak)
        return self.save(serializer)

    @staticmethod
    def get_peak(peak_id):
        peak = Mountain.objects.get(id=peak_id)
        return PeakSerializer(instance=peak).data

    def update_peak(self, data, peak_id):
        instance = Mountain.objects.get(id=peak_id)
        serializer = PeakSerializer(instance, data=data)
        return self.save(serializer)

    @staticmethod
    def delete_peak(peak_id):
        Mountain.objects.get(id=peak_id).delete()

    @staticmethod
    def get_peaks(sw_long, sw_lat, ne_long, ne_lat):
        peaks = Mountain.objects.filter(longitude__gte=sw_long,
                                        longitude__lte=ne_long,
                                        latitude__gte=sw_lat,
                                        latitude__lte=ne_lat)
        return PeakSerializer(peaks, many=True).data
