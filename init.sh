#!/bin/bash
set -e

if [ "$2" = "--enable-interceptor-client" ]; then
  echo 'Starting interceptord'
  rm -rf /tmp/ben.lock
  interceptord.py &
fi

echo 'Starting jasmind'
exec "$@"
