Summary:	It lets quickly search around www.deskmod.com site
Summary(pl.UTF-8):	Umożliwienie szybkiego poruszania się po portalu www.deskmod.com
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
Requires(post,postun):	mozilla >= 5:1.7.3-3
Requires(post,postun):	textutils
Requires:	mozilla >= 2:1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
It lets quickly search around www.deskmod.com site.

%description -l pl.UTF-8
Pozwala na szybkie poruszanie się oraz przeszukiwanie portalu
www.deskmod.com, na którym znajdują się motywy oraz skórki do różnych
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
if [ "$1" = 1 ]; then
	%{_sbindir}/mozilla-chrome+xpcom-generate
fi

%postun
[ ! -x %{_sbindir}/mozilla-chrome+xpcom-generate ] || %{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
