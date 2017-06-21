# ansible-role-selenium-grid
[![Build Status](https://travis-ci.org/singleplatform-eng/ansible-role-selenium-grid.svg?branch=master)](https://travis-ci.org/singleplatform-eng/ansible-role-selenium-grid)

Role to install and manage Selenium Grid Hubs and Nodes. This role does not manage java installation or browser configuration. 
# Requirements
* java
* desired browsers
* X server or a virtual X frame buffer

Selenium requires java but instead of making a dependency on another ansible role, this role opts to simply take a path to the java runtime you want to use. [geerlingguy.java][ag1] is an easy to use option.
Note: Selenium grid 3+ requires Java 8.

This role also leaves the management of browsers and their drivers to other roles. There are roles available for Chrome, Chromedriver, and Firefox available on ansible galaxy. 

If not running a headless browser, you will need to manage displays outside of this role. [pablerass.xvfb][ag2] is a simple role for running Xvfb.


# Role Variables
By default the role will add a hub and node on the target host listening publicly on the default ports and no browsers configured. 
* selenium_version (default: 2.53.0) - version of the selenium jar to download. Note that different versions have different java requirements which are not managed by this role.
* selenium_java_path (default: /usr/bin/java) - path to the java binary
* selenium_jar_path (default: /opt/selenium) - path where selenium jars will be stored
* selenium_log_path (default: /var/log/selenium) - path where logs will be stored
* selenium_hub_pid_file: (default: /var/run/selenium-hub.pid) - path to pid file used by hub start up script
* selenium_node_pid_file: (default: /var/run/selenium-node.pid) - path to pid file used by node start up script
* selenium_manage_user: (default: true) - boolean to create the {{selenium_user}} and {{selenium_group}} user and group
* selenium_manage_jar: (default: true) - boolean to manage the download of the selenium jar file
* selenium_hub_enabled: (default: true) - boolean to configure the hub service on target host
* selenium_node_enabled: (default: true) - boolean to configure the node service on target host
* selenium_node_capabilies: (default: []) - list of capabilites for a node service. Takes a yaml list of dictionaries e.g
  ```yaml
  selenium_node_capabilities:
    - browserName: chrome
      maxInstances: 5
    - browserName: firefox
      maxInstances: 5
  ```
  See the [selenium grid wiki for node json configs][wn1].
* selenium_node_proxy: (default: org.openqa.grid.selenium.proxy.DefaultRemoteProxy)
* selenium_node_max_session: (default: 5)
* selenium_node_port: (default: 5555)
* selenium_node_host: (default: localhost) - hostname or ip node listens on
* selenium_node_register: (default: true)
* selenium_node_register_cycle: (default: 5000)
* selenium_node_hub_port: (default: 4444)
* selenium_node_hub_host: (default: localhost) - hostname or ip hub listens on

See the [selenium grid wiki for hub json configuration][wn2].
* selenium_hub_port: (default: 4444)
* selenium_hub_new_session_wait_timeout: (default: -1)
* selenium_hub_servlets: (default: []) - yaml list converted to json via filter
* selenium_hub_without_servlets: (default: []) - yaml list converted to json via filter
* selenium_hub_custom: (default: {}) - yaml list converted to json via filter
* selenium_hub_capability_matcher: (default: org.openqa.grid.internal.utils.DefaultCapabilityMatcher)
* selenium_hub_capability_throw: (default: true)
* selenium_hub_clean_up_cycle: (default: 5000)
* selenium_hub_debug: (default: false)
* selenium_hub_browser_timeout: (default: 0)

# Example Playbook
```yaml
- hosts: all
  become: yes
  roles:
    - ansible-role-selenium-grid
```

   [wn1]: <https://github.com/SeleniumHQ/selenium/blob/selenium-2.53.0/java/server/src/org/openqa/grid/common/defaults/DefaultNode.json>
   [wn2]: <https://github.com/SeleniumHQ/selenium/blob/selenium-2.53.0/java/server/src/org/openqa/grid/common/defaults/DefaultHub.json>
   [ag1]: <https://galaxy.ansible.com/geerlingguy/java/>
   [ag2]: <https://galaxy.ansible.com/pablerass/xvfb/>
