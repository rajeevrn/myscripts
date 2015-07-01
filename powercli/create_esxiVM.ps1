#Conditions: Not responsible for any damage

#Purpose:
        #This script creates multiple ESXi VMs with GOS as "ESXi 5.5"

#eg:- The below script creates 4 ESXivms with names esxi551 to esxi554
 

#Connect with me - virtualtraces.com

#----------------------------- script start ------------------------------


#Configurations

$esx="<host name>"
$user="root"
$password='<passwd>'
$VMprefix="esxi55" 

#For loop for creating ESXiVMs and setting them as "ESXi5.x"

1..4 | foreach{
$y="{0:D1}" -f $_
$VM_Name = $VMprefix + $y
}

Connect-VIServer -Server $esx -User $user -Password $password -ErrorAction Stop
New-VM -VMHost $esx -Name $VM_Name -NumCpu 2 -MemoryGB 8 -DiskGB 8 -GuestId "rhel5_64Guest" -Datastore "400GB" -Version v9 -NetworkName "VM Network"
set-VM -VM  $VM_Name -GuestId "vmkernel5Guest" -Confirm:$False 
start-vm -VM $VM_Name

