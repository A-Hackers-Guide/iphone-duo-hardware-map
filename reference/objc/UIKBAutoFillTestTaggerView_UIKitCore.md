# `UIKBAutoFillTestTaggerView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIPickerViewDataSource`, `UIPickerViewDelegate`
- 10 instance variables, 6 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"UIKBAutoFillTestTagRequest" _currentRequest;
@"UIPickerView" _pickerView;
@"UIToolbar" _toolbar;
@"UIBarButtonItem" _nextBarButtoItem;
@"UIBarButtonItem" _previousBarButtonItem;
@"UIBarButtonItem" _doneBarButtonItem;
@"UIVisualEffectView" _visualEffectView;
@"UILabel" _titleLabel;
@"<UIKBAutoFillTestTaggerViewDelegate>" _delegate;
@"NSArray" _tagRequests;
```

## Properties

```
@property (T@"<UIKBAutoFillTestTaggerViewDelegate>",W,N,V_delegate) delegate;
@property (T@"NSArray",C,N,V_tagRequests) tagRequests;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIKBAutoFillTestTaggerView pickerView:rowHeightForComponent:];
-[UIKBAutoFillTestTaggerView numberOfComponentsInPickerView:];
-[UIKBAutoFillTestTaggerView _updateTitle];
-[UIKBAutoFillTestTaggerView pickerView:didSelectRow:inComponent:];
-[UIKBAutoFillTestTaggerView setDelegate:];
-[UIKBAutoFillTestTaggerView pickerView:numberOfRowsInComponent:];
-[UIKBAutoFillTestTaggerView delegate];
-[UIKBAutoFillTestTaggerView initWithFrame:];
-[UIKBAutoFillTestTaggerView setTagRequests:];
-[UIKBAutoFillTestTaggerView _textFieldTypes];
-[UIKBAutoFillTestTaggerView _doneBarButtonAction:];
-[UIKBAutoFillTestTaggerView _formTypes];
-[UIKBAutoFillTestTaggerView _nextBarButtonAction:];
-[UIKBAutoFillTestTaggerView _performTagRequest:];
-[UIKBAutoFillTestTaggerView _previousBarButtonAction:];
-[UIKBAutoFillTestTaggerView _updateToolbarButtons];
-[UIKBAutoFillTestTaggerView pickerView:titleForRow:forComponent:];
-[UIKBAutoFillTestTaggerView tagRequests];
```
