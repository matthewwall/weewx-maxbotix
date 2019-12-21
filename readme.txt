maxbotix - weewx service and driver for maxbotix range finder sensors
Copyright 2015 Matthew Wall

This extension can be used as a service to augment existing observations, or
as a driver to collect only the maxbotix sensor readings.

Values from the sensor will be saved as 'range'.  To retain these values,
modify the weewx database schema as described in the customization guide.

Installation instructions:

1) run the installer:

wee_extension --install weewx-maxbotix.tgz

2) modify weewx.conf:

If using as a service:

[Maxbotix]
    port = /dev/ttyUSB0

[Engine]
    [[Services]]
        data_services = user.maxbotix.MaxbotixService

If using as a driver:

[Station]
    station_type = Maxbotix

[Maxbotix]
    port = /dev/ttyUSB0
    driver = user.maxbotix

3) start weewx

sudo /etc/init.d/weewx start
