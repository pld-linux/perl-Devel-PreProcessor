%include	/usr/lib/rpm/macros.perl
Summary:	Devel-PreProcessor perl module
Summary(pl):	Modu³ perla Devel-PreProcessor
Name:		perl-Devel-PreProcessor
Version:	1999.0220
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Devel/Devel-PreProcessor-%{version}.tar.gz
Patch0:		perl-Devel-PreProcessor-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel-PreProcessor perl module inlining and other Perl source
manipulations.

%description -l pl
Modu³ perla Devel-PreProcessor.

%prep
%setup -q -n Devel-PreProcessor-1999.022
%patch -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Devel/PreProcessor
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Devel/PreProcessor.pm
%{perl_sitearch}/auto/Devel/PreProcessor

%{_mandir}/man3/*
