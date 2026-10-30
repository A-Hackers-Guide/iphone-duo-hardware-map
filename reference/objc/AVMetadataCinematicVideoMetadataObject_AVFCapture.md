# `AVMetadataCinematicVideoMetadataObject`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetadataObject`
- Protocols: `NSCopying`
- 1 instance variables, 1 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"NSData" _payload;
```

## Properties

```
@property (T@"AVTimedMetadataGroup",R,N) timedMetadataGroup;
```

## Class methods

```
+[AVMetadataCinematicVideoMetadataObject cinematicVideoMetadataFormatDescription];
+[AVMetadataCinematicVideoMetadataObject cinematicVideoMetadataObjectWithPayload:input:time:];
```

## Instance methods

```
-[AVMetadataCinematicVideoMetadataObject dealloc];
-[AVMetadataCinematicVideoMetadataObject payload];
-[AVMetadataCinematicVideoMetadataObject description];
-[AVMetadataCinematicVideoMetadataObject copyWithZone:];
-[AVMetadataCinematicVideoMetadataObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:];
-[AVMetadataCinematicVideoMetadataObject initWithPayload:input:time:];
-[AVMetadataCinematicVideoMetadataObject timedMetadataGroup];
```
