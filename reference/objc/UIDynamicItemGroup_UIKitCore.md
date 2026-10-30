# `UIDynamicItemGroup`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDynamicItem`
- 3 instance variables, 10 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _itemsToOffsets;
{CGPoint="x"d"y"d} _center;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _transform;
```

## Properties

```
@property (T@"NSArray",R,C,N) items;
@property (T{CGPoint=dd},N,V_center) center;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
@property (T{CGAffineTransform=dddddd},N,V_transform) transform;
@property (TQ,?,R,N) collisionBoundsType;
@property (T@"UIBezierPath",?,R,N) collisionBoundingPath;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIDynamicItemGroup setCenter:];
-[UIDynamicItemGroup setTransform:];
-[UIDynamicItemGroup items];
-[UIDynamicItemGroup transform];
-[UIDynamicItemGroup center];
-[UIDynamicItemGroup bounds];
-[UIDynamicItemGroup initWithItems:];
```
