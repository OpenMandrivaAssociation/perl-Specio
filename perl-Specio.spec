%define	upstream_name    Specio
%define upstream_version 0.42

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Type constraints and coercions for Perl
License:	Artistic 2.0
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl-devel
BuildRequires:	perl(namespace::clean)
BuildRequires:	perl(Module::Build)

BuildArch:	noarch


%description
Type constraints and coercions for Perl

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL installdirs=vendor destdir=%{buildroot}
%make

%install
%makeinstall_std

%files
%doc Changes 
%{perl_vendorlib}/Specio
%{perl_vendorlib}/Specio.pm
%{perl_vendorlib}/Test/Specio.pm
%{_mandir}/*/*
