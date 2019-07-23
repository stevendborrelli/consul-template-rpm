Name:           consul-template
Version:        0.20.0
Release:        1%{?dist}
Summary:        Generic template rendering and notifications with Consul

Group:          System Environment/Daemons
License:        MPLv2.0
URL:            http://www.consul.io
Source0:        https://releases.hashicorp.com/%{name}/%{version}/%{name}_%{version}_linux_amd64.tgz
Source1:        %{name}.service

%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
BuildRequires:  systemd-units
Requires:       systemd
%endif
Requires(pre): shadow-utils

%description
Generic template rendering and notifications with Consul

%prep
tar zxvf  %{_sourcedir}/%{name}_%{version}_linux_amd64.tgz

%install
mkdir -p %{buildroot}/%{_bindir}
cp consul-template %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}/templates
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}/config.d

%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
mkdir -p %{buildroot}/%{_unitdir}
cp %{SOURCE1} %{buildroot}/%{_unitdir}/
%endif

%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service
%endif

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%dir %attr(750, root, root) %{_sysconfdir}/%{name}
%dir %attr(750, root, root) %{_sysconfdir}/%{name}/templates
%dir %attr(750, root, root) %{_sysconfdir}/%{name}/config.d
%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
%{_unitdir}/%{name}.service
%endif
%attr(755, root, root) %{_bindir}/consul-template

%doc


%changelog
* Tue Jul 23 2019 Anton Samets <sharewax@gmail.com> - 0.20.0-1
- new upstream version; new URLs; consul-template actualized

* Thu Apr 2 2015 Chris <Chris.Aubuchon@gmail.com>
* updated to 0.8.0
