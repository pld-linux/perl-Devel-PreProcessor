%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	PreProcessor
Summary:	Devel::PreProcessor perl module
Summary(pl):	Modu³ perla Devel::PreProcessor
Name:		perl-Devel-PreProcessor
Version:	1999.0220
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::PreProcessor perl module inlining and other Perl source
manipulations.

%description -l pl
Modu³ perla Devel::PreProcessor.

%prep
%setup -q -n %{pdir}-%{pnam}-1999.022
%patch -p1

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Devel/PreProcessor.pm
%{_mandir}/man3/*
