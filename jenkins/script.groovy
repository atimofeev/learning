def buildApp() {
    echo 'building the app'
}

def testApp() {
    echo 'testing the app'
}

def deployApp() {
    echo 'deploying the app'
    echo "version ${params.VERSION_CH}"
}

return this