%define		pdir	Devel
%define		pnam	PreProcessor
Summary:	Devel::PreProcessor - module inlining and other Perl source manipulations
Summary(pl.UTF-8):	Devel::PreProcessor - moduł osadzający i inne manipulacje na źródłach w Perlu
Name:		perl-Devel-PreProcessor
Version:	2003.1128
Release:	4
# same as perl
# README says it is Artistic only
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1bb472d159833263085b44d866381deb
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/Devel-PreProcessor/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::PreProcessor is a Perl module that prforms inlining and other
Perl source manipulations.

%description -l pl.UTF-8
Moduł Perla Devel::PreProcessor obsługuje osadzanie kodu i inne
manipulacje na kodzie źródłowym w Perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p3

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Devel/PreProcessor.pm
%{_mandir}/man3/*
