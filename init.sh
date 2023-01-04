#!/bin/bash
set -e

if [ "$2" = "--enable-interceptor-client" ]; then
  echo 'Starting interceptord'
  rm -rf /tmp/interceptord.lock
fi

echo 'Starting jasmind'
