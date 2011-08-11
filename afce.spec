%define		rel	51
Name:		afce
Version:	0.9.0
Release:	%mkrel 1
Summary:	Block-scheme redactor
License:	GPL
Group:		Education
URL:		http://vicking.narod.ru/flowchart/
Source:		%{name}-%{version}-%{rel}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
BuildRequires:	libqt4-devel

%description
Block-scheme redactor

%prep
%setup -q -n %{name}-%{version}-%{rel}

%build
qmake
%make

%install
rm -rf %{buildroot}
%__install -Dm0655 %{name} %{buildroot}/%{bindir}/%{name}
#install *.so

%files

%clean
rm -rf %{buildroot}