%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	PreProcessor
Summary:	Devel::PreProcessor perl module
Summary(pl):	Modu� perla Devel::PreProcessor
Name:		perl-Devel-PreProcessor
Version:	2003.1128
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1bb472d159833263085b44d866381deb
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::PreProcessor Perl module - inlining and other Perl source
manipulations.

%description -l pl
Modu� Perla Devel::PreProcessor obs�uguje osadzanie kodu i inne
manipulacje na kodzie �r�d�owym w Perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p3

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
