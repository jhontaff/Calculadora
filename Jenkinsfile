pipeline{
    agent any
    triggers {
        pollSCM '*/5 * * * *'
    }
    stages {
        stage('Desarrollo') {
            steps {
                echo "Actualizando datos repositorio"
                bat "docker build -t calculadora ."
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
                bat "docker run -d -p 80:80 --name calculadora calculadora"
            }
        }
    }
}