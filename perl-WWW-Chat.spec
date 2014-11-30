#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	WWW
%define		pnam	webchat
%include	/usr/lib/rpm/macros.perl
Summary:	WWW::Chat Perl modules - processing web chat scripts
Summary(pl.UTF-8):	Moduły Perla WWW::Chat - przetwarzanie skryptów chata
Name:		perl-WWW-Chat
Version:	0.64
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	1b8ebf6aa942dfd1c79ce6dff7bae134
URL:		http://search.cpan.org/dist/webchat/
BuildRequires:	perl-Data-Dump >= 0.01
BuildRequires:	perl-HTML-Parser >= 2.21
BuildRequires:	perl-URI >= 1.00
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libwww >= 5.47
BuildRequires:	rpm-perlprov >= 4.1-13
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

%description -l pl.UTF-8
Ten pakiet zawiera program webchatpp wraz z modułami pomocniczymi
WWW::Chat i WWW::Chat::Processor.

webchatpp jest preprocesorem tłumaczącym skrypty chata na zwykłe
skrypty Perla używające modułów libwww. Utworzony skrypt jest
przekazywany do Perla, który przeprowadza dialog. Skrypty chata są
przydatne do tworzenia testów aplikacji WWW lub automatyzacji dialogów
z aplikacjami WWW.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
%{perl_vendorlib}/WWW/Chat.pm
%{perl_vendorlib}/WWW/Chat
%{_mandir}/man[13]/*
