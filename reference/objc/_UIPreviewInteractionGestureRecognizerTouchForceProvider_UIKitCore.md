# `_UIPreviewInteractionGestureRecognizerTouchForceProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `_UIPreviewInteractionTouchForceProviding`
- 2 instance variables, 7 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _active;
@"UITouchForceGestureRecognizer" _gestureRecognizer;
```

## Properties

```
@property (TB,N,GisActive,V_active) active;
@property (T@"UITouchForceGestureRecognizer",&,N,V_gestureRecognizer) gestureRecognizer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,R,N) touchForce;
```

## Instance methods

```
-[_UIPreviewInteractionGestureRecognizerTouchForceProvider locationInCoordinateSpace:];
-[_UIPreviewInteractionGestureRecognizerTouchForceProvider cancelInteraction];
-[_UIPreviewInteractionGestureRecognizerTouchForceProvider _handleGestureRecognizer:];
-[_UIPreviewInteractionGestureRecognizerTouchForceProvider gestureRecognizer];
-[_UIPreviewInteractionGestureRecognizerTouchForceProvider dealloc];
-[_UIPreviewInteractionGestureRecognizerTouchForceProvider setActive:];
-[_UIPreviewInteractionGestureRecognizerTouchForceProvider touchForce];
-[_UIPreviewInteractionGestureRecognizerTouchForceProvider gestureRecognizerShouldBegin:];
-[_UIPreviewInteractionGestureRecognizerTouchForceProvider setGestureRecognizer:];
-[_UIPreviewInteractionGestureRecognizerTouchForceProvider isActive];
-[_UIPreviewInteractionGestureRecognizerTouchForceProvider initWithGestureRecognizer:];
-[_UIPreviewInteractionGestureRecognizerTouchForceProvider initWithView:configuration:];
```
