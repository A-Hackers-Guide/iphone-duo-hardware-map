# `UIZoomTransitionInteractionContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
B _willBegin;
{CGPoint="x"d"y"d} _location;
{CGVector="dx"d"dy"d} _velocity;
```

## Properties

```
@property (T{CGPoint=dd},N,V_location) location;
@property (T{CGVector=dd},N,V_velocity) velocity;
@property (TB,N,V_willBegin) willBegin;
```

## Instance methods

```
-[UIZoomTransitionInteractionContext location];
-[UIZoomTransitionInteractionContext velocity];
-[UIZoomTransitionInteractionContext setLocation:];
-[UIZoomTransitionInteractionContext setVelocity:];
-[UIZoomTransitionInteractionContext setWillBegin:];
-[UIZoomTransitionInteractionContext willBegin];
```
