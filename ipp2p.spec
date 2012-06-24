#
# Conditional build:
%bcond_without	dist_kernel	# allow non-distribution kernel
%bcond_without	kernel		# don't build kernel modules
%bcond_without	smp		# don't build SMP module
%bcond_without	userspace	# don't build userspace module
%bcond_with	verbose		# verbose build (V=1)
#
%define		_orig_name	ipp2p
%define		_rel	1
#
Summary:	IPP2P - a netfilter extension to identify P2P filesharing traffic
Summary(pl):	IPP2P - rozszerzenie filtra pakiet�w identyfikuj�ce ruch P2P
Name:		kernel-net-ipp2p
Epoch:		1
Version:	0.6
Release:	%{_rel}@%{_kernel_ver_str}
License:	GPL
Group:		Base/Kernel
Source0:	http://rnvs.informatik.uni-leipzig.de/%{_orig_name}/downloads/%{_orig_name}.06.tar.gz
# Source0-md5:	9ac3ab4f48755500dbb0020292088efe
URL:		http://rnvs.informatik.uni-leipzig.de/ipp2p/
%{?with_userspace:BuildRequires:	iptables-devel}
%if %{with kernel} && %{with dist_kernel}
BuildRequires:	kernel-module-build
%endif
BuildRequires:	rpmbuild(macros) >= 1.153
BuildRequires:	sed >= 4.0
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
Summary(pl):	IPP2P - rozszerzenie filtra pakiet�w identyfikuj�ce ruch P2P
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
Summary(pl):	IPP2P - rozszerzenie filtra pakiet�w identyfikuj�ce ruch P2P
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
sed -i "s:shell iptables:shell %{_sbindir}/iptables:" Makefile

%build
%if %{with userspace}
%{__make} libipt_ipp2p.so \
    CFLAGS="%{rpmcflags}"
%endif

%if %{with kernel}
# kernel module(s)
for cfg in %{?with_dist_kernel:%{?with_smp:smp} up}%{!?with_dist_kernel:nondist}; do
    if [ ! -r "%{_kernelsrcdir}/config-$cfg" ]; then
	exit 1
    fi
    rm -rf include
    install -d include/{linux,config}
    ln -sf %{_kernelsrcdir}/config-$cfg .config
    ln -sf %{_kernelsrcdir}/include/linux/autoconf-$cfg.h include/linux/autoconf.h
    ln -sf %{_kernelsrcdir}/include/asm-%{_target_base_arch} include/asm
    touch include/config/MARKER
    %{__make} -C %{_kernelsrcdir} clean \
	RCS_FIND_IGNORE="-name '*.ko' -o" \
	M=$PWD O=$PWD \
	%{?with_verbose:V=1}
    %{__make} -C %{_kernelsrcdir} modules \
	M=$PWD O=$PWD \
	%{?with_verbose:V=1}
    mv ipt_%{_orig_name}{,-$cfg}.ko
done
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with userspace}
install -d $RPM_BUILD_ROOT%{_libdir}/iptables
install libipt_%{_orig_name}.so $RPM_BUILD_ROOT%{_libdir}/iptables
%endif

%if %{with kernel}
install -d $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}{,smp}/kernel/net/ipv4/netfilter
install ipt_%{_orig_name}-%{?with_dist_kernel:up}%{!?with_dist_kernel:nondist}.ko \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/kernel/net/ipv4/netfilter/ipt_%{_orig_name}.ko
%if %{with smp} && %{with dist_kernel}
install ipt_%{_orig_name}-smp.ko \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/kernel/net/ipv4/netfilter/ipt_%{_orig_name}.ko
%endif
%endif

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

%if %{with kernel}
%files
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/kernel/net/ipv4/netfilter/*

%if %{with smp} && %{with dist_kernel}
%files -n kernel-smp-net-ipp2p
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/kernel/net/ipv4/netfilter/*
%endif
%endif

%if %{with userspace}
%files -n iptables-ipp2p
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/iptables/*.so
%endif
