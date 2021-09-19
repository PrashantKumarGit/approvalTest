pipeline {
    agent any
    parameters {
        string(name: 'Greeting', defaultValue: 'Hello', description: 'How should I greet the world?')
    }
    environment {
                jiraStoryList = "foo"
     }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Get Jira Story') {
            steps {
                script {
                    jiraStoryList = sh(script: "python jiraStory.py ${params.Greeting}", returnStdout: true).toString().trim()
                    echo 'Story ID: ${jiraStoryList}'
                }
            }
        }
        stage('Approval') {
            steps {
                echo 'Approving...'
                timeout(time: 1, unit: 'DAYS') {
                    input message: "${jiraStoryList}", submitter: 'prashantkumar'
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
