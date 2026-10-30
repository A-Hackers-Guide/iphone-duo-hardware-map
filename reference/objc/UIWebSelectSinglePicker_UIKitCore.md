# `UIWebSelectSinglePicker`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPickerView`
- Protocols: `UIWebFormControl`, `UIPickerViewDataSource`, `UIPickerViewDelegate`
- 6 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"DOMHTMLSelectElement" _selectNode;
@"NSArray" _optionItems;
@"<UIWebSelectedItemPrivate>" _selectedOptionItem;
q _selectedIndex;
@"<UIWebSelectedItemPrivate>" _optionToSelectWhenDone;
q _indexToSelectWhenDone;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIWebSelectSinglePicker numberOfComponentsInPickerView:];
-[UIWebSelectSinglePicker dealloc];
-[UIWebSelectSinglePicker pickerView:didSelectRow:inComponent:];
-[UIWebSelectSinglePicker pickerView:numberOfRowsInComponent:];
-[UIWebSelectSinglePicker controlBeginEditing];
-[UIWebSelectSinglePicker controlEndEditing];
-[UIWebSelectSinglePicker controlView];
-[UIWebSelectSinglePicker initWithDOMHTMLSelectElement:allItems:];
-[UIWebSelectSinglePicker pickerView:attributedTitleForRow:forComponent:];
```
