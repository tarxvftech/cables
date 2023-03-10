#!/bin/bash
for p in cables/*.yaml; do
	rf="$(basename "$p" .yaml)"
	#rf="${f%.*}"
	echo $rf
	wireviz --prepend-file devices.yaml "$p" -o build/"$rf"
done
for p in connectors_temp/*.yaml; do
	rf="$(basename "$p" .yaml)"
	#rf="${f%.*}"
	echo $rf
	wireviz --prepend-file devices.yaml "$p" -o build_connectors/"$rf"
done
