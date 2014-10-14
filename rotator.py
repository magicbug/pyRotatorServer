import serial

from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "pyRotatorServer!"

@app.route('/azimuth/<degrees>')
def post_azimuth(degrees):
    # Create suitable string for GS232
    az = "az" + str(degrees) + "\n"

    # Create suitable string for GS232
    ser = serial.Serial(2, 9600, stopbits=1, timeout=None, xonxoff=0, rtscts=0)  # open first serial port

    # Check Serial Ports Open
    ser.isOpen()

    # Write Azimuth to serial port
    ser.write(az)

    # Close Com port
    ser.close()

    # Return Elevation in Degrees in json format
    return jsonify(azimuth=degrees)

@app.route('/elevation/<degrees>')
def post_elevation(degrees):
    # Create suitable string for GS232
    el = "el" + str(degrees) + "\n"

    # Open Serial Port
    ser = serial.Serial(2, 9600, stopbits=1, timeout=None, xonxoff=0, rtscts=0)  # open first serial port

    # Check Serial Ports Open
    ser.isOpen()

    # Write Elevation Movement
    ser.write(el)

    # Close Com port
    ser.close()

    # Return Elevation in Degrees in json format
    return jsonify(elevation=degrees)

if __name__ == "__main__":
    app.debug = True
    app.run()
