$apiKey = ""
$workspacesparams = @{
    Headers = @{'X-Api-Key'="$apiKey"}
    Method = 'Get'
    URI = "https://api.getpostman.com/workspaces"
}
$workSpaces = Invoke-RestMethod @workspacesparams
$chosenWorkspace= ($workSpaces.workspaces | Out-GridView -PassThru  -Title 'Please Choose a workspace')
$workspaceparams = @{
    Headers = @{'X-Api-Key'="$apiKey"}
    Method = 'Get'
    URI = "https://api.getpostman.com/workspaces/$($chosenWorkspace.id)"
}
$workspace = Invoke-RestMethod @workspaceparams
$chosenCollection= ($workspace.workspace.collections | Out-GridView -PassThru  -Title 'Please Choose a Collection')
$chosenEnvironment= ($workspace.workspace.environments | Out-GridView -PassThru  -Title 'Please Choose an Environment')
$newmanCommand = "newman run https://api.getpostman.com/collections/$($chosenCollection.uid)?apikey=$apiKey --environment https://api.getpostman.com/environments/$($chosenEnvironment.uid)?apikey=$apiKey --bail"
Write-Host $newmanCommand 
Start-Process cmd -Argument "/k $newmanCommand"