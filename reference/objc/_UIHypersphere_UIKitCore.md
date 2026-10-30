# `_UIHypersphere`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIHyperregion_Internal`, `NSSecureCoding`, `NSCopying`
- 3 instance variables, 7 properties, 13 instance methods, 2 class methods

## Instance variables

```
^d __center;
Q __dimensions;
d __radius;
```

## Properties

```
@property (Tr^d,R,N) _center;
@property (Td,N,S_setRadius:,V__radius) _radius;
@property (TQ,R,N,V__dimensions) _dimensions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIHypersphere supportsSecureCoding];
+[_UIHypersphere keyPathsForValuesAffectingSelf];
```

## Instance methods

```
-[_UIHypersphere initWithDimensions:];
-[_UIHypersphere dealloc];
-[_UIHypersphere encodeWithCoder:];
-[_UIHypersphere description];
-[_UIHypersphere initWithCoder:];
-[_UIHypersphere _dimensions];
-[_UIHypersphere copyWithZone:];
-[_UIHypersphere isEqual:];
-[_UIHypersphere _closestPoint:toPoint:];
-[_UIHypersphere _radius];
-[_UIHypersphere _center];
-[_UIHypersphere _mutateCenter:];
-[_UIHypersphere _setRadius:];
```
