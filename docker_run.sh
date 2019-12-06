set -a; source ~/.env; set +a;
docker run -d -e BOT_NAME=Marvin -e BOT_TOKEN=MDQzNzJmZjctNTk4Ni00NzgyLWIzMjMtNDllNDNmMTQwMDZmOTMwMTVjMTItMWM2_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f -e BOT_USERNAME=Marvinh -e BOT_PASSWORD=Tested@2020 -e ENABLE_PASSWORD='T!m32G0Br0'  -v $PWD/k8s/users.properties:/opt/wibot/users.properties registry-qa.webex.com/marvin:test2
