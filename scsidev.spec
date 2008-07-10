Summary:	scsidev - alternative scheme for SCSI devices
Summary(pl.UTF-8):	scsidev - alternatywny sposób nazywania urządzeń SCSI
Name:		scsidev
Version:	2.37
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.garloff.de/kurt/linux/scsidev/%{name}-%{version}.tar.gz
# Source0-md5:	e3f2116f5b069503fda62363634dc4c6
Patch0:		%{name}-makefile.patch
URL:		http://www.garloff.de/kurt/linux/scsidev/#scsidev
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/sbin

%description
If your SCSI config changes from time to time, e.g. because you have
external devices which are not always switched on or connected then
the kernel's mapping to the device nodes is not always the way you
would expect it. This program creates a mapping which remains
unchanged in most of these cases.

%description -l pl.UTF-8
Jeżeli konfiguracja SCSI zmienia się w czasie, np. ponieważ urządzenia
zewnętrzne nie są zawsze podłączone lub włączone, mapowania jądra
dotyczące urządzeń SCSI nie są takie same. Ten program tworzy
mapowanie nie zmieniające się w większości przypadków.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%attr(755,root,root) %{_bindir}/scsidev
%{_mandir}/man8/scsidev.8*
