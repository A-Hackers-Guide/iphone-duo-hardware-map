# `_UIHyperplane`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIHyperregion_Internal`, `NSSecureCoding`, `NSCopying`
- 3 instance variables, 7 properties, 13 instance methods, 2 class methods

## Instance variables

```
^d __point;
^d __normal;
Q __dimensions;
```

## Properties

```
@property (Tr^d,R,N) _point;
@property (Tr^d,R,N) _normal;
@property (TQ,R,N,V__dimensions) _dimensions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIHyperplane supportsSecureCoding];
+[_UIHyperplane keyPathsForValuesAffectingSelf];
```

## Instance methods

```
-[_UIHyperplane initWithDimensions:];
-[_UIHyperplane dealloc];
-[_UIHyperplane encodeWithCoder:];
-[_UIHyperplane description];
-[_UIHyperplane initWithCoder:];
-[_UIHyperplane _dimensions];
-[_UIHyperplane copyWithZone:];
-[_UIHyperplane isEqual:];
-[_UIHyperplane _closestPoint:toPoint:];
-[_UIHyperplane _normal];
-[_UIHyperplane _mutateNormal:];
-[_UIHyperplane _mutatePoint:];
-[_UIHyperplane _point];
```
