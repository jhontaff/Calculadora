pipeline{
    agent any
    triggers {
        pollSCM '*/5 * * * *'
    }
    stages {
        stage('Build') { /*extrae los cambios realizados en el repositorio */
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
                sh 'docker run -d -p 8090 --name calculadora calculadora'
            }
        }
    }
}