%global tl_name przechlewski-book
%global tl_revision 23552

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Examples from Przechlewskis LaTeX book
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/examples/przechlewski-book-examples
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/przechlewski-book.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/przechlewski-book.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides machine-readable copies of the examples from the
book "Praca magisterska i dyplomowa z programem LaTeX".

