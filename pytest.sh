#!/bin/sh


export DATABASE_TEST_URL="sqlite://:memory:"
pytest -s -v
