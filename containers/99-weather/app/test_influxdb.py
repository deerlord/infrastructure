import interface

client = interface.InfluxDB()
client.connect()
client.create_database()
data = {'dt': 1595243443, 'sunrise': 1595243663, 'sunset': 1595296278}
client.current(data)
print(client.get_current())
