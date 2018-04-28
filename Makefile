install:
	pip install 

test_python:
	python3 ./src/tokyupdater.py

build_python:
	rm -rf ./dist 
	rm -rf ./src/dist/
	pyinstaller --noconsole ./src/tokyupdater.spec --workpath ./build --distpath ./dist --hidden-import pyserial
	cp -R ./dist/tokyupdater/ ./src/dist/tokyupdater.app/Contents/MacOS/

test_binary:
	./dist/tokyupdater/tokyupdater
