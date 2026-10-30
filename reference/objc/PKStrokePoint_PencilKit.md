# `PKStrokePoint`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 13 properties, 27 instance methods, 1 class methods

## Instance variables

```
{PKStrokePathPointsPrivate="constants"{shared_ptr<PKStrokePathPointsShared>="__ptr_"^{PKStrokePathPointsShared}"__cntrl_"^{__shared_weak_count}}"pointsData"{vector<unsigned char, std::allocator<unsigned char>>="__begin_"*"__end_"*""{?="__cap_"*}}} _strokeDataPointsPrivate;
```

## Properties

```
@property (Td,R,N) _edgeWidth;
@property (Td,R,N) _radius2;
@property (Td,R,N) elevation;
@property (T{CGPoint=dd},R,N) location;
@property (Td,R,N) timeOffset;
@property (T{CGSize=dd},R,N) size;
@property (Td,R,N) opacity;
@property (Td,R,N) force;
@property (Td,R,N) azimuth;
@property (Td,R,N) altitude;
@property (Td,R,N) secondaryScale;
@property (Td,R,N) threshold;
@property (Td,R,N) lateralJitter;
```

## Class methods

```
+[PKStrokePoint _sharedConstantData];
```

## Instance methods

```
-[PKStrokePoint location];
-[PKStrokePoint altitude];
-[PKStrokePoint opacity];
-[PKStrokePoint timeOffset];
-[PKStrokePoint threshold];
-[PKStrokePoint size];
-[PKStrokePoint hash];
-[PKStrokePoint description];
-[PKStrokePoint force];
-[PKStrokePoint copyWithZone:];
-[PKStrokePoint isEqual:];
-[PKStrokePoint azimuth];
-[PKStrokePoint elevation];
-[PKStrokePoint _compressedPoint];
-[PKStrokePoint _edgeWidth];
-[PKStrokePoint _radius2];
-[PKStrokePoint _strokeDataPointsPrivate];
-[PKStrokePoint initWithLocation:timeOffset:size:opacity:force:azimuth:altitude:];
-[PKStrokePoint initWithLocation:timeOffset:size:opacity:force:azimuth:altitude:edgeWidth:radius2:];
-[PKStrokePoint initWithLocation:timeOffset:size:opacity:force:azimuth:altitude:edgeWidth:radius2:threshold:];
-[PKStrokePoint initWithLocation:timeOffset:size:opacity:force:azimuth:altitude:secondaryScale:];
-[PKStrokePoint initWithLocation:timeOffset:size:opacity:force:azimuth:altitude:secondaryScale:threshold:];
-[PKStrokePoint initWithLocation:timeOffset:size:opacity:force:azimuth:altitude:secondaryScale:threshold:lateralJitter:];
-[PKStrokePoint initWithLocation:timeOffset:size:opacity:force:azimuth:altitude:secondaryScale:threshold:lateralJitter:elevation:];
-[PKStrokePoint initWithSlice:index:];
-[PKStrokePoint lateralJitter];
-[PKStrokePoint secondaryScale];
```
