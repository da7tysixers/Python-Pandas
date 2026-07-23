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






