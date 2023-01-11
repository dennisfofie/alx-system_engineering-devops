# This is file am trying to install django using puppet script

package {"django":
	ensure => "4.0.0",
	provider => "pip"
}
