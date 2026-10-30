# `UIGestureDelayedTouch`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `_UIGestureDelaying`
- 6 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
q _delayCount;
B _clonedForSecondDelivery;
@"UITouch" _touch;
@"UITouch" _stateWhenDelayed;
@"UITouch" _stateWhenDelivered;
@"UIEvent" _event;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIGestureDelayedTouch phaseForDelivery];
-[UIGestureDelayedTouch timestampForDelivery];
-[UIGestureDelayedTouch description];
-[UIGestureDelayedTouch copyWithZone:];
```
