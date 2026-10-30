# `UIFocusMovementHint`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
d _translationAmount;
d _rotationAmount;
{CGVector="dx"d"dy"d} _movementDirection;
```

## Properties

```
@property (Td,N,V_translationAmount) translationAmount;
@property (Td,N,V_rotationAmount) rotationAmount;
@property (T{CGVector=dd},R,N,V_movementDirection) movementDirection;
@property (T{CATransform3D=dddddddddddddddd},R,N) perspectiveTransform;
@property (T{CGVector=dd},R,N) rotation;
@property (T{CGVector=dd},R,N) translation;
@property (T{CATransform3D=dddddddddddddddd},R,N) interactionTransform;
```

## Instance methods

```
-[UIFocusMovementHint rotation];
-[UIFocusMovementHint perspectiveTransform];
-[UIFocusMovementHint copyWithZone:];
-[UIFocusMovementHint translation];
-[UIFocusMovementHint initWithMovementDirection:itemSize:];
-[UIFocusMovementHint interactionTransform];
-[UIFocusMovementHint movementDirection];
-[UIFocusMovementHint rotationAmount];
-[UIFocusMovementHint setRotationAmount:];
-[UIFocusMovementHint setTranslationAmount:];
-[UIFocusMovementHint translationAmount];
```
