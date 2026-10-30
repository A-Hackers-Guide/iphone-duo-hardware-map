# `_UIPackedRegion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIHyperregion_Internal`, `NSSecureCoding`, `NSCopying`
- 2 instance variables, 6 properties, 13 instance methods, 2 class methods

## Instance variables

```
Q __dimensions;
@"NSArray" __regions;
```

## Properties

```
@property (T@"NSArray",C,N,S_setRegions:,V__regions) _regions;
@property (TQ,R,N,V__dimensions) _dimensions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIPackedRegion supportsSecureCoding];
+[_UIPackedRegion keyPathsForValuesAffectingSelf];
```

## Instance methods

```
-[_UIPackedRegion observeValueForKeyPath:ofObject:change:context:];
-[_UIPackedRegion initWithDimensions:];
-[_UIPackedRegion _setRegions:];
-[_UIPackedRegion dealloc];
-[_UIPackedRegion _isBoundaryCrossedFromPoint:toPoint:];
-[_UIPackedRegion _regions];
-[_UIPackedRegion encodeWithCoder:];
-[_UIPackedRegion description];
-[_UIPackedRegion initWithCoder:];
-[_UIPackedRegion _dimensions];
-[_UIPackedRegion copyWithZone:];
-[_UIPackedRegion isEqual:];
-[_UIPackedRegion _closestPoint:toPoint:];
```
