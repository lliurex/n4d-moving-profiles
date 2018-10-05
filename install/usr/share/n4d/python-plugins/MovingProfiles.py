
import json


class MovingProfiles:

	config_file="/etc/moving-profiles/setup.conf"
	
	
	def __init__(self):
		self.load()
		self.compute_list()
		
	#__init__
	
	def startup(self,options):
		pass
	#startup
	
	
	# **********************************
	# gets the computed list of patterns
	# Used by client
	# **********************************
	def get_list(self):
		return self.data
	#get_list
	
	
	
	# **********************************
	# gets json setup, used by settings
	# manager
	# **********************************
	def get_conf(self):
		return self.db
	#get_conf
	
	# **********************************
	# sets json setup, used by settings
	# manager. Setup is stored to disk
	# **********************************
	def set_conf(self,data):
		self.db=data
		self.save()
		self.compute_list()
	#set_conf
	
	
	# **********************************
	# internal function that recomputes
	# client list
	# **********************************
	def compute_list(self):
		self.data={"include":{},"exclude":{}}
		
		selected_id=self.db["setup"]["selected"]
		rules=[]
		
		for profile in self.db["setup"]["profiles"]:
		
			if profile["id"]==selected_id:
			
				rules=profile["rules"]
			
				break
		
		
		for rule in self.db["setup"]["rules"]:
		
			if rule["id"] in rules:
				n=0
				for regex in rule["regex"]:
				
					pattern=regex["pattern"]
					rtype=regex["type"]
					
					rname="{0}::{1}".format(rule["id"],n)
					
					if rtype=="include":
						self.data["include"][rname]=pattern
					elif rtype=="exclude":
						self.data["exclude"][rname]=pattern
				
					n=n+1
				
		
	#compute_list
	
	
	def load(self):
		f=open(self.config_file,"r")
		self.db=json.load(f)
		f.close()
	#load
	
	def save(self):
		f=open(self.config_file,"w")
		json.dump(self.db,f)
		f.close()
	#save
	


if __name__=="__main__":
	pass

