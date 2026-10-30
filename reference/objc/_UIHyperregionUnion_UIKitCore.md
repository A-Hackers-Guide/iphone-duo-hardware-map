# `_UIHyperregionUnion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIHyperregion_Internal`, `_UIHyperregion`, `NSSecureCoding`, `NSCopying`
- 3 instance variables, 7 properties, 15 instance methods, 2 class methods

## Instance variables

```
Q __dimensions;
@"NSArray" __regions;
^d __temp;
```

## Properties

```
@property (T^d,R,N,V__temp) _temp;
@property (T@"NSArray",C,N,S_setRegions:,V__regions) _regions;
@property (TQ,R,N,V__dimensions) _dimensions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIHyperregionUnion supportsSecureCoding];
+[_UIHyperregionUnion keyPathsForValuesAffectingSelf];
```

## Instance methods

```
-[_UIHyperregionUnion observeValueForKeyPath:ofObject:change:context:];
-[_UIHyperregionUnion initWithDimensions:];
-[_UIHyperregionUnion _setRegions:];
-[_UIHyperregionUnion dealloc];
-[_UIHyperregionUnion _regionIndexForClosestPoint:toPoint:];
-[_UIHyperregionUnion _isBoundaryCrossedFromPoint:toPoint:];
-[_UIHyperregionUnion _regions];
-[_UIHyperregionUnion _temp];
-[_UIHyperregionUnion encodeWithCoder:];
-[_UIHyperregionUnion description];
-[_UIHyperregionUnion initWithCoder:];
-[_UIHyperregionUnion _dimensions];
-[_UIHyperregionUnion copyWithZone:];
-[_UIHyperregionUnion isEqual:];
-[_UIHyperregionUnion _closestPoint:toPoint:];
```
