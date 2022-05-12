%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		kbackup
Version:	22.04.1
Release:	1
Summary:	A simple and easy to use program to backup directories or files
License:	GPLv2
Group:		Archiving/Backup
URL:		http://www.kde-apps.org/content/show.php?action=content&content=44998
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(SharedMimeInfo)
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
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --with-html --all-name --with-man

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/icons/*/*/*/*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/kxmlgui5/kbackup/kbackupui.rc
%{_datadir}/metainfo/org.kde.kbackup.appdata.xml
%{_mandir}/man1/kbackup.1*
