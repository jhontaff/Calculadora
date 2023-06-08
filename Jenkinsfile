pipeline{
    agent any

    stages {
        stage('Desarrollo') { /*extrae los cambios realizados en el repositorio */
            steps {
                echo "Actualizando datos repositorio"
                git branch: 'dev', credentialsId: 'jenkins-token', url: 'https://github.com/jhontaff/Calculadora.git'
                sh '''
                echo "Datos cargados"
                '''
                }

        }
        stage('QA'){
            steps{
                echo "Probando..."
                sh '''
                echo "Realizando testeo"
                '''
            }
        }
        stage('Despliegue'){
            steps{
                echo "Desplegando..."
                sh '''
                echo "Realizando despliegue"
                '''
            }
        }
    }
}