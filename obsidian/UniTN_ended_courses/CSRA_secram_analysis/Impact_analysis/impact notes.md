1. communication channels
	1. communication security
		- *security*
	2. air-to-ground communication
		- *drone to station*
	3. ground-to-ground communication
		- *station to station (synchronization with different service provider)
	4. vehicle-to-vehicle communication 
		- *kinda like crash management*
	5. LAN e internet connections
		- internal 
		- external 
2. info needed
	1. mapping
		-  *Horizontal and vertical space*
	2. weather
	3. regulations (laws)
	4. gps
	5. congestion information
	6. drone state sensing info
		1. internal (components state)
		2. external (environmental info)
3. security
	1. vehicles authentication
	2. operators authentication
	3. operators permissions
	4. information encryption
	5. sensitive data protection (both  people and performance)
		- transit
		- storage
4. protocols
	1. crash protocol (internal failure or hit something)
	2. trajectory protocol 
		- *Run-time controll,* 
		- *Monitors trajectory progress and adjust trajectory, if needed, Supports contingency – rescue*
		- *dynamically adjustment of geo-fancing areas*
	3. initial set-up protocol 
		- *Generates and files a nominal trajectory*
		- *adjusts trajectory in case of other congestion or pre-occupied airspace* 
		- *Verifies for fixed, human-made, or terrain avoidance*
		- *Verifies for usable airspace and any airspace restrictions*
		- *Verifies for wind/weather forecast and associated airspace constraints*
	4. weather changes protocol
	5. lost connection protocol
5. power
6. data collection (statistical - feedback of the flight)