pipeline{
    agent any
    triggers {
        pollSCM '*/5 * * * *'
    }
    stages {
        stage('Build') { /*extrae los cambios realizados en el repositorio */
            steps {
                echo "Actualizando datos repositorio"
                git branch: 'dev', credentialsId: 'jenkins-token', url: 'https://github.com/jhontaff/Calculadora.git'
                sh 'docker build -t calculadora'
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
                sh 'docker run -d -p 2020:80 calculadora'
            }
        }
    }
}