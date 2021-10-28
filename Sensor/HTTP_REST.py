from Sensor.ReqInstaller import installer
import configparser
try:
    import requests
except ImportError:
    installer()
failed_attempts = []


def post(json: dict):
    config = configparser.ConfigParser()
    config.read("./config.ini")
    url = config["Backend"]["url"]
    fallback_url = config["Backend"]["fallback_url"]
    r = requests.post(url, json=json)
    status_code = r.status_code
    print(status_code)
    if status_code == "500":
        if len(failed_attempts) == 10:
            del failed_attempts[-1]
        failed_attempts.append(json)
    if failed_attempts[0] != json:
        for entry in failed_attempts:
            r2 = requests.post(fallback_url, json=entry)
            if r2.status_code == "200":
                failed_attempts.remove(entry)
