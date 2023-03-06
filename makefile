run: cables/devices.yaml
	mkdir -p build/
	bash build.sh

cables/devices.yaml:  devices/*/*/*.yaml
	python main.py
