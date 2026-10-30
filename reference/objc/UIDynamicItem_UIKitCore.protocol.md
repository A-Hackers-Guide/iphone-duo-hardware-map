# `UIDynamicItem` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 7 instance methods, 0 class methods

## Properties

```
@property (T{CGPoint=dd},N) center;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
@property (T{CGAffineTransform=dddddd},N) transform;
@property (TQ,?,R,N) collisionBoundsType;
@property (T@"UIBezierPath",?,R,N) collisionBoundingPath;
```

## Instance methods

```
-[UIDynamicItem setCenter:];
-[UIDynamicItem setTransform:];
-[UIDynamicItem transform];
-[UIDynamicItem center];
-[UIDynamicItem bounds];
-[UIDynamicItem collisionBoundingPath];
-[UIDynamicItem collisionBoundsType];
```
