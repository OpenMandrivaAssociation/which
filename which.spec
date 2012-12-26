Name:		which
Summary:	Displays where a particular program in your path is located
Version:	2.20
Release:	11
License:	GPLv3
Group:		System/Base
Source0:	ftp://ftp.gnu.org/gnu/which/%{name}-%{version}.tar.bz2
URL:		ftp://ftp.gnu.org/gnu/which/
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
%configure2_5x
%make

%install
%makeinstall_std

rm -rf %{buildroot}%{_infodir}/dir


%files
%defattr(-, root, root)
%doc README* AUTHORS EXAMPLES INSTALL NEWS
%{_bindir}/which
%{_mandir}/man1/which.1*
%{_infodir}/*


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 2.20-7mdv2011.0
+ Revision: 670807
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 2.20-6mdv2011.0
+ Revision: 608168
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 2.20-5mdv2010.1
+ Revision: 520291
- rebuilt for 2010.1

* Sat Oct 03 2009 Funda Wang <fwang@mandriva.org> 2.20-4mdv2010.0
+ Revision: 452793
- rebuild

* Thu Dec 25 2008 Oden Eriksson <oeriksson@mandriva.com> 2.20-3mdv2009.1
+ Revision: 319106
- rediffed one fuzzy patch

* Thu Aug 07 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.20-1mdv2009.0
+ Revision: 265359
- update to new version 2.20

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.19-3mdv2009.0
+ Revision: 225925
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 2.19-2mdv2008.1
+ Revision: 171172
- rebuild

* Wed Jan 23 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.19-1mdv2008.1
+ Revision: 157109
- new version
- rediff the AFS patch
- add missing buildrequires on binutils-devel and readline-devel
- new license policy

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 16 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.17-1mdv2008.1
+ Revision: 98845
- new version
- bunzip patches

* Fri Aug 24 2007 Thierry Vignaud <tv@mandriva.org> 2.16-5mdv2008.0
+ Revision: 70944
- convert prereq
- Import which



* Sun Jul 02 2006 Stefan van der Eijk <stefan@mandriva.org> 2.16-4
- %%mkrel

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.16-3mdk
- Rebuild

* Sun Jan 23 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.16-2mdk
- rebuild
- drop .bz2 ending for man pages in %%files
- fix summary-ended-with-dot

* Thu Dec 11 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.16-1mdk
- new release
- rediff and simplify patch 3

* Tue Jul 22 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.14-5mdk
- rebuild

* Thu Jan 02 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.14-4mdk
- build release

* Mon Oct 28 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.14-3mdk
- remove useless prefix
- patch 2 : use access instead stat in AFS environment 

* Wed Aug 14 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.14-2mdk
- Automated rebuild with gcc 3.2-0.3mdk

* Fri Aug  2 2002 Jeff Garzik <jgarzik@mandrakesoft.com> 2.14-1mdk
- Version 2.14
- Use %%configure2_5x, %%makeinstall_std
- Do not regenerate autoconf/automake files, breaks build

* Tue May 07 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.13-5mdk
- Automated rebuild in gcc3.1 environment

* Fri Aug 17 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.13-4mdk
- new release
- sanitize spec file

* Sun Mar 04 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.12-4mdk
- Fix info files entry.
- Fix %%files.

* Fri Feb 23 2001 Jeff Garzik <jgarzik@mandrakesoft.com> 2.12-3mdk
- Whoops, info files were not getting installed

* Fri Feb 23 2001 Jeff Garzik <jgarzik@mandrakesoft.com> 2.12-2mdk
- Change specfile permissions (rpmlint warning)
- List more docs in doc macro
- Generate automake and autoconf-derived files in prep stage

* Mon Nov 13 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.12-1mdk
- new and shiny vesion.

* Tue Aug 22 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.11-1mdk
- BM
- 2.11
- Even More Cleanup Of Specs :-)

* Tue Jun 20 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.9-5mdk
- Clean up specs.
- Use makeinstall macros.

* Wed Apr  5 2000 Jeff Garzik <jgarzik@mandrakesoft.com> 2.9-4mdk
- new group System/Base
- updated BuildRoot

* Fri Nov 5 1999 Damien Krotkine <damien@mandrakesoft.com>
- Mandrake release

* Wed Aug 18 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- add defattr

* Sun Aug 08 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- 2.8 :
	* aclocal.m4 was missing from the tar, resulting in
	  a build failure if autoconf isn't installed.


* Thu Jul 08 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Upgrade to the offical version of Gnu project.
- Rewriting the spec-files.
- 2.7 :
    * Support for aliases
    * Configure/compile fix in the `tilde' directory.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale
- handle RPM_OPT_FLAGS
- Makefiles and source code are NOT docs.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Jun 13 1997 Erik Troan <ewt@redhat.com>
- built against glibc
