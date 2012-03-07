# Spec is based on Giovanni Mariani's work in MIB

Name:		kbackup
Version:	0.7.1
Release:	%mkrel 1
Summary:	A simple and easy to use program to backup directories or files
License:	GPLv2
Group:		Archiving/Backup
URL:		http://www.kde-apps.org/content/show.php?action=content&content=44998
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	cmake
# From configure output
BuildRequires:	shared-mime-info >= 0.71
BuildRequires:	kdelibs4-devel
BuildRequires:	qt4-devel
BuildRequires:	desktop-file-utils

%description
KBackup is a program that lets you back up any directories or files,
whereby it uses an easy to use directory tree to select the things to
back up. The program was designed to be very simple in its use so that it
can be used by non-computer experts. The storage format is the well known
TAR format, whereby the data is still stored in compressed format (bzip2
or gzip).

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}

%makeinstall_std -C build

%find_lang %{name} --with-html

desktop-file-install \
	--remove-category="X-SuSE-Backup" \
	--add-category="Archiving" \
	--dir %{buildroot}%{_kde_applicationsdir} \
	%{buildroot}%{_kde_applicationsdir}/%{name}.desktop

%clean
%__rm -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%{_kde_bindir}/%{name}
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_appsdir}/%{name}/icons/hicolor/22x22/*/*
%{_kde_iconsdir}/hicolor/*/*/*
%{_kde_appsdir}/%{name}/*.rc
%{_kde_datadir}/mime/packages/%{name}.xml

