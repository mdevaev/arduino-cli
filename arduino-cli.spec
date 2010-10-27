%define svn_build 1

%if %{svn_build}
%define build_version %(date +%%Y%%m%%d)svn%{?dist}
%else
%define build_version 1
%endif


Name:		arduino-cli
Version:	1.0
Release:	%{build_version}
Summary:	CLI development tools for Arduino without Java and Arduino IDE
Group:		Development/Tools
License:	GPL
URL:		http://code.google.com/p/arduino-cli
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch
Requires:	avr-libc, avr-gcc, avr-gcc-c++, avr-binutils, avrdude
%description
%{summary}



%prep
%if %{svn_build}
%setup -q -n %{name}
%else
%setup -q
%endif


%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/%{_datadir}/arduino
cp -a arduino/* ${RPM_BUILD_ROOT}/%{_datadir}/arduino
cp -a tools/Makefile.sketch ${RPM_BUILD_ROOT}/%{_datadir}/arduino


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-, root, root, -)
%{_datadir}/arduino

%changelog
* Sat Sep 04 2010 Devaev Maxim <mdevaev@gmail.com> 1.0-20100904svn
- Arduino Libs version 0019

* Sat Aug 21 2010 Devaev Maxim <mdevaev@gmail.com> 1.0-20100821svn
- Modified externals, replaced arduino dir to hardware
- Refactorig of project Makefile, renamed Makefile to Makefile.sketch

* Sat Aug 14 2010 Devaev Maxim <mdevaev@gmail.com> 1.0-20100814svn
- Initial build

