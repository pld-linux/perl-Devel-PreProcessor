%include	/usr/lib/rpm/macros.perl
Summary:	Devel-PreProcessor perl module
Summary(pl):	Modu� perla Devel-PreProcessor
Name:		perl-Devel-PreProcessor
Version:	1999.0220
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Devel/Devel-PreProcessor-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel-PreProcessor perl module inlining and other Perl source
manipulations.

%description -l pl
Modu� perla Devel-PreProcessor.

%prep
%setup -q -n Devel-PreProcessor-1999.022
%patch -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Devel/PreProcessor.pm
%{_mandir}/man3/*
