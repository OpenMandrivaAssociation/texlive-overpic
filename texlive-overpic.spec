# revision 19712
# category Package
# catalog-ctan /macros/latex/contrib/overpic
# catalog-date 2010-09-13 11:39:12 +0200
# catalog-license lppl
# catalog-version 0.53
Name:		texlive-overpic
Version:	0.53
Release:	1
Summary:	Combine LaTeX commands over included graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/overpic
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/overpic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/overpic.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The overpic environment is a cross between the LaTeX picture
environment and the \includegraphics command of graphicx. The
resulting picture environment has the same dimensions as the
included eps graphic. LaTeX commands can be placed on the
graphic at defined positions. A grid for orientation is
available.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/overpic/overpic.sty
%doc %{_texmfdistdir}/doc/latex/overpic/README
%doc %{_texmfdistdir}/doc/latex/overpic/README.de
%doc %{_texmfdistdir}/doc/latex/overpic/opic-abs.pdf
%doc %{_texmfdistdir}/doc/latex/overpic/opic-abs.tex
%doc %{_texmfdistdir}/doc/latex/overpic/opic-rel.pdf
%doc %{_texmfdistdir}/doc/latex/overpic/opic-rel.tex
%doc %{_texmfdistdir}/doc/latex/overpic/overpic-readme-de.pdf
%doc %{_texmfdistdir}/doc/latex/overpic/overpic-readme-de.tex
%doc %{_texmfdistdir}/doc/latex/overpic/overpic-readme.pdf
%doc %{_texmfdistdir}/doc/latex/overpic/overpic-readme.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
