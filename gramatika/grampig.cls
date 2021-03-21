\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{grampig}

\LoadClass[10pt, utf8, border=0.4cm]{standalone}

\RequirePackage[PunctStyle=banjiao]{xeCJK}
\RequirePackage{enumitem}
\RequirePackage{fontspec}
\RequirePackage{xcolor}
\RequirePackage{ruby}
\RequirePackage{microtype}
\RequirePackage{array}
\RequirePackage[croatian]{babel}
\RequirePackage{array}
\RequirePackage{booktabs}
\RequirePackage{makecell}

\definecolor{navy}{HTML}{001F3F}
\definecolor{blue}{HTML}{0074D9}
\definecolor{aqua}{HTML}{7FDBFF}
\definecolor{teal}{HTML}{39CCCC}
\definecolor{olive}{HTML}{3D9970}
\definecolor{green}{HTML}{2ECC40}
\definecolor{lime}{HTML}{01FF70}
\definecolor{yellow}{HTML}{FFDC00}
\definecolor{orange}{HTML}{FF851B}
\definecolor{red}{HTML}{FF4136}
\definecolor{fuchsia}{HTML}{F012BE}
\definecolor{purple}{HTML}{B10DC9}
\definecolor{maroon}{HTML}{85144B}
\definecolor{white}{HTML}{FFFFFF}
\definecolor{silver}{HTML}{DDDDDD}
\definecolor{gray}{HTML}{AAAAAA}
\definecolor{black}{HTML}{111111}

\newcommand{\backgroundcolor}{white}
\newcommand{\foregroundcolor}{black}
\newcommand{\accentcolor}{gray}

\DeclareOption{basic}{
	\renewcommand{\backgroundcolor}{yellow}
	\renewcommand{\foregroundcolor}{black}
	\renewcommand{\accentcolor}{maroon}
}
\DeclareOption{intermediate}{
	\renewcommand{\backgroundcolor}{navy}
	\renewcommand{\foregroundcolor}{aqua}
	\renewcommand{\accentcolor}{yellow}
}
\DeclareOption{advanced}{
	\renewcommand{\backgroundcolor}{maroon}
	\renewcommand{\foregroundcolor}{yellow}
	\renewcommand{\accentcolor}{orange}
}
\DeclareOption{pig}{
	\renewcommand{\backgroundcolor}{maroon}
	\renewcommand{\foregroundcolor}{pink}
	\renewcommand{\accentcolor}{lime}
}
\DeclareOption{ocha}{
	\renewcommand{\backgroundcolor}{silver}
	\renewcommand{\foregroundcolor}{maroon}
	\renewcommand{\accentcolor}{orange}
}
\ProcessOptions\relax

\newcommand*{\e}[1]{{\color{\accentcolor}#1}}
\newcommand*{\br}{\\[0.4em]}
\newcommand*{\bh}{\\[-0.2em]}
\newcommand*{\p}[1]{\mbox{#1}\CJKglue}
\newcommand*{\f}[2]{\ruby{#1}{#2}}

\renewcommand{\rubysep}{-0em}
\renewcommand{\rubysize}{0.5}

\pagecolor{\backgroundcolor}
\color{\foregroundcolor}

\setlength{\tabcolsep}{0.5ex}

\setmainfont[Numbers={Lining, Monospaced},Ligatures=TeX,LetterSpace=True,BoldFont=*-Semibold]{Source Serif 4}
\setCJKmainfont{Source Han Serif JP}

\setlist{wide,leftmargin=*,itemsep=0em,parsep=0em,topsep=0em}
\setlength{\parindent}{0pt}
\newlength{\width}
\setlength{\width}{10cm}