# server
The django server which will run on the AWS EC2 server to serve website.

Using this website, the users can see a description of the project and a short resume of each team member.

A download page allow the users to get the sphr-controller software. 

All the data is stored into a postgres database. 

##Known issues:
- The path to the stored file in the database is not good so the images are not stored in the right place and are not accessible from the website.
- Some responsivity issues (on mobiles, there is supposed to be an icon to access the links in the navbar but there is not)
- Display issues (picture is too big for the header in the team view, pictures of the features are not properly aligned)

