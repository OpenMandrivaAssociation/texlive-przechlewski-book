Name:		texlive-przechlewski-book
Version:	23552
Release:	2
Summary:	Examples from Przechlewski's LaTeX book
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/examples/przechlewski-book-examples
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/przechlewski-book.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/przechlewski-book.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides machine-readable copies of the examples
from the book "Praca magisterska i dyplomowa z programem
LaTeX".

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/przechlewski-book/papalike.bst
%{_texmfdistdir}/tex/latex/przechlewski-book/upmgr.cls
%{_texmfdistdir}/tex/latex/przechlewski-book/wkmgr.cls
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/LICENSE
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/Makefile
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/README
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/README.pl
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/TAM-pl.pdf
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/b313.bib
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p21.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p22.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p23.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p24.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p31.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p310.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p311.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p312.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p313.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p313_utf8.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p32.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p33.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p34.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p35.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p36.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p37.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p38.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p39.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p41.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p42.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p43.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p44.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p45.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/p46.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/rys1_5.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/wkmgr.bib
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/wkmgr.html
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/wkmgr1.pdf
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/wkmgr1.tex
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/wkmgr2.pdf
%doc %{_texmfdistdir}/doc/latex/przechlewski-book/wkmgr2.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
