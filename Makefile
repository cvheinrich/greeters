.PHONY: check format type clean

check:
	pixi run --environment dev check

format:
	pixi run --environment dev format

type:
	pixi run --environment dev type

clean: check format type
