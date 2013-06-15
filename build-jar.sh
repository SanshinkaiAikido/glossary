rm -rf classes
mkdir -p classes/org/svg/glossary/xml
javac -classpath lib/xercesImpl-2.9.1.jar:lib/xml-apis-2.9.1.jar:lib/castor-1.3-core.jar:lib/castor-1.3.jar -d classes src/org/svg/glossary/*.java src/org/svg/glossary/xml/*.java
jar cf glossary.jar -C classes org
