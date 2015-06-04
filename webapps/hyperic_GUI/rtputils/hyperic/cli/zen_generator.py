def zencoder(dct, action=""):
  str = ""
  keylabel = ""
  str += ".form[align='center']>form[action='/cgi-bin/hyperic-cli.py' method='POST' align='center']>fieldset[align='right' style='width: 40%;']>input[type=hidden name=hidden value=hidden]+input[type=hidden name=actionName value=" + action + "]+legend{Fields marked * are Necessary:}+"
  for key, values in dct.items():
    flag, type = values
    if flag == 'True':
      keylabel = key + '*'
    else:
      keylabel = key
    str += "(label[for='%s']{%s:}+input[type='%s'name='%s'id='%s']+br)+" % (key, keylabel, type, key, key)
  str += r"+input[type='submit'name='submit'id='submit']+br"
  return str

def zen_generator(_tuple):
  _string, dct = _tuple
  print ',',
  print "'%s': r'''" % _string
  print zencoder(dct, _string)
  print "'''"


dct_list = [
('stop_server',
{}),
('start_server',
{}),
('status_server',
{}),
('dump_server',
{}),
('restart_server',
{}),
('resource_get',
{
  'id' : ('False', 'text'),
  'platformName' : ('False', 'text'),
  'verbose' : ('False', 'text'),
  'children' : ('False', 'text'),
}),
('resource_find',
{
  'agentId' : ('False', 'text'),
  'prototype' : ('False', 'text'),
  'description' : ('False', 'text'),
  'verbose' : ('False', 'text'),
  'children' : ('False', 'text'),
}),
('resource_delete',
{
  'id' : ('True', 'text'),
}),
('resource_move',
{
  'targetId' : ('True', 'text'),
  'destinationId' : ('True', 'text'),
}),
('alertdefinition_listDefinitions', {
  'alertNameFilter' : ('False', 'text'),
  'resourceNameFilter' : ('False', 'text'),
  'groupName' : ('False', 'text'),
  'resourceId' : ('False', 'text'),
  'escalationId' : ('False', 'text'),
  'excludeTypeBased' : ('False', 'text'),
}),
('alertdefinition_listTypeDefinitions',{
  'excludeIds' : ('False', 'text'),
}), 
('alertdefinition_delete', {
  'id' : ('True', 'text'),
}),
('metric_getTemplates', { 
  'prototype' : ('True', 'text'),
}),
('metric_getMetricTemplate', {
  'id' : ('True', 'text'),
}),
('metric_getMetrics', {
  'resourceId' : ('True', 'text'),
  'enabled' : ('False', 'text'),
}),
('metric_getMetric', {
  'id' : ('True', 'text'),
}),
('metric_getData', 
{
  'metricId' : ('True', 'text'),
  'start' : ('True', 'text'),
  'end' : ('True', 'text'),
}),
('metric_getGroupData',  {
  'groupId' : ('True', 'text'),
  'templateId' : ('True', 'text'),
  'start' : ('True', 'text'),
  'end' : ('True', 'text'),
}),
('metric_getResourceData', {
  'ids' : ('True', 'text'),
  'templateId' : ('True', 'text'),
  'start' : ('True', 'text'),
  'end' : ('True', 'text'),
}),
('agent_get', {
  'id' : ('True', 'text'),
}),
('agent_transferPlugin', {
 'agentAddress': ('False', 'text'),
 'agentPort': ('False', 'text'),
 'fqdn': ('False', 'text'),
 'id': ('True', 'text'),
 'plugin': ('False', 'text'),
}),
('agent_ping', {
'id' : ('True', 'text'),
}),
('autodiscovery_approve',{
  'id' : ('True', 'text'),
}),
('maintenance_get' , {
  'groupId' : ('True', 'text'),
}),
('maintenance_schedule', {
  'groupId' : ('True', 'text'),
  'start' : ('True', 'text'),
  'end' : ('True', 'text'),
}),
('maintenance_unschedule', {
  'groupId' : ('True', 'text'),
}),


('escalation_get', {
  'name' : ('True', 'text'),
}),
('escalation_delete', {
  'id' : ('True', 'text'),
}),
('group,get', {
  'name' : ('True', 'text'),
}),
('group_list', {
  'compatible' : ('False', 'text'),
}),
('group_delete', { 
'id' : ('True', 'text'),
}),
('role_get', {
  'name' : ('True', 'text'),
}),
('role_delete', {
  'id' : ('True', 'text'),
}),
('alert_getLastAlertFixedBy', {
  'id' : ('True', 'text'),
}),
('alert_find', {
  'begin' : ('True', 'text'),
  'end' : ('True', 'text'),
  'count' : ('True', 'text'),
  'severity' : ('True', 'text'),
  'inEscalation' : ('False', 'text'),
  'notFixed' : ('False', 'text'),
}),
('alert_findByResource', {
  'resourceId' : ('True', 'text'),
  'begin' : ('True', 'text'),
  'end' : ('True', 'text'),
  'count' : ('True', 'text'),
  'severity' : ('False', 'text'),
  'inEscalation' : ('False', 'text'),
  'notFixed' : ('False', 'text'),
}),
('alert_ack', {
  'id' : ('True', 'text'),
  'reason' : ('True', 'text'),
  'pause' : ('False', 'text'),
}),
('alert_fix', {
  'id' : ('True', 'text'),
}),
('alert_delete', {
  'id' : ('True', 'text'),
}),
('metricData_get', {
  'id' : ('True', 'text'),
  'start' : ('True', 'text'),
  'end' : ('True', 'text'),
}),
('metricData_getLast', {
  'id' : ('True', 'text'),
}),
('metricData_getMulti', {
  'id' : ('True', 'text'),
  'start' : ('True', 'text'),
  'end' : ('True', 'text'),
}),
('metricData_getMultiLast', {
  'id' : ('True', 'text'),
}),
('event_find', {
  'begin' : ('True', 'text'),
  'end' : ('True', 'text'),
  'count' : ('True', 'text'),
  'status' : ('False', 'text'),
  'type' : ('False', 'text'),
}),
('event_findByResource', {
  'resourceId' : ('True', 'text'),
  'begin' : ('True', 'text'),
  'end' : ('True', 'text'),
}),
('control_actions', {
  'resourceId' : ('True', 'text'),
}),
('control_history', {
  'resourceId' : ('True', 'text'),
}),
('control_execute', {
  'resourceId' : ('True', 'text'),
  'action' : ('True', 'text'),
  'arguments' : ('False', 'text'),
}),
('application_delete', {
  'id' : ('True', 'text'),
}),
]

map (zen_generator, dct_list)
