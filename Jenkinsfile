pipeline{
    agent any

    stages {
        stage('Desarrollo') { /*extrae los cambios realizados en el repositorio */
            steps {
                echo "Actualizando datos repositorio"
                git branch: 'dev', credentialsId: 'jenkins-token', url: 'https://github.com/jhontaff/Calculadora.git'
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
            }
        }
    }
}