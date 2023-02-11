import csv
import socket
import time

with open("positioning_data.csv", 'r') as file:
  csvreader = csv.reader(file)
  send_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  for row in csvreader:
    row[0]=row[0].replace('"', '')
    aux = row[0].split(";")
    if(aux[2]!="Y"):
        result = f"0;{aux[7]};{aux[6]};{aux[1]};{aux[2]};{aux[3]};{aux[4]};{aux[5]};0"
        send_server_socket.sendto(bytes(result, "utf-8"),("publisher",8053))
        print(result)
        time.sleep(0.2)