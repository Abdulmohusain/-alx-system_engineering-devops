# Install a package
package { 'python3':
  ensure   => '3.8.10'
}

package { 'python3-pip':
  ensure   => installed
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3'
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
