import socket
import network
from ds18x20_thermometer import read_temp
from creds import SSID, PSK # Define SSID and PSK for local WLAN in creds.py

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PSK)
    while not wlan.isconnected():
        pass
    print("Connected to WiFi")
    print(wlan.ifconfig())

def handle_connection(conn):
    request = conn.recv(1024)
    request = str(request)
    conn.send("HTTP/1.0 200 OK\r\nContent-type: text/html; charset=utf-8\r\n\r\n")
    conn.send(f"{read_temp()}")
    conn.close()

def start_server():
    addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(1)

    print("Ready to accept connections")
    while True:
        conn, addr = s.accept()
        handle_connection(conn)

connect_wifi()
start_server()
