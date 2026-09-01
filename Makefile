.PHONY: help install analyze analyze-json test lint zip validate

help:
	@echo "Targets:"
	@echo "  install      Install dev/test dependencies (pytest)"
	@echo "  analyze      Run the dispute baseline analysis report"
	@echo "  analyze-json Emit baseline metrics as JSON"
	@echo "  test         Run the pytest suite"
	@echo "  lint         Check internal Markdown links resolve"
	@echo "  zip          Rebuild nab-dmaic-dispute-handling.zip from the sample tree"
	@echo "  validate     lint + test + analyze (end-to-end package check)"

install:
	python3 -m pip install -r requirements-dev.txt

analyze:
	python3 scripts/analyze_disputes.py

analyze-json:
	python3 scripts/analyze_disputes.py --json

test:
	python3 -m pytest -q

lint:
	python3 scripts/check_links.py

zip:
	python3 scripts/build_package_zip.py

validate: lint test analyze
	@echo "Package validation complete."
