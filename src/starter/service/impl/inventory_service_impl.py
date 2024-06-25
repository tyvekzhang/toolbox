"""Inventory domain service impl"""

import subprocess
import platform


from src.common.service.impl.service_impl import ServiceImpl
from src.starter.exception.system import PingException
from src.starter.mapper.inventory_mapper import InventoryMapper
from src.starter.model.inventory_do import InventoryDO
from src.starter.service.inventory_service import InventoryService


class InventoryServiceImpl(ServiceImpl[InventoryMapper, InventoryDO], InventoryService):
    def __init__(self, mapper: InventoryMapper):
        """
        Initialize the UserServiceImpl instance.

        Args:
            mapper (InventoryMapper): The UserMapper instance to use for database operations.
        """
        super().__init__(mapper=mapper)
        self.mapper = mapper

    async def ping_ip(self, ip_address: str, timeout: int = 4):
        """
        Ping an IP address.

        :param ip_address: The IP address to ping.
        :param timeout: Timeout in seconds for each ping request.
        :raises PingException: If the IP address is not reachable.
        """
        try:
            # Detect the operating system
            system = platform.system().lower()

            if system == "windows":
                # Windows uses '-n' for count and '-w' for timeout (in milliseconds)
                response = subprocess.run(
                    ["ping", "-n", "1", "-w", str(timeout * 1000), ip_address],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
            else:
                # Unix-based systems (Linux, macOS) use '-c' for count and '-W' for timeout (in seconds)
                response = subprocess.run(
                    ["ping", "-c", "1", "-W", str(timeout), ip_address],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )

            if response.returncode != 0:
                raise PingException(f"Ping to {ip_address} failed.")
        except subprocess.TimeoutExpired:
            raise PingException(f"Ping to {ip_address} timed out.")
        except subprocess.SubprocessError as e:
            raise PingException(f"Ping to {ip_address} failed with error: {e}")
