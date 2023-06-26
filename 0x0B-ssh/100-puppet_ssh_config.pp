# Set up SSH authorized key
ssh_authorized_key { 'ubuntu':
  ensure => present,
  user   => 'ubuntu',
  type   => 'ssh-rsa',
  key    => 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN',
}

# Configure SSH client
file { '/etc/ssh/ssh_config':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => @(END),
    Host 34.239.207.160
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
  END
  notify  => Service['ssh'],
}

service { 'ssh':
  ensure => running,
  enable => true,
}
