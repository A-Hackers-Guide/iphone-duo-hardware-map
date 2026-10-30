# `_UIKeyboardIndirectTextSelectionGestureState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _isShiftKeyBeingHeld;
q _type;
q _state;
Q _flickDirection;
Q _touchCount;
{CGPoint="x"d"y"d} _translation;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (Tq,N,V_state) state;
@property (T{CGPoint=dd},N,V_translation) translation;
@property (TQ,N,V_flickDirection) flickDirection;
@property (TB,N,V_isShiftKeyBeingHeld) isShiftKeyBeingHeld;
@property (TQ,N,V_touchCount) touchCount;
```

## Class methods

```
+[_UIKeyboardIndirectTextSelectionGestureState supportsSecureCoding];
```

## Instance methods

```
-[_UIKeyboardIndirectTextSelectionGestureState isShiftKeyBeingHeld];
-[_UIKeyboardIndirectTextSelectionGestureState setState:];
-[_UIKeyboardIndirectTextSelectionGestureState setFlickDirection:];
-[_UIKeyboardIndirectTextSelectionGestureState touchCount];
-[_UIKeyboardIndirectTextSelectionGestureState setType:];
-[_UIKeyboardIndirectTextSelectionGestureState type];
-[_UIKeyboardIndirectTextSelectionGestureState flickDirection];
-[_UIKeyboardIndirectTextSelectionGestureState encodeWithCoder:];
-[_UIKeyboardIndirectTextSelectionGestureState setTranslation:];
-[_UIKeyboardIndirectTextSelectionGestureState initWithCoder:];
-[_UIKeyboardIndirectTextSelectionGestureState isEqual:];
-[_UIKeyboardIndirectTextSelectionGestureState translation];
-[_UIKeyboardIndirectTextSelectionGestureState state];
-[_UIKeyboardIndirectTextSelectionGestureState setIsShiftKeyBeingHeld:];
-[_UIKeyboardIndirectTextSelectionGestureState setTouchCount:];
```
