#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : plasma-nm
Version  : 5.13.4
Release  : 1
URL      : https://download.kde.org/stable/plasma/5.13.4/plasma-nm-5.13.4.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.13.4/plasma-nm-5.13.4.tar.xz
Source99 : https://download.kde.org/stable/plasma/5.13.4/plasma-nm-5.13.4.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: plasma-nm-lib
Requires: plasma-nm-license
Requires: plasma-nm-data
Requires: plasma-nm-locales
BuildRequires : ModemManager-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : modemmanager-qt-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : plasma-framework-dev
BuildRequires : qca-qt5-dev

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
Requires: plasma-nm-lib
Requires: plasma-nm-data
Provides: plasma-nm-devel

%description dev
dev components for the plasma-nm package.


%package lib
Summary: lib components for the plasma-nm package.
Group: Libraries
Requires: plasma-nm-data
Requires: plasma-nm-license

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
%setup -q -n plasma-nm-5.13.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535210464
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1535210464
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/plasma-nm
cp COPYING %{buildroot}/usr/share/doc/plasma-nm/COPYING
cp COPYING.LIB %{buildroot}/usr/share/doc/plasma-nm/COPYING.LIB
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
%find_lang plasmanetworkmanagement_fortisslvpnui
%find_lang plasmanetworkmanagement_iodineui
%find_lang plasmanetworkmanagement_openswanui
%find_lang plasmanetworkmanagement_pptpui
%find_lang plasmanetworkmanagement_sshui
%find_lang plasmanetworkmanagement_sstpui
%find_lang plasmanetworkmanagement_strongswanui

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kcm_networkmanagement/qml/ConnectionItem.qml
/usr/share/kcm_networkmanagement/qml/Dialog.qml
/usr/share/kcm_networkmanagement/qml/Header.qml
/usr/share/kcm_networkmanagement/qml/ListItem.qml
/usr/share/kcm_networkmanagement/qml/main.qml
/usr/share/knotifications5/networkmanagement.notifyrc
/usr/share/kservices5/kcm_networkmanagement.desktop
/usr/share/kservices5/plasma-applet-org.kde.plasma.networkmanagement.desktop
/usr/share/kservices5/plasmanetworkmanagement_fortisslvpnui.desktop
/usr/share/kservices5/plasmanetworkmanagement_iodineui.desktop
/usr/share/kservices5/plasmanetworkmanagement_l2tpui.desktop
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
%defattr(-,root,root,-)
/usr/share/doc/plasma-nm/COPYING
/usr/share/doc/plasma-nm/COPYING.LIB

%files locales -f plasma_applet_org.kde.plasma.networkmanagement.lang -f plasmanetworkmanagement-kded.lang -f plasmanetworkmanagement-libs.lang -f plasmanetworkmanagement_l2tpui.lang -f plasmanetworkmanagement_openconnectui.lang -f plasmanetworkmanagement_openvpnui.lang -f plasmanetworkmanagement_vpncui.lang -f plasmanetworkmanagement-kcm.lang -f plasmanetworkmanagement_fortisslvpnui.lang -f plasmanetworkmanagement_iodineui.lang -f plasmanetworkmanagement_openswanui.lang -f plasmanetworkmanagement_pptpui.lang -f plasmanetworkmanagement_sshui.lang -f plasmanetworkmanagement_sstpui.lang -f plasmanetworkmanagement_strongswanui.lang
%defattr(-,root,root,-)

