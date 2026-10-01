class RouteEntry:
    def __init__(self, network: str, mask: str, next_hop: str | None, interface: str):
        pass


class RoutingTable:
    def __init__(self):
        pass

    def add_route(self, entry: RouteEntry) -> None:
        pass

    def __str__(self) -> str:
        pass
