#
# Conditional build:
%bcond_without	smp		# don't build SMP module
%bcond_without	dist_kernel	# allow non-distribution kernel
%bcond_with	verbose		# verbose build (V=1)
#
%define		_orig_name	ipp2p
%define		_rel 1
%define		no_install_post_compress_modules	1
#
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

%description -n kernel-smp-net-ipp2p -l pl
- -- pusty --

%package -n iptables-ipp2p
Summary:	ipp2p
Summary(pl):	ipp2p
Release:	%{_rel}
Group:		Base/Kernel
Requires:	iptables

%description -n iptables-ipp2p
- -- empty --

%description -n iptables-ipp2p -l pl
- -- pusty --

%prep
%setup -q -n %{_orig_name}

#%patch

%build
# iptables module
cat << EOF > Makefile
CC		= %{__cc}
CFLAGS		= %{rpmcflags} -fPIC -DNETFILTER_VERSION=\\"1.2.9\\"
INCPATH		= -I%{_includedir}/iptables
LD		= %{__ld}
.SUFFIXES:	.c .o .so
.c.o:
		\$(CC) \$(CFLAGS) \$(INCPATH) -c -o \$@ \$<
.o.so:
		\$(LD) -shared -o \$@ \$<
all:		libipt_%{_orig_name}.so
EOF
%{__make}

# kernel module
cfg=%{_kernelsrcdir}/config-%{?with_smp:smp}%{!?with_smp:%{?with_dist_kernel:up}%{!?with_dist_kernel:nondist}}
if [ ! -r "$cfg" ]; then
    exit 1
fi
CWD=`pwd`
%{__make} -C %{_kernelsrcdir} SUBDIRS=$PWD O=$PWD %{?with_verbose:V=1} mrproper
ln -sf $cfg .config
install -d include/{linux,config}
ln -sf %{_kernelsrcdir}/include/asm-%{_arch} include/asm
touch include/config/MARKER
echo "obj-m := ipt_%{_orig_name}.o" > Makefile
%{__make} -C %{_kernelsrcdir} SUBDIRS=$PWD O=$PWD %{?with_verbose:V=1} modules

%install
rm -rf $RPM_BUILD_ROOT
install -d \
    $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver_str}%{?with_smp:smp}/kernel/drivers/net \
    $RPM_BUILD_ROOT%{_libdir}/iptables

if [ %(echo %{_kernel_ver_str} | cut -d. -f1-2) == "2.6" ]; then
    ext="ko"
else
    ext="o"
fi

install \
    ipt_%{_orig_name}.$ext \
    $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver_str}%{?with_smp:smp}/kernel/drivers/net/

install \
    libipt_%{_orig_name}.so \
    $RPM_BUILD_ROOT%{_libdir}/iptables/

%post
%depmod %{_kernel_ver_str}

%postun
%depmod %{_kernel_ver_str}

%post -n kernel-smp-net-ipp2p
%depmod %{_kernel_ver_str}

%postun -n kernel-smp-net-ipp2p
%depmod %{_kernel_ver_str}

%post -n iptables-ipp2p
%postun -n iptables-ipp2p

%clean
rm -rf $RPM_BUILD_ROOT

%if !%{with smp}
%files
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver_str}/kernel/drivers/net/*
%endif

%if %{with smp}
%files -n kernel-smp-net-ipp2p
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver_str}smp/kernel/drivers/net/*
%endif

%files -n iptables-ipp2p
%defattr(644,root,root,755)
%{_prefix}/lib/iptables/*
