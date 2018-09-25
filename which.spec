Name:		which
Summary:	Displays where a particular program in your path is located
Version:	2.21
Release:	3
License:	GPLv3
Group:		System/Base
URL:		ftp://ftp.gnu.org/gnu/which/
Source0:	ftp://ftp.gnu.org/gnu/which/%{name}-%{version}.tar.gz
Patch0:		which-2.6.jbj.patch
Patch1:		which-2.21-coverity-fixes.patch
# (tpg) liberty-devel
BuildRequires:	binutils-devel
BuildRequires:	readline-devel

%description
The which command shows the full pathname of a specified program, if
the specified program is in your PATH.

%prep
%autosetup -p1

%build
# (tpg) add missing file
touch ChangeLog

%configure
%make_build

%install
%make_install

rm -rf %{buildroot}%{_infodir}/dir

%files
%doc README* AUTHORS EXAMPLES INSTALL NEWS
%{_bindir}/which
%{_mandir}/man1/which.1*
%{_infodir}/*
