# `TPNumberPad`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- 3 instance variables, 3 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _buttons;
B _numberButtonsEnabled;
d _buttonBackgroundAlpha;
```

## Properties

```
@property (TB,N,V_numberButtonsEnabled) numberButtonsEnabled;
@property (T@"NSArray",&,D) buttons;
@property (Td,N,V_buttonBackgroundAlpha) buttonBackgroundAlpha;
```

## Instance methods

```
-[TPNumberPad buttons];
-[TPNumberPad intrinsicContentSize];
-[TPNumberPad dealloc];
-[TPNumberPad setButtons:];
-[TPNumberPad buttonDown:];
-[TPNumberPad buttonTapped:];
-[TPNumberPad buttonCancelled:];
-[TPNumberPad buttonUp:];
-[TPNumberPad initWithButtons:];
-[TPNumberPad _addButton:];
-[TPNumberPad _layoutGrid];
-[TPNumberPad buttonBackgroundAlpha];
-[TPNumberPad buttonLongPressed:];
-[TPNumberPad buttonLongPressedViaGesture:];
-[TPNumberPad buttonUpOutside:];
-[TPNumberPad handleCurrentLocaleDidChangeNotification:];
-[TPNumberPad numberButtonsEnabled];
-[TPNumberPad reloadButtonImages];
-[TPNumberPad replaceButton:atIndex:];
-[TPNumberPad setButtonBackgroundAlpha:];
-[TPNumberPad setNumberButtonsEnabled:];
```
