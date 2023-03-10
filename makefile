run: cables/devices.yaml
	mkdir -p build/
	mkdir -p build_connectors/
	bash build.sh

cables/devices.yaml:  devices/*/*/*.yaml
	python main.py

clean:
	-rm -r build build_connectors connectors_temp
