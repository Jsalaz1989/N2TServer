# Created profile with new-item -path $profile -itemtype file -force at C:\Users\Jaime\Documents\WindowsPowerShell\Profile.ps1
# Filled it with: Set-Alias -Name n2tServer -Value C:/Users/Jaime/Documents/Nand2Tetris/N2TServer/scripts/main

"n2ts moving to root folder: $PSScriptRoot"
cd $PSScriptRoot

# TODO: see if this should go in flaskRun.ps1
$env:PYTHONDONTWRITEBYTECODE = '1'  # disables generation of .pyc files
$env:FLASK_APP = 'app'
$env:FLASK_ENV = 'development'  # TODO: figure out how to set this to 'production' during production 
$env:FLASK_CONFIG = 'config.py'


If ($args[0] -eq "venv" -and $args[1] -eq "create") { .\/venvCreate }
Else 
{
    .\/venvActivate

    If ($args[0]        -eq     "venv")
    {
        If     ($args[1]    -eq     "activate")     { .\/venvActivate }
        ElseIf ($args[1]    -eq     "update")       { .\/venvUpdate }
        ElseIf ($args[1]    -eq     "freeze")       { .\/venvFreeze }
    }
    ElseIf ($args[0]    -eq "db")
    {
        If     ($args[1]    -eq     "create")       { .\/dbCreate }
        ElseIf ($args[1]    -eq     "migrate")      { .\/dbMigrate }
        ElseIf ($args[1]    -eq     "run")          { .\/dbRun }
    }
    ElseIf ($args[0]    -eq     "flask")    { .\/flaskRun }
    ElseIf ($args[0]    -eq     "run") 
    { 
        .\/dbRun 
        .\/flaskRun
    }
}

"n2ts returning to root folder: $PSScriptRoot"
cd $PSScriptRoot