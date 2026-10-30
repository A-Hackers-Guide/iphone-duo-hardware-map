# `_UIHoverTouchDeliveryTable`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _beginningGestureRecognizers;
@"NSMutableSet" _updatingGestureRecognizers;
@"NSMutableSet" _exitingGestureRecognizers;
@"UITouch" _touch;
```

## Properties

```
@property (T@"UITouch",R,N,V_touch) touch;
@property (T@"NSSet",R,N) gestureRecognizers;
```

## Instance methods

```
-[_UIHoverTouchDeliveryTable touch];
-[_UIHoverTouchDeliveryTable gestureRecognizers];
-[_UIHoverTouchDeliveryTable _cancelAllGestureRecognizers];
-[_UIHoverTouchDeliveryTable removeGestureRecognizer:];
-[_UIHoverTouchDeliveryTable initWithTouch:];
-[_UIHoverTouchDeliveryTable updateForEvent:forcingHitTest:];
-[_UIHoverTouchDeliveryTable updateGestureRecognizerForDelivery:];
```
