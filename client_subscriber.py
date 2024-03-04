import paho.mqtt.client as mqtt
import time

##On message Function to Listen and Decode Message
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")

def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_message = on_message ##On message invoked whenever message received

    client.connect("localhost", 1883, 60)  # Change the address if the broker is on another machine
    subscribe_topic = input("Enter topic to subscribe: ")
    client.subscribe(subscribe_topic)

    try:
        client.loop_forever()
    except:
        print("Disconnecting....")


if __name__ == "__main__":
    main()
