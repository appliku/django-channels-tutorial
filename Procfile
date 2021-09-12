web: bash run-daphne.sh
channel_worker: python manage.py runworker channel_layer -v2
release: bash release.sh
beat: celery -A djangito.celery:app beat -S redbeat.RedBeatScheduler  --loglevel=DEBUG --pidfile /tmp/celerybeat.pid
worker: celery -A djangito.celery:app  worker -Q default -n djangito.%%h --without-gossip --without-mingle --without-heartbeat --loglevel=INFO --max-memory-per-child=512000 --concurrency=1
