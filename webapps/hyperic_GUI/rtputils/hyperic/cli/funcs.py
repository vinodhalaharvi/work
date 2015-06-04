#!/usr/bin/python
#===============================================================================
# Script provided by Vinod Halaharvi ( vinod.halaharvi@rtpnet.net, vinod.halaharvi@gmail.com )
# RTP Network Services, Inc. / 904-236-6993 ( http://www.rtpnet.net )
# DESCRIPTION: Fuctions are invoked, each function first check if the 
#	input param "data" has a value if no then it  returns for "data request" 
# 	if data is provide then the right action is invoked passing this "data" to that function
# 	and the return value ( along with content type) is passed back to the web user. 
#===============================================================================
import  sys
import re
#from rtputils.hyperic.cli.htmlmap import *
from htmlmap import *
import json
import xml.dom.minidom
import sys
import subprocess
import shlex
import os


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


def rest(controller='user', action='list', data={}, type='get', app="hqapi1"):
    import urllib
    import urllib2
    import base64
    import re
    url = "http://localhost:7080/hqu/%s/%s/%s.hqu?" % ( app, controller, action)
    print 
    print url
    print

    if isinstance(data, dict):
	for key, value in data.items():
	    if not value:
		del data[key]
    print data
    
    if type == 'get':
	assert "hyperic_username" in os.environ
	assert "hyperic_password" in os.environ
	xmlString =  urllib2.urlopen( urllib2.Request(
        url=url,
        data=urllib.urlencode(data),
        headers={"Authorization": "Basic %s" % base64.encodestring('%s:%s' % (os.environ["hyperic_username"], os.environ["hyperic_password"])).replace('\n', '')})).read()
	return xml.dom.minidom.parseString(xmlString).toprettyxml()
    elif type == 'post':
	print data
	assert "hyperic_username" in os.environ
	assert "hyperic_password" in os.environ
	xmlString = urllib2.urlopen( urllib2.Request(
		url=url,
		data=data,
		headers={'Content-Type': 'application/xml',"Authorization": "Basic %s" % base64.encodestring('%s:%s' % (os.environ["hyperic_username"], os.environ["hyperic_password"])).replace('\n', '')})).read()
	return xml.dom.minidom.parseString(xmlString).toprettyxml()
        
import cgi
def cgiFieldStorageToDict( fieldStorage):
   """Get a plain dictionary, rather than the '.value' system used by the cgi module."""
   params = {}
   for key in fieldStorage.keys():
      params[ key ] = fieldStorage[ key ].value
   return params
        
def start_server(data):
	"""docstring for start_server"""
	if not data:
		return ("text/html", htmlmapper('start_server'))
	data =  run("sudo su - hyperic -c 'sh %s/bin/hq-server.sh start'" %("/opt/local/software/hyperic/server-5.7.1-EE", )).read()
	return ("text/html", data)

def stop_server(data):
	"""docstring for stop_server"""
	if not data:
		return ("text/html", htmlmapper('stop_server'))
	data =  run("sudo su - hyperic -c 'sh %s/bin/hq-server.sh stop'" %("/opt/local/software/hyperic/server-5.7.1-EE", )).read()
	return ("text/html", data)

def status_server(data):
	"""docstring for status_server"""
	if not data:
		return ("text/html", htmlmapper('status_server'))
	data =  run("sudo su - hyperic -c 'sh %s/bin/hq-server.sh status'" %("/opt/local/software/hyperic/server-5.7.1-EE", )).read()
	return ("text/html", data)

def restart_server(data):
	"""docstring for restart_server"""
	if not data:
		return ("text/html", htmlmapper('restart_server'))
	data =  run("sudo su - hyperic -c 'sh %s/bin/hq-server.sh restart'" %("/opt/local/software/hyperic/server-5.7.1-EE", )).read()
	return ("text/html", data)

def dump_server(data):
	"""docstring for dump_server"""
	if not data:
		return ("text/html", htmlmapper('dump_server'))
	data =  run("sudo su - hyperic -c 'sh %s/bin/hq-server.sh dump'" %("/opt/local/software/hyperic/server-5.7.1-EE", )).read()
	return ("text/html", data)

def get_server_config_file(data):
	"""docstring for print_server_config_file"""
	if not data:
		return ("text/html", htmlmapper('get_server_config_file'))
	data = run("sudo su - hyperic -c 'cat %s/conf/hq-server.conf'" %("/opt/local/software/hyperic/server-5.7.1-EE")).read()
	return ("text/html", data)

def user_list(data):
  return ("application/html", "<p></p><textarea style=\"width:100%\">" + rest('user', 'list', data) + "</textarea>")

def user_changePassword(data):
  if not data:
    return ("text/html", htmlmapper('user_changePassword'))
  return ("application/xml", rest('user', 'changePassword', data))

def user_sync(data):
  if not data: 
    return ("text/html", htmlmapper('user_sync', rest('user', 'list', data)))
  return ("text/html", '%s' % rest('user', 'sync', data['xml_to_sync'], 'post'))

def user_delete(data):
  if not data:
    return  ("text/html", htmlmapper('user_delete'))
  return ("application/xml", rest('user', 'delete', data))

def user_create(data):
  if not data:
    return ("text/html", htmlmapper('user_create'))
  return ("application/xml", rest('user', 'create', data))

def resource_getResourcePrototypes(data):
  if not data:
    return ("text/html", htmlmapper('resource_getResourcePrototypes'))
  return ("application/xml", rest('resource', 'getResourcePrototypes', data))

def resource_getResourcePrototype(data):
  if not data:
    return ("text/html", htmlmapper('resource_getResourcePrototype'))
  return ("application/xml", rest('resource', 'getResourcePrototype', data))

def resource_get(data):
  if not data:
    return ("text/html", htmlmapper('resource_get'))
  return ("application/xml", rest('resource', 'get', data))

def resource_find(data):
  if not data:
    return ("text/html", htmlmapper('resource_find'))
  return ("application/xml", rest('resource', 'get', data))
    

def resource_sync(data):
  if not data:
    return ("text/html", htmlmapper('resource_sync'))
  return ("text/html" , '<textarea name="" id="" cols="20" rows="10"><strong>%s</strong></textarea>' % rest('resource', 'sync', data['xml_to_sync'], 'post'))

def resource_delete(data):
  if not data:
    return ("text/html", htmlmapper('resource_delete'))
  return ("application/xml", '<textarea name="" id="" cols="20" rows="10"><strong>%s</strong></textarea>' % rest('resource', 'delete', data['xml_to_sync']))

def resource_move(data):
  if not data:
    return ("text/html", htmlmapper('resource_move'))
  return ("application/xml", '<textarea name="" id="" cols="20" rows="10"><strong>%s</strong></textarea>' % rest('resource', 'move', data['xml_to_sync']))

def alertdefinition_listDefinitions(data):
  if not data:
    return ("text/html", htmlmapper('alertdefinition_listDefinitions'))
  return ("application/xml", rest('alertdefinition', 'listDefinitions', data))

def alertdefinition_listTypeDefinitions(data):
  if not data:
    return ("text/html", htmlmapper('alertdefinition_listTypeDefinitions'))
  return ("application/xml", rest('alertdefinition', 'listTypeDefinitions', data))
  
def alertdefinition_delete(data):
  if not data:
    return ("text/html", htmlmapper('alertdefinition_delete'))
  return ("application/xml", rest('alertdefinition', 'delete', data))
  
def metric_getTemplates(data):
  if not data:
    return ("text/html", htmlmapper('metric_getTemplates'))
  return ("application/xml", rest('metric', 'getTemplates', data))

def metric_getMetricTemplate(data):
  if not data:
    return ("text/html", htmlmapper('metric_getMetricTemplate'))
  return ("application/xml", rest('metric', 'getTemplate', data))
  
def metric_getMetrics(data):
  if not data:
    return ("text/html", htmlmapper('metric_getMetrics'))
  return ("application/xml", rest('metric', 'getMetrics', data))
  
def metric_getMetric(data):
  if not data:
    return ("text/html", htmlmapper('metric_getMetric'))
  return ("application/xml", rest('metric', 'getMetric', data))
  
def metric_getData(data):
  if not data:
    return ("text/html", htmlmapper('metric_getData'))
  return ("application/xml", rest('metric', 'getData', data))

def metric_getGroupData(data):
  if not data:
    return ("text/html", htmlmapper('metric_getGroupData'))
  return ("application/xml", rest('metric', 'getGroupData', data))
    

def metric_getResourceData(data):
  if not data:
    return ("text/html", htmlmapper('metric_getResourceData'))
  return ("application/xml", rest('metric', 'getResourceData', data))
  
def agent_get(data):
  if not data:
    return ("text/html", htmlmapper('agent_get'))
  return ("application/xml", rest('agent', 'get', data))

def agent_ping(data):
  if not data:
    return ("text/html", htmlmapper('agent_ping'))
  return ("application/xml", rest('agent', 'ping', data))


def autodiscovery_approve(data):
  if not data:
    return ("text/html", htmlmapper('autodiscovery_approve'))
  return ("application/xml", rest('autodiscovery', 'approve', data))


def maintenance_get(data):
  if not data:
    return ("text/html", htmlmapper('maintenance_get'))
  return ("application/xml", rest('maintenance', 'get', data))

def maintenance_schedule(data):
  if not data:
    return ("text/html", htmlmapper('maintenance_schedule'))
  return ("application/xml", rest('maintenance', 'schedule', data))
  

def maintenance_unschedule(data):
  if not data:
    return ("text/html", htmlmapper('maintenance_unschedule'))
  return ("application/xml", rest('maintenance', 'unschedule', data))

def escalation_get(data):
  if not data:
    return ("text/html", htmlmapper('escalation_get'))
  return ("application/xml", rest('escalation', 'get', data))

def escalation_delete(data):
  if not data:
    return ("text/html", htmlmapper('escalation_delete'))
  return ("application/xml", rest('escalation', 'delete', data))

def group_get(data):
  if not data:
    return ("text/html", htmlmapper('group_get'))
  return ("application/xml", rest('group', 'get', data))

def group_list(data):
  if not data:
    return ("text/html", htmlmapper('group_list'))
  return ("application/xml", rest('group', 'list', data))

def group_delete(data):
  if not data:
    return ("text/html", htmlmapper('group_delete'))
  return ("application/xml", rest('group', 'delete', data))

def role_get(data):
  if not data:
    return ("text/html", htmlmapper('role_get'))
  return ("application/xml", rest('role', 'get', data))

def role_delete(data):
  if not data:
    return ("text/html", htmlmapper('role_delete'))
  return ("application/xml", rest('role', 'delete', data))

def alert_getLastAlertFixedBy(data):
  if not data:
    return ("text/html", htmlmapper('alert_getLastAlertFixedBy'))
  return ("application/xml", rest('alert', 'getLastAlertFixedBy', data))

def alert_find(data):
  if not data:
    return ("text/html", htmlmapper('alert_find'))
  return ("application/xml", rest('alert', 'find', data))

def alert_findByResource(data):
  if not data:
    return ("text/html", htmlmapper('alert_findByResource'))
  return ("application/xml", rest('alert', 'findByResource', data))

def alert_ack(data):
  if not data:
    return ("text/html", htmlmapper('alert_ack'))
  return ("application/xml", rest('alert', 'ack', data))

def alert_fix(data):
  if not data:
    return ("text/html", htmlmapper('alert_fix'))
  return ("application/xml", rest('alert', 'fix', data))

def alert_delete(data):
  if not data:
    return ("text/html", htmlmapper('alert_delete'))
  return ("application/xml", rest('alert', 'delete', data))

def metricData_get(data):
  if not data:
    return ("text/html", htmlmapper('metricData_get'))
  return ("application/xml", rest('metricData', 'get', data))

def metricData_getLast(data):
  if not data:
    return ("text/html", htmlmapper('metricData_getLast'))
  return ("application/xml", rest('metricData', 'getLast', data))

def metricData_getMulti(data):
  if not data:
    return ("text/html", htmlmapper('metricData_getMulti'))
  return ("application/xml", rest('metricData', 'getMulti', data))

def metricData_getMultiLast(data):
  if not data:
    return ("text/html", htmlmapper('metricData_getMultiLast'))
  return ("application/xml", rest('metricData', 'getMultiLast', data))

def event_find(data):
  if not data:
    return ("text/html", htmlmapper('event_find'))
  return ("application/xml", rest('event', 'find', data))

def event_findByResource(data):
  if not data:
    return ("text/html", htmlmapper('event_findByResource'))
  return ("application/xml", rest('event', 'findByResource', data))

def control_actions(data):
  if not data:
    return ("text/html", htmlmapper('control_actions'))
  return ("application/xml", rest('control', 'actions', data))

def control_history(data):
  if not data:
    return ("text/html", htmlmapper('control_history'))
  return ("application/xml", rest('control', 'history', data))

def control_execute(data):
  if not data:
    return ("text/html", htmlmapper('control_execute'))
  return ("application/xml", rest('control', 'execute', data))

def application_delete(data):
  if not data:
    return ("text/html", htmlmapper('application_delete'))
  return ("application/xml", rest('application', 'delete', data))
  
  
def sql_serverResources(data):
  if not data:
    return ("text/html", htmlmapper('sql_serverResources'))
  return ("application/javascript", '<script type="text/javascript">$("table").dataTable();</script>' + "".join(re.findall('".*?".*"(.*)"', rest('query', 'runQuery', {'query':'serverResources'}, 'get', 'query'))).replace('\\',''))
  
  
#change func.py, add a new function, add dictionary mapping
#change htmlmap.py  
#############################################  
  
def dashes(_string):
  return re.sub('\s+', '_', _string)

def spaces(_string):
  return re.sub('_', ' ', _string)
    
def check_dict(_string=None):
  if dct.has_key(dashes(_string)):
    return ('callfunction', dct[dashes(_string)])
  else:
    return ('justoutput', '<div align="center">' + '<br />'.join([spaces(key) for key in dct.keys() if re.match(".*%s.*" % dashes(_string), key)])+ '</div>') 

def todict(datastring):
  try:
    temp = [ {key:value} for key,value in [item.split('=') for item in datastring.split(",")]]
    data = {}
    for item in temp:
      data.update(item)
    return data
  except:
    raise 

def parseinput(input):
  yield re.sub(input, '\s+', '_')
  
def parseinput1(input):
  inputs  = re.split('\s+', input)
  try:
    (controller, action, data) = inputs[:3]
    return ( controller, action , data)
  except:
    pass
  try:
    (controller, action) = inputs[:2]
    return ( controller, action , {})
  except:
    pass
  print 
  print "Available commands..\n" + "<br />".join([key for key in dct.keys() if re.match('.*' + input + '.*', key )]).replace('_', ' ')
  return ( None, None , None)

def html(_string):
  #result = ""
  #result += "Content-type: text/html\n\n"
  #result += _string
  #return result
  return _string


dct = {
  'start_server': start_server,
  'stop_server': stop_server,
  'restart_server': restart_server,
  'dump_server': dump_server,
  'status_server': status_server,
  'get_server_config_file': get_server_config_file,

  'user_list': user_list,
  'user_changePassword': user_changePassword,
  'user_sync': user_sync ,
  'user_create': user_create,
  'user_delete': user_delete,
  'resource_getResourcePrototypes': resource_getResourcePrototypes,
  'resource_getResourcePrototype': resource_getResourcePrototype,
  'resource_get': resource_get,
  'resource_find': resource_find,
  'resource_sync': resource_sync,
  'resource_delete': resource_delete,
  'resource_move': resource_move, 
  'alertdefinition_listDefinitions':alertdefinition_listDefinitions,
  'alertdefinition_listTypeDefinitions':alertdefinition_listTypeDefinitions,
  'alertdefinition_delete':alertdefinition_delete,
  'metric_getTemplates': metric_getTemplates,
  'metric_getMetricTemplate':metric_getMetricTemplate,
  'metric_getMetrics':metric_getMetrics,
  'metric_getMetric':metric_getMetric,
  'metric_getData':metric_getData,
  'metric_getGroupData':metric_getGroupData,
  'metric_getResourceData':metric_getResourceData,
  'agent_get':agent_get,
  'agent_ping':agent_ping,
  'autodiscovery_approve':autodiscovery_approve,
  'maintenance_get':maintenance_get,
  'maintenance_schedule':maintenance_schedule,
  'maintenance_unschedule':maintenance_unschedule,
  'escalation_get': escalation_get,
  'escalation_delete': escalation_delete,
  'group_get': group_get,
  'group_list': group_list,
  'group_delete': group_delete,
  'role_get': role_get,
  'role_delete': role_delete,
  'alert_getLastAlertFixedBy': alert_getLastAlertFixedBy,
  'alert_find': alert_find,
  'alert_findByResource': alert_findByResource,
  'alert_ack': alert_ack,
  'alert_fix': alert_fix,
  'alert_delete': alert_delete,
  'metricData_get': metricData_get,
  'metricData_getLast': metricData_getLast,
  'metricData_getMulti': metricData_getMulti,
  'metricData_getMultiLast': metricData_getMultiLast,
  'event_find': event_find,
  'event_findByResource': event_findByResource,
  'control_actions': control_actions,
  'control_history': control_history,
  'control_execute': control_execute,
  'application_delete': application_delete,
  'sql_serverResources': sql_serverResources,
}  
