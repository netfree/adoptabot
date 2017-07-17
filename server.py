from finch import Finch
from time import sleep

f = Finch()

zAccel = f.acceleration()[2]

i_temp = f.temperature();
i_l_light, i_r_light = f.light();

alpha_light = 0.20
alpha2_light = 0.25
alpha_temp = 0.65

while zAccel > -0.7:
    
	left_obstacle, right_obstacle = f.obstacle()
	l_light, r_light = f.light()
	temp = f.temperature()
	
	print(temp)

	if temp > i_temp + alpha_temp :
		k = 1
		while k < 11:
			f.led(141,21,165)
			f.wheels(-1,-1)
			sleep(0.2)
			f.led(255,255,255)
			f.wheels(1,1)
			sleep(0.2)
			f.wheels(1,1)
			k = k + 1	
		i_temp = f.temperature()		
	
	if i_l_light + alpha_light <= l_light or i_r_light + alpha_light <= r_light:	
			f.led(0,0,255)
			f.wheels(-1,-0.3)
			sleep(0.2)
			f.wheels(0.3,1)
			sleep(0.2)
			f.led(0,0,255)

	if i_l_light - alpha2_light > l_light or i_r_light - alpha2_light > r_light:
			f.led(0,0,0)
			f.wheels(0.4,0.4)
			sleep(7)
			f.wheels(0,0)
			f.led(0,0,0)	


	if left_obstacle:
	
		f.led(255,0,0)
		f.wheels(-0.3,-1.0)
		sleep(1.0)

	elif right_obstacle:
		
		f.led(255,255,0)
		f.wheels(-1.0, -0.3)
		sleep(1.0)

	else:
		f.wheels(1.0, 1.0)
		f.led(0,255,0)
	zAccel = f.acceleration()[2]
    
f.close()
