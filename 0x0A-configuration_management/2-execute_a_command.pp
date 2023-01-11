# This puppet file kill a procees
exec {"pkill":
	command => "pkill -f killmenow",
	path => ["/usr/bin", "/usr/sbin"]
}
