"""
	N4D MovingProfiles plugin

	Copyright (C) 2021  Enrique Medina Gremaldos <quiqueiii@gmail.com>

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.
	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.
	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import n4d.responses
import json

class MovingProfiles:

	config_file="/etc/moving-profiles/setup.conf"
	
	def __init__(self):
		self.load()
		self.compute_list()
		
	#__init__
	
	def get_list(self):
		# Gets the computed list of patterns used by client
	
		return n4d.responses.build_successful_call_response(self.data)
	#get_list
	
	def get_conf(self):
		# Gets json setup, used by settings manager

		return n4d.responses.build_successful_call_response(self.db)
	#get_conf
	
	def set_conf(self,data):
		# Sets json setup, used by settings manager
		# Setup is stored to disk
		
		self.db=data
		self.save()
		self.compute_list()
		return n4d.responses.build_successful_call_response()
	#set_conf
	
	def compute_list(self):
		# Internal function that recomputes client list
		
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
	
