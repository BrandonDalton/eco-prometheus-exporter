<img src="banner.png" width="100%" >

# Eco Prometheus Exporter

Simple Prometheus exporter that extracts information from an Eco server, I wanted a way to display metrics within Grafana and get experience creating a Prometheus exporter.

## Docker Setup

### Docker CLI:

Adjust the APP_HOST environment variable to point to your server.

```
docker run -d -it -p 9877:9877 -e APP_HOST="http://0.0.0.0" --name eco-prometheus-exporter saltonn/eco-prometheus-exporter
```

## Local Setup

## Metrics Gathered

| Metric Name | Description |
|-------------|-------------|
|world_animals             |             |
|world_plants             |             |
|online_players             |             |
|total_player             |             |
|laws             |             |
|active_online_players             |             |
|peak_active_players             |             |
|max_active_players             |             |
|trades             |             |
|contracts           |             |
