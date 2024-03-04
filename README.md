# MQTT Subscriber and Publisher

This repository contains Python scripts to set up an MQTT subscriber and publisher using the Paho MQTT library.

## Requirements

- Python 3.x
- Paho MQTT library (`pip install paho-mqtt`)
- Mosquitto MQTT broker (running locally on default port 1883)

## Usage

1. **Initialize Mosquitto Broker:**

   Before running the subscriber and publisher, ensure that the Mosquitto MQTT broker is running locally. You can start the Mosquitto broker by executing the following command in the terminal:

   ```bash
   mosquitto -v

Make sure the broker is listening on the default port 1883.

### To Run Subscriber
Execute the subscriber.py script to listen to messages published on the MQTT broker. The subscriber script prompts you to enter the topic you wish to subscribe to.


### To Run Publisher
Execute the publisher.py script to publish messages to the MQTT broker. The publisher script prompts you to enter the message you want to publish.

