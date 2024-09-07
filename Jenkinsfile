pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "ruvini925/ws-coursework-web"
    }

    stages {
        stage('Checkout Code') {
            steps {
                retry(3) {
                    git branch: 'main', url: 'https://github.com/Ruvini-Rangathara/WS-Coursework.git'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh "docker build -t ${DOCKER_IMAGE}:${env.BUILD_ID} ."
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'test-dockerhubpassword', variable: 'test-dockerhubpass')]) {
                    script {
                        // Login to Docker Hub

                        sh "echo ${dockerhubPassword} | docker login -u ruvini925 --password-stdin"
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Push Docker image to Docker Hub
                    sh "docker push ${DOCKER_IMAGE}:${env.BUILD_ID}"
                }
            }
        }
    }

    post {
        always {
            // Logout from Docker Hub
            sh 'docker logout'
        }
        success {
            // Notification on success
            echo "Docker image built and pushed successfully!"
        }
        failure {
            // Notification on failure
            echo "Failed to build or push the Docker image."
        }
    }
}
