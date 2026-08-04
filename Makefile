.PHONY: docs clean

docs:
	MPLCONFIGDIR=_build/matplotlib DOC_LANGUAGE=en sphinx-build -W --keep-going -c . -b html docs/en _site/en
	MPLCONFIGDIR=_build/matplotlib DOC_LANGUAGE=fr sphinx-build -W --keep-going -c . -b html docs/fr _site/fr
	cp docs/landing/index.html _site/index.html

clean:
	rm -rf _site
