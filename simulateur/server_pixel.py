from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

from vrtneopixel import *

app = Flask(__name__)
api = Api(app)

# initialize the Flask-Cors extension with default arguments in order to allow CORS for all domains on all routes.
CORS(app)

# LED strip configuration:
LED_COUNT      = (10, 15)      # Number of LED pixels.
LED_PIN        = 18      # Raspberry Pi GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
# Intialize the library (must be called once before other functions).
strip.begin()

class Pixel(Resource):

    def post(self, pixel):
        parser = reqparse.RequestParser()
        parser.add_argument("red", type=int)
        parser.add_argument("blue", type=int)
        parser.add_argument("green", type=int)
        args = parser.parse_args()

        strip.setPixelColor(pixel, Color(args["red"], args["blue"], args["green"])) 
        strip.show()

        return "Ok", 200

api.add_resource(Pixel, "/pixel/<int:pixel>")

# app.run(debug=True)
app.run()

# pour tester avec curl:
# $ curl -X POST -H 'content-type: application/json' -d '{ "red": 200, "blue": 200, "green": 200}' http://localhost:5000/pixel/2
# "Ok"

