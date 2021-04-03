\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{tekst}

\LoadClass{article}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax

\RequirePackage[PunctStyle=banjiao]{xeCJK}
\RequirePackage[margin=1cm,top=2cm,bottom=2cm,includeheadfoot=False]{geometry}
\RequirePackage{graphicx}
\RequirePackage{xltabular}
\RequirePackage{booktabs}
\RequirePackage{enumitem}
\RequirePackage{fontspec}
\RequirePackage[onehalfspacing]{setspace}
\RequirePackage{xcolor}
\RequirePackage{ruby}
\RequirePackage{microtype}
\RequirePackage{array}
\RequirePackage[croatian]{babel}
\RequirePackage{array}
\RequirePackage[all]{nowidow}
\RequirePackage{makecell}
\RequirePackage{multicol}
\RequirePackage{pbox}
\RequirePackage{titlesec}
\RequirePackage{indentfirst}
\setlength{\columnsep}{2em}

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

\newcommand*{\br}{\\[0.4em]}
\newcommand*{\bh}{\\[-0.2em]}
\newcommand*{\p}[1]{\mbox{#1}\CJKglue}
\newcommand*{\f}[2]{\ruby{#1}{#2}}
\newcommand*{\ansline}[1][1.5cm]{\rule{#1}{0.5pt}}

\renewcommand{\rubysep}{-0.3em}
\renewcommand{\rubysize}{0.4}

\setlength{\tabcolsep}{0.5ex}

\setmainfont[Numbers={Lining, Monospaced},Ligatures=TeX,LetterSpace=True,BoldFont=*-Semibold]{Source Serif Pro}
\setCJKmainfont[BoldFont=*-Bold,AutoFakeSlant=0.2]{Source Han Serif JP}
\setsansfont[Numbers={Lining, Monospaced},Ligatures=TeX,LetterSpace=True,BoldFont=*-Semibold]{Source Sans Pro}
\setCJKsansfont[BoldFont=*-Bold,AutoFakeSlant=0.2]{Source Han Sans JP}
\setlistdepth{3}
\setlist{leftmargin=*,itemsep=0em,parsep=0em,topsep=0em}
\setlist[2,3]{leftmargin=2em,itemsep=0em,parsep=0em,topsep=0em}
\setlength{\parindent}{2em}
\setlength{\parskip}{1.2em}
\setlength{\fboxsep}{1em}

\newcommand{\dictentry}[4]{%
	\begin{minipage}{\linewidth}%
		\singlespacing%
		\raggedright%
		{\Large\vspace{-1em} #1 \hspace*{\fill}}%
		{\normalsize \mbox{\raggedleft #2}}\\
		{\itshape{}#4}\\
		\begin{itemize}#3\end{itemize}%
	\end{minipage}\vspace{1.5em}
}

\newcommand{\choicebox}[1]{%
\begin{center}%
	\fbox{\pbox{\linewidth}{\relax\ifvmode\centering\fi #1}}%
\end{center}%
}