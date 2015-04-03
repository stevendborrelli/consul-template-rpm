Name:           consul-template
Version:        0.8.0
Release:        2%{?dist}
Summary:        Generic template rendering and notifications with Consul

Group:          System Environment/Daemons
License:        MPLv2.0
URL:            http://www.consul.io
Source0:        https://github.com/hashicorp/%{name}/releases/download/v%{version}/%{name}_%{version}_linux_amd64.tar.gz
Source1:        %{name}.service

%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
BuildRequires:  systemd-units
Requires:       systemd
%endif
Requires(pre): shadow-utils

%description
Generic template rendering and notifications with Consul

%prep
%setup -q -b 0 -n %{name}_%{version}_linux_amd64

%install
mkdir -p %{buildroot}/%{_bindir}
cp consul-template %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}/templates

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
%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
%{_unitdir}/%{name}.service
%endif
%attr(755, root, root) %{_bindir}/consul-template

%doc


%changelog
* Thu Apr 2 2015 Chris <Chris.Aubuchon@gmail.com>
* updated to 0.8.0
