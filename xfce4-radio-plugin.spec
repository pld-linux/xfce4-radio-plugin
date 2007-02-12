Summary:	Radio plugin for the Xfce panel
Summary(pl.UTF-8):   Wtyczka z radiem dla panelu Xfce
Name:		xfce4-radio-plugin
Version:	0.2.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	b67b164266a58f3651201be11b6aea04
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-radio-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
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

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
