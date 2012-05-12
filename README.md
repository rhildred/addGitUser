addGitUser
==========

add a user that can only access the server resources in their home directory through git over http

to run:

  curl https://raw.github.com/rhildred/addGitUser/master/addGitUser | bash -s

started with:

an account set up under cpanel that I can ssh to, mod_auth_digest installed and activated

in detail:

* make basic directories git and rails_apps ... also a tmp directory that we will delete

* make the bare first repo

* clone working copy in to tmp

* write the post-receive hook

* make the .htaccess with the security and the rewrite rule 

* make the .htaccess to run our script

* make our script

* commit everything and check out into the rails_apps work tree

* link in to work tree

* set the rest of the userdir permissions

* clean up tmp directory
