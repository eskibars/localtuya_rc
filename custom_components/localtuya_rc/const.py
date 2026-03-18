"""Constants for the LocalTuyaIR Remote Control integration."""

DOMAIN = "localtuya_rc"
DEFAULT_FRIENDLY_NAME = "Tuya IR Remote Control"
NOTIFICATION_TITLE = "Tuya IR Remote Control"

CONF_LOCAL_KEY = "local_key"
CONF_PROTOCOL_VERSION = "protocol_version"
CONF_CLOUD_INFO = "cloud_info"
CONF_CONTROL_TYPE = "control_type"

CONF_SERIAL_NUMBER = "serial_number"
CONF_PRODUCT_CATEGORY = "product_category"
CONF_PRODUCT_NAME = "product_name"
CONF_PRODUCT_ID = "product_id"
CONF_PERSISTENT_CONNECTION = "persistent_connection"

DEFAULT_PERSISTENT_CONNECTION = False

CONTROL_TYPE_AUTO = "Auto"
CONTROL_TYPE_LEGACY = "201/202"
CONTROL_TYPE_MODERN = "1-13"
CONTROL_TYPE_OPTIONS = [
    CONTROL_TYPE_AUTO,
    CONTROL_TYPE_LEGACY,
    CONTROL_TYPE_MODERN,
]

CONTROL_TYPE_1_DPS = ("201", "202")
CONTROL_TYPE_2_DPS = ("1", "2")


def normalize_control_type(control_type):
    """Convert config and tinytuya control_type values to an integer."""
    if control_type in (None, "", 0, "0", CONTROL_TYPE_AUTO):
        return None
    if control_type in (1, "1", CONTROL_TYPE_LEGACY):
        return 1
    if control_type in (2, "2", CONTROL_TYPE_MODERN):
        return 2
    return None


def serialize_control_type(control_type):
    """Convert a normalized control type into the config value."""
    normalized = normalize_control_type(control_type)
    if normalized == 1:
        return CONTROL_TYPE_LEGACY
    if normalized == 2:
        return CONTROL_TYPE_MODERN
    return CONTROL_TYPE_AUTO


def infer_control_type_from_status(status):
    """Infer TinyTuya control_type from a DPS payload."""
    if not isinstance(status, dict):
        return None
    dps = status.get("dps")
    if not isinstance(dps, dict):
        return None
    if any(dp in dps for dp in CONTROL_TYPE_1_DPS):
        return 1
    if any(dp in dps for dp in CONTROL_TYPE_2_DPS):
        return 2
    return None

CODE_STORAGE_VERSION = 1
CODE_STORAGE_CODES = f"{DOMAIN}_codes"

# Tuya protocol versions in order of preference
TUYA_VERSIONS = [3.3, 3.4, 3.5, 3.2, 3.1]
