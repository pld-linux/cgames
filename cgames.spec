Summary:	Games for the Linux console
Summary(pl):	Gry na linuksow± konsolê
Name:		cgames
Version:	2.2
Release:	2
License:	GPL
Group:		Applications/Games
Source0:	http://www.muppetlabs.com/~breadbox/pub/software/%{name}-%{version}.tar.gz
# Source0-md5:	6e260e87728bd67975cafbf09d480a01
URL:		http://www.muppetlabs.com/~breadbox/software/cgames.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The programs in this distribution are re-implementations of games for
the Linux console. Included please find three games:

* cblocks -- sliding-block puzzles
* cmines -- minesweeper
* csokoban -- sokoban

The games make use of the Linux console font (this means they won't
work in any xterm!) and mouse support to improve the user interface.

%description -l pl

Programy w tym pakiecie to reimplementacja gier dla linuksowej
konsoli. Mo¿na tu znale¼æ trzy gry:

* cblocks -- ³amig³ówka z przesuwaniem klocków
* cmines -- saper
* csokoban -- sokoban

Gry wykorzystuj± fonty konsolowe (to oznacza, ¿e nie bêd± dzia³aæ w
¿adnym xtermie!) i myszkê do usprawnienia interfejsu u¿ytkownika.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
cp -f /usr/share/automake/config.* .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6} \
	$RPM_BUILD_ROOT%{_datadir}/{csokoban,cblocks}

install csokoban/csokoban $RPM_BUILD_ROOT%{_bindir}
install cmines/cmines $RPM_BUILD_ROOT%{_bindir}
install cblocks/cblocks $RPM_BUILD_ROOT%{_bindir}
install */*.6 $RPM_BUILD_ROOT%{_mandir}/man6
install csokoban/series/* $RPM_BUILD_ROOT%{_datadir}/csokoban
install cblocks/series/* $RPM_BUILD_ROOT%{_datadir}/cblocks

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/csokoban
%{_datadir}/cblocks
%{_mandir}/man6/*
