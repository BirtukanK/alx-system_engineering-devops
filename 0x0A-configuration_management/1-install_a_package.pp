# Defines a Puppet manifest to install Flask using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Exec['update_pip3'],
}

# Update pip3 to the latest version
exec { 'update_pip3':
  command => 'pip3 install --upgrade pip',
  path    => '/usr/bin',
  unless  => 'pip3 show pip | grep -q "Version: 21."',
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Exec['update_pip3'],
}
