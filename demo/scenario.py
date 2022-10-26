"""
@auther Hyunwoong
@since 7/1/2020
@see https://github.com/gusdnd852
"""

from kocrawl.dust import DustCrawler
from kocrawl.weather import WeatherCrawler
from kochat.app import Scenario
from kocrawl.map import MapCrawler
from kocrawl.window import WindowCrawler
from kocrawl.LED import LEDCrawler
from kocrawl.PDLC import PDLCCrawler

window = Scenario(
    intent='window',
    api=WindowCrawler().request,
    scenario={
        'DATE':['지금'],
        'object': [], #창문 LED PDLC
        'do': [] # OPEN or CLOSE
    }
)
#30분 간격으로 예약이 가능하게..
LED = Scenario(
    intent='LED',
    api=LEDCrawler().request,
    scenario={
        'ROOM':['내방'],
        'DATE':['지금'],
        'object': [], #전등 LED PDLC
        'do': [] # ON OFF
    }
)
PDLC = Scenario(
    intent='PDLC',
    api=PDLCCrawler().request,
    scenario={
        'DATE':['지금'],
        'object': [], # LED PDLC
        'do': [] # UP DOWN
    }
)

weather = Scenario(
    intent='weather',
    api=WeatherCrawler().request,
    scenario={
        'LOCATION': [],
        'DATE': ['오늘'] #기본 값
    }
)

dust = Scenario(
    intent='dust',
    api=DustCrawler().request,
    scenario={
        'LOCATION': [],
        'DATE': ['오늘']
    }
)

restaurant = Scenario(
    intent='restaurant',
    api=MapCrawler().request,
    scenario={
        'LOCATION': [],
        'PLACE': ['맛집']
    }
)

travel = Scenario(
    intent='travel',
    api=MapCrawler().request,
    scenario={
        'LOCATION': [],
        'PLACE': ['관광지']
    }
)

