# `AVMetadataHumanHandObject`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetadataObject`
- Protocols: `NSCopying`
- 4 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
B _hasConfidence;
d _confidence;
B _hasChirality;
Q _chirality;
```

## Properties

```
@property (Tq,R) handID;
@property (TB,R,V_hasConfidence) hasConfidence;
@property (Td,R,V_confidence) confidence;
@property (TB,R,V_hasChirality) hasChirality;
@property (TQ,R,V_chirality) chirality;
```

## Class methods

```
+[AVMetadataHumanHandObject humanHandObjectWithFigEmbeddedCaptureDeviceObjectDictionary:input:timeStamp:];
```

## Instance methods

```
-[AVMetadataHumanHandObject dealloc];
-[AVMetadataHumanHandObject hasConfidence];
-[AVMetadataHumanHandObject description];
-[AVMetadataHumanHandObject copyWithZone:];
-[AVMetadataHumanHandObject confidence];
-[AVMetadataHumanHandObject chirality];
-[AVMetadataHumanHandObject handID];
-[AVMetadataHumanHandObject hasChirality];
-[AVMetadataHumanHandObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:];
-[AVMetadataHumanHandObject initWithFigEmbeddedCaptureDeviceObjectDictionary:input:timeStamp:type:];
-[AVMetadataHumanHandObject initWithType:time:duration:bounds:optionalInfoDict:originalMetadataObject:sourceCaptureInput:];
```
