from Sensor.ReqInstaller import installer
try:
    import requests
except ImportError:
    installer()


def post():
    pass