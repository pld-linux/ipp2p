%define		_orig_name	ipp2p
Summary:	ipp2p
Summary(pl):	ipp2p
Name:		%{_orig_name}
Version:	05b
Release:	1
License:	GPL
Group:		Base/Kernel
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
%setup -q -n %{_orig_name}%{version}

#%patch

%build
./configure --prefix=%{_prefix}
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

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
