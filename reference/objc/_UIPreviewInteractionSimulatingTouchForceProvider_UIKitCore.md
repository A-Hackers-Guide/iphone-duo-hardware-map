# `_UIPreviewInteractionSimulatingTouchForceProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIPreviewInteractionTouchForceProviding`
- 4 instance variables, 6 properties, 6 instance methods, 0 class methods

## Instance variables

```
d _targetTouchForce;
{CGPoint="x"d"y"d} _location;
@"<UICoordinateSpace>" _coordinateSpace;
B _active;
```

## Properties

```
@property (TB,N,GisActive,V_active) active;
@property (Td,R,N) touchForce;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIPreviewInteractionSimulatingTouchForceProvider locationInCoordinateSpace:];
-[_UIPreviewInteractionSimulatingTouchForceProvider cancelInteraction];
-[_UIPreviewInteractionSimulatingTouchForceProvider setActive:];
-[_UIPreviewInteractionSimulatingTouchForceProvider touchForce];
-[_UIPreviewInteractionSimulatingTouchForceProvider isActive];
-[_UIPreviewInteractionSimulatingTouchForceProvider initWithTouchForce:location:coordinateSpace:];
```
