#!/bin/bash

# Script: test.sh
# Description: send concurrent ping request from redis client

redis-cli ping & redis-cli ping & redis-cli ping

