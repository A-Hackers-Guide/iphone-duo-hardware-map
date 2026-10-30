# `UIRegion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSCoding`
- 1 instance variables, 2 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"PKRegion" _region;
```

## Properties

```
@property (T@"UIBezierPath",R,N) path;
@property (T@"PKRegion",R,N) _region;
```

## Class methods

```
+[UIRegion infiniteRegion];
```

## Instance methods

```
-[UIRegion initWithSize:];
-[UIRegion initWithPath:];
-[UIRegion encodeWithCoder:];
-[UIRegion initWithCoder:];
-[UIRegion copyWithZone:];
-[UIRegion containsPoint:];
-[UIRegion path];
-[UIRegion initWithRadius:];
-[UIRegion _region];
-[UIRegion regionByIntersectionWithRegion:];
-[UIRegion containsPoints:locationStride:results:resultsStride:count:];
-[UIRegion inverseRegion];
-[UIRegion regionByDifferenceFromRegion:];
-[UIRegion regionByUnionWithRegion:];
```
