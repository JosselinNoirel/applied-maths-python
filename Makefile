.PHONY: docs clean

docs:
	DOC_LANGUAGE=en sphinx-build -W --keep-going -c . -b html docs/en _site/en
	DOC_LANGUAGE=fr sphinx-build -W --keep-going -c . -b html docs/fr _site/fr
	cp docs/landing/index.html _site/index.html

clean:
	rm -rf _site

