# Flask Devops Service

A simple Flask API to initiate rebuilds for services on a machine

## How To

- Copy `.env.example` to `.env`, set variables

## Requirements

- Running service to be restarted
- Nginx proxy service with config outlined in `config/nginx.conf`
- Git installed on target machine
- Build script at specified location for service
- Environment variables set in `.env`
