# `AVMetadataVideoPreviewHistogramObject`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetadataObject`
- Protocols: `NSCopying`
- 1 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSData" _lumaHistogramData;
```

## Properties

```
@property (T@"NSData",R,V_lumaHistogramData) lumaHistogramData;
@property (TQ,R) lumaHistogramBinCount;
```

## Class methods

```
+[AVMetadataVideoPreviewHistogramObject videoPreviewHistogramObjectWithLumaHistogramData:input:time:];
```

## Instance methods

```
-[AVMetadataVideoPreviewHistogramObject dealloc];
-[AVMetadataVideoPreviewHistogramObject description];
-[AVMetadataVideoPreviewHistogramObject copyWithZone:];
-[AVMetadataVideoPreviewHistogramObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:];
-[AVMetadataVideoPreviewHistogramObject initWithLumaHistogramData:time:sourceCaptureInput:];
-[AVMetadataVideoPreviewHistogramObject lumaHistogramBinCount];
-[AVMetadataVideoPreviewHistogramObject lumaHistogramData];
```
