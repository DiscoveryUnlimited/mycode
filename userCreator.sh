#!/bin/bash

#Script that adds a User to Linux and assigns to a group

#Ask for user and group name
userinput(){
    echo "Enter new user name:"
    read USER
    echo
    echo "Enter user's group:"
    read GROUP
    echo
    echo "...................."
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
    echo
    echo "...................."
    echo "User Creation Complete:"
    echo
    sudo id $USER
    sleep 1
    echo
    echo "...................."
}

#Ask if they would like to create additional user
close(){
    echo "Would you like to create another User? (y/n)"
    read CLOSE
    echo
}

#Run program while close is not "n"
echo "Welcome to the User Creator"
sleep 2
echo
echo "...................."
echo "Create New User"
echo

while [ "$CLOSE" != "n" ]
do
    userinput
    assignuser
    close
done

sleep 1
echo "...................."
echo "Exiting Application"
echo
