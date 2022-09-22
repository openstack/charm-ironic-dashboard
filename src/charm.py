#!/usr/bin/env python3
#
# Copyright 2022 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""An Operator Charm for deploying the Ironic Dashboard in Charmed OpenStack.
"""

import logging

from ops.charm import CharmBase
from ops.main import main
from ops.model import ActiveStatus

from charms.openstack_libs.v0.dashboard_plugin_requires import (
    HorizonPlugin,
    HorizonAvailableEvent,
)


logger = logging.getLogger(__name__)


class IronicDashboardCharm(CharmBase):
    """

    """

    def __init__(self, *args):
        super().__init__(*args)
        self.dashboard = HorizonPlugin(
            self, install_packages=['python3-ironic-ui'],
        )
        self.framework.observe(
            self.dashboard.on.available, self._dashboard_available
        )

    def _dashboard_available(self, event: HorizonAvailableEvent):
        """Invoked when the dashboard is now available.

        :param event: the DashboardAvailableEvent to indicate the dashboard
                      is now available.
        :type event: HorizonAvailableEvent
        """
        self.model.unit.status = ActiveStatus('ready')


if __name__ == "__main__":
    main(IronicDashboardCharm)
