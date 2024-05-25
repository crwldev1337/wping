#!/bin/bash
WPING="wping.py"
WPING_ALIAS="wping"

chmod +x "$WPING"
sudo mv "$WPING" "/usr/local/bin/$WPING_ALIAS"
