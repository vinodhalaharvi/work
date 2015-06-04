import sys
import subprocess
import shlex
import os

def start_server(global_config):
	"""docstring for start_server"""
	return run("sudo su - hyperic -c 'sh %s/bin/hq-server.sh start'" %(global_config["hypericsearch.server_base_path"],))
def stop_server(global_config):
	"""docstring for stop_server"""
	return run("sudo su - hyperic -c 'sh %s/bin/hq-server.sh stop'" %(global_config["hypericsearch.server_base_path"],))
def status_server(global_config):
	"""docstring for status_server"""
	return run("sudo su - hyperic -c 'sh %s/bin/hq-server.sh status'" %(global_config["hypericsearch.server_base_path"],))
def restart_server(global_config):
	"""docstring for restart_server"""
	return run("sudo su - hyperic -c 'sh %s/bin/hq-server.sh restart'" %(global_config["hypericsearch.server_base_path"],))
def dump_server(global_config):
	"""docstring for dump_server"""
	return run("sudo su - hyperic -c 'sh %s/bin/hq-server.sh dump'" %(global_config["hypericsearch.server_base_path"],))
def get_server_config_file(global_config):
	"""docstring for print_server_config_file"""
	return run("sudo su - hyperic -c 'cat %s/conf/hq-server.conf'" %(global_config["hypericsearch.server_base_path"],))
def run(command):
	"""docstring for run"""
	print "RUNNING COMMAND .. " 
	print command
	p = subprocess.Popen(shlex.split(command), 
				stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
				stderr=subprocess.STDOUT, close_fds=True, 
				env=os.environ)
	(child_stdin, child_stdout_and_stderr) = (p.stdin, p.stdout)
	return child_stdout_and_stderr



def read_config_file(global_config, configfilepath):
	"""docstring for read_config_file"""
	with open(configfilepath) as config:
		for line in  config.readlines():
			if "=" in line and not line.startswith("#"):
				key, value = line.strip().split("=", 1)
				global_config[key] = value
	return global_config

if __name__ == '__main__':
	global_config = {}
	configfilepath = sys.argv[1]
	read_config_file(global_config, configfilepath)
	print get_server_config_file(global_config).read()
