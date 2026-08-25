 New-AzResourceGroup -Name {Name} -Location {Location}

 #Clear the screen
    Clear-Host

#Check Version of PowerShell
    $PSVersionTable.PSVersion
    $PSVersionTable


# Command basics
# Verb-noun
get-help get-verb | more
# To have two Poweshell in one window use ALT + the plus sign (+) 
# on the right side of the window. This will split the window into two panes. 
#You can also use the command "split-pane" to split the window.

get-verb | more
# get-verb | more is a command that will display all the verbs available in PowerShell. 
# The "more" command allows you to view the output one page at a time.

get-verb -Verb Set | Format-List
# The command "get-verb -Verb Set | Format-List" will display all the verbs that are related to the "Set" action in PowerShell.
# The output will be formatted as a list, making it easier to read and understand.

# How to get command information you may need.
Get-Command -Verb Get -Noun *DNS*
#This code helps with commands

Get-Verb -Verb M*
#This Get-Verb -Verb M* command will display all the verbs that start 
#with the letter "M" in PowerShell.

Help about* | more
#This help you get help about specific proccess in PowerShell. 
#The "about*" command will display all the help topics that start with the word 
#"about". The "more" command allows you to view the output one page at a time.

New-AzResourceGroup -Name "YourResourceGroupName" -Location "EastUS"
#Creating resource group in Azure Cloud.

az deployment group create --resource-group "YourResourceGroupName" --template-file "uploaded json file" --parameters "azure uploaded json parameter file"
#Azure deployment using the CLI powershell cmdlet. Upload the template and parameter arm files
#The arm file can be extracted or created from scratch.

az group create -l "EastUS" -n "YourResourceGroupName"
#This command will create a resource group in Azure using the Azure CLI. Using Bash.

az provider show --namespace "YourFile" -o table
#This shows namespace of the file you're looking for in Azure cloud

dotnet publish -o publish
#Write this in the terminal if you want to create a publish application
#run it within the app package opened in VS code.

bash
#If you have git installed from command line, you can use bash 
#to run bash commands in the terminal. Just type "bash" in the terminal
# and you will be able to run bash commands.


