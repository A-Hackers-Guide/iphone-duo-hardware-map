# `_UIHyperAsymmetricExtender`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIHyperExtender_Internal`, `_UIHyperExtender`, `NSSecureCoding`, `NSCopying`
- 4 instance variables, 7 properties, 13 instance methods, 2 class methods

## Instance variables

```
^d __extentBeyondMinimum;
^d __extentBeyondMaximum;
^d __temp;
Q __dimensions;
```

## Properties

```
@property (Tr^d,R,N) _extentBeyondMinimum;
@property (Tr^d,R,N) _extentBeyondMaximum;
@property (TQ,R,N,V__dimensions) _dimensions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIHyperAsymmetricExtender supportsSecureCoding];
+[_UIHyperAsymmetricExtender keyPathsForValuesAffectingSelf];
```

## Instance methods

```
-[_UIHyperAsymmetricExtender initWithDimensions:];
-[_UIHyperAsymmetricExtender dealloc];
-[_UIHyperAsymmetricExtender _getExtentVector:forUnconstrainedPoint:closestPoint:];
-[_UIHyperAsymmetricExtender encodeWithCoder:];
-[_UIHyperAsymmetricExtender description];
-[_UIHyperAsymmetricExtender initWithCoder:];
-[_UIHyperAsymmetricExtender _dimensions];
-[_UIHyperAsymmetricExtender copyWithZone:];
-[_UIHyperAsymmetricExtender isEqual:];
-[_UIHyperAsymmetricExtender _extentBeyondMaximum];
-[_UIHyperAsymmetricExtender _extentBeyondMinimum];
-[_UIHyperAsymmetricExtender _mutateExtentBeyondMaximum:];
-[_UIHyperAsymmetricExtender _mutateExtentBeyondMinimum:];
```
