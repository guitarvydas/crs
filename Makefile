all: v0 v1 v2 

init:
	npm install
	node pbp/das/das2json.mjs crs.drawio
	rm -f out.*

v0: init
	@echo ''
	@echo 'version 0'
	python3 main.py . "q" v0 crs.drawio.json
v1: init
	@echo ''
	@echo 'version 1'
	python3 main.py . "q" v1 crs.drawio.json
v2: init
	@echo ''
	@echo 'version 2'
	python3 main.py . "q" v2 crs.drawio.json

# WIP...
L0: init
	@echo ''
	@echo 'version L0'
	python3 main.py . "q" L0 crs.drawio.json
