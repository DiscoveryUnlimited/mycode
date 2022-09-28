#!/bin/bash
# script that adds a User to Linux and assigns to a group

#Ask for user and group name
userinput(){
    echo "Enter new user name:"
    read USER
    echo "Enter user's group:"
    read GROUP
}

#Create user and assign group
assignuser(){
    echo "Creating user"
    sudo useradd $USER
    echo "Adding to group"
    sudo groupadd $GROUP
    sudo usermod -aG $GROUP $USER
    echo "Complete"
    sudo id $USER
}

#Ask if they would like to create additional user
close(){
    echo "Would you like to create another User? (y/n)"
    read CLOSE
}

#Run program if close
echo "Create New User"
sleep 1

while [ "$CLOSE" != "n" ]
do
    userinput
    assignuser
    close
done


