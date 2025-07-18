all:
	npm install
	node pbp/das/das2json.mjs crs.drawio
	rm -f out.*
	# arg #3 is reserved and not used in this demo
	python3 main.py . "" main crs.drawio.json
