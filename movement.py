from pymavlink import mavutil
#Mavutil has helper functions for connections and sending messages

# Start a connection listening on a UDP port - 14550 default mavlink connection for ground control and 14551 second connection
the_connection = mavutil.mavlink_connection('udpin:localhost:14551')

# Wait for the first heartbeat -- aircraft sends heartbeats to like other programs know the aircraft is there 
#the aircraft has the system id and the component id of the device on the system. 
#   This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

#Local Position Movment 
the_connection.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(10, the_connection.target_system, 
        the_connection.target_component, mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        int(0b100111111000), 30, 0, -10, 0, 0, 0, 0, 0, 0, 1.57, 0))

#Global Position Movment 
the_connection.mav.send(mavutil.mavlink.MAVLink_set_position_target_global_int_message(10, the_connection.target_system, 
         the_connection.target_component, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
         int(0b110111111000), int(-5.3629849 * 10 ** 7), int(-149.1649185 * 10 ** 7), 10, 0, 0, 0, 0, 0, 0, 1.57, 0))

#Return messages with the positions updated
while 1:
    msg = the_connection.recv_match(type='LOCAL_POSITION_NED', blocking=True)
    print(msg);


