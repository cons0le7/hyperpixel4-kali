#!/bin/bash

SCRIPT_NAME="rotation.sh"
SCRIPT_SOURCE="$(pwd)/$SCRIPT_NAME"
SCRIPT_DEST="/usr/local/bin/$SCRIPT_NAME"
SERVICE_FILE="/etc/systemd/system/hyperpixel_rotate.service"

if [[ ! -f $SCRIPT_SOURCE ]]; then
    echo "Source script $SCRIPT_SOURCE does not exist."
    exit 1
fi

sudo cp "$SCRIPT_SOURCE" "$SCRIPT_DEST"
sudo chmod +x "$SCRIPT_DEST"

cat << EOF | sudo tee "$SERVICE_FILE"
[Unit]
Description=My Custom Script Service
After=network.target

[Service]
Type=simple
ExecStart=$SCRIPT_DEST
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable hyperpixel_rotate.service
sudo systemctl start hyperpixel_rotate.service 

echo "Service for $SCRIPT_NAME has been created and enabled to start at boot."
