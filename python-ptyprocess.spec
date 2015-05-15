%global pypi_name ptyprocess

%if 0%{?fedora}
    %global with_python3 1
%endif

Name:           python-ptyprocess
Version:        0.4
Release:        1%{?dist}
Summary:        Run a subprocess in a pseudo terminal

License:        ISC
URL:            https://github.com/pexpect/ptyprocess
Source0:        https://pypi.python.org/packages/source/p/ptyprocess/ptyprocess-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  pytest
%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%endif

%description
Launch a subprocess in a pseudo terminal (pty), and interact with both the
process and its pty.

%if 0%{?with_python3}
%package -n python3-ptyprocess
Summary:        Run a subprocess in a pseudo terminal
%description -n python3-ptyprocess
Launch a subprocess in a pseudo terminal (pty), and interact with both the
process and its pty.
%endif

%prep
%setup -qn ptyprocess-%{version}
rm -r tests/__pycache__ tests/*.pyc
%if 0%{?with_python3}
rm -rf %{py3dir}
cp -ar . %{py3dir}
%endif

%build
%{__python} setup.py build
%if 0%{?with_python3}
pushd %{py3dir}
LC_ALL=en_US.UTF-8 \
    %{__python3} setup.py build
popd
%endif

%install
%if 0%{?with_python3}
pushd %{py3dir}
LC_ALL=en_US.UTF-8 \
    %{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif
%{__python} setup.py install --skip-build --root %{buildroot}

%check
# The next version will include tests. There aren't any yet...:
# https://github.com/pexpect/ptyprocess/pull/4
%if 0%{?with_python3}
pushd %{py3dir}
%{_bindir}/py.test-3*
popd
%endif
py.test

%files
# TODO add COPYING with next release
%doc README.rst
%{python_sitelib}/ptyprocess/
%{python_sitelib}/ptyprocess-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-ptyprocess
%doc README.rst
%{python3_sitelib}/ptyprocess/
%{python3_sitelib}/ptyprocess-%{version}-py?.?.egg-info
%endif

%changelog
* Wed Jan 07 2015 Thomas Spura <tomspur@fedoraproject.org> - 0.4-1
- update to 0.4

* Wed Dec 03 2014 Thomas Spura <tomspur@fedoraproject.org> - 0.3.1-2
- Generalize with_python3 macro
- Add comment to tests section

* Tue Nov 25 2014 Thomas Spura <tomspur@fedoraproject.org> - 0.3.1-1
- initial spec for ptyprocess (#1167830)
