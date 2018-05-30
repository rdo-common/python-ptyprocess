%global modname ptyprocess

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-ptyprocess
Version:        0.5.2
Release:        3%{?dist}
Summary:        Run a subprocess in a pseudo terminal

License:        ISC
URL:            https://github.com/pexpect/ptyprocess
Source0:        https://files.pythonhosted.org/packages/source/p/ptyprocess/ptyprocess-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  pytest

%description
Launch a subprocess in a pseudo terminal (pty), and interact with both the
process and its pty.

%package -n python2-ptyprocess
Summary:        Run a subprocess in a pseudo terminal
%{?python_provide:%python_provide python2-%{modname}}
%description -n python2-ptyprocess
Launch a subprocess in a pseudo terminal (pty), and interact with both the
process and its pty.

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-ptyprocess
Summary:        Run a subprocess in a pseudo terminal
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-ptyprocess
Launch a subprocess in a pseudo terminal (pty), and interact with both the
process and its pty.
%endif

%prep
%setup -qn ptyprocess-%{version}

%build
%py2_build
%if 0%{?with_python3}
LC_ALL=en_US.UTF-8 \
    %py3_build
%endif

%install
%if 0%{?with_python3}
LC_ALL=en_US.UTF-8 \
    %py3_install
%endif
%py2_install

%check
%if 0%{?with_python3}
%{_bindir}/py.test-3.* -v
%endif
%{_bindir}/py.test-2.* -v

%files -n python2-ptyprocess
%license LICENSE
%doc README.rst
%{python2_sitelib}/ptyprocess/
%{python2_sitelib}/ptyprocess-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-ptyprocess
%license LICENSE
%doc README.rst
%{python3_sitelib}/ptyprocess/
%{python3_sitelib}/ptyprocess-%{version}-py?.?.egg-info
%endif

%changelog
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Charalampos Stratakis <cstratak@redhat.com> - 0.5.2-1
- Update to 0.5.2 (#1467330)

* Thu Feb 23 2017 Orion Poplawski <orion@cora.nwra.com> - 0.5.1-6
- Really build python3 on EPEL

* Thu Feb 23 2017 Orion Poplawski <orion@cora.nwra.com> - 0.5.1-5
- Build python3 on EPEL
- Run tests verbosely

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 0.5.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 04 2016 Thomas Spura <tomspur@fedoraproject.org> - 0.5.1-1
- update to 0.5.1 (#1304136)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Thomas Spura <tomspur@fedoraproject.org> - 0.5-3
- Use new python macros

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 21 2015 Thomas Spura <tomspur@fedoraproject.org> - 0.5-1
- update to 0.5 (#1223718)

* Wed Jan 07 2015 Thomas Spura <tomspur@fedoraproject.org> - 0.4-1
- update to 0.4

* Wed Dec 03 2014 Thomas Spura <tomspur@fedoraproject.org> - 0.3.1-2
- Generalize with_python3 macro
- Add comment to tests section

* Tue Nov 25 2014 Thomas Spura <tomspur@fedoraproject.org> - 0.3.1-1
- initial spec for ptyprocess (#1167830)
