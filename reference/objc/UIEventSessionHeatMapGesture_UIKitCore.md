# `UIEventSessionHeatMapGesture`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _touches;
q _touchType;
q _uiInterfaceOrientation;
q _hardwareKeyboardState;
q _magicKeyboardState;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_touches) touches;
@property (Tq,V_touchType) touchType;
@property (Tq,N,V_uiInterfaceOrientation) uiInterfaceOrientation;
@property (Tq,N,V_hardwareKeyboardState) hardwareKeyboardState;
@property (Tq,N,V_magicKeyboardState) magicKeyboardState;
```

## Instance methods

```
-[UIEventSessionHeatMapGesture touches];
-[UIEventSessionHeatMapGesture containsTouchID:];
-[UIEventSessionHeatMapGesture hardwareKeyboardState];
-[UIEventSessionHeatMapGesture initWithTouchType:interfaceOrientation:hardwareKeyboardState:magicKeyboardState:];
-[UIEventSessionHeatMapGesture magicKeyboardState];
-[UIEventSessionHeatMapGesture setHardwareKeyboardState:];
-[UIEventSessionHeatMapGesture setMagicKeyboardState:];
-[UIEventSessionHeatMapGesture setTouchType:];
-[UIEventSessionHeatMapGesture setTouches:];
-[UIEventSessionHeatMapGesture setUiInterfaceOrientation:];
-[UIEventSessionHeatMapGesture touchType];
-[UIEventSessionHeatMapGesture uiInterfaceOrientation];
```
