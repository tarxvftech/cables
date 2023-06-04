```
tarxvf, 2023 late may early june


trapezoid microusb-b pin numberings
   ___________
  / 1 2 3 4 5  \
 /              \
/________________\

expected for normal USB
1 vcc red
2 d- white
3 d+ green
4 id n/a (used for USB OTG apparently)
5 gnd black

Reported Hytera pinout, unconfirmed (radio reference post):
Red +5v  -- +5v (probably okay to not connect...?)
White D- -- RXD
Green D+ -- TXD
Black GND -- GND


As measured on BlueMax49ers adapter (2023 May/June)
1 red
2 NC
3 green
4 white
5 black


Known good regular USB cable, same test methodology
1 red
2 white
3 green
4 NC
5 black

2023 06 03:
	It works! RadioReference is wrong, but close enough.
Working configuration:
	green to rx on usb serial adapter
	white to TX on usb serial adapter 
	(i.e. we transmit to radio on white, radio transmits to us on green)

```
