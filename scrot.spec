Summary:	Screen-shot capture using Imlib 2
Name:		scrot
Version:	1.2
Release:	1
License:	BSD
Group:		Graphics
Source0:	https://github.com/resurrecting-open-source-projects/scrot/archive/%{version}.tar.gz
Url:		http://www.linuxbrit.co.uk
BuildRequires:	pkgconfig(giblib)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(imlib2)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	autoconf2.5
BuildRequires:	autoconf-archive

%description
A nice and straightforward screen capture utility implementing the 
dynamic loaders of imlib2.

%prep
%setup -q 

%build
autoreconf -fiv
%configure
%make

%install
%{makeinstall_std}

%files
%_bindir/%name
%_mandir/man1/%name.1.*
