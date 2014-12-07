%define oname uthash

Name:		uthash-devel
Version:	1.9.9
Release:	2
Summary:	A hash table for C structures
License:	BSD
URL:		http://troydhanson.github.io/uthash
Source0:	https://github.com/troydhanson/%{oname}/archive/v%{version}.tar.gz
BuildArch:	noarch
%rename		uthash

%description
Any C structure can be stored in a hash table using uthash. Just add a
UT_hash_handle to the structure and choose one or more fields in your 
structure to act as the key. Then use these macros to store, retrieve or 
delete items from the hash table. 

%prep
%setup -qn %{oname}-%{version}
%apply_patches

%build

%install
install -d %{buildroot}%{_includedir}
cp -pa src/*.h %{buildroot}%{_includedir}/

%check
cd tests
%make

%files
%doc LICENSE doc/*.txt
%{_includedir}/ut*.h
