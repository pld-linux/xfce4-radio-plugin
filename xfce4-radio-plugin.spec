Summary:	Radio plugin for the Xfce panel
Summary(pl):	Wtyczka z radiem dla panelu Xfce
Name:		xfce4-radio-plugin
Version:	0.2.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	b67b164266a58f3651201be11b6aea04
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools
BuildRequires:	xfce4-panel-devel >= 4.3.90.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an Xfce panel plugin which allows you to control your V4l
radio device. You can turn your radio on/off, tune it to some
frequency and manage station presets.

%description -l pl
Ten pakiet zawiera wtyczkê dla panelu Xfce pozwalaj±c± sterowaæ
radiem dostêpnym przez interfejs V4l. Mo¿na w³±czaæ i wy³±czaæ radio,
stroiæ na jak±¶ czêstotliwo¶æ i zarz±dzaæ ustawieniami stacji.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I %{_datadir}/xfce4/dev-tools/m4macros
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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-radio-plugin
%{_datadir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/*/*.png
