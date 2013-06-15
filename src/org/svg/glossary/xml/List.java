/*
 * This class was automatically generated with 
 * <a href="http://www.castor.org">Castor 1.3</a>, using an XML
 * Schema.
 * $Id$
 */

package org.svg.glossary.xml;

/**
 * Class List.
 * 
 * @version $Revision$ $Date$
 */
@SuppressWarnings("serial")
public class List implements java.io.Serializable {


      //--------------------------/
     //- Class/Member Variables -/
    //--------------------------/

    /**
     * Field _id.
     */
    private java.lang.String _id;

    /**
     * Field _romaji.
     */
    private java.lang.String _romaji;

    /**
     * Field _kanji.
     */
    private java.lang.String _kanji;

    /**
     * Field _show.
     */
    private boolean _show;

    /**
     * keeps track of state for field: _show
     */
    private boolean _has_show;

    /**
     * Field _gtl.
     */
    private boolean _gtl;

    /**
     * keeps track of state for field: _gtl
     */
    private boolean _has_gtl;

    /**
     * Field _localList.
     */
    private java.util.List<org.svg.glossary.xml.Local> _localList;

    /**
     * Field _itemList.
     */
    private java.util.List<org.svg.glossary.xml.Item> _itemList;


      //----------------/
     //- Constructors -/
    //----------------/

    public List() {
        super();
        this._localList = new java.util.ArrayList<org.svg.glossary.xml.Local>();
        this._itemList = new java.util.ArrayList<org.svg.glossary.xml.Item>();
    }


      //-----------/
     //- Methods -/
    //-----------/

    /**
     * 
     * 
     * @param vItem
     * @throws java.lang.IndexOutOfBoundsException if the index
     * given is outside the bounds of the collection
     */
    public void addItem(
            final org.svg.glossary.xml.Item vItem)
    throws java.lang.IndexOutOfBoundsException {
        this._itemList.add(vItem);
    }

    /**
     * 
     * 
     * @param index
     * @param vItem
     * @throws java.lang.IndexOutOfBoundsException if the index
     * given is outside the bounds of the collection
     */
    public void addItem(
            final int index,
            final org.svg.glossary.xml.Item vItem)
    throws java.lang.IndexOutOfBoundsException {
        this._itemList.add(index, vItem);
    }

    /**
     * 
     * 
     * @param vLocal
     * @throws java.lang.IndexOutOfBoundsException if the index
     * given is outside the bounds of the collection
     */
    public void addLocal(
            final org.svg.glossary.xml.Local vLocal)
    throws java.lang.IndexOutOfBoundsException {
        this._localList.add(vLocal);
    }

    /**
     * 
     * 
     * @param index
     * @param vLocal
     * @throws java.lang.IndexOutOfBoundsException if the index
     * given is outside the bounds of the collection
     */
    public void addLocal(
            final int index,
            final org.svg.glossary.xml.Local vLocal)
    throws java.lang.IndexOutOfBoundsException {
        this._localList.add(index, vLocal);
    }

    /**
     */
    public void deleteGtl(
    ) {
        this._has_gtl= false;
    }

    /**
     */
    public void deleteShow(
    ) {
        this._has_show= false;
    }

    /**
     * Method enumerateItem.
     * 
     * @return an Enumeration over all possible elements of this
     * collection
     */
    public java.util.Enumeration<? extends org.svg.glossary.xml.Item> enumerateItem(
    ) {
        return java.util.Collections.enumeration(this._itemList);
    }

    /**
     * Method enumerateLocal.
     * 
     * @return an Enumeration over all possible elements of this
     * collection
     */
    public java.util.Enumeration<? extends org.svg.glossary.xml.Local> enumerateLocal(
    ) {
        return java.util.Collections.enumeration(this._localList);
    }

    /**
     * Returns the value of field 'gtl'.
     * 
     * @return the value of field 'Gtl'.
     */
    public boolean getGtl(
    ) {
        return this._gtl;
    }

    /**
     * Returns the value of field 'id'.
     * 
     * @return the value of field 'Id'.
     */
    public java.lang.String getId(
    ) {
        return this._id;
    }

    /**
     * Method getItem.
     * 
     * @param index
     * @throws java.lang.IndexOutOfBoundsException if the index
     * given is outside the bounds of the collection
     * @return the value of the org.svg.glossary.xml.Item at the
     * given index
     */
    public org.svg.glossary.xml.Item getItem(
            final int index)
    throws java.lang.IndexOutOfBoundsException {
        // check bounds for index
        if (index < 0 || index >= this._itemList.size()) {
            throw new IndexOutOfBoundsException("getItem: Index value '" + index + "' not in range [0.." + (this._itemList.size() - 1) + "]");
        }

        return (org.svg.glossary.xml.Item) _itemList.get(index);
    }

    /**
     * Method getItem.Returns the contents of the collection in an
     * Array.  <p>Note:  Just in case the collection contents are
     * changing in another thread, we pass a 0-length Array of the
     * correct type into the API call.  This way we <i>know</i>
     * that the Array returned is of exactly the correct length.
     * 
     * @return this collection as an Array
     */
    public org.svg.glossary.xml.Item[] getItem(
    ) {
        org.svg.glossary.xml.Item[] array = new org.svg.glossary.xml.Item[0];
        return (org.svg.glossary.xml.Item[]) this._itemList.toArray(array);
    }

    /**
     * Method getItemCount.
     * 
     * @return the size of this collection
     */
    public int getItemCount(
    ) {
        return this._itemList.size();
    }

    /**
     * Returns the value of field 'kanji'.
     * 
     * @return the value of field 'Kanji'.
     */
    public java.lang.String getKanji(
    ) {
        return this._kanji;
    }

    /**
     * Method getLocal.
     * 
     * @param index
     * @throws java.lang.IndexOutOfBoundsException if the index
     * given is outside the bounds of the collection
     * @return the value of the org.svg.glossary.xml.Local at the
     * given index
     */
    public org.svg.glossary.xml.Local getLocal(
            final int index)
    throws java.lang.IndexOutOfBoundsException {
        // check bounds for index
        if (index < 0 || index >= this._localList.size()) {
            throw new IndexOutOfBoundsException("getLocal: Index value '" + index + "' not in range [0.." + (this._localList.size() - 1) + "]");
        }

        return (org.svg.glossary.xml.Local) _localList.get(index);
    }

    /**
     * Method getLocal.Returns the contents of the collection in an
     * Array.  <p>Note:  Just in case the collection contents are
     * changing in another thread, we pass a 0-length Array of the
     * correct type into the API call.  This way we <i>know</i>
     * that the Array returned is of exactly the correct length.
     * 
     * @return this collection as an Array
     */
    public org.svg.glossary.xml.Local[] getLocal(
    ) {
        org.svg.glossary.xml.Local[] array = new org.svg.glossary.xml.Local[0];
        return (org.svg.glossary.xml.Local[]) this._localList.toArray(array);
    }

    /**
     * Method getLocalCount.
     * 
     * @return the size of this collection
     */
    public int getLocalCount(
    ) {
        return this._localList.size();
    }

    /**
     * Returns the value of field 'romaji'.
     * 
     * @return the value of field 'Romaji'.
     */
    public java.lang.String getRomaji(
    ) {
        return this._romaji;
    }

    /**
     * Returns the value of field 'show'.
     * 
     * @return the value of field 'Show'.
     */
    public boolean getShow(
    ) {
        return this._show;
    }

    /**
     * Method hasGtl.
     * 
     * @return true if at least one Gtl has been added
     */
    public boolean hasGtl(
    ) {
        return this._has_gtl;
    }

    /**
     * Method hasShow.
     * 
     * @return true if at least one Show has been added
     */
    public boolean hasShow(
    ) {
        return this._has_show;
    }

    /**
     * Returns the value of field 'gtl'.
     * 
     * @return the value of field 'Gtl'.
     */
    public boolean isGtl(
    ) {
        return this._gtl;
    }

    /**
     * Returns the value of field 'show'.
     * 
     * @return the value of field 'Show'.
     */
    public boolean isShow(
    ) {
        return this._show;
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
     * Method iterateItem.
     * 
     * @return an Iterator over all possible elements in this
     * collection
     */
    public java.util.Iterator<? extends org.svg.glossary.xml.Item> iterateItem(
    ) {
        return this._itemList.iterator();
    }

    /**
     * Method iterateLocal.
     * 
     * @return an Iterator over all possible elements in this
     * collection
     */
    public java.util.Iterator<? extends org.svg.glossary.xml.Local> iterateLocal(
    ) {
        return this._localList.iterator();
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
    public void removeAllItem(
    ) {
        this._itemList.clear();
    }

    /**
     */
    public void removeAllLocal(
    ) {
        this._localList.clear();
    }

    /**
     * Method removeItem.
     * 
     * @param vItem
     * @return true if the object was removed from the collection.
     */
    public boolean removeItem(
            final org.svg.glossary.xml.Item vItem) {
        boolean removed = _itemList.remove(vItem);
        return removed;
    }

    /**
     * Method removeItemAt.
     * 
     * @param index
     * @return the element removed from the collection
     */
    public org.svg.glossary.xml.Item removeItemAt(
            final int index) {
        java.lang.Object obj = this._itemList.remove(index);
        return (org.svg.glossary.xml.Item) obj;
    }

    /**
     * Method removeLocal.
     * 
     * @param vLocal
     * @return true if the object was removed from the collection.
     */
    public boolean removeLocal(
            final org.svg.glossary.xml.Local vLocal) {
        boolean removed = _localList.remove(vLocal);
        return removed;
    }

    /**
     * Method removeLocalAt.
     * 
     * @param index
     * @return the element removed from the collection
     */
    public org.svg.glossary.xml.Local removeLocalAt(
            final int index) {
        java.lang.Object obj = this._localList.remove(index);
        return (org.svg.glossary.xml.Local) obj;
    }

    /**
     * Sets the value of field 'gtl'.
     * 
     * @param gtl the value of field 'gtl'.
     */
    public void setGtl(
            final boolean gtl) {
        this._gtl = gtl;
        this._has_gtl = true;
    }

    /**
     * Sets the value of field 'id'.
     * 
     * @param id the value of field 'id'.
     */
    public void setId(
            final java.lang.String id) {
        this._id = id;
    }

    /**
     * 
     * 
     * @param index
     * @param vItem
     * @throws java.lang.IndexOutOfBoundsException if the index
     * given is outside the bounds of the collection
     */
    public void setItem(
            final int index,
            final org.svg.glossary.xml.Item vItem)
    throws java.lang.IndexOutOfBoundsException {
        // check bounds for index
        if (index < 0 || index >= this._itemList.size()) {
            throw new IndexOutOfBoundsException("setItem: Index value '" + index + "' not in range [0.." + (this._itemList.size() - 1) + "]");
        }

        this._itemList.set(index, vItem);
    }

    /**
     * 
     * 
     * @param vItemArray
     */
    public void setItem(
            final org.svg.glossary.xml.Item[] vItemArray) {
        //-- copy array
        _itemList.clear();

        for (int i = 0; i < vItemArray.length; i++) {
                this._itemList.add(vItemArray[i]);
        }
    }

    /**
     * Sets the value of field 'kanji'.
     * 
     * @param kanji the value of field 'kanji'.
     */
    public void setKanji(
            final java.lang.String kanji) {
        this._kanji = kanji;
    }

    /**
     * 
     * 
     * @param index
     * @param vLocal
     * @throws java.lang.IndexOutOfBoundsException if the index
     * given is outside the bounds of the collection
     */
    public void setLocal(
            final int index,
            final org.svg.glossary.xml.Local vLocal)
    throws java.lang.IndexOutOfBoundsException {
        // check bounds for index
        if (index < 0 || index >= this._localList.size()) {
            throw new IndexOutOfBoundsException("setLocal: Index value '" + index + "' not in range [0.." + (this._localList.size() - 1) + "]");
        }

        this._localList.set(index, vLocal);
    }

    /**
     * 
     * 
     * @param vLocalArray
     */
    public void setLocal(
            final org.svg.glossary.xml.Local[] vLocalArray) {
        //-- copy array
        _localList.clear();

        for (int i = 0; i < vLocalArray.length; i++) {
                this._localList.add(vLocalArray[i]);
        }
    }

    /**
     * Sets the value of field 'romaji'.
     * 
     * @param romaji the value of field 'romaji'.
     */
    public void setRomaji(
            final java.lang.String romaji) {
        this._romaji = romaji;
    }

    /**
     * Sets the value of field 'show'.
     * 
     * @param show the value of field 'show'.
     */
    public void setShow(
            final boolean show) {
        this._show = show;
        this._has_show = true;
    }

    /**
     * Method unmarshal.
     * 
     * @param reader
     * @throws org.exolab.castor.xml.MarshalException if object is
     * null or if any SAXException is thrown during marshaling
     * @throws org.exolab.castor.xml.ValidationException if this
     * object is an invalid instance according to the schema
     * @return the unmarshaled org.svg.glossary.xml.List
     */
    public static org.svg.glossary.xml.List unmarshal(
            final java.io.Reader reader)
    throws org.exolab.castor.xml.MarshalException, org.exolab.castor.xml.ValidationException {
        return (org.svg.glossary.xml.List) org.exolab.castor.xml.Unmarshaller.unmarshal(org.svg.glossary.xml.List.class, reader);
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
