import os
import time
from prometheus_client import start_http_server, Gauge
import requests
import re

class AppMetrics:
    def __init__(self, app_port, app_host, polling_interval_seconds):
        self.app_port = app_port
        self.app_host = app_host
        self.polling_interval_seconds = polling_interval_seconds

        # Prometheus metrics to collect
        self.world_animals = Gauge("world_animals", "Animals")
        self.world_plants = Gauge("world_plants", "Plants")
        self.online_players = Gauge("online_players", "Online Players")
        self.total_players = Gauge("total_players", "Total Players")
        self.laws = Gauge("laws", "Laws")
        self.active_online_players = Gauge("active_online_players", "Active and Online Players")
        self.peak_active_players = Gauge("peak_active_players", "Peak Active Players")
        self.max_active_players = Gauge("max_active_players", "Max Active Players")
        self.trades = Gauge("trades", "Trades")
        self.contracts = Gauge("contracts", "Contracts")

    def run_metrics_loop(self):
        """Metrics fetching loop"""

        while True:
            self.fetch()
            time.sleep(self.polling_interval_seconds)

    def fetch(self):
        resp = requests.get(url=f"{self.app_host}:{self.app_port}/info")
        status_data = resp.json()
        economy_desc = status_data["EconomyDesc"]
        result = re.findall(r'\b\d+\b',economy_desc)

        self.world_animals.set(status_data["Animals"])
        self.world_plants.set(status_data["Plants"])
        self.online_players.set(status_data["OnlinePlayers"])
        self.total_players.set(status_data["TotalPlayers"])
        self.laws.set(status_data["Laws"])
        self.active_online_players.set(status_data["ActiveAndOnlinePlayers"])
        self.peak_active_players.set(result[0])
        self.max_active_players.set(result[1])
        

def main():

    polling_interval_seconds = int(os.getenv("POLLING_INTERVAL_SECONDS", "5"))
    app_host = os.getenv("APP_HOST", "0.0.0.0")
    app_port = int(os.getenv("APP_PORT", "3001"))
    exporter_port = int(os.getenv("EXPORTER_PORT", "9877"))

    app_metrics = AppMetrics(
        app_port=app_port,
        polling_interval_seconds=polling_interval_seconds,
        app_host=app_host
    )
    start_http_server(exporter_port)
    app_metrics.run_metrics_loop()

if __name__ == "__main__":
    main()