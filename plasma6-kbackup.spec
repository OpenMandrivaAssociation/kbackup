#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		plasma6-kbackup
Version:	24.02.1
Release:	%{?git:0.%{git}.}1
Summary:	A simple and easy to use program to backup directories or files
License:	GPLv2
Group:		Archiving/Backup
URL:		http://www.kde-apps.org/content/show.php?action=content&content=44998
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/kbackup/-/archive/%{gitbranch}/kbackup-%{gitbranchd}.tar.bz2#/kbackup-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/kbackup-%{version}.tar.xz
%endif
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(SharedMimeInfo)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	shared-mime-info >= 0.71
BuildRequires:	desktop-file-utils

%description
KBackup is a program that lets you back up any directories or files,
whereby it uses an easy to use directory tree to select the things to
back up. The program was designed to be very simple in its use so that it
can be used by non-computer experts. The storage format is the well known
TAR format, whereby the data is still stored in compressed format (bzip2
or gzip).

%prep
%autosetup -p1 -n kbackup-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --with-html --all-name --with-man

%files -f %{name}.lang
%{_bindir}/kbackup
%{_datadir}/applications/org.kde.kbackup.desktop
%{_datadir}/icons/*/*/*/*
%{_datadir}/mime/packages/kbackup.xml
%{_datadir}/metainfo/org.kde.kbackup.appdata.xml
%{_mandir}/man1/kbackup.1*
