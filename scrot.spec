
%define name	scrot
%define version	0.8
%define rel     3
%define release %mkrel %rel
%define summary Screen-shot capture using Imlib 2



Summary:        %summary
Name:           %name
Version: 	%version
Release: 	%release
License: 	BSD
Group:		Graphics
Source: 	http://linuxbrit.co.uk/downloads/%{name}-%{version}.tar.gz
Url: 		http://www.linuxbrit.co.uk
BuildRoot:      %{_tmppath}/%{name}-buildroot
Buildrequires:  libgiblib-devel
Buildrequires:  autoconf2.5

	

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
rm -rf %buildroot
mkdir -p %buildroot%_defaultdocdir
%{makeinstall_std}

mv %buildroot%_prefix/doc/* %buildroot%_defaultdocdir

%clean 
rm -rf %buildroot

%files
%defattr(-,root,root,755)
%doc %_defaultdocdir/%name
%doc AUTHORS ChangeLog README TODO
%_bindir/%name
%_mandir/man1/%name.1.*
