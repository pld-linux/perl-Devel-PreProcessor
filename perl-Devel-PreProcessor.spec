%include	/usr/lib/rpm/macros.perl
Summary:	Devel-PreProcessor perl module
Summary(pl):	Modu� perla Devel-PreProcessor
Name:		perl-Devel-PreProcessor
Version:	1999.0204
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Devel/Devel-PreProcessor-%{version}.tar.gz
Patch:		perl-Devel-PreProcessor-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Devel-PreProcessor perl module inlining and other Perl source manipulations.

%description -l pl
Modu� perla Devel-PreProcessor.

%prep
%setup -q -n Devel-PreProcessor-%{version}
%patch -p1

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

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
