Name:		which
Summary:	Displays where a particular program in your path is located
Version:	2.20
Release:	18
License:	GPLv3
Group:		System/Base
URL:		ftp://ftp.gnu.org/gnu/which/
Source0:	ftp://ftp.gnu.org/gnu/which/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/gnu/which/%{name}-%{version}.tar.gz.sig
Patch0:		which-2.6.jbj.patch
Patch1:		which-2.12-fixinfo.patch
Patch2:		which-2.19-afs.patch
# (tpg) liberty-devel
BuildRequires:	binutils-devel
BuildRequires:	readline-devel
%description
The which command shows the full pathname of a specified program, if
the specified program is in your PATH.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
%configure
%make

%install
%makeinstall_std

rm -rf %{buildroot}%{_infodir}/dir

%files
%doc README* AUTHORS EXAMPLES INSTALL NEWS
%{_bindir}/which
%{_mandir}/man1/which.1*
%{_infodir}/*

