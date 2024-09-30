from jug.lib.logger import logger
from flask import render_template
from jug.lib import gLib
from jug.lib import weather_api
import random


class PathCtl:

    def __init__(self, url):
        # self.url = url.rstrip('/').capitalize()
        self.url = url.rstrip('/').title()

    def getPop(self):
        return gLib.getPop()

    def getMoon(self, moon_phase):
        return gLib.getMoon(moon_phase)

    def getAdverb(self):
        return gLib.getAdverb()

    def getAdjective(self):
        return gLib.getAdjective()

    def getPronoun(self):
        return gLib.getPronoun()

    def getFamousFor(self):
        return gLib.getFamousFor()
    def getFamousSyn(self):
        return gLib.getFamousSyn()

    def getWeather(self):

        location = self.url
        weather = weather_api.Weather_api()
        weatherDict = weather.do_weather(location)
        logger.info(f'weather: {weatherDict}')

        return weatherDict


    def doPath(self):

        weatherDict = self.getWeather()

        country = weatherDict["country"]
        local_datetime = weatherDict["datetime"]

        moon_phase = self.getMoon(weatherDict["moon_phase"])

        # moon_phase = weatherDict["moon_phase"]
        # t = type(moon_phase)
        # logger.info(f'moonphase: {t}')
        # logger.info(f'moonphase: {moon_phase[0][0]}')
        # logger.info(f'moonphase: {moon_phase[0][1]}')


        return render_template(
            "pathHtml.jinja",
            city = self.url,
            population = self.getPop(),
            moon_phase = moon_phase,
            adv = self.getAdverb(),
            adj = self.getAdjective(),
            famousSyn = self.getFamousSyn(),
            famousFor = self.getFamousFor(),
            pronoun = self.getPronoun(),
            weatherDict = self.getWeather(),
            local_datetime = local_datetime,
            country = country
        )


    def doStart(self):
        return self.doPath()

