# `AVMetadataCatHeadObject`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetadataObject`
- Protocols: `NSCopying`
- 1 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
q _objectID;
```

## Class methods

```
+[AVMetadataCatHeadObject catHeadObjectWithFigEmbeddedCaptureDeviceObjectDictionary:input:timeStamp:];
```

## Instance methods

```
-[AVMetadataCatHeadObject objectID];
-[AVMetadataCatHeadObject description];
-[AVMetadataCatHeadObject copyWithZone:];
-[AVMetadataCatHeadObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:];
-[AVMetadataCatHeadObject initWithFigEmbeddedCaptureDeviceObjectDictionary:input:timeStamp:type:];
-[AVMetadataCatHeadObject initWithObjectID:time:duration:bounds:];
-[AVMetadataCatHeadObject initWithObjectID:time:duration:bounds:optionalInfoDict:originalMetadataObject:sourceCaptureInput:];
```
