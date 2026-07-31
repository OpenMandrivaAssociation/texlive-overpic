%global tl_name overpic
%global tl_revision 79813

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3
Release:	%{tl_revision}.1
Summary:	Combine LaTeX commands over included graphics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/overpic
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/overpic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/overpic.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/overpic.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The overpic environment is a cross between the LaTeX picture environment
and the \includegraphics command of graphicx. The resulting picture
environment has the same dimensions as the included graphic. LaTeX
commands can be placed on the graphic at defined positions; a grid for
orientation is available.

