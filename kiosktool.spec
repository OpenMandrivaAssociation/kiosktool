%define svn    1233438
Name:          kiosktool
Version:       1.99.1
Release:       0.%svn.1
Summary:       Tool for system administrators to enable KDE's KIOSK
Group:         Networking/File transfer
License:       GPLv2+
Url:           https://www.kde.org
Source0:       %{name}-%{version}.%svn.tar.bz2
BuildRequires: kdelibs4-devel
BuildRequires: kdebase4-workspace

%description
Point&Click tool for system administrators to enable KDE's KIOSK 
features or otherwise preconfigure KDE for groups of users.

%files
%defattr(-,root,root)
%_kde_bindir/kiosktool
%_kde_bindir/kiosktool-kdedirs
%_kde_datadir/applications/kde4/kiosktool.desktop
%_kde_appsdir/kiosktool/actions.kiosk
%_kde_appsdir/kiosktool/general.kiosk
%_kde_appsdir/kiosktool/kiosktoolui.rc
%_kde_appsdir/kiosktool/themes.kiosk
%_kde_iconsdir/hicolor/16x16/apps/kiosktool.png
%_kde_iconsdir/hicolor/22x22/apps/kiosktool.png
%_kde_iconsdir/hicolor/32x32/apps/kiosktool.png
%_kde_iconsdir/hicolor/48x48/apps/kiosktool.png
%_kde_iconsdir/hicolor/scalable/actions/kiosktool_filt_gid.svgz
%_kde_iconsdir/hicolor/scalable/actions/kiosktool_filt_uid.svgz

#-------------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4 
%make
 
%install
%makeinstall_std -C build
