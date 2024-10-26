%define	upstream_name    Specio

Name:		perl-%{upstream_name}
Version:	0.48
Release:	1

Summary:	Type constraints and coercions for Perl
License:	Artistic 2.0
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/%{upstream_name}-%{version}.tar.gz

BuildRequires:  perl-devel
BuildRequires:	perl(namespace::clean)
BuildRequires:	perl(Module::Build)

BuildArch:	noarch


%description
Type constraints and coercions for Perl

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
perl Makefile.PL installdirs=vendor destdir=%{buildroot}
%make_build

%install
%make_install

%files
%doc Changes 
%{perl_vendorlib}/Specio
%{perl_vendorlib}/Specio.pm
%{perl_vendorlib}/Test/Specio.pm
%{_mandir}/*/*
