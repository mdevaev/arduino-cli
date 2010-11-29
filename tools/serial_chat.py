#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import serial


##### Private constants #####
ALL_PORT_RATES_LIST = (
	300, 1200, 2400, 4800, 9600, 14400,
	19200, 28800, 38400, 57600, 115200
)


READ_PORT_MODE = "r"
WRITE_PORT_MODE = "w"

ALL_PORT_MODES_LIST = (
	READ_PORT_MODE,
	WRITE_PORT_MODE
)


##### Private functions #####
def help() :
	print ( "using: %s <device> <mode> <speed>\n"
		"\tdevice:\n"
		"\t\t/dev/ttyS0 - COM1\n"
		"\t\t/dev/ttyUSB0 - for devices with COM-over-USB\n"
		"\tmode:\n"
		"\t\tr - reading from serial port\n"
		"\t\tw - writing to serial port\n"
		"\tspeed:\n"
		"\t\t300, 1200, 2400, 4800, 9600, 14400\n"
		"\t\t19200, 28800, 38400, 57600, 115200" ) % (sys.argv[0])


##### Main ####
if __name__ == "__main__" :
	if len(sys.argv) != 4 :
		help()
		sys.exit(1)
	if not sys.argv[2] in ALL_PORT_MODES_LIST :
		print "Port mode not in list %s" % (str(ALL_PORT_MODES_LIST))
		sys.exit(1)
	if not int(sys.argv[3]) in ALL_PORT_RATES_LIST :
		print "Rate not in list %s" % (str(ALL_PORT_RATES_LIST))
		sys.exit(1)

	tty = serial.Serial(sys.argv[1], int(sys.argv[3]))
	try :
		if sys.argv[2] == READ_PORT_MODE :
			print "Reading data from \"%s\"...\nOutput: " % (sys.argv[1]),
			while True :
				byte = tty.read()
				sys.stdout.write("\nOutput: " if byte == "\n" else byte)
				sys.stdout.flush()
		elif sys.argv[2] == WRITE_PORT_MODE :
			print "Writing data to port \"%s\"..." % (sys.argv[1])
			while True :
				sys.stdout.write("Input: ")
				tty.write(raw_input())
				tty.flush()
	except KeyboardInterrupt :
		print
		tty.close()

