%include	/usr/lib/rpm/macros.perl
%define	pdir	WWW
%define	pnam	webchat
Summary:	WWW::Chat perl modules for processing web chat scripts
Summary(pl):	Modu³y perla WWW::Chat - do przetwarzania skryptów chata
Name:		perl-WWW-Chat
Version:	0.64
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Data-Dump >= 0.01
BuildRequires:	perl-HTML-Parser >= 2.21
BuildRequires:	perl-URI >= 1.00
BuildRequires:	perl-libwww >= 5.47
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the 'webchatpp' program, with its support
modules WWW::Chat and WWW::Chat::Processor.

The 'webchatpp' program is a preprocessor that turns chat scripts into
plain perl scripts using libwww-perl. When the script created by
webchatpp is feed to perl it will perform the chatting. Chat scripts
are useful for setting up test suites for web applications or just to
automate dialogues with web applications.

%description -l pl
Ten pakiet zawiera program webchatpp wraz z modu³ami pomocniczymi
WWW::Chat i WWW::Chat::Processor.

webchatpp jest preprocesorem t³umacz±cym skrypty chata na zwyk³e
skrypty perla u¿ywaj±ce modu³ów libwww. Utworzony skrypt jest
przekazywany do perla, który przeprowadza dialog. Skrypty chata
s± przydatne do tworzenia testów aplikacji WWW lub automatyzacji
dialogów z aplikacjami WWW.

%prep
%setup -q -n %{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README manual_test.pl
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/WWW/Chat.pm
%{perl_sitelib}/WWW/Chat
%{_mandir}/man[13]/*
