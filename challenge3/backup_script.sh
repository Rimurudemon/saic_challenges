#!/bin/bash

perform_backup() {
    backup_folder="./backups"
    mkdir -p "$backup_folder"

    docker container cp container_name_html:/path/to/mapped/data "$backup_folder/html_css_js_$(date '+%Y-%m-%d').zip"

    docker container cp container_name_rails:/path/to/mapped/data "$backup_folder/ruby_on_rails_$(date '+%Y-%m-%d').zip"
}
