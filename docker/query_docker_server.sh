#!/bin/bash

curl -XPOST http://localhost:5005/webhooks/rest/webhook \
  -H "Content-type: application/json" \
  -d '{"sender": "test", "message": "hello"}'

