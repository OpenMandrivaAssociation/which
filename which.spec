Name:		which
Summary:	Displays where a particular program in your path is located
Version:	2.23
Release:	1
License:	GPLv3
Group:		System/Base
URL:		ftp://ftp.gnu.org/gnu/which/
Source0:	ftp://ftp.gnu.org/gnu/which/%{name}-%{version}.tar.gz
Patch1:		which-2.21-coverity-fixes.patch
# (tpg) liberty-devel
BuildRequires:	binutils-devel
BuildRequires:	readline-devel
BuildSystem:	autotools

%description
The which command shows the full pathname of a specified program, if
the specified program is in your PATH.

%install -a
rm -f %{buildroot}%{_infodir}/dir

%files
%doc README* AUTHORS EXAMPLES INSTALL NEWS
%{_bindir}/which
%{_mandir}/man1/which.1*
%{_infodir}/*
