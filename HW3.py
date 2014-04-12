def diff_time( old , new ):
	old_sec = int(old[6:8])
	old_min = int(old[3:5])
	old_hr = int(old[0:2])
	old_time = old_sec + old_min*60 + old_hr*3600
	
	new_sec = int(new[6:8])
	new_min = int(new[3:5])
	new_hr = int(new[0:2])
	new_time = new_sec + new_min*60 + new_hr*3600
	
	return new_time - old_time


if __name__ == "__main__":
	a = diff_time('00:00:10', '00:01:05')
	if a == 55:
		print "Succ"
	else:
		print "Fail"



###in other files you can use this function:
#import HW3
#print HW3.diff_time('00:00:08' , '00:01:10')



###test:
#old = '00:00:10'
#old_sec = int(old[6:8])
#old_min = int(old[3:5])
#old_hr = int(old[0:2])
#old_time = old_sec + old_min*60 + old_hr*3600
#print old_time
#
#new = '00:01:05'
#new_sec = int(new[6:8])
#new_min = int(new[3:5])
#new_hr = int(new[0:2])
#new_time = new_sec + new_min*60 + new_hr*3600
#print new_time

