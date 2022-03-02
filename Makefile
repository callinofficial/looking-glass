FUNCTION = looking-glass

check:
	aws lambda get-function --function-name $(FUNCTION) --region $(AWS_REGION)

requirements:
	mkdir -p ./requirements/
	python -m pip install --upgrade --upgrade-strategy eager -r ./$(FUNCTION)/requirements.txt -t ./requirements/
	cd ./requirements/ && zip -r ../requirements.zip .
	-rm -rf ./requirements/

build:
	-rm -rf ./build/ ./$(FUNCTION).zip
	cp ./requirements.zip ./$(FUNCTION).zip
	mkdir -p ./build/
	cp -r ./$(FUNCTION)/. ./build/
	cd ./build/ && zip -ur ../$(FUNCTION).zip . -x "*__pycache__*" "*.DS_Store*" "*.git*" "Makefile" "requirements.txt" "dev-requirements.txt" "*.venv*" ".chalice*";
	-rm -rf ./build/

upload:
	aws s3 cp ./$(FUNCTION).zip s3://$(BUCKET_NAME)/$(STAGE)/$(FUNCTION).zip

deploy: 
	aws lambda update-function-code --function-name looking-glass --s3-bucket $(BUCKET_NAME) --s3-key $(STAGE)/$(FUNCTION).zip