import unittest

import sys
sys.path.insert(0, '../')

from weatherchart import WeatherChart

class TestPre(unittest.TestCase):
    def test_get_weather_by_lat_long(self):
        wchart = WeatherChart('1f285517a7b88e19c9f4631ff1cd368a', 'Asia/Hong_Kong')

        print( wchart.get_forecast('22.300910042194783', '114.17070449064359' ) )

    def test_get_image(self):
        wchart = WeatherChart('1f285517a7b88e19c9f4631ff1cd368a', 'Asia/Hong_Kong')

        print( wchart.get_forecast_chart_image('22.300910042194783', '114.17070449064359', 'out.jpg' ) )



# if __name__ == '__main__':
# 	print("Getting Weather Data")
# 	print( get_weather_data_by_location( '22.300910042194783', '114.17070449064359') )