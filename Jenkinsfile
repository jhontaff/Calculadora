pipeline{
    agent {
        docker {
            image 'docker:24.0.2'
            label 'jenkins-docker'
        }
    }
    triggers {
        pollSCM '*/5 * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Actualizando datos repositorio"
                sh 'docker build -t calculadora .'
                }

        }
        stage('QA'){
            steps{
                echo "Probando..."
            }
        }
        stage('Despliegue'){
            steps{
                echo "Desplegando..."
                sh 'docker run -d -p 2020:80 --name calculadora calculadora'
            }
        }
    }
}