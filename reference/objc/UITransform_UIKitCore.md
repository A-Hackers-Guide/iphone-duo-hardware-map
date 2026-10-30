# `UITransform`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `NSCopying`
- 1 instance variables, 5 properties, 11 instance methods, 7 class methods

## Instance variables

```
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _transform;
```

## Properties

```
@property (T{CGAffineTransform=dddddd},R,N,V_transform) transform;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UITransform identity];
+[UITransform transformWithCGAffineTransform:];
+[UITransform rotationWithDegrees:];
+[UITransform rotationWithRadians:];
+[UITransform scale:];
+[UITransform scaleX:scaleY:];
+[UITransform translation:];
```

## Instance methods

```
-[UITransform succinctDescriptionBuilder];
-[UITransform init];
-[UITransform descriptionWithMultilinePrefix:];
-[UITransform transform];
-[UITransform succinctDescription];
-[UITransform hash];
-[UITransform description];
-[UITransform copyWithZone:];
-[UITransform isEqual:];
-[UITransform descriptionBuilderWithMultilinePrefix:];
-[UITransform _initWithTransform:];
```
