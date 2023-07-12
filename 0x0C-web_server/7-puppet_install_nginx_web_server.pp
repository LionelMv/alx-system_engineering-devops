# Install Nginx web server (with Puppet)

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  enable => true,
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
  require => Package['nginx'],
}

file { '/var/www/html/404.html':
  ensure  => present,
  content => 'Ceci n\'est pas une page.',
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => '
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    location = / {
        echo "Hello World!";
    }

    location /redirect_me {
        return 301 http://example.com/destination_page;
    }

    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
}
',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

