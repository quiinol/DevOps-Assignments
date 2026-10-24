# Assignment 8: Jenkins Hello World Job

## Objective
Create a GitHub repository containing a shell script and configure a Jenkins Freestyle job to execute it.

## GitHub Repository
https://github.com/quiinol/devops-sample-code

## Script
The file `hello-world.sh` contains:

    #!/bin/bash
    echo "Hello, Jenkins!"

## Jenkins Configuration
- Job name: HelloWorld
- Job type: Freestyle project
- Source Code Management: Git
- Repository: https://github.com/quiinol/devops-sample-code.git
- Branch: */main
- Build step: Execute shell
- Command: sh hello-world.sh

## Expected Output
    Hello, Jenkins!
    Finished: SUCCESS

## Result
The Jenkins Freestyle job successfully cloned the GitHub repository and executed the shell script.
