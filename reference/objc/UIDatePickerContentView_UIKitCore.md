# `UIDatePickerContentView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 5 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
{?="isAmPm"b1"useDigitFont"b1} _datePickerContentViewFlags;
@"UILabel" _titleLabel;
d _titleLabelMaxX;
q _titleAlignment;
@"_UIDatePickerMode" _mode;
```

## Properties

```
@property (T@"_UIDatePickerMode",&,N,V_mode) mode;
@property (T@"UILabel",R,N,V_titleLabel) titleLabel;
@property (Td,N,V_titleLabelMaxX) titleLabelMaxX;
@property (TB,N) isAmPm;
@property (TB,N) useDigitFont;
@property (Tq,N,V_titleAlignment) titleAlignment;
```

## Instance methods

```
-[UIDatePickerContentView setTitleAlignment:];
-[UIDatePickerContentView useDigitFont];
-[UIDatePickerContentView titleAlignment];
-[UIDatePickerContentView _canBeReusedInPickerView];
-[UIDatePickerContentView titleLabel];
-[UIDatePickerContentView initWithMode:];
-[UIDatePickerContentView setTitleLabelMaxX:];
-[UIDatePickerContentView layoutSubviews];
-[UIDatePickerContentView setUseDigitFont:];
-[UIDatePickerContentView setMode:];
-[UIDatePickerContentView isAmPm];
-[UIDatePickerContentView mode];
-[UIDatePickerContentView setIsAmPm:];
-[UIDatePickerContentView titleLabelMaxX];
-[UIDatePickerContentView initWithFrame:];
```
