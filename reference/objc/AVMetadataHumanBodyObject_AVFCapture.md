# `AVMetadataHumanBodyObject`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetadataBodyObject`
- Protocols: `NSCopying`
- 2 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
B _hasConfidence;
d _confidence;
```

## Class methods

```
+[AVMetadataHumanBodyObject humanBodyObjectWithFigEmbeddedCaptureDeviceObjectDictionary:input:timeStamp:];
```

## Instance methods

```
-[AVMetadataHumanBodyObject hasConfidence];
-[AVMetadataHumanBodyObject description];
-[AVMetadataHumanBodyObject copyWithZone:];
-[AVMetadataHumanBodyObject confidence];
-[AVMetadataHumanBodyObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:];
-[AVMetadataHumanBodyObject initWithBodyID:time:duration:bounds:];
-[AVMetadataHumanBodyObject initWithBodyID:time:duration:bounds:optionalInfoDict:originalMetadataObject:sourceCaptureInput:];
-[AVMetadataHumanBodyObject initWithFigEmbeddedCaptureDeviceObjectDictionary:input:timeStamp:];
```
