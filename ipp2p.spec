%define		_orig_name	ipp2p
Summary:	ipp2p
Summary(pl):	ipp2p
Name:		%{_orig_name}
Version:	05b
Release:	1
License:	GPL
Group:		Kernel
######		Unknown group!
Source0:	http://rnvs.informatik.uni-leipzig.de/%{_orig_name}/downloads/%{name}.%{version}.tar.gz
# Source0-md5:	5cf214c6132d88ac5f0c859e6b8ae792
BuildRequires:	kernel-module-build
BuildRequires:	iptables-devel
#Requires:
URL:		http://rnvs.informatik.uni-leipzig.de/ipp2p/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
- -- empty --

%description -l pl
- -- pusty --

%prep
%setup -q -n %{_orig_name}

#%patch

%build
rm -rf build-done
install -d build-done/{UP/SMP}
## iptables
#%%{__make} libipt_ipp2p 
## kernel
ln -sf %{_kernelsrcdir}/config-up .config
rm -rf include
install -d include/{linux,config}
ln -sf %{_kernelsrcdir}/include/linux/autoconf.h  include/linux/autoconf.h 
ln -sf %{_kernelsrcdir}/include/asm-%{_arch} include/asm
touch include/config/MARKER
echo 'obj-m := ipt_ipp2p.o' >Makefile
%{__make} -C %{_kernelsrcdir} SUBDIR=$PWD O=$PWD V=1 modules

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
