Summary:	Lightweight GTK+ music manager
Name:		pragha
Version:	1.1.1
Release:	1
Group:		Sound
License:	GPLv3+
URL:		http://pragha.wikispaces.com/
Source0:	https://github.com/downloads/matiasdelellis/pragha/%{name}-%{version}.tar.bz2	
Patch0:		pragha-0.97.0-cflags-O3.patch
BuildRequires:	libalsa-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk2-devel
BuildRequires:	libflac-devel
BuildRequires:	keybinder-devel
BuildRequires:	gstreamer0.10-devel
BuildRequires:	pkgconfig(gstreamer-app-0.10)
BuildRequires:	libcddb-devel
BuildRequires:	libcdio-devel
BuildRequires:	libcurl-devel
#BuildRequires:  liblastfm-devel >= 0.4
BuildRequires:	libnotify-devel
BuildRequires:	sqlite-devel
BuildRequires:	taglib-devel
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
