#!/usr/bin/env bash

set -eux
pgloader --context 'pgloader.ini' 'ss14_sqlite_to_postgres.pgloader'
