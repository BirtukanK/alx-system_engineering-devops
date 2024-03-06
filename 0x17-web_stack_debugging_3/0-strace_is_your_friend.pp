# 0-strace_is_your_friend.pp
exec { 'fix-apache-problem':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/usr/bin', '/usr/sbin', '/bin']
  }
