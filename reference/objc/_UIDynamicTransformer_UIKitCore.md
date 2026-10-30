# `_UIDynamicTransformer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDynamicItem`
- 2 instance variables, 9 properties, 6 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _center;
@? _action;
```

## Properties

```
@property (T{CGPoint=dd},N) center;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
@property (T{CGAffineTransform=dddddd},N) transform;
@property (TQ,?,R,N) collisionBoundsType;
@property (T@"UIBezierPath",?,R,N) collisionBoundingPath;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDynamicTransformer setCenter:];
-[_UIDynamicTransformer setTransform:];
-[_UIDynamicTransformer transform];
-[_UIDynamicTransformer center];
-[_UIDynamicTransformer bounds];
-[_UIDynamicTransformer initWithActionBlock:];
```
