# `_UIPreviewInteractionCompatibilityTouchForceProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `_UIPreviewInteractionTouchForceProviding`
- 4 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"UIView" _view;
@"_UITouchesObservingGestureRecognizer" _gestureRecognizer;
@"UITouch" _currentTouch;
B _active;
```

## Properties

```
@property (TB,N,GisActive,V_active) active;
@property (T@"UIView",R,W,N,V_view) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,R,N) touchForce;
```

## Instance methods

```
-[_UIPreviewInteractionCompatibilityTouchForceProvider locationInCoordinateSpace:];
-[_UIPreviewInteractionCompatibilityTouchForceProvider cancelInteraction];
-[_UIPreviewInteractionCompatibilityTouchForceProvider gestureRecognizer:shouldReceiveTouch:];
-[_UIPreviewInteractionCompatibilityTouchForceProvider initWithView:];
-[_UIPreviewInteractionCompatibilityTouchForceProvider dealloc];
-[_UIPreviewInteractionCompatibilityTouchForceProvider setActive:];
-[_UIPreviewInteractionCompatibilityTouchForceProvider touchForce];
-[_UIPreviewInteractionCompatibilityTouchForceProvider view];
-[_UIPreviewInteractionCompatibilityTouchForceProvider gestureRecognizerShouldBegin:];
-[_UIPreviewInteractionCompatibilityTouchForceProvider isActive];
-[_UIPreviewInteractionCompatibilityTouchForceProvider _handleTouchObservingGestureRecognizer:];
```
