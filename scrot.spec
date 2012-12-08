%define name	scrot
%define version	0.8
%define rel     3
%define release %rel
%define summary Screen-shot capture using Imlib 2

Summary:        %summary
Name:           %name
Version: 	%version
Release: 	%release
License: 	BSD
Group:		Graphics
Source: 		http://linuxbrit.co.uk/downloads/%{name}-%{version}.tar.gz
Url: 		http://www.linuxbrit.co.uk
BuildRequires:  pkgconfig(giblib)
BuildRequires:  autoconf2.5

%description
A nice and straightforward screen capture utility implementing the 
dynamic loaders of imlib2.

%prep
%setup -q 

%build
CFLAGS="$RPM_OPT_FLAGS"
%configure2_5x

%make

%install
mkdir -p %buildroot%_defaultdocdir
%{makeinstall_std}
mv %buildroot%_prefix/doc/* %buildroot%_defaultdocdir

%files
%doc %_defaultdocdir/%name
%_bindir/%name
%_mandir/man1/%name.1.*


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.8-3mdv2010.0
+ Revision: 433631
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.8-2mdv2009.0
+ Revision: 140776
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 15 2007 Pascal Terjan <pterjan@mandriva.org> 0.8-2mdv2008.0
+ Revision: 63819
- Fix manpage listing
- Tag the documentation as doc
- Use autoconf 2.5
- Improve description wraping
- Import scrot



* Mon Apr 03 2006 Sebastien Savarin <plouf@mandriva.org> 0.8-1mdk
- First Mandriva Linux release
