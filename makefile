run: cables/devices.yaml
	mkdir -p build/
	wireviz --prepend-file devices.yaml \
		cables/Module17_YaesuFT8xx.yaml -o build/Module17_YaesuFT8xx
	wireviz --prepend-file devices.yaml \
		cables/Module17_YaesuFTM.yaml -o build/Module17_YaesuFTM

cables/devices.yaml:  devices/*/*/*.yaml
	python main.py
