# `TPSimpleNumberPad`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TPNumberPad`
- 3 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"UIButton" _deleteButton;
B _showsDeleteButton;
@"<TPSimpleNumberPadDelegate>" _delegate;
```

## Properties

```
@property (T@"<TPSimpleNumberPadDelegate>",V_delegate) delegate;
@property (TB,N,V_showsDeleteButton) showsDeleteButton;
```

## Class methods

```
+[TPSimpleNumberPad _numberPadCharacters];
```

## Instance methods

```
-[TPSimpleNumberPad initWithFrame:style:];
-[TPSimpleNumberPad setDelegate:];
-[TPSimpleNumberPad delegate];
-[TPSimpleNumberPad setShowsDeleteButton:];
-[TPSimpleNumberPad buttonUp:];
-[TPSimpleNumberPad initWithButtons:];
-[TPSimpleNumberPad _deleteButtonClicked:withEvent:];
-[TPSimpleNumberPad _updateDeleteButton];
-[TPSimpleNumberPad numberPadButtonClass];
-[TPSimpleNumberPad setNumberButtonsEnabled:];
-[TPSimpleNumberPad showsDeleteButton];
```
