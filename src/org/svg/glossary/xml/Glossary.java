/*
 * This class was automatically generated with 
 * <a href="http://www.castor.org">Castor 1.3</a>, using an XML
 * Schema.
 * $Id$
 */

package org.svg.glossary.xml;

/**
 * Class Glossary.
 * 
 * @version $Revision$ $Date$
 */
@SuppressWarnings("serial")
public class Glossary implements java.io.Serializable {


      //--------------------------/
     //- Class/Member Variables -/
    //--------------------------/

    /**
     * Field _name.
     */
    private java.lang.String _name;

    /**
     * Field _author.
     */
    private java.lang.String _author;

    /**
     * Field _version.
     */
    private java.lang.String _version;

    /**
     * Field _date.
     */
    private java.lang.String _date;

    /**
     * Field _extra.
     */
    private org.svg.glossary.xml.Extra _extra;

    /**
     * Field _listList.
     */
    private java.util.List<org.svg.glossary.xml.List> _listList;


      //----------------/
     //- Constructors -/
    //----------------/

    public Glossary() {
        super();
        this._listList = new java.util.ArrayList<org.svg.glossary.xml.List>();
    }


      //-----------/
     //- Methods -/
    //-----------/

    /**
     * 
     * 
     * @param vList
     * @throws java.lang.IndexOutOfBoundsException if the index
     * given is outside the bounds of the collection
     */
    public void addList(
            final org.svg.glossary.xml.List vList)
    throws java.lang.IndexOutOfBoundsException {
        this._listList.add(vList);
    }

    /**
     * 
     * 
     * @param index
     * @param vList
     * @throws java.lang.IndexOutOfBoundsException if the index
     * given is outside the bounds of the collection
     */
    public void addList(
            final int index,
            final org.svg.glossary.xml.List vList)
    throws java.lang.IndexOutOfBoundsException {
        this._listList.add(index, vList);
    }

    /**
     * Method enumerateList.
     * 
     * @return an Enumeration over all possible elements of this
     * collection
     */
    public java.util.Enumeration<? extends org.svg.glossary.xml.List> enumerateList(
    ) {
        return java.util.Collections.enumeration(this._listList);
    }

    /**
     * Returns the value of field 'author'.
     * 
     * @return the value of field 'Author'.
     */
    public java.lang.String getAuthor(
    ) {
        return this._author;
    }

    /**
     * Returns the value of field 'date'.
     * 
     * @return the value of field 'Date'.
     */
    public java.lang.String getDate(
    ) {
        return this._date;
    }

    /**
     * Returns the value of field 'extra'.
     * 
     * @return the value of field 'Extra'.
     */
    public org.svg.glossary.xml.Extra getExtra(
    ) {
        return this._extra;
    }

    /**
     * Method getList.
     * 
     * @param index
     * @throws java.lang.IndexOutOfBoundsException if the index
     * given is outside the bounds of the collection
     * @return the value of the org.svg.glossary.xml.List at the
     * given index
     */
    public org.svg.glossary.xml.List getList(
            final int index)
    throws java.lang.IndexOutOfBoundsException {
        // check bounds for index
        if (index < 0 || index >= this._listList.size()) {
            throw new IndexOutOfBoundsException("getList: Index value '" + index + "' not in range [0.." + (this._listList.size() - 1) + "]");
        }

        return (org.svg.glossary.xml.List) _listList.get(index);
    }

    /**
     * Method getList.Returns the contents of the collection in an
     * Array.  <p>Note:  Just in case the collection contents are
     * changing in another thread, we pass a 0-length Array of the
     * correct type into the API call.  This way we <i>know</i>
     * that the Array returned is of exactly the correct length.
     * 
     * @return this collection as an Array
     */
    public org.svg.glossary.xml.List[] getList(
    ) {
        org.svg.glossary.xml.List[] array = new org.svg.glossary.xml.List[0];
        return (org.svg.glossary.xml.List[]) this._listList.toArray(array);
    }

    /**
     * Method getListCount.
     * 
     * @return the size of this collection
     */
    public int getListCount(
    ) {
        return this._listList.size();
    }

    /**
     * Returns the value of field 'name'.
     * 
     * @return the value of field 'Name'.
     */
    public java.lang.String getName(
    ) {
        return this._name;
    }

    /**
     * Returns the value of field 'version'.
     * 
     * @return the value of field 'Version'.
     */
    public java.lang.String getVersion(
    ) {
        return this._version;
    }

    /**
     * Method isValid.
     * 
     * @return true if this object is valid according to the schema
     */
    public boolean isValid(
    ) {
        try {
            validate();
        } catch (org.exolab.castor.xml.ValidationException vex) {
            return false;
        }
        return true;
    }

    /**
     * Method iterateList.
     * 
     * @return an Iterator over all possible elements in this
     * collection
     */
    public java.util.Iterator<? extends org.svg.glossary.xml.List> iterateList(
    ) {
        return this._listList.iterator();
    }

    /**
     * 
     * 
     * @param out
     * @throws org.exolab.castor.xml.MarshalException if object is
     * null or if any SAXException is thrown during marshaling
     * @throws org.exolab.castor.xml.ValidationException if this
     * object is an invalid instance according to the schema
     */
    public void marshal(
            final java.io.Writer out)
    throws org.exolab.castor.xml.MarshalException, org.exolab.castor.xml.ValidationException {
        org.exolab.castor.xml.Marshaller.marshal(this, out);
    }

    /**
     * 
     * 
     * @param handler
     * @throws java.io.IOException if an IOException occurs during
     * marshaling
     * @throws org.exolab.castor.xml.ValidationException if this
     * object is an invalid instance according to the schema
     * @throws org.exolab.castor.xml.MarshalException if object is
     * null or if any SAXException is thrown during marshaling
     */
    public void marshal(
            final org.xml.sax.ContentHandler handler)
    throws java.io.IOException, org.exolab.castor.xml.MarshalException, org.exolab.castor.xml.ValidationException {
        org.exolab.castor.xml.Marshaller.marshal(this, handler);
    }

    /**
     */
    public void removeAllList(
    ) {
        this._listList.clear();
    }

    /**
     * Method removeList.
     * 
     * @param vList
     * @return true if the object was removed from the collection.
     */
    public boolean removeList(
            final org.svg.glossary.xml.List vList) {
        boolean removed = _listList.remove(vList);
        return removed;
    }

    /**
     * Method removeListAt.
     * 
     * @param index
     * @return the element removed from the collection
     */
    public org.svg.glossary.xml.List removeListAt(
            final int index) {
        java.lang.Object obj = this._listList.remove(index);
        return (org.svg.glossary.xml.List) obj;
    }

    /**
     * Sets the value of field 'author'.
     * 
     * @param author the value of field 'author'.
     */
    public void setAuthor(
            final java.lang.String author) {
        this._author = author;
    }

    /**
     * Sets the value of field 'date'.
     * 
     * @param date the value of field 'date'.
     */
    public void setDate(
            final java.lang.String date) {
        this._date = date;
    }

    /**
     * Sets the value of field 'extra'.
     * 
     * @param extra the value of field 'extra'.
     */
    public void setExtra(
            final org.svg.glossary.xml.Extra extra) {
        this._extra = extra;
    }

    /**
     * 
     * 
     * @param index
     * @param vList
     * @throws java.lang.IndexOutOfBoundsException if the index
     * given is outside the bounds of the collection
     */
    public void setList(
            final int index,
            final org.svg.glossary.xml.List vList)
    throws java.lang.IndexOutOfBoundsException {
        // check bounds for index
        if (index < 0 || index >= this._listList.size()) {
            throw new IndexOutOfBoundsException("setList: Index value '" + index + "' not in range [0.." + (this._listList.size() - 1) + "]");
        }

        this._listList.set(index, vList);
    }

    /**
     * 
     * 
     * @param vListArray
     */
    public void setList(
            final org.svg.glossary.xml.List[] vListArray) {
        //-- copy array
        _listList.clear();

        for (int i = 0; i < vListArray.length; i++) {
                this._listList.add(vListArray[i]);
        }
    }

    /**
     * Sets the value of field 'name'.
     * 
     * @param name the value of field 'name'.
     */
    public void setName(
            final java.lang.String name) {
        this._name = name;
    }

    /**
     * Sets the value of field 'version'.
     * 
     * @param version the value of field 'version'.
     */
    public void setVersion(
            final java.lang.String version) {
        this._version = version;
    }

    /**
     * Method unmarshal.
     * 
     * @param reader
     * @throws org.exolab.castor.xml.MarshalException if object is
     * null or if any SAXException is thrown during marshaling
     * @throws org.exolab.castor.xml.ValidationException if this
     * object is an invalid instance according to the schema
     * @return the unmarshaled org.svg.glossary.xml.Glossary
     */
    public static org.svg.glossary.xml.Glossary unmarshal(
            final java.io.Reader reader)
    throws org.exolab.castor.xml.MarshalException, org.exolab.castor.xml.ValidationException {
        return (org.svg.glossary.xml.Glossary) org.exolab.castor.xml.Unmarshaller.unmarshal(org.svg.glossary.xml.Glossary.class, reader);
    }

    /**
     * 
     * 
     * @throws org.exolab.castor.xml.ValidationException if this
     * object is an invalid instance according to the schema
     */
    public void validate(
    )
    throws org.exolab.castor.xml.ValidationException {
        org.exolab.castor.xml.Validator validator = new org.exolab.castor.xml.Validator();
        validator.validate(this);
    }

}
