Name:		which
Summary:	Displays where a particular program in your path is located
Version:	2.16
Release:	%mkrel 4
License:	GPL
Group:		System/Base
Source0:	ftp://ftp.gnu.org/gnu/which/%{name}-%{version}.tar.bz2
URL:		ftp://ftp.gnu.org/gnu/which/
Patch0:		which-2.6.jbj.patch.bz2
Patch1:		which-2.12-fixinfo.patch.bz2
Patch2:		which-2.16-afs.patch.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prereq:		/sbin/install-info

%description
The which command shows the full pathname of a specified program, if
the specified program is in your PATH.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -rf %buildroot%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%files
%defattr(-, root, root)
%doc README* AUTHORS EXAMPLES INSTALL NEWS
%{_bindir}/which
%{_mandir}/man1/which.1*
%{_infodir}/*
