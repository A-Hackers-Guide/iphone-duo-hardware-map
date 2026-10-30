# `_UIHyperrepeatedRegion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIHyperregion_Internal`, `NSSecureCoding`, `NSCopying`
- 8 instance variables, 10 properties, 21 instance methods, 2 class methods

## Instance variables

```
^Q __repetitions;
^d __offset;
^d __increment;
^d __maximumIndices;
{?="maximumIndices"b1} _clean;
Q __dimensions;
@"<_UIHyperregion>" __region;
^d __temp;
```

## Properties

```
@property (T^d,R,N,V__temp) _temp;
@property (T@"<_UIHyperregion>",&,N,S_setRegion:,V__region) _region;
@property (Tr^Q,R,N) _repetitions;
@property (Tr^d,R,N) _offset;
@property (Tr^d,R,N) _increment;
@property (TQ,R,N,V__dimensions) _dimensions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIHyperrepeatedRegion supportsSecureCoding];
+[_UIHyperrepeatedRegion keyPathsForValuesAffectingSelf];
```

## Instance methods

```
-[_UIHyperrepeatedRegion initWithDimensions:];
-[_UIHyperrepeatedRegion dealloc];
-[_UIHyperrepeatedRegion _isBoundaryCrossedFromPoint:toPoint:];
-[_UIHyperrepeatedRegion _temp];
-[_UIHyperrepeatedRegion encodeWithCoder:];
-[_UIHyperrepeatedRegion description];
-[_UIHyperrepeatedRegion initWithCoder:];
-[_UIHyperrepeatedRegion _dimensions];
-[_UIHyperrepeatedRegion copyWithZone:];
-[_UIHyperrepeatedRegion isEqual:];
-[_UIHyperrepeatedRegion _closestPoint:toPoint:];
-[_UIHyperrepeatedRegion _offset];
-[_UIHyperrepeatedRegion _region];
-[_UIHyperrepeatedRegion _increment];
-[_UIHyperrepeatedRegion _indexOfClosestSubregion:toPoint:];
-[_UIHyperrepeatedRegion _mutableMaximumIndices];
-[_UIHyperrepeatedRegion _mutateIncrement:];
-[_UIHyperrepeatedRegion _mutateOffset:];
-[_UIHyperrepeatedRegion _mutateRepetitions:];
-[_UIHyperrepeatedRegion _repetitions];
-[_UIHyperrepeatedRegion _setRegion:];
```
