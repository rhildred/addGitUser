addGitUser
==========

add a user that can only access the server resources in their home directory through git over http

to run:

curl | bash -s stable <username>

started with:

centos 6.2 network install + web server (http://mirror.centos.org/centos/6/os/x86_64/)
added port 80 in /etc/sysconfig/iptables
ran setsebool -P httpd_enable_homedirs true
ran yum install git

in detail:

# setup user that can't login so that they can't make any changes "manually"

# apache userdir permissions

# make basic directories git and rails_apps ... also a tmp directory that we will delete

# make the bare first repo

# clone working copy in to tmp

# write the post-receive hook

# make the .htaccess with the security and the rewrite rule 

# make the .htaccess to run our script

# make our script

# commit everything and check out into the rails_apps work tree

# link in to work tree

# set the rest of the userdir permissions

# try to make the script executable in selinux (this failed)

# clean up tmp directory and make user the owner if setuid is being used, otherwise apache
