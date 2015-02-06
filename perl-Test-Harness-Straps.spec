%define upstream_name    Test-Harness-Straps
%define upstream_version 0.30

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    5

Summary:    Internal Test::Harness Iterator
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(File::Spec)
BuildRequires: perl(Module::Build)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The construct

  use if CONDITION, MODULE => ARGUMENTS;

has no effect unless 'CONDITION' is true. In this case the effect is the
same as of

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor

./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.300.0-3mdv2011.0
+ Revision: 658549
- rebuild for updated spec-helper

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-2mdv2011.0
+ Revision: 552181
- rebuild

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-1mdv2010.0
+ Revision: 395361
- import perl-Test-Harness-Straps


* Sun Jul 12 2009 cpan2dist 0.30-1mdv
- initial mdv release, generated with cpan2dist
