# What this does.

This programs reads a sensor (text file) with a 2 minutes collection window
to send off to the server in a json format

The assignment send to grab the average and use {"average": float} but
this doesn't work and results in a 400 status error. This is fixed by changing
the json to {"avg": float}