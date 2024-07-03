# Execute a command
exec { 'pkill_killnow':
  command => '/usr/bin/pkill killnow',
  path    => '/usr/bin:/usr/sbin:/bin',
}
