# Created profile with new-item -path $profile -itemtype file -force at C:\Users\Jaime\Documents\WindowsPowerShell\Profile.ps1
# Filled it with: Set-Alias -Name n2ts -Value C:/Users/Jaime/Documents/Nand2Tetris/N2TServer/scripts/main

$env:PYTHONDONTWRITEBYTECODE = '1'  # disables generation of .pyc files
$env:FLASK_APP = '../server'
$env:FLASK_ENV = 'development'
$env:FLASK_CONFIG = 'config.py'

"n2ts moving to root folder: $PSScriptRoot"
cd $PSScriptRoot


If ($args[0] -eq "venv" -and $args[1] -eq "create") { .\/venvCreate }
Else 
{
    .\/venvActivate

    If ($args[0]        -eq "venv")
    {
        If     ($args[1]    -eq "activate")     { .\/venvActivate }
        ElseIf ($args[1]    -eq "update")       { .\/venvUpdate }
        ElseIf ($args[1]    -eq "freeze")       { .\/venvFreeze }
    }
    ElseIf ($args[0]    -eq "db")
    {
        If     ($args[1]    -eq "create")       { .\/dbCreate }
        ElseIf ($args[1]    -eq "migrate")      { .\/dbMigrate }
        ElseIf ($args[1]    -eq "run")          { .\/dbRun }
    }
    ElseIf ($args[0]    -eq "flask") { .\/flaskRun }
    ElseIf ($args[0]    -eq "run") 
    { 
        .\/dbRun 
        .\/flaskRun
    }
}

"n2ts returning to root folder: $PSScriptRoot"
cd $PSScriptRoot