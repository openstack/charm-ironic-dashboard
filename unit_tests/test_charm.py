# Copyright 2021 Canonical Ltd
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

import unittest
import sys

sys.path.append('lib')  # noqa
sys.path.append('src')  # noqa

from charm import IronicDashboardCharm
from ops.model import ActiveStatus
from ops.testing import Harness


class TestCharm(unittest.TestCase):
    def setUp(self):
        self.harness = Harness(IronicDashboardCharm)
        self.harness.begin()
        self.addCleanup(self.harness.cleanup)

    def test_add_relation(self):
        rel_id = self.harness.add_relation('dashboard', 'openstack-dashboard')
        self.harness.add_relation_unit(rel_id, "openstack-dashboard/0")
        self.harness.update_relation_data(rel_id, 'openstack-dashboard', {
            'release': 'testing'
        })
        assert isinstance(self.harness.charm.model.unit.status,
                          ActiveStatus)
