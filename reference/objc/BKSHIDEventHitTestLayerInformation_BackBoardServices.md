# `BKSHIDEventHitTestLayerInformation`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`, `BSProtobufSerializable`, `NSCopying`, `NSMutableCopying`
- 9 instance variables, 16 properties, 21 instance methods, 3 class methods

## Instance variables

```
Q _validMask;
f _cumulativeOpacity;
f _backgroundAverage;
f _backgroundStandardDeviation;
f _backgroundAverageContrastThreshold;
{CATransform3D="m11"d"m12"d"m13"d"m14"d"m21"d"m22"d"m23"d"m24"d"m31"d"m32"d"m33"d"m34"d"m41"d"m42"d"m43"d"m44"d} _cumulativeLayerTransform;
{CATransform3D="m11"d"m12"d"m13"d"m14"d"m21"d"m22"d"m23"d"m24"d"m31"d"m32"d"m33"d"m34"d"m41"d"m42"d"m43"d"m44"d} _cumulativeContentsTransform;
B _hasInsecureFilter;
B _detectedOcclusion;
```

## Properties

```
@property (TQ,R,N) validMask;
@property (T{CATransform3D=dddddddddddddddd},R,N) cumulativeLayerTransform;
@property (T{CATransform3D=dddddddddddddddd},R,N) cumulativeContentsTransform;
@property (Tf,R,N) cumulativeOpacity;
@property (Tf,R,N) backgroundAverage;
@property (Tf,R,N) backgroundStandardDeviation;
@property (Tf,R,N) backgroundAverageContrastThreshold;
@property (TB,R,N) hasInsecureFilter;
@property (TB,R,N) detectedOcclusion;
@property (T@"NSArray",R,C,N) minimumBackgroundColor;
@property (T@"NSArray",R,C,N) maximumBackgroundColor;
@property (T{CATransform3D=dddddddddddddddd},R,N) cumulativeTransform;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventHitTestLayerInformation build:];
+[BKSHIDEventHitTestLayerInformation protobufSchema];
+[BKSHIDEventHitTestLayerInformation new];
```

## Instance methods

```
-[BKSHIDEventHitTestLayerInformation maximumBackgroundColor];
-[BKSHIDEventHitTestLayerInformation mutableCopyWithZone:];
-[BKSHIDEventHitTestLayerInformation initForProtobufDecoding];
-[BKSHIDEventHitTestLayerInformation detectedOcclusion];
-[BKSHIDEventHitTestLayerInformation validMask];
-[BKSHIDEventHitTestLayerInformation init];
-[BKSHIDEventHitTestLayerInformation backgroundAverage];
-[BKSHIDEventHitTestLayerInformation appendDescriptionToFormatter:];
-[BKSHIDEventHitTestLayerInformation _updateCCHmacContext:];
-[BKSHIDEventHitTestLayerInformation cumulativeOpacity];
-[BKSHIDEventHitTestLayerInformation minimumBackgroundColor];
-[BKSHIDEventHitTestLayerInformation backgroundAverageContrastThreshold];
-[BKSHIDEventHitTestLayerInformation hash];
-[BKSHIDEventHitTestLayerInformation cumulativeTransform];
-[BKSHIDEventHitTestLayerInformation hasInsecureFilter];
-[BKSHIDEventHitTestLayerInformation description];
-[BKSHIDEventHitTestLayerInformation backgroundStandardDeviation];
-[BKSHIDEventHitTestLayerInformation cumulativeContentsTransform];
-[BKSHIDEventHitTestLayerInformation copyWithZone:];
-[BKSHIDEventHitTestLayerInformation isEqual:];
-[BKSHIDEventHitTestLayerInformation cumulativeLayerTransform];
```
