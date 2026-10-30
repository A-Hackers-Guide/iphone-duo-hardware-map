# `UIKeyboardFloatingTransitionState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"UIView" _inputView;
d _borderWidth;
@"UIColor" _borderColor;
d _cornerRadius;
{CGPoint="x"d"y"d} _scale;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputViewFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _platterViewFrame;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _platterInsets;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _initialInputViewTransform;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _finalInputViewTransform;
```

## Properties

```
@property (T@"UIView",&,N,V_inputView) inputView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_inputViewFrame) inputViewFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_platterViewFrame) platterViewFrame;
@property (T{UIEdgeInsets=dddd},N,V_platterInsets) platterInsets;
@property (T{CGPoint=dd},N,V_scale) scale;
@property (T{CGAffineTransform=dddddd},N,V_initialInputViewTransform) initialInputViewTransform;
@property (T{CGAffineTransform=dddddd},N,V_finalInputViewTransform) finalInputViewTransform;
@property (Td,N,V_borderWidth) borderWidth;
@property (T@"UIColor",C,N,V_borderColor) borderColor;
@property (Td,N,V_cornerRadius) cornerRadius;
```

## Instance methods

```
-[UIKeyboardFloatingTransitionState setBorderColor:];
-[UIKeyboardFloatingTransitionState platterInsets];
-[UIKeyboardFloatingTransitionState setBorderWidth:];
-[UIKeyboardFloatingTransitionState setScale:];
-[UIKeyboardFloatingTransitionState setCornerRadius:];
-[UIKeyboardFloatingTransitionState scale];
-[UIKeyboardFloatingTransitionState inputView];
-[UIKeyboardFloatingTransitionState borderWidth];
-[UIKeyboardFloatingTransitionState cornerRadius];
-[UIKeyboardFloatingTransitionState setInputView:];
-[UIKeyboardFloatingTransitionState setPlatterInsets:];
-[UIKeyboardFloatingTransitionState borderColor];
-[UIKeyboardFloatingTransitionState finalInputViewTransform];
-[UIKeyboardFloatingTransitionState initialInputViewTransform];
-[UIKeyboardFloatingTransitionState inputViewFrame];
-[UIKeyboardFloatingTransitionState platterViewFrame];
-[UIKeyboardFloatingTransitionState setFinalInputViewTransform:];
-[UIKeyboardFloatingTransitionState setInitialInputViewTransform:];
-[UIKeyboardFloatingTransitionState setInputViewFrame:];
-[UIKeyboardFloatingTransitionState setPlatterViewFrame:];
```
