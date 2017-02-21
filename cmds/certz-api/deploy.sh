#!/bin/bash -xe

gcloud app deploy --version last -q --verbosity=info \
    --project zonescloud \
    certz-api/app.yaml

#tiny-ci-api/queue.yaml
