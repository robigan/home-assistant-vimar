"""Constant for Vimar component."""

# Home-Assistant specific consts
DOMAIN = "vimar"

CONF_SCHEMA = "schema"
CONF_CERTIFICATE = "certificate"
CONF_GLOBAL_CHANNEL_ID = "global_channel_id"
CONF_IGNORE_PLATFORM = "ignore"

DEFAULT_USERNAME = "admin"
DEFAULT_SCHEMA = "https"
DEFAULT_PORT = 443
DEFAULT_CERTIFICATE = "rootCA.VIMAR.crt"
DEFAULT_TIMEOUT = 6

# Device overrides
CONF_OVERRIDE = "device_override"

# vimar integration specific const

DEVICE_TYPE_LIGHTS = "lights"
DEVICE_TYPE_COVERS = "covers"
DEVICE_TYPE_SWITCHES = "switches"
DEVICE_TYPE_CLIMATES = "climates"
DEVICE_TYPE_MEDIA_PLAYERS = "media_players"
DEVICE_TYPE_SCENES = "scenes"
DEVICE_TYPE_FANS = "fans"
DEVICE_TYPE_SENSORS = "sensors"
DEVICE_TYPE_OTHERS = "others"


VIMAR_CLIMATE_OFF = "VIMAR_CLIMATE_OFF"
VIMAR_CLIMATE_AUTO = "VIMAR_CLIMATE_AUTO"
VIMAR_CLIMATE_MANUAL = "VIMAR_CLIMATE_MANUAL"
VIMAR_CLIMATE_HEAT = "VIMAR_CLIMATE_HEAT"
VIMAR_CLIMATE_COOL = "VIMAR_CLIMATE_COOL"


VIMAR_CLIMATE_OFF_I = "0"
VIMAR_CLIMATE_AUTO_I = "8"
VIMAR_CLIMATE_MANUAL_I = "6"

VIMAR_CLIMATE_HEAT_I = "0"
VIMAR_CLIMATE_COOL_I = "1"

VIMAR_CLIMATE_OFF_II = "6"
VIMAR_CLIMATE_AUTO_II = "0"
VIMAR_CLIMATE_MANUAL_II = "1"

VIMAR_CLIMATE_NEUTRAL_II = "0"
VIMAR_CLIMATE_HEAT_II = "2"
VIMAR_CLIMATE_COOL_II = "1"

AVAILABLE_PLATFORMS = {
    DEVICE_TYPE_LIGHTS: "light",
    DEVICE_TYPE_COVERS: "cover",
    DEVICE_TYPE_SWITCHES: "switch",
    DEVICE_TYPE_CLIMATES: "climate",
    DEVICE_TYPE_MEDIA_PLAYERS: "media_player",
    DEVICE_TYPE_SCENES: "scene",
    # DEVICE_TYPE_FANS: 'fan',
    DEVICE_TYPE_SENSORS: "sensor",
    # DEVICE_TYPE_OTHERS: ''
}
