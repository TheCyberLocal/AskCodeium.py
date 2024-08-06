import socket

class PortManager:
    """
    port_manager = PortManager()

    # Get a free port
    port1 = port_manager.get_free_port()
    print(f"Allocated port: {port1}")

    # Get another free port
    port2 = port_manager.get_free_port()
    print(f"Allocated port: {port2}")

    # Release the first port
    port_manager.release_port(port1)
    print(f"Released port: {port1}")

    # Get a free port again (should be the same as port1 if it's the next available)
    port3 = port_manager.get_free_port()
    print(f"Allocated port: {port3}")
    """
    def __init__(self, start_port=8000, end_port=9000):
        self.start_port = start_port
        self.end_port = end_port
        self.used_ports = set()

    def get_free_port(self):
        for port in range(self.start_port, self.end_port):
            if port not in self.used_ports and self._is_port_free(port):
                self.used_ports.add(port)
                return port
        raise Exception("No free ports available")

    def _is_port_free(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            return sock.connect_ex(('localhost', port)) != 0

    def release_port(self, port):
        self.used_ports.discard(port)
