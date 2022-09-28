#!/bin/bash

#Script that adds a User to Linux and assigns to a group

#Ask for user and group name
userinput(){
    echo "Enter new user name:"
    read USER
    echo "Enter user's group:"
    read GROUP
    sleep 1
}

#Create user and assign group
assignuser(){
    echo "Creating user"
    sudo useradd $USER
    sleep 1
    echo "Adding to group"
    sudo groupadd $GROUP
    sudo usermod -aG $GROUP $USER
    sleep 2
    echo "User Creation Complete"
    sudo id $USER
    sleep 2
}

#Ask if they would like to create additional user
close(){
    echo "Would you like to create another User? (y/n)"
    read CLOSE
}

#Run program while close is not "n"
echo "Welcome to the User Creator"
sleep 2
echo "Create New User"
sleep 2

while [ "$CLOSE" != "n" ]
do
    userinput
    assignuser
    close
done


