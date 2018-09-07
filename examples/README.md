### Collection of sample program fragments ###
using a python client to play interactively tic-tac-toe and andvanced variants on bigger boards.

The code should use the python implementation in https://github.com/K2InformaticsGmbH/tcpjson to connect to the egambo game server.

The direct tcp connection mechanism will allow fast and concurrent training of intelligent bots over a single connection. One socket will be needed per player. A single socket is sufficient if you are playing against a (rather stupid) server side bot ("bot1" or "bot2").
Intelligent bot training beyond beginner level will need two user registrations, two passwords and two sockets, one each per competitor. 

A server for public playing will be announced soon on this page, together with account registration instructions.

Pull requests for improvements or additional clients are very welcome.



