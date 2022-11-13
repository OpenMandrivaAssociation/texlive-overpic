Name:		texlive-overpic
Version:	53889
Release:	1
Summary:	Combine LaTeX commands over included graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/overpic
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/overpic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/overpic.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The overpic environment is a cross between the LaTeX picture
environment and the \includegraphics command of graphicx. The
resulting picture environment has the same dimensions as the
included eps graphic. LaTeX commands can be placed on the
graphic at defined positions. A grid for orientation is
available.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/overpic
%doc %{_texmfdistdir}/doc/latex/overpic

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
