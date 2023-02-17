from pymavlink import mavutil
#Mavutil has helper functions for connections and sending messages

# Start a connection listening on a UDP port - 14550 default mavlink connection for ground control and 14551 second connection
the_connection = mavutil.mavlink_connection('udpin:localhost:14551')

# Wait for the first heartbeat -- aircraft sends heartbeats to like other programs know the aircraft is there 
#the aircraft has the system id and the component id of the device on the system. 
#   This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))


#Commands -- YAW  (Relative vs Absolute angle)
the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                      mavutil.mavlink.MAV_CMD_CONDITION_YAW, 0, 45, 25, 0, 1, 0, 0, 0)
                                    #5th command 0 -> Absolute 1-> Relative

#Commands -- Change Speed 
the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                     mavutil.mavlink.MAV_CMD_DO_CHANGE_SPEED, 0, 0, 10, 0, 0, 0, 0, 0)
                                    #3rd Param m/s
