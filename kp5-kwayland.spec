# TODO:
# wayland-scanner from wayland project
#
%define		kdeplasmaver	5.5.4
%define		qtver		5.3.2
%define		kpname		kwayland

Summary:	Qt-style Client and Server library wrapper for the Wayland libraries
Name:		kp5-%{kpname}
Version:	5.5.4
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	c0e92aa7fd9f868bb565b5d39a382d81
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	wayland-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
Qt-style Client and Server library wrapper for the Wayland libraries.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
/etc/xdg/org_kde_kwayland.categories
%attr(755,root,root) %ghost %{_libdir}/libKF5WaylandClient.so.5
%attr(755,root,root) %{_libdir}/libKF5WaylandClient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5WaylandServer.so.5
%attr(755,root,root) %{_libdir}/libKF5WaylandServer.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KWayland
%{_includedir}/KF5/kwayland_version.h
%{_libdir}/cmake/KF5Wayland
%{_libdir}/qt5/mkspecs/modules/qt_KWaylandClient.pri
%{_libdir}/qt5/mkspecs/modules/qt_KWaylandServer.pri
%attr(755,root,root) %{_libdir}/libKF5WaylandClient.so
%attr(755,root,root) %{_libdir}/libKF5WaylandServer.so
