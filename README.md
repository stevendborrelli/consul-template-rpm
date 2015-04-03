# RPM Spec for Consul-template

Tries to follow the [packaging guidelines](https://fedoraproject.org/wiki/Packaging:Guidelines) from Fedora.

* Binary: `/usr/bin/consul-template`
* Config: `/etc/consul-template/`

# Build

Build the RPM as a non-root user from your home directory:

* Check out this repo. Seriously - check it out. Nice.
    ```
    git clone <this_repo_url>
    ```

* Install `rpmdevtools` and `mock`.
    ```
    sudo yum install rpmdevtools mock
    ```

* Set up your rpmbuild directory tree.
    ```
    rpmdev-setuptree
    ```

* Link the spec file and sources.
    ```
    ln -s $HOME/consul-template-rpm/SPECS/consul-template.spec rpmbuild/SPECS/
    find $HOME/consul-template-rpm/SOURCES -type f -exec ln -s {} rpmbuild/SOURCES/ \;
    ```

* Download remote source files
    ```
    spectool -g -R rpmbuild/SPECS/consul-template.spec
    ```

* Build the RPM
    ```
    rpmbuild -ba rpmbuild/SPECS/consul-template.spec
    ```

## Result

One RPM for the Consul template binary

# Run

* Install the RPM.
* Put config files in `/etc/consul-template/`.
* Start the service and tail the logs `systemctl start consul-template.service` and `journalctl -f`.
  * To enable at reboot `systemctl enable consul-template.service`.

## Config

Config files are loaded in lexicographical order from the `config-dir`. Some
sample configs are provided.

# More info

See the [consul.io](http://www.consul.io) website.
