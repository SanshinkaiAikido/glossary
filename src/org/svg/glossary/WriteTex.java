package org.svg.glossary;

import java.io.*;

import org.svg.glossary.xml.*;

class WriteTex {
	public static String convertTex(String theString) {
		return theString.replaceAll("ô", "\\\\=o").replaceAll("û", "\\\\=u").replaceAll("Ô", "\\\\=O").replaceAll("Û", "\\\\=U");
	}

	public static String convertTexNoDot(String theString) {
		return theString.replaceAll("ô", "\\\\=o").replaceAll("û", "\\\\=u").replaceAll("Ô", "\\\\=O").replaceAll("Û", "\\\\=U").replaceAll("·", "");
	}

	public static String normaliseName(String theString) {
		return theString.replaceAll("ô", "o").replaceAll("û", "u").replaceAll("Ô", "O").replaceAll("Û", "U").replaceAll(" ", "").replaceAll("·", "").replaceAll("\\.", "");//TODO remove .
		//TODO use oo and uo for the form without bar?
	}

	public static String getLocal(org.svg.glossary.xml.Local[] theLocals, String theLang) {
		for (int i = 0; i < theLocals.length; i++) {
			if (theLang.equals(theLocals[i].getLang())) {
				return theLocals[i].getName();
			}
		}
		System.err.println("Unknown language " + theLang + " for Locals " + theLocals);
		System.exit(1);
		return "";
	}

	public static void writeAppInstallBegin(BufferedWriter aBW) throws IOException {
		aBW.write("from Products.ATVocabularyManager.config import TOOL_NAME as ATVOCABULARYTOOL\n"
				+ "from Products.CMFCore.utils import getToolByName\n"
				+ "def install(self):\n"
				+ "    vocabs = {}\n");
	}

	public static void writeAppInstallEnd(BufferedWriter aBW) throws IOException {
		aBW.write("    portal=getToolByName(self,'portal_url').getPortalObject()\n"
				+ "    atvm = getToolByName(portal, ATVOCABULARYTOOL)\n"
				+ "    for vkey in vocabs.keys():\n"
				+ "        vocabname = vkey\n"
				+ "        if not hasattr(atvm, vocabname):\n"
				+ "            atvm.invokeFactory('SimpleVocabulary', vocabname)\n"
				+ "        vocab = atvm[vocabname]\n"
				+ "        if len(vocab.getFolderContents()) < 2:\n"
				+ "            for (ikey, value) in vocabs [vkey]:\n"
				+ "                if not hasattr(vocab, ikey):\n"
				+ "                    vocab.invokeFactory('SimpleVocabularyTerm', ikey)\n"
				+ "                    vocab[ikey].setTitle(value)");
	}

	public static String getLit(org.svg.glossary.xml.Local[] theLocals, String theLang) {
		for (int i = 0; i < theLocals.length; i++) {
			if (theLang.equals(theLocals[i].getLang())) {
				return theLocals[i].getLit();
			}
		}
		System.err.println("Unknown language " + theLang + " for Locals " + theLocals);
		System.exit(1);
		return "";
	}

	public static void main(String[] args) {
		if (args.length != 1) {
			System.err.println("Syntax: java write-tex filename.xml");
			System.exit(1);
		}
		String aListRomaji = null;
		String aListRomajiNormal = null;
		String aListKanji = null;
		String aListLocal = null;
		String aItemRomaji = null;
		String aItemRomajiNormal = null;
		String aItemKanji = null;
		String aItemLocal = null;
		try {
			org.svg.glossary.xml.Glossary aGlossary = (Glossary)Glossary.unmarshal(new FileReader(args[0]));
			System.out.println("Glossary Name: " + aGlossary.getName());
			System.out.println("Glossary Author: " + aGlossary.getAuthor());
			System.out.println("Glossary Version: " + aGlossary.getVersion());
			System.out.println("Glossary Date: " + aGlossary.getDate());
			org.svg.glossary.xml.Local[] aLocals = aGlossary.getExtra().getItem(0).getLocal();
			BufferedWriter aTranslateGlossaryFile = new BufferedWriter(new FileWriter("translateGlossary.py"));
			aTranslateGlossaryFile.write("## Script (Python) \"translateGlossary\"\n");
			aTranslateGlossaryFile.write("##bind container=container\n");
			aTranslateGlossaryFile.write("##bind context=context\n");
			aTranslateGlossaryFile.write("##bind namespace=\n");
			aTranslateGlossaryFile.write("##bind script=script\n");
			aTranslateGlossaryFile.write("##bind subpath=traverse_subpath\n");
			aTranslateGlossaryFile.write("##parameters=list, item\n");
			aTranslateGlossaryFile.write("##title=return translation for given glossary list item and item item\n");
			aTranslateGlossaryFile.write("##\n");
			aTranslateGlossaryFile.write("# This Python file uses the following encoding: utf-8\n");
			BufferedWriter aFormatRomajiFile = new BufferedWriter(new FileWriter("formatRomaji.py"));
			aFormatRomajiFile.write("## Script (Python) \"formatRomaji\"\n");
			aFormatRomajiFile.write("##bind container=container\n");
			aFormatRomajiFile.write("##bind context=context\n");
			aFormatRomajiFile.write("##bind namespace=\n");
			aFormatRomajiFile.write("##bind script=script\n");
			aFormatRomajiFile.write("##bind subpath=traverse_subpath\n");
			aFormatRomajiFile.write("##parameters=list, item\n");
			aFormatRomajiFile.write("##title=return formatted romaji for given glossary list item and item item\n");
			aFormatRomajiFile.write("##\n");
			aFormatRomajiFile.write("# This Python file uses the following encoding: utf-8\n");
			for (int e = 0; e < aLocals.length; e++) {
				BufferedWriter aContentFile = null;
				if (e == 0) {
					aContentFile = new BufferedWriter(new FileWriter("contents.tex"));
				}
				String aLang = aLocals[e].getLang();
				System.out.println("Glossary Lang " + aLang);
				aTranslateGlossaryFile.write("if context.REQUEST['LANGUAGE'] == '" + aLang + "':\n");
				aFormatRomajiFile.write("if context.REQUEST['LANGUAGE'] == '" + aLang + "':\n");
				BufferedWriter aRomajiFile = new BufferedWriter(new FileWriter("romaji-" + aLang + ".tex"));
				BufferedWriter aRomajiHTMLFile = new BufferedWriter(new FileWriter("romaji-html-" + aLang + ".tex"));
				BufferedWriter aGlossaryFile = new BufferedWriter(new FileWriter("glossary-" + aLang + ".tex"));
				BufferedWriter aGlossaryHTMLFile = new BufferedWriter(new FileWriter("glossary-" + aLang + ".html"));
				aGlossaryHTMLFile.write("<html>\n");
				aGlossaryHTMLFile.write("<head>\n");
				aGlossaryHTMLFile.write("<title>" + aLocals[e].getName().replaceAll("ô", "&#333;").replaceAll("û", "&#363;") + "</title>\n");
				aGlossaryHTMLFile.write("<meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />\n");
				aGlossaryHTMLFile.write("</head>\n");
				aGlossaryHTMLFile.write("<body>\n");
				aGlossaryHTMLFile.write("<h1>" + aLocals[e].getName().replaceAll("ô", "&#333;").replaceAll("û", "&#363;") + "</h1>\n");
				aGlossaryHTMLFile.write("<table>\n");
				boolean aFirstGH = true;
				BufferedWriter aVocabularyFile = new BufferedWriter(new FileWriter("AppInstall.py"));
				writeAppInstallBegin(aVocabularyFile);
				StringBuffer aListsVocabulary = new StringBuffer("    vocabs['lists'] = (\n");
				org.svg.glossary.xml.List[] aLists = aGlossary.getList();
				boolean listElse = false;
				for (int l = 0; l < aLists.length; l++) {
					aListRomaji = aLists[l].getRomaji();
					aListRomajiNormal =  normaliseName(aListRomaji);
					aListKanji = aLists[l].getKanji();
					aListLocal = getLocal(aLists[l].getLocal(), aLang);
					System.out.println("\t" + aListRomajiNormal + "\n\t\t" + aListLocal);
					aRomajiFile.write("\\def\\r" + aListRomajiNormal + "{{" + convertTexNoDot(aListRomaji) + "}}\n");
					aRomajiFile.write("\\def\\d" + aListRomajiNormal + "{{" + convertTex(aListRomaji) + "}}\n");
					if ("nl".equals(aLang)) {
						aRomajiHTMLFile.write("\\def\\h" + aListRomajiNormal + "{{\\htmladdnormallink" + "{" + convertTex(aListRomaji).replace("·", "") + "}{http://sanshinkai.eu/woordenlijst/?lang=nl\\#" + normaliseName(aListRomaji) + "}}}\n");
					} else if ("de".equals(aLang)) {
						aRomajiHTMLFile.write("\\def\\h" + aListRomajiNormal + "{{\\htmladdnormallink" + "{" + convertTex(aListRomaji).replace("·", "") + "}{http://sanshinkai.eu/woerterverzeichnis/?lang=de\\#" + normaliseName(aListRomaji) + "}}}\n");
					} else if ("fr".equals(aLang)) {
						aRomajiHTMLFile.write("\\def\\h" + aListRomajiNormal + "{{\\htmladdnormallink" + "{" + convertTex(aListRomaji).replace("·", "") + "}{http://sanshinkai.eu/glossaire/?lang=fr\\#" + normaliseName(aListRomaji) + "}}}\n");
					} else if ("sr".equals(aLang)) {
						aRomajiHTMLFile.write("\\def\\h" + aListRomajiNormal + "{{\\htmladdnormallink" + "{" + convertTex(aListRomaji).replace("·", "") + "}{http://sanshinkai.eu/pecnik/?lang=sr\\#" + normaliseName(aListRomaji) + "}}}\n");
					} else if ("mk".equals(aLang)) {
						aRomajiHTMLFile.write("\\def\\h" + aListRomajiNormal + "{{\\htmladdnormallink" + "{" + convertTex(aListRomaji).replace("·", "") + "}{http://sanshinkai.eu/pecnik/?lang=mk\\#" + normaliseName(aListRomaji) + "}}}\n");
					} else {
						aRomajiHTMLFile.write("\\def\\h" + aListRomajiNormal + "{{\\htmladdnormallink" + "{" + convertTex(aListRomaji).replace("·", "") + "}{http://sanshinkai.eu/glossary/\\#" + normaliseName(aListRomaji) + "}}}\n");
					}
					aVocabularyFile.write("    vocabs['" + aListRomajiNormal.replaceAll("/", "_") + "'] = (\n");
					aVocabularyFile.write("        ('~', 'unknown'),\n");
					aVocabularyFile.write("        ('-', ' '),\n");
					aVocabularyFile.write("        (',', 'multiple'),\n");
					aListsVocabulary.append("        ('" + aLists[l].getId() + "', '" + aListRomaji.replaceAll("·", "") + "'),\n");
					String aListLit = getLit(aLists[l].getLocal(), aLang);
					// according to XSD both Local and Lit are optional
					if (aListLocal == null || aListLocal.equals("")) {
						// No Local therfore translation is Lit if no Local is avaiable
						aRomajiFile.write("\\def\\t" + aListRomajiNormal + "{{" + convertTex(aListLit) + "}}\n");
					} else {
						// translation is Local
						aRomajiFile.write("\\def\\t" + aListRomajiNormal + "{{" + convertTex(aListLocal) + "}}\n");
					}
					if (aListLit == null || aListLit.equals("")) {
						// no Lit therefore literal is Local
//						aRomajiFile.write("\\def\\l" + aListRomajiNormal + "{{" + convertTex(aListLocal) + "}}\n");
					} else {
						// literal is Lit
						aRomajiFile.write("\\def\\l" + aListRomajiNormal + "{{" + convertTex(aListLit) + "}}\n");
					}
					if (!aLists[l].hasShow() || aLists[l].getShow()) {
						if (aFirstGH) {
							aFirstGH = false;
						} else {
							aGlossaryHTMLFile.write("<tr><td>&nbsp;</td></tr>\n");
						}
						aGlossaryHTMLFile.write("<tr><td><b><a name=\"" + normaliseName(aListRomaji) + "\"");
						aGlossaryHTMLFile.write(">" + aListKanji + "</a></b></td><td>");
						if (!(aListKanji.contains("?") || (aLists[l].hasGtl() && !aLists[l].getGtl()))) {
							aGlossaryHTMLFile.write("<a href=\"http://translate.google.com/translate_tts?q="+aListKanji+"&tl=ja\" target=\"_blank\">*</a>");
						}
						aGlossaryHTMLFile.write("</td><td><b>" + aListRomaji.replaceAll("ô", "&#333;").replaceAll("û", "&#363;") + "</b></td><td><b>" + aListLocal.replaceAll("ô", "&#333;").replaceAll("û", "&#363;") + "</b></td></tr>\n");
						if (e == 0) {
							aContentFile.write("\\g" + aListRomajiNormal + "\n");
						}
						aGlossaryFile.write("\\def\\g" + aListRomajiNormal + "{{\n");
						aGlossaryFile.write("\\noindent\\par\\begin{tabular}{@{}p{2.75cm}p{5cm}p{8.25cm}@{}}\n");
						if (aListKanji != null && !"".equals(aListKanji)) {
							aGlossaryFile.write("{\\fontspec{Sazanami Gothic}\\Large\\bfseries " + aListKanji + "}\t&\\Large{\\bfseries{" + convertTex(aListRomaji) + "}}\t& \\Large{" + convertTex(aListLocal) + "}\\\\\n");
						} else {
						aGlossaryFile.write("\t&\\Large{\\bfseries{" + convertTex(aListRomaji) + "}}\t& \\Large{" + convertTex(aListLocal) + "}\\\\\n");
						}
						aGlossaryFile.write("\t&& \\\\\n");
						aTranslateGlossaryFile.write("    if list == '" + aListRomajiNormal + "':\n");
						aFormatRomajiFile.write("    if list == '" + aListRomajiNormal + "':\n");
						listElse = true;
					}
					org.svg.glossary.xml.Item[] aItems = aLists[l].getItem();
					for (int i = 0; i < aItems.length; i++) {
						aItemRomaji = aItems[i].getRomaji();
						aItemKanji = aItems[i].getKanji();
						String aItemId = (String)aItems[i].getId();
						aItemRomajiNormal = normaliseName(aItemRomaji);
						aItemLocal = getLocal(aItems[i].getLocal(), aLang);
						aRomajiFile.write("\\def\\r" + aItemRomajiNormal + "{{" + convertTexNoDot(aItemRomaji) + "}}\n");
						aRomajiFile.write("\\def\\d" + aItemRomajiNormal + "{{" + convertTex(aItemRomaji) + "}}\n");
						if ("nl".equals(aLang)) {
							aRomajiHTMLFile.write("\\def\\h" + aItemRomajiNormal + "{{\\htmladdnormallink{" + convertTex(aItemRomaji).replace("·", "") + "}{http://sanshinkai.eu/woordenlijst/?lang=nl\\#" + normaliseName(aListRomaji) + "-" + aItemId + "}}}\n");
						} else if ("de".equals(aLang)) {
							aRomajiHTMLFile.write("\\def\\h" + aItemRomajiNormal + "{{\\htmladdnormallink{" + convertTex(aItemRomaji).replace("·", "") + "}{http://sanshinkai.eu/woerterverzeichnis/?lang=de\\#" + normaliseName(aListRomaji) + "-" + aItemId + "}}}\n");
						} else if ("fr".equals(aLang)) {
							aRomajiHTMLFile.write("\\def\\h" + aItemRomajiNormal + "{{\\htmladdnormallink{" + convertTex(aItemRomaji).replace("·", "") + "}{http://sanshinkai.eu/glossaire/?lang=fr\\#" + normaliseName(aListRomaji) + "-" + aItemId + "}}}\n");
						} else if ("sr".equals(aLang)) {
							aRomajiHTMLFile.write("\\def\\h" + aItemRomajiNormal + "{{\\htmladdnormallink{" + convertTex(aItemRomaji).replace("·", "") + "}{http://sanshinkai.eu/pecnik/?lang=sr\\#" + normaliseName(aListRomaji) + "-" + aItemId + "}}}\n");
						} else if ("mk".equals(aLang)) {
							aRomajiHTMLFile.write("\\def\\h" + aItemRomajiNormal + "{{\\htmladdnormallink{" + convertTex(aItemRomaji).replace("·", "") + "}{http://sanshinkai.eu/pecnik/?lang=mk\\#" + normaliseName(aListRomaji) + "-" + aItemId + "}}}\n");
						} else {
							aRomajiHTMLFile.write("\\def\\h" + aItemRomajiNormal + "{{\\htmladdnormallink{" + convertTex(aItemRomaji).replace("·", "") + "}{http://sanshinkai.eu/glossary/\\#" + normaliseName(aListRomaji) + "-" + aItemId + "}}}\n");
						}
						aVocabularyFile.write("        ('" + aItemId + "', '" + aItemRomaji.replaceAll("·", "") + "'),\n");
						String aItemLit = getLit(aItems[i].getLocal(), aLang);
						aTranslateGlossaryFile.write("        if item == '':\n");
						aTranslateGlossaryFile.write("            return \"" + aListLocal/*.replaceAll("ô", "&#333;").replaceAll("û", "&#363;")*/ + "\"\n");
						aFormatRomajiFile.write("        if item == '':\n");
						aFormatRomajiFile.write("            return \"" + aListRomaji + "\"\n");
						// according to XSD both Local and Lit are optional
						if (aItemLocal == null || aItemLocal.equals("")) {
							// no Local
System.out.println("no local");
							if (aItemLit != null && !aItemLit.equals("")) {
								// no Local and has Lit, use Lit
System.out.println("no local and has lit, use lit");

System.out.println("write Romaji");
								aRomajiFile.write("\\def\\t" + aItemRomajiNormal + "{{" + convertTex(aItemLit) + "}}\n");
								if ((!aLists[l].hasShow() || aLists[l].getShow()) && (!aItems[i].hasShow() || aItems[i].getShow())) {
System.out.println("write TranslateGlossary");
									aTranslateGlossaryFile.write("        if item == '" + aItemId + "':\n");
									aTranslateGlossaryFile.write("            return \"" + aItemLit/*.replaceAll("ô", "&#333;").replaceAll("û", "&#363;")*/ + "\"\n");
System.out.println("write FormatRomaji");
									aFormatRomajiFile.write("        if item == '" + aItemId + "':\n");
									aFormatRomajiFile.write("            return \"" + aItemRomaji + "\"\n");
System.out.println("write Glossary");
									aGlossaryHTMLFile.write("<tr><td><a name=\"" + normaliseName(aListRomaji) + "-" + aItemId + "\">" + aItemKanji + "</a></td><td>");
									if (!(aItemKanji.contains("?") || (aItems[i].hasGtl() && aItems[i].getGtl()))) {
										aGlossaryHTMLFile.write("<a href=\"http://translate.google.com/translate_tts?q="+aItemKanji+"&tl=ja\" target=\"_blank\">*</a>");
									}
									aGlossaryHTMLFile.write("</td><td>" + aItemRomaji.replaceAll("ô", "&#333;").replaceAll("û", "&#363;") + "</td><td>" + aItemLit.replaceAll("ô", "&#333;").replaceAll("û", "&#363;") + "</td></tr>\n");
									if (aItemKanji != null && !"".equals(aItemKanji)) {
	 									aGlossaryFile.write("{\\fontspec{Sazanami Gothic}" + aItemKanji + "}\t&" + convertTex(aItemRomaji) + "\t& " + " [" + convertTex(aItemLit) + "]\\\\\n");//TODO
									} else {
										aGlossaryFile.write("\t&" + convertTex(aItemRomaji) + "\t& " + " [" + convertTex(aItemLit) + "]\\\\\n");//TODO
									}
								}
							} else {
								// no Local and no Lit, error
								throw new Exception("Both Local and Lit not available");
							}
						} else {
							// has Local, use Local
System.out.println("has local, use local");
System.out.println("write Romaji");
							aRomajiFile.write("\\def\\t" + aItemRomajiNormal + "{{" + convertTex(aItemLocal) + "}}\n");
						}
						if (aItemLit == null || aItemLit.equals("")) {
							// no Lit
System.out.println("no lit");
//							aRomajiFile.write("\\def\\l" + aItemRomajiNormal + "{{" + convertTex(aItemLocal) + "}}\n");
							if ((!aLists[l].hasShow() || aLists[l].getShow()) && (!aItems[i].hasShow() || aItems[i].getShow())) {
								// no Lit and has Local?, useLocal
System.out.println("no lit and has local, use local");
								//TODOaGlossaryFile.write("\\htmladdnormallink{}{" + convertTex(aItemRomaji) + "}{asfd}\t& " + convertTex(aItemLocal) + "\\\\\n");
System.out.println("write Glossary");
								aGlossaryHTMLFile.write("<tr><td><a name=\"" + normaliseName(aListRomaji) + "-" + aItemId + "\">" + aItemKanji + "</a></td><td>");
								if (!(aItemKanji.contains("?") || (aItems[i].hasGtl() && aItems[i].getGtl()))) {
									aGlossaryHTMLFile.write("<a href=\"http://translate.google.com/translate_tts?q="+aItemKanji+"&tl=ja\" target=\"_blank\">*</a>");
								}
								aGlossaryHTMLFile.write("</td><td>" + aItemRomaji.replaceAll("ô", "&#333;").replaceAll("û", "&#363;") + "</td><td>" + aItemLocal.replaceAll("ô", "&#333;").replaceAll("û", "&#363;") + "</td></tr>\n");
                                if (aItemKanji != null && !"".equals(aItemKanji)) {
    								aGlossaryFile.write("{\\fontspec{Sazanami Gothic}" + aItemKanji + "}\t&" + convertTex(aItemRomaji) + "\t& " + convertTex(aItemLocal) + "\\\\\n");
                                } else {
    								aGlossaryFile.write("\t&" + convertTex(aItemRomaji) + "\t& " + convertTex(aItemLocal) + "\\\\\n");
                                }
System.out.println("write TranslateGlossary");
								aTranslateGlossaryFile.write("        if item == '" + aItemId + "':\n");
								aTranslateGlossaryFile.write("            return \"" + aItemLocal/*.replaceAll("ô", "&#333;").replaceAll("û", "&#363;")*/ + "\"\n");
System.out.println("write FormatRomaji");
								aFormatRomajiFile.write("        if item == '" + aItemId + "':\n");
								aFormatRomajiFile.write("            return \"" + aItemRomaji + "\"\n");
							}
						} else {
							// has Lit
System.out.println("has lit");
							if (aItemLocal != null && !aItemLocal.equals("")) {
System.out.println("write Romaji");
								aRomajiFile.write("\\def\\l" + aItemRomajiNormal + "{{" + convertTex(aItemLit) + "}}\n");
								if ((!aLists[l].hasShow() || aLists[l].getShow()) && (!aItems[i].hasShow() || aItems[i].getShow())) {
System.out.println("write FormatRomaji");
									aFormatRomajiFile.write("        if item == '" + aItemId + "':\n");
									aFormatRomajiFile.write("            return \"" + aItemRomaji + "\"\n");
									if (aItemLocal == null || aItemLocal.equals("")) {
										// no Local and has Lit, use Lit
System.out.println("no local and has lit, use lit");
									} else {
										// has Local and has Lit, use Local and use Lit
System.out.println("has local and has lit, use local and use lit");
System.out.println("write Glossary");
										aGlossaryHTMLFile.write("<tr><td><a name=\"" + normaliseName(aListRomaji) + "-" + aItemId + "\">" + aItemKanji + "</a></td><td>");
										if (!(aItemKanji.contains("?") || (aItems[i].hasGtl() && aItems[i].getGtl()))) {
                                                                		        aGlossaryHTMLFile.write("<a href=\"http://translate.google.com/translate_tts?q="+aItemKanji+"&tl=ja\" target=\"_blank\">*</a>");
		                                                                }
										aGlossaryHTMLFile.write("</td><td>" + aItemRomaji.replaceAll("ô", "&#333;").replaceAll("û", "&#363;") + "</td><td>" + aItemLocal.replaceAll("ô", "&#333;").replaceAll("û", "&#363;") + " [" + aItemLit.replaceAll("ô", "&#333;").replaceAll("û", "&#363;") + "]</td></tr>\n");
                                        if (aItemKanji != null && !"".equals(aItemKanji)) {
    										aGlossaryFile.write("{\\fontspec{Sazanami Gothic}" + aItemKanji + "}\t&" + convertTex(aItemRomaji) + "\t& " + convertTex(aItemLocal) + " [" + convertTex(aItemLit) + "]\\\\\n");//TODO
                                        } else {
    										aGlossaryFile.write(convertTex("\t&" + aItemRomaji) + "\t& " + convertTex(aItemLocal) + " [" + convertTex(aItemLit) + "]\\\\\n");//TODO
                                        }
System.out.println("write TranslateGlossary");
										aTranslateGlossaryFile.write("        if item == '" + aItemId + "':\n");
										aTranslateGlossaryFile.write("            return \"" + aItemLocal/*.replaceAll("ô", "&#333;").replaceAll("û", "&#363;")*/ + " [" + aItemLit/*.replaceAll("ô", "&#333;").replaceAll("û", "&#363;")*/ + "]\"\n");
									}
								}
							}
						}
					}
					aTranslateGlossaryFile.write("        else:\n");
					aTranslateGlossaryFile.write("            return 'unknown item %s for list %s' %(item, list)\n");
					aFormatRomajiFile.write("        else:\n");
					aFormatRomajiFile.write("            return 'unknown item %s for list %s' %(item, list)\n");
					aVocabularyFile.write("    )\n");
					if (!aLists[l].hasShow() || aLists[l].getShow()) {
						aGlossaryFile.write("\\end{tabular}\n");
						aGlossaryFile.write("\\vspace{.5cm}\n");
						aGlossaryFile.write("}}\n");
						aGlossaryFile.write("\n");
					}
				}
				aGlossaryHTMLFile.write("</table>\n");
				aGlossaryHTMLFile.write("<br />\n");
				aGlossaryHTMLFile.write("<small>" + aLang + " " + aGlossary.getVersion() + " " + aGlossary.getDate() + "</small>\n");
				aGlossaryHTMLFile.write("</body>");
				aListsVocabulary.append("    )\n");
				aVocabularyFile.write(aListsVocabulary.toString());
				writeAppInstallEnd(aVocabularyFile);
				aVocabularyFile.close();
				aRomajiFile.close();
				aRomajiHTMLFile.close();
				aGlossaryFile.close();
				aGlossaryHTMLFile.close();
				if (listElse) {
					aTranslateGlossaryFile.write("    else:\n");
				}
				aTranslateGlossaryFile.write("        return 'unknown list %s' %list\n");
				if (listElse) {
					aFormatRomajiFile.write("    else:\n");
				}
				aFormatRomajiFile.write("        return 'unknown list %s' %list\n");
				if (e == 0) {
					aContentFile.close();
				}
			}
			aTranslateGlossaryFile.write("return 'untranslated list %s and item %s for language %s' %(list, item, context.REQUEST['LANGUAGE'])\n");
			aTranslateGlossaryFile.close();
			aFormatRomajiFile.write("return 'untranslated list %s and item %s for language %s' %(list, item, context.REQUEST['LANGUAGE'])\n");
			aFormatRomajiFile.close();
		} catch (Exception e) {
			System.err.println("Exception caught in main: " + e);
			System.err.println("List Romaji: " + aListRomaji);
			System.err.println("List Romaji Normalised: " + aListRomajiNormal);
			System.err.println("List Local: " + aListLocal);
			System.err.println("Item Romaji: " + aItemRomaji);
			System.err.println("Item Romaji Normalised: " + aItemRomajiNormal);
			System.err.println("Item Local: " + aItemLocal);
			e.printStackTrace();
			System.exit(1);
		}
	}
}
