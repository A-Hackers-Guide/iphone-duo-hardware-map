# `AVMetadataSaliencyHeatMap`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetadataObject`
- Protocols: `NSCopying`
- 4 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
q _bytesPerRow;
q _width;
q _height;
@"NSData" _heatMap;
```

## Properties

```
@property (Tq,R,V_bytesPerRow) bytesPerRow;
@property (Tq,R,V_width) width;
@property (Tq,R,V_height) height;
@property (T@"NSData",R,V_heatMap) heatMap;
```

## Class methods

```
+[AVMetadataSaliencyHeatMap saliencyHeatMapWithFigEmbeddedCaptureDeviceObjectDictionary:input:timeStamp:];
```

## Instance methods

```
-[AVMetadataSaliencyHeatMap bytesPerRow];
-[AVMetadataSaliencyHeatMap dealloc];
-[AVMetadataSaliencyHeatMap width];
-[AVMetadataSaliencyHeatMap copyWithZone:];
-[AVMetadataSaliencyHeatMap height];
-[AVMetadataSaliencyHeatMap heatMap];
-[AVMetadataSaliencyHeatMap initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:];
-[AVMetadataSaliencyHeatMap initWithFigEmbeddedCaptureDeviceObjectDictionary:input:timeStamp:type:];
-[AVMetadataSaliencyHeatMap initWithHeatMap:width:height:bytesPerRow:time:duration:bounds:optionalInfoDict:originalMetadataObject:sourceCaptureInput:];
```
