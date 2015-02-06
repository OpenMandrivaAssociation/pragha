Summary:	Lightweight GTK+ music manager
Name:		pragha
Version:	1.1.1
Release:	2
Group:		Sound
License:	GPLv3+
URL:		http://pragha.wikispaces.com/
Source0:	https://github.com/downloads/matiasdelellis/pragha/%{name}-%{version}.tar.bz2	
Patch0:		pragha-0.97.0-cflags-O3.patch
BuildRequires:	alsa-oss-devel
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	gtk2-devel
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(keybinder)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-app-0.10)
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libcurl)
#BuildRequires:  liblastfm-devel >= 0.4
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(sqlite)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	desktop-file-utils
Requires:       gstreamer0.10-plugins-base

%description
Pragha is is a lightweight GTK+ music manager that aims to be fast, bloat-free,
and light on memory consumption. It is written completely in C and GTK+.

Pragha is a fork of Consonance Music Manager, discontinued by the original
author.

%prep
%setup -q
#%patch0 -p1 -b -O3


%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}
# remove duplicate docs
rm -rf %{buildroot}%{_datadir}/%{name}/doc

%files -f %{name}.lang
# FIXME add AUTHORS and README if not empty
%doc ChangeLog FAQ NEWS
%{_bindir}/pragha
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}/
#%{_datadir}/%{name}/
%{_mandir}/man1/pragha.1.*
