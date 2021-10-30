pipeline {
    agent any
    parameters {
        string(name: 'StoryLine', defaultValue: '', description: 'How should I greet the world?')
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
                    jiraStoryList = sh(script: "python jiraStory.py ${params.StoryLine}", returnStdout: true).toString().trim()
                    echo 'Story ID: ${jiraStoryList}'
                }
            }
        }
        stage('Approval') {
            steps {
                script {
                    def userInput
                    try {
                        userInput = input(
                            id: 'Proceed1', message: 'Was this successful?', parameters: [
                            [$class: 'BooleanParameterDefinition', defaultValue: true, description: '', name: 'Please confirm you agree with this']
                            ])
                    } catch(err) { // input false
                        def user = err
                        userInput = false
                        echo "Aborted by: [${user}]"
                    }
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
