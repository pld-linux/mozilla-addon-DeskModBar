Summary:	It lets quickly search around www.deskmod.com site
Summary(pl):	Pozwala na szybkie poruszanie siê po portalu www.deskmod.com
Name:		mozilla-addon-DeskModBar
%define		_realname	deskmodbar
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.deskmod.com/mozillabar/%{_realname}.xpi
Source1:	%{_realname}-installed-chrome.txt
URL:		http://www.deskmod.com/mozillabar/
BuildRequires:	unzip
BuildArch:	noarch
Requires:	mozilla >= 1.0-7
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _chromedir      %{_libdir}/mozilla/chrome

%description
It lets quickly search around www.deskmod.com site.

%description -l pl
Pozwala na szybkie poruszanie siê oraz przeszukiwanie portalu
www.deskmod.com, na którym znajduj± siê tematy oraz skórki do ró¿nych
programów.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%post
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
