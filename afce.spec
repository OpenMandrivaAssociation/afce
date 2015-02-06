%define version 0.9.7
%define name afce
%define release 2
# empty debug
%define debug_package	%{nil}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Algorithm Flowchart Editor
License:	GPLv3
Group:		Education
URL:		https://github.com/viktor-zin/afce
# to build from git:
#┌─[ symbianflo @ abfonly ] - [ Mandrivausers.ro ] 
#└─[ MRB:aint-no-shit $]: cat BUILDING.md | grep sources
Source0:	https://github.com/viktor-zin/afce/archive/v%{version}.tar.gz

# switch to qt5 ,read BUILDING.md.Sflo
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	qt5-linguist-tools
BuildRequires:	qt5-qttranslations


%description
Flowchart editor with code generation and vector graphics.
AFCE allow to create, edit, print and export flowcharts easyly
for a few minutes. Flowcharts can be exported to several grafical
formats including SVG and PNG.

%prep
%setup -q

%build
%qmake_qt5
%make

%install
%makeinstall INSTALL_ROOT=%{buildroot}

%files
%doc README.RU.txt README.md BUILDING.md LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_iconsdir}/afc.ico
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml