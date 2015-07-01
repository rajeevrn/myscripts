# Standard conditions apply. Please test it before using. Not responsible for any damage. 
# virtualtraces.com

#This script checks the virtual machine if it is in shutdown state and poweron if yes.
# else this will shutdown and wait for it to shutdown and then poweron.
# Create a text file containing the list of virtual machines on which we need to perform the operations.


Connect to vCenter server
$vcerver= Read-host "Enter the vCenter name to connect"
Connect-VIServer $vcserver

 
## Read in List
$vmlist = Get-Content C:\vmlist.txt
write-host "$vmlist"

 
## Shut down VMs

foreach ($vm in $vmlist)
{

if (get-VM $vm |where{$_.Powerstate -eq "PoweredOn"})
{
Shutdown-VMGuest $vm -Confirm:$false
}
do {
Write-host "waiting for" $vm "to shutdown"
sleep 5
}

until
(get-VM $vm |where {$_.Powerstate -eq "PoweredOff"})
sleep 3

Write-host "$vm is shutdown now , starting $vm"
Start-VM $vm 
}
