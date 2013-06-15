package org.svg.glossary;

import org.apache.xerces.parsers.DOMParser;

class ValidateXML {
	public static void main(String[] args) {
		if (args.length != 1 && args.length != 2) {
			System.err.println("Syntax: java validate-xml filename.xml [filename.xsd]");
			System.exit(1);
		}
		try {
			DOMParser aParser = new DOMParser();
			aParser.setFeature("http://apache.org/xml/features/validation/schema", true);//http://xml.org/sax/features/validation
			aParser.setFeature("http://apache.org/xml/features/continue-after-fatal-error", false);
			aParser.setFeature("http://apache.org/xml/features/validation/schema-full-checking", true);
			if (args.length == 2) {
				aParser.setProperty("http://apache.org/xml/properties/schema/external-noNamespaceSchemaLocation", args[1]);
			}
			aParser.parse(args[0]);
		} catch (Exception e) {
			System.err.println("Exception caught in main: " + e);
			System.exit(1);
		}
	}
}
