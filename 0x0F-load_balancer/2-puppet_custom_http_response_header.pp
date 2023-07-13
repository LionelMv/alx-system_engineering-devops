# Creating a custom HTTP header using Puppet

$nginx_config = @(END)
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files $uri $uri/ =404;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
}
END

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

file { '/var/www/html/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page",
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => $nginx_config,
  require => Package['nginx'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

exec { 'add_custom_header':
  command     => '/bin/sed -i "/^\s*http {/a \ \ \ \ add_header X-Served-By $var;" /etc/nginx/nginx.conf',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => Exec['add_custom_header'],
}
