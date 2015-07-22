from ipaddress import *
import ipaddress
import sys
# Author Vinod Halaharvi

def print_IPV4_network(network, hosts=True, othernetwork=None, verbose=False):
	"""docstring for print_IPV4_network"""
	if verbose:
		for attr in ("version",
			"max_prefixlen",
			"is_multicast",
			"is_private",
			"is_unspecified",
			"is_reserved",
			"is_loopback",
			"is_link_local",
			"network_address",
			"broadcast_address",
			"hostmask",
			"with_prefixlen",
			"compressed",
			"exploded",
			"with_netmask",
			"with_hostmask",
			"num_addresses",
			"prefixlen",):
			print  "%s: %s" % (attr, getattr(network, attr))
	if hosts:
		print
		print "Hosts:"
		for host in  network.hosts():
			print host
	print


def print_IPV4_address(address):
	"""docstring for print_IPV4_address"""
	for attr in (
		    "version",
		    "max_prefixlen",
		    "compressed",
		    "exploded",
		    "packed",
		    "is_multicast",
		    "is_private",
		    "is_unspecified",
		    "is_reserved",
		    "is_loopback",
		    "is_link_local",
		):
		print  "%s: %s" % (attr, getattr(address, attr))
	print

def summarize_ip_address_range(first, last):
	"""docstring for summarize_ip_address_range"""
	return [ipaddr for ipaddr in ipaddress.summarize_address_range(
		ipaddress.IPv4Address('192.0.2.0'),
		ipaddress.IPv4Address('192.0.2.130'))]

if __name__ == '__main__':
	print_IPV4_network(ip_network('192.0.2.0/24'), verbose=True)	
	sys.exit(0)
	for net in  summarize_ip_address_range('192.0.2.0', '192.0.2.130'):
		print net


	for address in  IPv4Network('192.168.0.0/26'):
		print_IPV4_address(address)

	for net in  list(ip_network('192.0.2.0/24').subnets(prefixlen_diff=4)):
		print net

	for host in ip_network('192.0.2.0/24').hosts():
		print host

