# `_UIAlignmentRegion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIHyperregion_Internal`, `NSSecureCoding`, `NSCopying`
- 4 instance variables, 8 properties, 16 instance methods, 2 class methods

## Instance variables

```
Q __dimensions;
@"<_UIHyperregion>" __region;
d __maximumDistance;
^d __temp;
```

## Properties

```
@property (T^d,R,N,V__temp) _temp;
@property (T@"<_UIHyperregion>",&,N,S_setRegion:,V__region) _region;
@property (Td,N,S_setMaximumDistance:,V__maximumDistance) _maximumDistance;
@property (TQ,R,N,V__dimensions) _dimensions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIAlignmentRegion supportsSecureCoding];
+[_UIAlignmentRegion keyPathsForValuesAffectingSelf];
```

## Instance methods

```
-[_UIAlignmentRegion _setMaximumDistance:];
-[_UIAlignmentRegion initWithDimensions:];
-[_UIAlignmentRegion dealloc];
-[_UIAlignmentRegion _isBoundaryCrossedFromPoint:toPoint:];
-[_UIAlignmentRegion _maximumDistance];
-[_UIAlignmentRegion _temp];
-[_UIAlignmentRegion encodeWithCoder:];
-[_UIAlignmentRegion description];
-[_UIAlignmentRegion initWithCoder:];
-[_UIAlignmentRegion _dimensions];
-[_UIAlignmentRegion copyWithZone:];
-[_UIAlignmentRegion isEqual:];
-[_UIAlignmentRegion _closestPoint:toPoint:];
-[_UIAlignmentRegion _region];
-[_UIAlignmentRegion _isAlignedForClosestPoint:toPoint:];
-[_UIAlignmentRegion _setRegion:];
```
