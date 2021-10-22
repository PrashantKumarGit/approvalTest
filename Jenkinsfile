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
                    def para
                    try{
                    para = input (
                            message: "Can we Proceed?",
                            submitter: "prashantkumar",
                            parameters: [text(name: 'PERSON', defaultValue: 'ABC', description: 'Member'), booleanParam(name: 'rd1', defaultValue: true, description: 'Proceed'), booleanParam(name: 'rd1', defaultValue: false, description: 'Abort')]
                       )
                        echo para['rd1']
                    } catch(all) {
                        echo "${para}, is aborted."
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
