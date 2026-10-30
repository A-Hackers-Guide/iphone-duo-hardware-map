# `_UIHyperrectangle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIHyperregion_Internal`, `_UIHyperregion`, `NSSecureCoding`, `NSCopying`
- 3 instance variables, 7 properties, 13 instance methods, 2 class methods

## Instance variables

```
^d __maximumPoint;
^d __minimumPoint;
Q __dimensions;
```

## Properties

```
@property (Tr^d,R,N) _minimumPoint;
@property (Tr^d,R,N) _maximumPoint;
@property (TQ,R,N,V__dimensions) _dimensions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIHyperrectangle supportsSecureCoding];
+[_UIHyperrectangle keyPathsForValuesAffectingSelf];
```

## Instance methods

```
-[_UIHyperrectangle initWithDimensions:];
-[_UIHyperrectangle dealloc];
-[_UIHyperrectangle encodeWithCoder:];
-[_UIHyperrectangle description];
-[_UIHyperrectangle initWithCoder:];
-[_UIHyperrectangle _dimensions];
-[_UIHyperrectangle copyWithZone:];
-[_UIHyperrectangle isEqual:];
-[_UIHyperrectangle _closestPoint:toPoint:];
-[_UIHyperrectangle _maximumPoint];
-[_UIHyperrectangle _minimumPoint];
-[_UIHyperrectangle _mutateMaximumPoint:];
-[_UIHyperrectangle _mutateMinimumPoint:];
```
