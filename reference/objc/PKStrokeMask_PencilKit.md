# `PKStrokeMask`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 13 instance methods, 0 class methods

## Instance variables

```
{vector<std::vector<ClipperLib::IntPoint>, std::allocator<std::vector<ClipperLib::IntPoint>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} _maskPaths;
{vector<_PKFloatRange, std::allocator<_PKFloatRange>>="__begin_"^{?}"__end_"^{?}""{?="__cap_"^{?}}} _centerlineSlices;
```

## Properties

```
@property (T@"NSData",R,N) rawValue;
```

## Instance methods

```
-[PKStrokeMask rawValue];
-[PKStrokeMask initWithArchive:];
-[PKStrokeMask saveToArchive:];
-[PKStrokeMask initWithRawValue:];
-[PKStrokeMask bezierPath];
-[PKStrokeMask _transformBy:];
-[PKStrokeMask _boundsWithTransform:];
-[PKStrokeMask calculateCenterlineSlices:];
-[PKStrokeMask centerlineSlices];
-[PKStrokeMask initWithBezierPath:stroke:];
-[PKStrokeMask initWithMaskPaths:centerlineSlices:];
-[PKStrokeMask maskPaths];
-[PKStrokeMask maskTransformedBy:];
```
