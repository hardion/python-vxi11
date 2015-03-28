%define name python-vxi11
%define version 0.7.1
%define unmangled_version 0.7.1
%define unmangled_version 0.7.1
%define release 1%{?dist}.maxlab

Summary: Python VXI-11 driver for controlling instruments over Ethernet
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: MIT License
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Alex Forencich <alex@alexforencich.com>
Url: http://alexforencich.com/wiki/en/python-vxi11/start
BuildRequires: python-setuptools

%description
This Python package supports the VXI-11 Ethernet
instrument control protocol for controlling VXI11 and LXI compatible instruments.

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
