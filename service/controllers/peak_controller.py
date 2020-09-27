from service.tools.data_access_layer import DataAccessLayer


class PeakController:

    @staticmethod
    def create_peak(data):
        return DataAccessLayer().create_peak(data)

    @staticmethod
    def get_peak(peak_id):
        return DataAccessLayer().get_peak(peak_id)

    @staticmethod
    def update_peak(data, peak_id):
        return DataAccessLayer().update_peak(data, peak_id)

    @staticmethod
    def delete_peak(peak_id):
        return DataAccessLayer().delete_peak(peak_id)

    @staticmethod
    def get_peaks(sw_long=-180, sw_lat=-90, ne_long=180, ne_lat=90):
        return DataAccessLayer().get_peaks(sw_long, sw_lat, ne_long, ne_lat)
