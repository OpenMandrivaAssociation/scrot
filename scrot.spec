Summary:	Screen-shot capture using Imlib 2
Name:		scrot
Version:	0.8
Release:	7
License:	BSD
Group:		Graphics
Source0:	http://linuxbrit.co.uk/downloads/%{name}-%{version}.tar.gz
Url:		http://www.linuxbrit.co.uk
BuildRequires:	pkgconfig(giblib)
BuildRequires:	autoconf2.5

%description
A nice and straightforward screen capture utility implementing the 
dynamic loaders of imlib2.

%prep
%setup -q 

%build
%configure

%make

%install
mkdir -p %buildroot%_defaultdocdir
%{makeinstall_std}
mv %buildroot%_prefix/doc/* %buildroot%_defaultdocdir

%files
%doc %_defaultdocdir/%name
%_bindir/%name
%_mandir/man1/%name.1.*
