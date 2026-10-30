# `UIWebSelectMultiplePicker`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPickerView`
- Protocols: `UIWebFormControl`, `UIPickerViewDataSource`, `UIPickerViewDelegate`
- 8 instance variables, 7 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"DOMHTMLSelectElement" _selectionNode;
@"NSArray" _cachedItems;
@"<UIWebSelectedItemPrivate>" _singleSelectionItem;
Q _singleSelectionIndex;
d _fontSize;
d _maximumTextWidth;
q _textAlignment;
d _layoutWidth;
```

## Properties

```
@property (T@"DOMHTMLSelectElement",&,N,V_selectionNode) _selectionNode;
@property (T@"NSArray",&,N,V_cachedItems) _cachedItems;
@property (T@"<UIWebSelectedItemPrivate>",&,N,V_singleSelectionItem) _singleSelectionItem;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIWebSelectMultiplePicker numberOfComponentsInPickerView:];
-[UIWebSelectMultiplePicker dealloc];
-[UIWebSelectMultiplePicker layoutSubviews];
-[UIWebSelectMultiplePicker pickerView:numberOfRowsInComponent:];
-[UIWebSelectMultiplePicker pickerView:viewForRow:forComponent:reusingView:];
-[UIWebSelectMultiplePicker _cachedItems];
-[UIWebSelectMultiplePicker _itemIndexForRowIndex:];
-[UIWebSelectMultiplePicker _selectionNode];
-[UIWebSelectMultiplePicker _singleSelectionItem];
-[UIWebSelectMultiplePicker controlBeginEditing];
-[UIWebSelectMultiplePicker controlEndEditing];
-[UIWebSelectMultiplePicker controlView];
-[UIWebSelectMultiplePicker initWithDOMHTMLSelectElement:cachedItems:singleSelectionItem:singleSelectionIndex:multipleSelection:];
-[UIWebSelectMultiplePicker pickerView:row:column:checked:];
-[UIWebSelectMultiplePicker set_cachedItems:];
-[UIWebSelectMultiplePicker set_selectionNode:];
-[UIWebSelectMultiplePicker set_singleSelectionItem:];
```
