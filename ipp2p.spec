#
# Conditional build:
%bcond_without	dist_kernel	# allow non-distribution kernel
%bcond_without	userspace	# don't build userspace module
%bcond_with	verbose		# verbose build (V=1)
#
%define		_orig_name	ipp2p
%define		_rel 2
%define		no_install_post_compress_modules	1
#
Summary:	IPP2P - a netfilter extension to identify P2P filesharing traffic
Summary(pl):	IPP2P - rozszerzenie filtru pakiet�w identyfikuj�ce ruch P2P
Name:		kernel-net-ipp2p
Version:	0.5c
Release:	%{_rel}@%{_kernel_ver_str}
License:	GPL
Group:		Base/Kernel
Source0:	http://rnvs.informatik.uni-leipzig.de/%{_orig_name}/downloads/%{_orig_name}-%{version}_2.6.tar.gz
# Source0-md5:	d4768dfdd872aa000971744bc9dc464f
URL:		http://rnvs.informatik.uni-leipzig.de/ipp2p/
%{?with_userspace:BuildRequires:	iptables-devel}
BuildRequires:	kernel-module-build
%{?with_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPP2P is a netfilter extension to identify P2P filesharing traffic.
The main goal for developing IPP2P was giving the adminstrator a
dynamic tool to filter the traffic in an intelligent way. So it
doesn't aim at prohibiting all P2P traffic but make it possible to
shape this traffic to a given rate. For this purpose IPP2P searchs the
payload of TCP packets for signaling patterns of P2P networks. As
these patterns are not being present in all P2P packets we had to use
some other netfilter extensions in order to get the whole IPP2P
package working as already described. IPP2P works together with
connection tracking and connection marking - in that way you can catch
the bigger part of all P2P packets and limit the bandwidth rate.

This package contains Linux kernel module.

%description -l pl
IPP2P to rozszerzenie netfiltra s�u��ce do identyfikowania ruchu
zwi�zanego z dzieleniem plik�w P2P. G�ownym celem tworzenia IPP2P jest
udost�pnienie administratorowi dynamicznego narz�dzia do filtrowania
ruchu w inteligentny spos�b. Nie jest nim zablokowanie ca�ego ruchu
P2P, ale umo�liwienie ograniczenia tego ruchu do danej przepustowo�ci.
W tym celu IPP2P przeszukuje zawarto�� (payload) pakiet�w TCP pod
k�tem wzorc�w sygnalizuj�cych sieci P2P. Je�li tych wzorc�w nie ma w
pakietach, musz� by� u�yte inne rozszerzenia netfiltra, aby IPP2P
dzia�a�o zgodnie z opisem. IPP2P wsp�pracuje ze �ledzeniem oraz
znakowaniem po��cze� - w ten spos�b mo�na wychwyci� wi�ksz� cz��
pakiet�w P2P i ograniczy� wykorzystanie ��cza przez nie.

Ten pakiet zawiera modu� j�dra Linuksa.

%package -n kernel-smp-net-ipp2p
Summary:	IPP2P - a netfilter extension to identify P2P filesharing traffic
Summary(pl):	IPP2P - rozszerzenie filtru pakiet�w identyfikuj�ce ruch P2P
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_smp}
Requires(post,postun):	/sbin/depmod

%description -n kernel-smp-net-ipp2p
IPP2P is a netfilter extension to identify P2P filesharing traffic.
The main goal for developing IPP2P was giving the adminstrator a
dynamic tool to filter the traffic in an intelligent way. So it
doesn't aim at prohibiting all P2P traffic but make it possible to
shape this traffic to a given rate. For this purpose IPP2P searchs the
payload of TCP packets for signaling patterns of P2P networks. As
these patterns are not being present in all P2P packets we had to use
some other netfilter extensions in order to get the whole IPP2P
package working as already described. IPP2P works together with
connection tracking and connection marking - in that way you can catch
the bigger part of all P2P packets and limit the bandwidth rate.

This package contains Linux SMP kernel module.

%description -n kernel-smp-net-ipp2p -l pl
IPP2P to rozszerzenie netfiltra s�u��ce do identyfikowania ruchu
zwi�zanego z dzieleniem plik�w P2P. G�ownym celem tworzenia IPP2P jest
udost�pnienie administratorowi dynamicznego narz�dzia do filtrowania
ruchu w inteligentny spos�b. Nie jest nim zablokowanie ca�ego ruchu
P2P, ale umo�liwienie ograniczenia tego ruchu do danej przepustowo�ci.
W tym celu IPP2P przeszukuje zawarto�� (payload) pakiet�w TCP pod
k�tem wzorc�w sygnalizuj�cych sieci P2P. Je�li tych wzorc�w nie ma w
pakietach, musz� by� u�yte inne rozszerzenia netfiltra, aby IPP2P
dzia�a�o zgodnie z opisem. IPP2P wsp�pracuje ze �ledzeniem oraz
znakowaniem po��cze� - w ten spos�b mo�na wychwyci� wi�ksz� cz��
pakiet�w P2P i ograniczy� wykorzystanie ��cza przez nie.

Ten pakiet zawiera modu� j�dra Linuksa SMP.

%package -n iptables-ipp2p
Summary:	IPP2P - a netfilter extension to identify P2P filesharing traffic
Summary(pl):	IPP2P - rozszerzenie filtru pakiet�w identyfikuj�ce ruch P2P
Release:	%{_rel}
Group:		Base/Kernel
Requires:	iptables

%description -n iptables-ipp2p
IPP2P is a netfilter extension to identify P2P filesharing traffic.
The main goal for developing IPP2P was giving the adminstrator a
dynamic tool to filter the traffic in an intelligent way. So it
doesn't aim at prohibiting all P2P traffic but make it possible to
shape this traffic to a given rate. For this purpose IPP2P searchs the
payload of TCP packets for signaling patterns of P2P networks. As
these patterns are not being present in all P2P packets we had to use
some other netfilter extensions in order to get the whole IPP2P
package working as already described. IPP2P works together with
connection tracking and connection marking - in that way you can catch
the bigger part of all P2P packets and limit the bandwidth rate.

This package contains iptables module needed to control IPP2P kernel
module.

%description -n iptables-ipp2p -l pl
IPP2P to rozszerzenie netfiltra s�u��ce do identyfikowania ruchu
zwi�zanego z dzieleniem plik�w P2P. G�ownym celem tworzenia IPP2P jest
udost�pnienie administratorowi dynamicznego narz�dzia do filtrowania
ruchu w inteligentny spos�b. Nie jest nim zablokowanie ca�ego ruchu
P2P, ale umo�liwienie ograniczenia tego ruchu do danej przepustowo�ci.
W tym celu IPP2P przeszukuje zawarto�� (payload) pakiet�w TCP pod
k�tem wzorc�w sygnalizuj�cych sieci P2P. Je�li tych wzorc�w nie ma w
pakietach, musz� by� u�yte inne rozszerzenia netfiltra, aby IPP2P
dzia�a�o zgodnie z opisem. IPP2P wsp�pracuje ze �ledzeniem oraz
znakowaniem po��cze� - w ten spos�b mo�na wychwyci� wi�ksz� cz��
pakiet�w P2P i ograniczy� wykorzystanie ��cza przez nie.

Ten pakiet zawiera modu� iptables potrzebny do sterowania modu�em
j�dra IPP2P.

%prep
%setup -q -n %{_orig_name}

%build
%if %{with userspace}
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
%endif

install -d build-done/{SMP,UP}
## UP
    rm -rf include
    install -d include/{linux,config}
    ln -sf %{_kernelsrcdir}/config-up .config
    install -d include/{linux,config}
    ln -sf %{_kernelsrcdir}/include/linux/autoconf-up.h include/linux/autoconf.h
    touch include/config/MARKER
    echo "obj-m := ipt_%{_orig_name}.o" > Makefile
    %{__make} -C %{_kernelsrcdir} modules \
	SUBDIRS=$PWD \
	O=$PWD \
	%{?with_verbose:V=1}
    mv ipt_%{_orig_name}.ko build-done/UP/ipt_%{_orig_name}.up
    
    %{__make} -C %{_kernelsrcdir} mrproper \
	SUBDIRS=$PWD \
	O=$PWD \
	%{?with_verbose:V=1}

## SMP
    rm -rf include
    install -d include/{linux,config}
    ln -sf %{_kernelsrcdir}/config-smp .config
    install -d include/{linux,config}
    ln -sf %{_kernelsrcdir}/include/linux/autoconf-smp.h include/linux/autoconf.h
    touch include/config/MARKER
    echo "obj-m := ipt_%{_orig_name}.o" > Makefile
    %{__make} -C %{_kernelsrcdir} modules \
	SUBDIRS=$PWD \
	O=$PWD \
	%{?with_verbose:V=1}
    mv ipt_%{_orig_name}.ko build-done/SMP/ipt_%{_orig_name}.ko

%install
rm -rf $RPM_BUILD_ROOT

%if %{with userspace}
install -d $RPM_BUILD_ROOT%{_libdir}/iptables
install libipt_%{_orig_name}.so $RPM_BUILD_ROOT%{_libdir}/iptables
%endif

install -d $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}{,smp}/kernel/net/ipv4/netfilter
install build-done/UP/ipt_%{_orig_name}.up \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/kernel/net/ipv4/netfilter/ipt_%{_orig_name}.ko
install build-done/SMP/ipt_%{_orig_name}.ko \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/kernel/net/ipv4/netfilter/ipt_%{_orig_name}.ko

%clean
rm -rf $RPM_BUILD_ROOT

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

%if %{with dist_kernel}
%files
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/kernel/net/ipv4/netfilter/*

%files -n kernel-smp-net-ipp2p
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/kernel/net/ipv4/netfilter/*
%endif

%if %{with userspace}
%files -n iptables-ipp2p
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/iptables/*.so
%endif
