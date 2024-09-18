# 101-setup_web_static.pp
class web_static {
  # Install nginx
  package { 'nginx':
    ensure => 'installed',
  }

  # Create directories
  file { '/data':
    ensure => 'directory',
  }

  file { '/data/web_static':
    ensure => 'directory',
  }

  file { '/data/web_static/releases':
    ensure => 'directory',
  }

  file { '/data/web_static/shared':
    ensure => 'directory',
  }

  # Create a test HTML file
  file { '/data/web_static/releases/test/index.html':
    content => '<html><head></head><body>Holberton School</body></html>',
  }

  # Create a symbolic link
  file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test',
  }

  # Allow nginx to serve static content
  file { '/etc/nginx/sites-available/default':
    content => "server {
        listen 80 default_server;
        listen [::]:80 default_server;

        server_name _;

        location / {
                try_files \$uri \$uri/ =404;
        }

        location /hbnb_static {
                alias /data/web_static/current/;
        }
    }",
    notify => Service['nginx'],
  }

  # Ensure nginx service is running
  service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => File['/etc/nginx/sites-available/default'],
  }
}

include web_static

