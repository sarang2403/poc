pipeline {
    agent any

    stages {

        // Stage 1 : Configure the DHCP Server
        stage('Configure DHCP Server') {
            steps {
                        sh '''
                        python3 configure_dhcp.py
                        '''
                    }
        }
    

        // Stage 2 : Check Reachability to Management Network
        stage('Check Reachability') {
            steps { 
                sh '''
                python3 check_connectivity.py
                '''
            }
        }

        // Stage 3 : Configure ISP Core
        stage('Configure ISP Core') {
            steps { 
                sh '''
                python3 configure_transit_network.py
                '''
            }
        }

    }


    post {
        success {
            script {
                emailext(
                    subject: "Build Success!", 
                    body: "${env.JOB_NAME} build ${env.BUILD_NUMBER} successful",
                    to: "sarang.kalantre@colorado.edu" 
                )
            }
        }
        failure {
            script {
                emailext(
                    subject: "Build Failure!",
                    body: "${env.JOB_NAME} build ${env.BUILD_NUMBER} failed.",
                    to: "sarang.kalantre@colorado.edu"
                )
            }
        }
    }
}