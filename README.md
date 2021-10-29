# What this does.

This programs reads a sensor (text file) with a 2 minute collection window
to send off to the server in a json format. This is customizable in the `config.ini` file 

To run the file you need `Python 3.6 or higher`.

For Windows: Run `main.py` or `python main.py`

For Linux: Run `python3.6 main.py`

## config.ini
In the config file you can define a few values. 

Under the Sensor category you can define which type of temperature you want to get from the sensor

The following is avalible: Fahrenheit, Kelvin, Celsius

You can also define how fast you can read from the sensor.

sensor_read_speed = 0.1 // This makes the sensor read every 100ms 

For the backend you can change urls and how often any information is to be pushed to the server.

## Challanges faced

In the assignment, you are told to send to the average temp in json and use something like: `{"average": float}` 
but this doesn't work and results in a 400 status error. After some trial and error I found out that this is fixed 
by changing the json to `{"avg": float}`
