# crane-game

Crane game that was displayed at NPCA booth at NADA school festival 2016.

## Version

Ver 1.0

## How to play

1. First, clone this reqpository.

### Configuration of back-end

1. Make your breadboard ready to be plugged wires. Use 6V alkaline batteries and 2 motor drivers such as L293D.
2. Wire your Rapsberry Pi into a breadboard in the right way.
3. Write to pins.json where you wired the cables.
4. Now it's ready! The program controls motors when a certain command is executed.

### Configuration of web server

1. `npm install`
2. `node server.js`

### Start playing

1. Access to http://[RPi-address]:3000.
2. Have fun!

## Environment

* Raspberry Pi
* Jessie-based Raspbian OS (non-sudo user can handle GPIO while Wheezy-based or earlier one cannot)
* Python 2.6 or later (Python 3.* might be suitable as well)
* Node.js (too old version is not suitable)

## License

Apache 2.0

## Contact

* E-mail: contact@hideo54.com
* Twitter: @hideo54
