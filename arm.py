from pymavlink import mavutil
#Mavutil has helper functions for connections and sending messages

# Start a connection listening on a UDP port - 14550 default mavlink connection for ground control and 14551 second connection
the_connection = mavutil.mavlink_connection('udpin:localhost:14551')

# Wait for the first heartbeat -- aircraft sends heartbeats to like other programs know the aircraft is there 
#the aircraft has the system id and the component id of the device on the system. 
#   This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

#using the connection to send a long command. the targtet system connection filled in with heartbeat
# 3rd parameter is replacing the command id (400) by getting the name aka arm disarm from documentation
the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                     mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)

#Command acknowledge returned 
msg = the_connection.recv_match(type='COMMAND_ACK', blocking=True)
print(msg)                   
# Returns: command: command# that was sent, command valid and executed                  

