# open-home

## How to set up mqtt-iot-router

### Requirements
1. Pip `sudo apt-get install python-pip`

### Install
1. Place mqtt-iot-router folder in your /opt dir
2. Run `pip install -r requirements.txt` from /opt/mqtt-iot-router/`
3. Add `python /opt/mqtt-iot-router/main.py /opt/mqtt-iot-router/config.json` to `/etc/rc.local` to enable the script to run at bootup
4. Run `python /opt/mqtt-iot-router/main.py /opt/mqtt-iot-router/config.json &`
