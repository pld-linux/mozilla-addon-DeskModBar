Summary:	It lets quickly search around www.deskmod.com site
Summary(pl):	Umo¿liwienie szybkiego poruszania siê po portalu www.deskmod.com
Name:		mozilla-addon-DeskModBar
%define		_realname	deskmodbar
Version:	1.0
Release:	4
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.deskmod.com/mozillabar/%{_realname}.xpi
# Source0-md5:	9c175c9fde253dfaaca887979e0dc8b7
Source1:	%{_realname}-installed-chrome.txt
URL:		http://www.deskmod.com/mozillabar/
BuildRequires:	unzip
Requires(post,postun):	mozilla
Requires(post,postun):	textutils
Requires:	mozilla >= 1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
It lets quickly search around www.deskmod.com site.

%description -l pl
Pozwala na szybkie poruszanie siê oraz przeszukiwanie portalu
www.deskmod.com, na którym znajduj± siê motywy oraz skórki do ró¿nych
programów.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt ||:
rm -f %{_libdir}/mozilla/components/{compreg,xpti}.dat \
	%{_datadir}/mozilla/chrome/{chrome.rdf,overlayinfo/*/*/*.rdf} ||:
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regxpcom ||:
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regchrome ||:

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt
rm -f %{_libdir}/mozilla/components/{compreg,xpti}.dat \
	%{_datadir}/mozilla/chrome/{chrome.rdf,overlayinfo/*/*/*.rdf}
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regxpcom
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regchrome

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
