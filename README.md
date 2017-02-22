# open-home

## How to set up mqtt-iot-router

1. Place mqtt-iot-router folder in your /opt dir
2. Add `python /opt/mqtt-iot-router/main.py /opt/mqtt-iot-router/config.json` to `/etc/rc.local` to enable the script to run at bootup
3. Run `python /opt/mqtt-iot-router/main.py /opt/mqtt-iot-router/config.json &`
