all:
	npm install
	node pbp/das/das2json.mjs crs.drawio
	rm -f out.*
	python3 main.py . "q" main crs.drawio.json
