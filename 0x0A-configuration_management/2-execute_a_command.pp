# Execute a command
exec { 'pkill killnow':
	path => '/usr/bin:/usr/sbin:/bin'
}

