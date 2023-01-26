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

Pip Requirements Command

```
pip install -r requirements.txt
```

Running the Exporter

```
python3 main.py
```

## Metrics Gathered

| Metric Name | Description |
|-------------|-------------|
|world_animals             |  Number of animals in the world           |
|world_plants             | Number of plants in the world             |
|online_players             | Number of online players             |
|total_player             | Total number of players that have joined the server             |
|laws             | Number of laws             |
|active_online_players             | Number of active players that are online             |
|peak_active_players             | Peak number of active players             |
|max_active_players             | Max number of active players             |
|trades             | Number of trades            |
|contracts           | Number of contracts             |

## Grafana Dashboards
