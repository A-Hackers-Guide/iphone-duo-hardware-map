# `_UITextInputSessionKeyboardDockItemButtonPressAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UITextInputSessionAction`
- 7 instance variables, 7 properties, 16 instance methods, 0 class methods

## Instance variables

```
Q _buttonPressResult;
Q _buttonType;
q _uiOrientation;
d _touchDuration;
{CGSize="width"d"height"d} _buttonSize;
{CGPoint="x"d"y"d} _touchDownPoint;
{CGPoint="x"d"y"d} _touchUpPoint;
```

## Properties

```
@property (TQ,N,V_buttonPressResult) buttonPressResult;
@property (TQ,N,V_buttonType) buttonType;
@property (Tq,N,V_uiOrientation) uiOrientation;
@property (T{CGSize=dd},N,V_buttonSize) buttonSize;
@property (T{CGPoint=dd},N,V_touchDownPoint) touchDownPoint;
@property (T{CGPoint=dd},N,V_touchUpPoint) touchUpPoint;
@property (Td,N,V_touchDuration) touchDuration;
```

## Instance methods

```
-[_UITextInputSessionKeyboardDockItemButtonPressAction buttonType];
-[_UITextInputSessionKeyboardDockItemButtonPressAction touchDuration];
-[_UITextInputSessionKeyboardDockItemButtonPressAction inputActionCount];
-[_UITextInputSessionKeyboardDockItemButtonPressAction setTouchDownPoint:];
-[_UITextInputSessionKeyboardDockItemButtonPressAction touchDownPoint];
-[_UITextInputSessionKeyboardDockItemButtonPressAction setButtonType:];
-[_UITextInputSessionKeyboardDockItemButtonPressAction buttonSize];
-[_UITextInputSessionKeyboardDockItemButtonPressAction description];
-[_UITextInputSessionKeyboardDockItemButtonPressAction uiOrientation];
-[_UITextInputSessionKeyboardDockItemButtonPressAction buttonPressResult];
-[_UITextInputSessionKeyboardDockItemButtonPressAction setButtonPressResult:];
-[_UITextInputSessionKeyboardDockItemButtonPressAction setButtonSize:];
-[_UITextInputSessionKeyboardDockItemButtonPressAction setTouchDuration:];
-[_UITextInputSessionKeyboardDockItemButtonPressAction setTouchUpPoint:];
-[_UITextInputSessionKeyboardDockItemButtonPressAction setUiOrientation:];
-[_UITextInputSessionKeyboardDockItemButtonPressAction touchUpPoint];
```
