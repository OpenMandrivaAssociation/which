Name:		which
Summary:	Displays where a particular program in your path is located
Version:	2.17
Release:	%mkrel 1
License:	GPL
Group:		System/Base
Source0:	ftp://ftp.gnu.org/gnu/which/%{name}-%{version}.tar.bz2
URL:		ftp://ftp.gnu.org/gnu/which/
Patch0:		which-2.6.jbj.patch
Patch1:		which-2.12-fixinfo.patch
Patch2:		which-2.16-afs.patch
Requires(post):	info-install
Requires(preun): info-install

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
rm -rf %{buildroot}
%makeinstall_std

rm -rf %{buildroot}%{_infodir}/dir

%clean
rm -rf %{buildroot}

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
