%define		_orig_name	ipp2p
%define		_rel 1

%define		no_install_post_compress_modiles	1

Summary:	ipp2p
Summary(pl):	ipp2p
Name:		kernel-net-ipp2p
Version:	05b
Release:	%{_rel}@%{_kernel_ver_str}
License:	GPL
Group:		Base/Kernel
Source0:	http://rnvs.informatik.uni-leipzig.de/%{_orig_name}/downloads/%{_orig_name}.%{version}.tar.gz
# Source0-md5:	5cf214c6132d88ac5f0c859e6b8ae792
BuildRequires:	kernel-module-build
BuildRequires:	iptables-devel
Requires(post,postun):	/sbin/depmod
URL:		http://rnvs.informatik.uni-leipzig.de/ipp2p/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
- -- empty --

%description -l pl
- -- pusty --

%package -n kernel-smp-net-ipp2p
Summary:	ipp2p
Summary(pl):	ipp2p
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod

%description -n kernel-smp-net-ipp2p
- -- empty --

%description -l pl -n kernel-smp-net-ipp2p
- -- pusty --

%package -n iptables-ipp2p
Summary:	ipp2p
Summary(pl):	ipp2p
Release:	%{_rel}
Group:		Base/Kernel
Requires:	iptables

%description -n iptables-ipp2p
- -- empty --

%description -l pl -n iptables-ipp2p
- -- pusty --

%prep
%setup -q -n %{_orig_name}

#%patch

%build
rm -rf build-done
install -d build-done/{UP,SMP}
## iptables
echo 'CC = gcc' >Makefile
echo 'CFLAGS = -O2 -Wall -DNETFILTER_VERSION=\"1.2.9\"' >>Makefile
echo 'libipt_ipp2p.so:   libipt_ipp2p.c ipt_ipp2p.h' >>Makefile
echo '	    $(CC) -I/usr/include/iptables -fPIC $(CFLAGS)  -c libipt_ipp2p.c' >>Makefile
echo '	    ld -shared -o libipt_ipp2p.so libipt_ipp2p.o' >>Makefile

make

## kernel
ln -sf %{_kernelsrcdir}/config-up .config
rm -rf include
install -d include/{linux,config}
ln -sf %{_kernelsrcdir}/include/linux/autoconf.h  include/linux/autoconf.h 
ln -sf %{_kernelsrcdir}/include/asm-%{_arch} include/asm
touch include/config/MARKER
echo 'obj-m := ipt_ipp2p.o' >Makefile
%{__make} -C %{_kernelsrcdir} SUBDIRS=$PWD O=$PWD V=1 modules
mv ipt_ipp2p.ko build-done/UP/

%{__make} -C %{_kernelsrcdir} SUBDIRS=$PWD O=$PWD V=1 mrproper

ln -sf %{_kernelsrcdir}/config-smp .config
rm -rf include
install -d include/{linux,config}
ln -sf %{_kernelsrcdir}/include/linux/autoconf.h  include/linux/autoconf.h 
ln -sf %{_kernelsrcdir}/include/asm-%{_arch} include/asm
touch include/config/MARKER
echo 'obj-m := ipt_ipp2p.o' >Makefile
%{__make} -C %{_kernelsrcdir} SUBDIRS=$PWD O=$PWD V=1 modules
mv ipt_ipp2p.ko build-done/SMP/

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}{,smp}/kernel/drivers/net/
install -d $RPM_BUILD_ROOT/usr/lib/iptables/

cp build-done/UP/* $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/kernel/drivers/net/
cp build-done/SMP/* $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/kernel/drivers/net/
cp libipt_ipp2p.so $RPM_BUILD_ROOT/usr/lib/iptables/
%post
%depmod %{_kernel_ver}

%postun
%depmod %{_kernel_ver}

%post -n kernel-smp-net-ipp2p
%depmod %{_kernel_ver}

%postun -n kernel-smp-net-ipp2p
%depmod %{_kernel_ver}

%post -n iptables-ipp2p
%postun -n iptables-ipp2p

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/kernel/drivers/net/*

%files -n kernel-smp-net-ipp2p
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/kernel/drivers/net/*

%files -n iptables-ipp2p
%defattr(644,root,root,755)
/usr/lib/iptables/*
