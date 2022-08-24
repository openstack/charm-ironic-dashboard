# Overview

This subordinate charm provides the Ironic Dashboard plugin for use with the OpenStack Dashboard.

# Usage

Example minimal deploy:

    juju deploy openstack-dashboard --channel yoga/stable
    juju deploy ironic-dashboard
    juju add-relation \
        openstack-dashboard:dashboard-plugin ironic-dashboard:dashboard

# Bugs

Please report bugs on [Launchpad](https://bugs.launchpad.net/charm-ironic-dashboard/+filebug).

For general questions please refer to the OpenStack [Charm Guide](https://docs.openstack.org/charm-guide/latest/).
