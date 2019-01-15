#!/bin/sh

#References 
	# Powershell on Linux : https://github.com/PowerShell/PowerShell/blob/master/docs/installation/linux.md
	# Powercli on Linux: https://code.vmware.com/web/dp/tool/vmware-powercli/10.0.0

echo "Checking the  code name of the Ubuntu 16.04" 
mystatus=`lsb_release -c | awk -F: '{print $2}' | xargs`


if [ "$mystatus" =  "xenial" ]; then
	echo "Starting the Installation of Powershell:-->"
	echo "Import the public repository GPG keys:-->"
		curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
	echo "Register the Microsoft Ubuntu repository:-->"
		curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | sudo tee /etc/apt/sources.list.d/microsoft.list
	echo "Update the list of products:-->"
		sudo apt-get update
	echo  "Installing PowerShell::-->"
		sudo apt-get install -y powershell
		sleep 5 
	echo "Printing the Powershell Version:-->"
		pwsh --version
		sleep 5
	echo "Setting the Repo to Trusted:-->"
		pwsh -c Set-PSRepository -Name PSGallery -InstallationPolicy Trusted
	echo "Getting the Repo Information:-->"
		pwsh -c Get-PSRepository		
	echo "Installing Powercli::--> This might take time"
		pwsh -c Install-Module VMware.PowerCLI -Scope CurrentUser 
	echo "Check the installation is completed:-->"
		pwsh -c Get-Module VMware.* -ListAvailable
else
	echo "It is not the correct version of Ubuntu 16.04"
fi