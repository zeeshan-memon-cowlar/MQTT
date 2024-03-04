import paho.mqtt.client as mqtt
import time

def main():
    #For Simplification, this client is only publisher at the moment
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

    client.connect("localhost", 1883, 60)  # Change the address if the broker is on another machine
    while True:
        message = input("Write a Message to Publish:")
        client.publish("test/status", message)
        print("Message Published ..\n")

if __name__ == "__main__":
    main()
