# `_UIRepeatingPressGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- Protocols: `_UIRepeatingGestureClockDelegate`
- 4 instance variables, 9 properties, 23 instance methods, 0 class methods

## Instance variables

```
Q _numberOfTouchesRequired;
d _force;
Q _changeCount;
@"_UIRepeatingGestureClock" _clock;
```

## Properties

```
@property (T@"_UIRepeatingGestureClock",&,N,V_clock) clock;
@property (TQ,N,V_numberOfTouchesRequired) numberOfTouchesRequired;
@property (Tq,N,S_setButtonType:) _buttonType;
@property (Td,R,N,V_force) _force;
@property (TQ,N,V_changeCount) changeCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIRepeatingPressGestureRecognizer clock];
-[_UIRepeatingPressGestureRecognizer _shouldReceivePress:];
-[_UIRepeatingPressGestureRecognizer changeCount];
-[_UIRepeatingPressGestureRecognizer setClock:];
-[_UIRepeatingPressGestureRecognizer touchesEnded:withEvent:];
-[_UIRepeatingPressGestureRecognizer _resetGestureRecognizer];
-[_UIRepeatingPressGestureRecognizer touchesCancelled:withEvent:];
-[_UIRepeatingPressGestureRecognizer pressesCancelled:withEvent:];
-[_UIRepeatingPressGestureRecognizer pressesEnded:withEvent:];
-[_UIRepeatingPressGestureRecognizer _isGestureType:];
-[_UIRepeatingPressGestureRecognizer setView:];
-[_UIRepeatingPressGestureRecognizer touchesBegan:withEvent:];
-[_UIRepeatingPressGestureRecognizer touchesMoved:withEvent:];
-[_UIRepeatingPressGestureRecognizer initWithTarget:action:];
-[_UIRepeatingPressGestureRecognizer pressesBegan:withEvent:];
-[_UIRepeatingPressGestureRecognizer pressesChanged:withEvent:];
-[_UIRepeatingPressGestureRecognizer setNumberOfTouchesRequired:];
-[_UIRepeatingPressGestureRecognizer setChangeCount:];
-[_UIRepeatingPressGestureRecognizer numberOfTouchesRequired];
-[_UIRepeatingPressGestureRecognizer _setButtonType:];
-[_UIRepeatingPressGestureRecognizer _buttonType];
-[_UIRepeatingPressGestureRecognizer _force];
-[_UIRepeatingPressGestureRecognizer repeatingGestureClockDidTick:];
```
