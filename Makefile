# ------------------------------------------------------------
# Makefile — generic git helper (simple version)
# ------------------------------------------------------------

BRANCH = main

.DEFAULT_GOAL := help

help:
	@echo ""
	@echo "Usage:"
	@echo " make push"
	@echo " make pull"
	@echo " make status"
	@echo " make log"
	@echo ""

push:
	git add .
	@if ! git diff --cached --quiet; then \
	git commit -m "$$(date)"; \
	fi
	git push -u origin $(BRANCH)

pull:
	git pull origin $(BRANCH)

status:
	git status

log:
	git --no-pager log --oneline -n 5

