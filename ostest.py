#! python3
#########################################
#  	  BASIC_OF_OS_MODULE_IN_PYTHON      #
#					   					#
#    		Created On 					#
#   	  1-January-2022				#
#										#
#		Made by:					    #
#         		-vivek choudhary 		#
#########################################
import os
from datetime import datetime

print(os.getcwd())              					#// To print current working dir
os.chdir('c:/Users/vivek.Choudhary/Desktop')	 	#// To change the dir
print(os.listdir())			  						#// To list the dir item
# os.makedirs('os-demo-2/osq')						#// To Make dir
# os.removedirs('os-demo-2/osq')					#// TO Remove dir
# os.renames(old, new)								#// To rename file 

# print(os.stat('shell.phtml').st_size) 			#// To print size	
#To check modified time 
# mod_time = os.stat('try.py').st_mtime
# print(datetime.fromtimestamp(mod_time))

#To apply filter for all file directly
# for dirpath, dirnames, filenames in os.walk('c:/Users/vivek.Choudhary/Desktop/tryhackme.com'):
# 	print('Current Path:', dirpath)
# 	print('Directories:', dirnames)
# 	print('Files:', filenames)
# 	print() 

print(os.environ.get('TEMP')) 	#// for envi which is check in sys properties of my computer

#To create file with less error
file_path = os.path.join(os.environ.get('TEMP') , 'vivektmp.txt')
with open(file_path, 'w') as f:
	f.write('TESTING THE CONTENT.....')
##some usefull os.path var#
os.path.exists('check.txt')       #//checking file existance
os.path.isdir('/check')			#//checking that dir exist or not in True or False result
os.path.isfile('check.txt')		#//checking that file exist or not in True or False result

##----------------END_OF_BASIC--------------#


########################################
#.ignore extra work or some random work #
# For graphic visual of code			#
#import snoop @snoop					#
#import heartrate						#
#heartrate.trace (browser = True) 	 	#
#from loguru import logger 				#
#########################################