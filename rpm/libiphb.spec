# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       libiphb

# >> macros
# << macros

Summary:    API for IP Heartbeat service
Version:    1.0.0
Release:    0
Group:      System/System Control
License:    LGPLv2+
URL:        http://github.com/nemomobile/libiphb
Source0:    %{name}-%{version}.tar.bz2
Source100:  libiphb.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(dsme)
BuildRequires:  pkgconfig(mce) >= 1.12.3

%description
This package contains C API for using IP Heartbeat service.


%package devel
Summary:    Development files for IP Heartbeat service
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains C headers for the IP Heartbeat API.


%package tests
Summary:    Tests package for IP Heartbeat service
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}

%description tests
Tests package to test IP Heartbeat functionality.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
unset LD_AS_NEEDED
# >> build pre
./verify_version.sh
chmod a+x autogen.sh
./autogen.sh
chmod a+x configure
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libiphb.so.*
%doc COPYING AUTHORS INSTALL README NEWS ChangeLog
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%attr(644,root,root)%{_includedir}/iphbd/*
%{_libdir}/libiphb.so
%{_libdir}/pkgconfig/libiphb.pc
%doc COPYING
# >> files devel
# << files devel

%files tests
%defattr(-,root,root,-)
/opt/tests/%{name}-tests/bin/hbtest
/opt/tests/%{name}-tests/bin/hbtest2
/opt/tests/%{name}-tests/bin/hbtest3
/opt/tests/%{name}-tests/tests.xml
%doc COPYING
# >> files tests
# << files tests
