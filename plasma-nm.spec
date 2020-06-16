#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : plasma-nm
Version  : 5.19.1
Release  : 40
URL      : https://download.kde.org/stable/plasma/5.19.1/plasma-nm-5.19.1.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.19.1/plasma-nm-5.19.1.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.19.1/plasma-nm-5.19.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: plasma-nm-data = %{version}-%{release}
Requires: plasma-nm-lib = %{version}-%{release}
Requires: plasma-nm-license = %{version}-%{release}
Requires: plasma-nm-locales = %{version}-%{release}
BuildRequires : ModemManager-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : ki18n-dev
BuildRequires : kirigami2-dev
BuildRequires : modemmanager-qt-dev
BuildRequires : openconnect-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : plasma-framework-dev
BuildRequires : prison-dev
BuildRequires : qca-qt5-dev
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev

%description
Plasma-nm
========================
Plasma applet written in QML for managing network connections

%package data
Summary: data components for the plasma-nm package.
Group: Data

%description data
data components for the plasma-nm package.


%package dev
Summary: dev components for the plasma-nm package.
Group: Development
Requires: plasma-nm-lib = %{version}-%{release}
Requires: plasma-nm-data = %{version}-%{release}
Provides: plasma-nm-devel = %{version}-%{release}
Requires: plasma-nm = %{version}-%{release}

%description dev
dev components for the plasma-nm package.


%package lib
Summary: lib components for the plasma-nm package.
Group: Libraries
Requires: plasma-nm-data = %{version}-%{release}
Requires: plasma-nm-license = %{version}-%{release}

%description lib
lib components for the plasma-nm package.


%package license
Summary: license components for the plasma-nm package.
Group: Default

%description license
license components for the plasma-nm package.


%package locales
Summary: locales components for the plasma-nm package.
Group: Default

%description locales
locales components for the plasma-nm package.


%prep
%setup -q -n plasma-nm-5.19.1
cd %{_builddir}/plasma-nm-5.19.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592333642
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1592333642
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma-nm
cp %{_builddir}/plasma-nm-5.19.1/COPYING %{buildroot}/usr/share/package-licenses/plasma-nm/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/plasma-nm-5.19.1/COPYING.LIB %{buildroot}/usr/share/package-licenses/plasma-nm/01a6b4bf79aca9b556822601186afab86e8c4fbf
pushd clr-build
%make_install
popd
%find_lang plasma_applet_org.kde.plasma.networkmanagement
%find_lang plasmanetworkmanagement-kded
%find_lang plasmanetworkmanagement-libs
%find_lang plasmanetworkmanagement_l2tpui
%find_lang plasmanetworkmanagement_openconnectui
%find_lang plasmanetworkmanagement_openvpnui
%find_lang plasmanetworkmanagement_vpncui
%find_lang plasmanetworkmanagement-kcm
%find_lang plasmanetworkmanagement_openswanui
%find_lang plasmanetworkmanagement_pptpui
%find_lang plasmanetworkmanagement_strongswanui
%find_lang kcm_mobile_broadband
%find_lang kcm_mobile_hotspot
%find_lang kcm_mobile_wifi
%find_lang plasmanetworkmanagement_fortisslvpnui
%find_lang plasmanetworkmanagement_iodineui
%find_lang plasmanetworkmanagement_sshui
%find_lang plasmanetworkmanagement_sstpui

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kcm_networkmanagement/qml/AddConnectionDialog.qml
/usr/share/kcm_networkmanagement/qml/ConfigurationDialog.qml
/usr/share/kcm_networkmanagement/qml/ConnectionItem.qml
/usr/share/kcm_networkmanagement/qml/Header.qml
/usr/share/kcm_networkmanagement/qml/ListItem.qml
/usr/share/kcm_networkmanagement/qml/main.qml
/usr/share/knotifications5/networkmanagement.notifyrc
/usr/share/kservices5/kcm_networkmanagement.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.networkmanagement.desktop
/usr/share/kservices5/plasmanetworkmanagement_fortisslvpnui.desktop
/usr/share/kservices5/plasmanetworkmanagement_iodineui.desktop
/usr/share/kservices5/plasmanetworkmanagement_l2tpui.desktop
/usr/share/kservices5/plasmanetworkmanagement_openconnect_globalprotectui.desktop
/usr/share/kservices5/plasmanetworkmanagement_openconnect_juniperui.desktop
/usr/share/kservices5/plasmanetworkmanagement_openconnectui.desktop
/usr/share/kservices5/plasmanetworkmanagement_openswanui.desktop
/usr/share/kservices5/plasmanetworkmanagement_openvpnui.desktop
/usr/share/kservices5/plasmanetworkmanagement_pptpui.desktop
/usr/share/kservices5/plasmanetworkmanagement_sshui.desktop
/usr/share/kservices5/plasmanetworkmanagement_sstpui.desktop
/usr/share/kservices5/plasmanetworkmanagement_strongswanui.desktop
/usr/share/kservices5/plasmanetworkmanagement_vpncui.desktop
/usr/share/kservicetypes5/plasma-networkmanagement-vpnuiplugin.desktop
/usr/share/metainfo/org.kde.plasma.networkmanagement.appdata.xml
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/contents.rcc
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/metadata.json

%files dev
%defattr(-,root,root,-)
/usr/lib64/libplasmanm_editor.so
/usr/lib64/libplasmanm_internal.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kcm_networkmanagement.so
/usr/lib64/qt5/plugins/kf5/kded/networkmanagement.so
/usr/lib64/qt5/plugins/libplasmanetworkmanagement_fortisslvpnui.so
/usr/lib64/qt5/plugins/libplasmanetworkmanagement_iodineui.so
/usr/lib64/qt5/plugins/libplasmanetworkmanagement_l2tpui.so
/usr/lib64/qt5/plugins/libplasmanetworkmanagement_openconnectui.so
/usr/lib64/qt5/plugins/libplasmanetworkmanagement_openswanui.so
/usr/lib64/qt5/plugins/libplasmanetworkmanagement_openvpnui.so
/usr/lib64/qt5/plugins/libplasmanetworkmanagement_pptpui.so
/usr/lib64/qt5/plugins/libplasmanetworkmanagement_sshui.so
/usr/lib64/qt5/plugins/libplasmanetworkmanagement_sstpui.so
/usr/lib64/qt5/plugins/libplasmanetworkmanagement_strongswanui.so
/usr/lib64/qt5/plugins/libplasmanetworkmanagement_vpncui.so
/usr/lib64/qt5/qml/org/kde/plasma/networkmanagement/libplasmanm_qmlplugins.so
/usr/lib64/qt5/qml/org/kde/plasma/networkmanagement/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plasma-nm/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/plasma-nm/4cc77b90af91e615a64ae04893fdffa7939db84c

%files locales -f plasma_applet_org.kde.plasma.networkmanagement.lang -f plasmanetworkmanagement-kded.lang -f plasmanetworkmanagement-libs.lang -f plasmanetworkmanagement_l2tpui.lang -f plasmanetworkmanagement_openconnectui.lang -f plasmanetworkmanagement_openvpnui.lang -f plasmanetworkmanagement_vpncui.lang -f plasmanetworkmanagement-kcm.lang -f plasmanetworkmanagement_openswanui.lang -f plasmanetworkmanagement_pptpui.lang -f plasmanetworkmanagement_strongswanui.lang -f kcm_mobile_broadband.lang -f kcm_mobile_hotspot.lang -f kcm_mobile_wifi.lang -f plasmanetworkmanagement_fortisslvpnui.lang -f plasmanetworkmanagement_iodineui.lang -f plasmanetworkmanagement_sshui.lang -f plasmanetworkmanagement_sstpui.lang
%defattr(-,root,root,-)

