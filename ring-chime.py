"""
Ring Chime notification service.
For more details about this platform, please refer to the documentation
https://home-assistant.io/components/ring/
"""

import logging
from datetime import timedelta

import voluptuous as vol
import homeassistant.helpers.config_validation as cv

from homeassistant.components.notify import (
    BaseNotificationService, ATTR_TARGET, ATTR_DATA)
from homeassistant.components.ring import (
    CONF_ATTRIBUTION, DEFAULT_ENTITY_NAMESPACE, DATA_RING)


EVENT_NOTIFY = "notify"
DEPENDENCIES = ['ring']


def get_service(hass, config, discovery_info=None):
    """Get the ring notification service."""
    return RingChimeNotificationService(hass)


class RingChimeNotificationService(BaseNotificationService):
    """Implement ring notification service."""

    def __init__(self, hass):
        """Initialize the service."""
        self.hass = hass
        self.ring = hass.data[DATA_RING]
        self.chimes = dict((i.id, i) for i in self.ring.chimes)

    @property
    def targets(self):
        """Return a dictionary of registered targets."""
        return dict((i.name, i.id) for i in self.chimes.values())

    def send_message(self, message="", **kwargs):
        """Send a message to a user."""
        targets = kwargs.get(ATTR_TARGET)
        data = dict(kwargs.get(ATTR_DATA) or {})
        
        volume = data.get('volume')

        kind = message
        if kind == "":
            kind = None

        for target in targets:
            chime = self.chimes[target]
            if volume and volume != chime.volume:
                chime.volume = volume
            chime.test_sound(kind=kind)
