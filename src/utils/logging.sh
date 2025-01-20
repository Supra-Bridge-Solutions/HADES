#!/bin/bash

# Utility function for logging messages
log_message() {
    local LEVEL="$1"
    local MESSAGE="$2"
    local LOG_FILE="/var/log/intrusion_detection.log"
    echo "[$(date)] $LEVEL: $MESSAGE" >> $LOG_FILE
}

log_info() {
    log_message "INFO" "$1"
}

log_error() {
    log_message "ERROR" "$1"
}
