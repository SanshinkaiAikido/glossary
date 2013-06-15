/*
 * This class was automatically generated with 
 * <a href="http://www.castor.org">Castor 1.3</a>, using an XML
 * Schema.
 * $Id$
 */

package org.svg.glossary.xml;

/**
 * Class Extra.
 * 
 * @version $Revision$ $Date$
 */
@SuppressWarnings("serial")
public class Extra implements java.io.Serializable {


      //--------------------------/
     //- Class/Member Variables -/
    //--------------------------/

    /**
     * Field _itemList.
     */
    private java.util.List<org.svg.glossary.xml.Item> _itemList;


      //----------------/
     //- Constructors -/
    //----------------/

    public Extra() {
        super();
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
     * Method unmarshal.
     * 
     * @param reader
     * @throws org.exolab.castor.xml.MarshalException if object is
     * null or if any SAXException is thrown during marshaling
     * @throws org.exolab.castor.xml.ValidationException if this
     * object is an invalid instance according to the schema
     * @return the unmarshaled org.svg.glossary.xml.Extra
     */
    public static org.svg.glossary.xml.Extra unmarshal(
            final java.io.Reader reader)
    throws org.exolab.castor.xml.MarshalException, org.exolab.castor.xml.ValidationException {
        return (org.svg.glossary.xml.Extra) org.exolab.castor.xml.Unmarshaller.unmarshal(org.svg.glossary.xml.Extra.class, reader);
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
