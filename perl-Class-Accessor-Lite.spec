#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Class
%define		pnam	Accessor-Lite
%include	/usr/lib/rpm/macros.perl
Summary:	Class::Accessor::Lite - a minimalistic variant of Class::Accessor
#Summary(pl.UTF-8):	
Name:		perl-Class-Accessor-Lite
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c487f0ebe2038363b68e9e68ae4beb54
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/Class-Accessor-Lite/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The module is a variant of Class::Accessor.  It is fast and requires less typing, has no dependencies to other modules, and does not mess up the @ISA.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Class/Accessor/*.pm
%{_mandir}/man3/*
