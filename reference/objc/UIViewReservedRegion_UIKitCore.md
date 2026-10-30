# `UIViewReservedRegion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 7 properties, 10 instance methods, 1 class methods

## Instance variables

```
impl;
cachedIdentifier;
cachedKind;
```

## Properties

```
@property (T@"UIViewReservedRegionIdentifier",N,R) identifier;
@property (T@"UIViewReservedRegionKind",N,R) kind;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,R) frame;
@property (T{UIEdgeInsets=dddd},N,R) margins;
@property (TB,N,R) active;
@property (Tq,N,R) hash;
@property (T@"NSString",N,R) description;
```

## Class methods

```
+[UIViewReservedRegion _reservedRegionForSceneRegion:view:];
```

## Instance methods

```
-[UIViewReservedRegion identifier];
-[UIViewReservedRegion init];
-[UIViewReservedRegion margins];
-[UIViewReservedRegion hash];
-[UIViewReservedRegion description];
-[UIViewReservedRegion isActive];
-[UIViewReservedRegion copyWithZone:];
-[UIViewReservedRegion isEqual:];
-[UIViewReservedRegion kind];
-[UIViewReservedRegion frame];
```
