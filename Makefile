
run_app:
	@echo starting web app
	python -m app.main
	# uvicorn app.main:app --reload

