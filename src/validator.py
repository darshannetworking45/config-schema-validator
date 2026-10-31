"""Network Automation Configuration Schema Validator."""

from dataclasses import dataclass
import ipaddress
from typing import Dict, List, Optional


class SchemaValidationError(Exception):
    """Raised when an automation variable dictionary violates schema constraints."""
    pass


class NetworkSchemaValidator:
    """Strict contract validator for device inventory variable models."""

    REQUIRED_DEVICE_FIELDS = ["hostname", "management_ip", "role", "site", "vlans"]
    VALID_ROLES = {"core", "distribution", "access", "wan_edge", "firewall", "spine", "leaf"}

    @classmethod
    def validate_device_vars(cls, data: Dict) -> List[str]:
        """
        Validates variable dictionaries against enterprise data modeling standards.
        Returns a list of human-readable error descriptions.
        """
        errors = []


        for field in cls.REQUIRED_DEVICE_FIELDS:
            if field not in data:
                errors.append(f"Missing mandatory field: '{field}'")


        if "hostname" in data:
            h = str(data["hostname"]).strip()
            if not h or len(h) > 63:
                errors.append(f"Invalid hostname '{h}': Must be 1-63 characters")


        if "management_ip" in data:
            try:
                ipaddress.ip_address(data["management_ip"])
            except ValueError:
                errors.append(f"Invalid management IP format: '{data['management_ip']}'")


        if "role" in data:
            role_val = str(data["role"]).lower()
            if role_val not in cls.VALID_ROLES:
                errors.append(f"Invalid role '{data['role']}': Must be one of {sorted(list(cls.VALID_ROLES))}")


        if "vlans" in data:
            if not isinstance(data["vlans"], list):
                errors.append("'vlans' attribute must be a list of integer VLAN IDs")
            else:
                for v in data["vlans"]:
                    if not isinstance(v, int) or not (1 <= v <= 4094):
                        errors.append(f"Invalid 802.1Q VLAN ID: {v}. Must be an integer between 1 and 4094.")

        return errors
