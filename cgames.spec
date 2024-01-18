Summary:	Games for the Linux console
Summary(pl.UTF-8):	Gry na linuksową konsolę
Name:		cgames
Version:	2.2b
Release:	1
License:	GPL v2+
Group:		Applications/Games
Source0:	http://www.muppetlabs.com/~breadbox/pub/software/%{name}-%{version}.tar.gz
# Source0-md5:	02e9ac92557257d5f4ed5b7391d640fd
URL:		http://www.muppetlabs.com/~breadbox/software/cgames.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The programs in this distribution are re-implementations of games for
the Linux console. Included please find three games:

* cblocks - sliding-block puzzles
* cmines - minesweeper
* csokoban - sokoban

The games make use of the Linux console font (this means they won't
work in any xterm!) and mouse support to improve the user interface.

%description -l pl.UTF-8

Programy w tym pakiecie to reimplementacja gier dla linuksowej
konsoli. Można tu znaleźć trzy gry:

* cblocks - łamigłówka z przesuwaniem klocków
* cmines - saper
* csokoban - sokoban

Gry wykorzystują fonty konsolowe (to oznacza, że nie będą działać w
żadnym xtermie!) i myszkę do usprawnienia interfejsu użytkownika.

%prep
%setup -q

%{__sed} -i -e 's/-g games //' cblocks/Makefile.in csokoban/Makefile.in

%build
%{__aclocal}
%{__autoconf}
cp -f /usr/share/automake/config.* .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/cblocks
%attr(755,root,root) %{_bindir}/cmines
%attr(755,root,root) %{_bindir}/csokoban
%{_datadir}/csokoban
%{_datadir}/cblocks
%{_mandir}/man6/cblocks.6*
%{_mandir}/man6/cmines.6*
%{_mandir}/man6/csokoban.6*
