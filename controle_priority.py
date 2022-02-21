
from re import T
import time
import datetime


################################################################################
#   Handle all connections and rights for the server
################################################################################
class my_task():

	name = None
	priority = -1
	period = -1
	execution_time = -1
	last_deadline = -1
	last_execution_time = None
	# global tank_stock
	# tank_stock=0
    	############################################################################
	def __init__(self, name, priority, period, execution_time, last_execution, state, oil, oilNeeded):

		self.name = name
		self.priority = priority
		self.period = period
		self.execution_time = execution_time
		self.last_execution_time = last_execution
		self.state = state 
		self.oil = oil 
		self.oilNeeded = oilNeeded


    	############################################################################
	def run(self):
		
		
		global tank_stock
		global roues_stock
		global moteur_stock

		# Update last_execution_time
		self.last_execution_time = datetime.datetime.now()

		print("\t" + self.name + " : Starting task (" + self.last_execution_time.strftime("%H:%M:%S") + ")")
		if(self.name == "Pump_1" or self.name == "Pump_2"):
			if(tank_stock < 50):
				tank_stock += self.oil
				print("La pompe ajoute :"+str(self.oil)+", le tank contient donc :" + str(tank_stock))
			else : 
				print("Le tank est rempli")
		
		if(self.oilNeeded > 0): 
			tank_stock -= self.oilNeeded
			if(self.name == "Machine_1"):
				roues_stock += 1
				print("Il y a "+str(roues_stock)+" roues dans le stock")
			if(self.name == "Machine_2"):
				moteur_stock += 1
				print("Il y a "+str(moteur_stock)+" moteur dans le stock")


			if(tank_stock<=0):
				print("rechargement du tank")
				pump_list = []
				pump_list.append(my_task(name="Pump_1", priority = 2, period = 5, execution_time = 2, last_execution = last_execution, state="", oil=10, oilNeeded=None))
				pump_list.append(my_task(name="Pump_2", priority = 1, period = 15, execution_time = 3, last_execution = last_execution, state="", oil=20, oilNeeded=None))
				task_to_run = None 
				for current_task in pump_list:
					task_to_run = current_task
					task_to_run.run()
			
			print("La "+str(self.name)+" utilise : "+str(self.oilNeeded)+" d'huile du tank, il reste donc "+str(tank_stock)+" d'huile")

	
		time.sleep(self.execution_time)
		current_hour = datetime.datetime.now()
		print("\t" + self.name + " : Ending task (" + current_hour.strftime("%H:%M:%S") + ")")



####################################################################################################
#
#
#
####################################################################################################
if __name__ == '__main__':


	last_execution = datetime.datetime.now()
	
	# global tank_stock
	tank_stock = 0
	roues_stock = 0 
	moteur_stock = 0 	

	# Instanciation of task objects
	task_list = []
	task_list.append(my_task(name="Pump_1", priority = 2, period = 5, execution_time = 2, last_execution = last_execution, state="", oil=10, oilNeeded=None))
	task_list.append(my_task(name="Pump_2", priority = 1, period = 15, execution_time = 3, last_execution = last_execution, state="", oil=20, oilNeeded=None))
	task_list.append(my_task(name="Machine_1", priority = 3, period = 5, execution_time = 5, last_execution = last_execution, state="", oil=None, oilNeeded=25))
	task_list.append(my_task(name="Machine_2", priority = 4, period = 3, execution_time = 3, last_execution = last_execution, state="", oil=None, oilNeeded=5))

	n = len(task_list)
	for i in range(n):
		for j in range(0, n-i-1):
			if task_list[j].priority > task_list[j+1].priority :
				task_list[j], task_list[j+1] = task_list[j+1], task_list[j]


	#for x in range(n):
		time_now = datetime.datetime.now()
		
		print("\nScheduler tick : " + time_now.strftime("%H:%M:%S"))
		for current_task in task_list:
			task_to_run = current_task
			task_to_run.run()

		# # Find the task with Earliest deadline

		# task_to_run = None


		# for current_task in task_list:
		# 	current_priority = current_task.priority 
		# 	for next_task in task_list:
		# 		if (current_task.priority < next_task.priority):
		# 			task_to_run = current_task
		# Start task
		# 			
	



