# `UIKBRenderingContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 9 instance variables, 11 properties, 23 instance methods, 1 class methods

## Instance variables

```
B _isFloating;
B _isGridLayout;
B _isNumberPad;
B _isColorAdaptiveNonLinearCarplayKeyboard;
Q _shiftState;
q _keyboardType;
@"UIKBRenderConfig" _renderConfig;
q _handBias;
@"UIView" _layoutView;
```

## Properties

```
@property (T@"UIView",W,N,V_layoutView) layoutView;
@property (TQ,N,V_shiftState) shiftState;
@property (Tq,N,V_keyboardType) keyboardType;
@property (T@"UIKBRenderConfig",&,N,V_renderConfig) renderConfig;
@property (Tq,N,V_handBias) handBias;
@property (TB,N,V_isFloating) isFloating;
@property (TB,N,V_isGridLayout) isGridLayout;
@property (TB,N,V_isNumberPad) isNumberPad;
@property (TB,N,V_isColorAdaptiveNonLinearCarplayKeyboard) isColorAdaptiveNonLinearCarplayKeyboard;
@property (T@"UIView<UIKBRenderingContextPopupView>",R,N) inputSwitcherView;
@property (T@"UIView<UIKBRenderingContextPopupView>",R,N) splitControlView;
```

## Class methods

```
+[UIKBRenderingContext renderingContextForRenderConfig:];
```

## Instance methods

```
-[UIKBRenderingContext shiftState];
-[UIKBRenderingContext handBias];
-[UIKBRenderingContext isGridLayout];
-[UIKBRenderingContext setLayoutView:];
-[UIKBRenderingContext setIsFloating:];
-[UIKBRenderingContext renderConfig];
-[UIKBRenderingContext setKeyboardType:];
-[UIKBRenderingContext isFloating];
-[UIKBRenderingContext layoutView];
-[UIKBRenderingContext inputSwitcherView];
-[UIKBRenderingContext setHandBias:];
-[UIKBRenderingContext setRenderConfig:];
-[UIKBRenderingContext setIsNumberPad:];
-[UIKBRenderingContext isColorAdaptiveNonLinearCarplayKeyboard];
-[UIKBRenderingContext setShiftState:];
-[UIKBRenderingContext keyboardType];
-[UIKBRenderingContext setIsColorAdaptiveNonLinearCarplayKeyboard:];
-[UIKBRenderingContext splitControlView];
-[UIKBRenderingContext setIsGridLayout:];
-[UIKBRenderingContext initWithRenderConfig:];
-[UIKBRenderingContext copyWithZone:];
-[UIKBRenderingContext isEqual:];
-[UIKBRenderingContext isNumberPad];
```
