# `_UIDatePickerOverlayPlatterView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 11 instance variables, 11 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _accessoryViewIgnoresDefaultInsets;
@"UIDatePicker" _datePicker;
@"_UIRoundedRectShadowView" _shadowView;
@"UIView" _backgroundView;
@"UIView" _accessoryView;
@"UIView" _previousContentView;
@"UIView" _contentView;
@"NSLayoutConstraint" _contentWidthConstraint;
@"NSLayoutConstraint" _contentHeightConstraint;
@"_UIDatePickerStyle" _datePickerStyle;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _contentBounds;
```

## Properties

```
@property (T@"_UIRoundedRectShadowView",R,N,V_shadowView) shadowView;
@property (T@"UIView",R,N,V_backgroundView) backgroundView;
@property (T@"UIView",R,N,V_accessoryView) accessoryView;
@property (T@"UIView",R,N,V_previousContentView) previousContentView;
@property (T@"UIView",R,N,V_contentView) contentView;
@property (T@"NSLayoutConstraint",R,N,V_contentWidthConstraint) contentWidthConstraint;
@property (T@"NSLayoutConstraint",R,N,V_contentHeightConstraint) contentHeightConstraint;
@property (T@"_UIDatePickerStyle",R,N,V_datePickerStyle) datePickerStyle;
@property (T@"UIDatePicker",R,N,V_datePicker) datePicker;
@property (TB,N,V_accessoryViewIgnoresDefaultInsets) accessoryViewIgnoresDefaultInsets;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_contentBounds) contentBounds;
```

## Instance methods

```
-[_UIDatePickerOverlayPlatterView setContentBounds:];
-[_UIDatePickerOverlayPlatterView accessoryView];
-[_UIDatePickerOverlayPlatterView contentBounds];
-[_UIDatePickerOverlayPlatterView datePickerStyle];
-[_UIDatePickerOverlayPlatterView layoutSubviews];
-[_UIDatePickerOverlayPlatterView shadowView];
-[_UIDatePickerOverlayPlatterView contentView];
-[_UIDatePickerOverlayPlatterView backgroundView];
-[_UIDatePickerOverlayPlatterView updateConstraints];
-[_UIDatePickerOverlayPlatterView preferredContentSize];
-[_UIDatePickerOverlayPlatterView datePicker];
-[_UIDatePickerOverlayPlatterView accessoryViewIgnoresDefaultInsets];
-[_UIDatePickerOverlayPlatterView contentHeightConstraint];
-[_UIDatePickerOverlayPlatterView contentWidthConstraint];
-[_UIDatePickerOverlayPlatterView datePickerTransitionAnimation];
-[_UIDatePickerOverlayPlatterView datePickerTransitionCompletion];
-[_UIDatePickerOverlayPlatterView initWithDatePicker:accessoryView:];
-[_UIDatePickerOverlayPlatterView preferredPlatterSize];
-[_UIDatePickerOverlayPlatterView prepareDatePickerTransitionWithDatePicker:];
-[_UIDatePickerOverlayPlatterView previousContentView];
-[_UIDatePickerOverlayPlatterView replaceDatePicker:];
-[_UIDatePickerOverlayPlatterView setAccessoryViewIgnoresDefaultInsets:];
```
