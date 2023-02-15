from pymavlink import mavutil
#Mavutil has helper functions for connections and sending messages

# Start a connection listening on a UDP port - 14550 default mavlink connection for ground control and 14551 second connection
the_connection = mavutil.mavlink_connection('udpin:localhost:14551')

# Wait for the first heartbeat -- aircraft sends heartbeats to like other programs know the aircraft is there 
#the aircraft has the system id and the component id of the device on the system. 
#   This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

# Once connected, use 'the_connection' to get and send messages

while 1:
    msg = the_connection.recv_match(type='ATTITUDE', blocking=True)
    print(msg) 