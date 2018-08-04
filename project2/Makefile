build:
	docker build -t honestbee/base_img .

run-app:
	docker run --expose=80 -p 8000:80 --name honestbee_web_app --privileged -itd -v /opt/honestbee:/opt/honestbee honestbee/base_img /bin/bash

login-app:
	docker exec -it honestbee_web_app /bin/bash

deploy-app:
	docker exec honestbee_web_app bash -c 'cd /opt/honestbee/project2; ansible-playbook -u ubuntu site.yml'
