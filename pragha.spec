Summary:	Lightweight GTK+ music manager
Name:		pragha
Version:	1.3.99.1
Release:	1
Group:		Sound
License:	GPLv3+
URL:		https://github.com/pragha-music-player/pragha
Source0:	https://github.com/pragha-music-player/pragha/archive/refs/tags/v%{version}.tar.gz
Patch0:		pragha-fix-makefile.patch
BuildRequires:	alsa-oss-devel
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-base-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libcurl)
#BuildRequires:  liblastfm-devel >= 0.4
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(libpeas-1.0)
BuildRequires:	pkgconfig(libpeas-gtk-1.0)
BuildRequires:	desktop-file-utils
BuildRequires:	xfce4-dev-tools

%description
Pragha is is a lightweight GTK+ music manager that aims to be fast, bloat-free,
and light on memory consumption. It is written completely in C and GTK+.

Pragha is a fork of Consonance Music Manager, discontinued by the original
author.

%prep
%autosetup -p1
./autogen.sh
%configure

%build
%make_build

%install
%make_install

%find_lang %{name}
# remove duplicate docs
rm -rf %{buildroot}%{_datadir}/%{name}/doc

# Nothing uses the -devel files, so no point in shipping them
rm -rf %{buildroot}%{_includedir} %{buildroot}%{_libdir}/*.so %{buildroot}%{_libdir}/pkgconfig

%files -f %{name}.lang
# FIXME add AUTHORS and README if not empty
%doc ChangeLog FAQ NEWS README
%{_bindir}/pragha
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_datadir}/pixmaps/%{name}/
#%{_datadir}/%{name}/
%{_mandir}/man1/pragha.1*
%{_libdir}/pragha
%{_datadir}/metainfo/io.github.pragha_music_player.metainfo.xml
%{_datadir}/pragha
