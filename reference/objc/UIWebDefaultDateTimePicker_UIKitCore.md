# `UIWebDefaultDateTimePicker`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIWebFormControl`
- 5 instance variables, 2 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"DOMHTMLInputElement" _inputElement;
@"UIDatePicker" _datePicker;
@"NSString" _formatString;
B _shouldRemoveTimeZoneInformation;
B _isTimeInput;
```

## Properties

```
@property (T@"DOMHTMLInputElement",&,N,V_inputElement) _inputElement;
@property (T@"UIDatePicker",&,N,V_datePicker) _datePicker;
```

## Instance methods

```
-[UIWebDefaultDateTimePicker dealloc];
-[UIWebDefaultDateTimePicker set_datePicker:];
-[UIWebDefaultDateTimePicker _dateChangeHandler:];
-[UIWebDefaultDateTimePicker _dateChanged];
-[UIWebDefaultDateTimePicker _dateChangedSetAsNumber];
-[UIWebDefaultDateTimePicker _dateChangedSetAsString];
-[UIWebDefaultDateTimePicker _datePicker];
-[UIWebDefaultDateTimePicker _inputElement];
-[UIWebDefaultDateTimePicker _sanitizeInputValueForFormatter:];
-[UIWebDefaultDateTimePicker _timeZoneOffsetFromGMT:];
-[UIWebDefaultDateTimePicker controlBeginEditing];
-[UIWebDefaultDateTimePicker controlEndEditing];
-[UIWebDefaultDateTimePicker controlView];
-[UIWebDefaultDateTimePicker initWithDOMHTMLInputElement:datePickerMode:];
-[UIWebDefaultDateTimePicker set_inputElement:];
```
