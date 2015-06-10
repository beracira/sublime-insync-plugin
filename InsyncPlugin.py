import sublime, sublime_plugin
import os

class InsyncCommand(sublime_plugin.WindowCommand):
	def run(self, cmd = None):
		if cmd == "pause":
			os.system("insync pause_syncing")
		if cmd == "resume":
			os.system("insync resume_syncing")
