Summary:	Radio plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka z radiem dla panelu Xfce
Name:		xfce4-radio-plugin
Version:	0.5.1
Release:	2
License:	GPL v3
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-radio-plugin/0.5/%{name}-%{version}.tar.bz2
# Source0-md5:	237001f3a134c28c16bcd07b57168150
Patch0:		%{name}-ui.patch
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-radio-plugin
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an Xfce panel plugin which allows you to control your V4l
radio device. You can turn your radio on/off, tune it to some
frequency and manage station presets.

%description -l pl.UTF-8
Ten pakiet zawiera wtyczkę dla panelu Xfce pozwalającą sterować radiem
dostępnym przez interfejs V4l. Można włączać i wyłączać radio, stroić
na jakąś częstotliwość i zarządzać ustawieniami stacji.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-radio-plugin
%{_datadir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/*/*.png
