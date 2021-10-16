#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : plasma-nm
Version  : 5.23.0
Release  : 53
URL      : https://download.kde.org/stable/plasma/5.23.0/plasma-nm-5.23.0.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.23.0/plasma-nm-5.23.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
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
BuildRequires : pkg-config
BuildRequires : pkgconfig(mobile-broadband-provider-info)
BuildRequires : plasma-framework-dev
BuildRequires : prison-dev
BuildRequires : qca-qt5-dev
BuildRequires : qtbase-dev mesa-dev

%description
auth dialog
AnyConnect works over HTTPS; authentication is through HTTP forms and
POST responses. Once you've filled in the forms that the server demands,
you're rewarded with an HTTP cookie which is handed on to OpenConnect to
actually make the connection.

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
%setup -q -n plasma-nm-5.23.0
cd %{_builddir}/plasma-nm-5.23.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634419588
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1634419588
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma-nm
cp %{_builddir}/plasma-nm-5.23.0/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/plasma-nm/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/plasma-nm-5.23.0/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-nm/3e8971c6c5f16674958913a94a36b1ea7a00ac46
cp %{_builddir}/plasma-nm-5.23.0/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/plasma-nm/3e8971c6c5f16674958913a94a36b1ea7a00ac46
cp %{_builddir}/plasma-nm-5.23.0/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-nm/2123756e0b1fc8243547235a33c0fcabfe3b9a51
cp %{_builddir}/plasma-nm-5.23.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/plasma-nm/a4c60b3fefda228cd7439d3565df043192fef137
cp %{_builddir}/plasma-nm-5.23.0/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/plasma-nm/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
cp %{_builddir}/plasma-nm-5.23.0/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-nm/19d98e1b6f8ef12849ea4012a052d3907f336c91
cp %{_builddir}/plasma-nm-5.23.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-nm/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/plasma-nm-5.23.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-nm/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/plasma-nm-5.23.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/plasma-nm/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/plasma-nm-5.23.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/plasma-nm/e458941548e0864907e654fa2e192844ae90fc32
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
%find_lang kcm_mobile_broadband
%find_lang kcm_mobile_hotspot
%find_lang kcm_mobile_wifi
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
/usr/share/kcm_networkmanagement/qml/AddConnectionDialog.qml
/usr/share/kcm_networkmanagement/qml/ConfigurationDialog.qml
/usr/share/kcm_networkmanagement/qml/ConnectionItem.qml
/usr/share/kcm_networkmanagement/qml/ListItem.qml
/usr/share/kcm_networkmanagement/qml/main.qml
/usr/share/knotifications5/networkmanagement.notifyrc
/usr/share/kservices5/kcm_networkmanagement.desktop
/usr/share/metainfo/org.kde.plasma.networkmanagement.appdata.xml
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/contents/ui/CompactRepresentation.qml
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/contents/ui/ConnectionItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/contents/ui/DetailsText.qml
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/contents/ui/ListItem.qml
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/contents/ui/PasswordField.qml
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/contents/ui/PopupDialog.qml
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/contents/ui/ShowQR.qml
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/contents/ui/Toolbar.qml
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/contents/ui/TrafficMonitor.qml
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.plasma.networkmanagement/metadata.json

%files dev
%defattr(-,root,root,-)
/usr/lib64/libplasmanm_editor.so
/usr/lib64/libplasmanm_internal.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kcm_networkmanagement.so
/usr/lib64/qt5/plugins/kf5/kded/networkmanagement.so
/usr/lib64/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_fortisslvpnui.so
/usr/lib64/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_iodineui.so
/usr/lib64/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_l2tpui.so
/usr/lib64/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_openconnect_anyconnect.so
/usr/lib64/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_openconnect_globalprotectui.so
/usr/lib64/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_openconnect_juniperui.so
/usr/lib64/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_openconnect_pulseui.so
/usr/lib64/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_openswanui.so
/usr/lib64/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_openvpnui.so
/usr/lib64/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_pptpui.so
/usr/lib64/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_sshui.so
/usr/lib64/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_sstpui.so
/usr/lib64/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_strongswanui.so
/usr/lib64/qt5/plugins/plasma/network/vpn/plasmanetworkmanagement_vpncui.so
/usr/lib64/qt5/qml/org/kde/plasma/networkmanagement/libplasmanm_qmlplugins.so
/usr/lib64/qt5/qml/org/kde/plasma/networkmanagement/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plasma-nm/19d98e1b6f8ef12849ea4012a052d3907f336c91
/usr/share/package-licenses/plasma-nm/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/plasma-nm/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/plasma-nm/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/plasma-nm/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/plasma-nm/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/plasma-nm/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/plasma-nm/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f plasma_applet_org.kde.plasma.networkmanagement.lang -f plasmanetworkmanagement-kded.lang -f plasmanetworkmanagement-libs.lang -f plasmanetworkmanagement_l2tpui.lang -f plasmanetworkmanagement_openconnectui.lang -f plasmanetworkmanagement_openvpnui.lang -f plasmanetworkmanagement_vpncui.lang -f plasmanetworkmanagement-kcm.lang -f kcm_mobile_broadband.lang -f kcm_mobile_hotspot.lang -f kcm_mobile_wifi.lang -f plasmanetworkmanagement_fortisslvpnui.lang -f plasmanetworkmanagement_iodineui.lang -f plasmanetworkmanagement_openswanui.lang -f plasmanetworkmanagement_pptpui.lang -f plasmanetworkmanagement_sshui.lang -f plasmanetworkmanagement_sstpui.lang -f plasmanetworkmanagement_strongswanui.lang
%defattr(-,root,root,-)

