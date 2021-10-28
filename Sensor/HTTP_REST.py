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
    # print(url)
    # print(fallback_url)
    r = requests.post(url=url, json=json)
    status_code = r.status_code
    print(f"Status code: {status_code}")
    if str(status_code) == "500":
        if len(failed_attempts) == 10:
            del failed_attempts[-1]
        failed_attempts.append(json)
    if bool(failed_attempts):
        if failed_attempts[0] != json:
            r2 = requests.post(url=fallback_url, json=failed_attempts)
            print(f"Fallback status code: {r2.status_code}")
            if str(r2.status_code) == "200":
                failed_attempts.clear()

    print(f"Failed: {failed_attempts}")
