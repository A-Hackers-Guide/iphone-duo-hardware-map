# `AVMetadataFaceObject`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetadataObject`
- Protocols: `NSCopying`
- 1 instance variables, 5 properties, 52 instance methods, 1 class methods

## Instance variables

```
@"AVMetadataFaceObjectInternal" _internal;
```

## Properties

```
@property (Tq,R) faceID;
@property (TB,R) hasRollAngle;
@property (Td,R) rollAngle;
@property (TB,R) hasYawAngle;
@property (Td,R) yawAngle;
```

## Class methods

```
+[AVMetadataFaceObject faceObjectWithFigEmbeddedCaptureDeviceFaceDictionary:input:timeStamp:];
```

## Instance methods

```
-[AVMetadataFaceObject hasRightEyeClosedConfidence];
-[AVMetadataFaceObject distance];
-[AVMetadataFaceObject rightEyeBounds];
-[AVMetadataFaceObject hasMaskConfidence];
-[AVMetadataFaceObject occludedFeatures];
-[AVMetadataFaceObject hasPayingAttention];
-[AVMetadataFaceObject hasYawAngle];
-[AVMetadataFaceObject eyesClosedConfidence];
-[AVMetadataFaceObject pitchAngle];
-[AVMetadataFaceObject orientation];
-[AVMetadataFaceObject dealloc];
-[AVMetadataFaceObject hasLookingAtCameraConfidence];
-[AVMetadataFaceObject metadataFrameProxy];
-[AVMetadataFaceObject hasOrientation];
-[AVMetadataFaceObject eyesOpenConfidence];
-[AVMetadataFaceObject hasRightEyeBounds];
-[AVMetadataFaceObject lookingAtCameraConfidence];
-[AVMetadataFaceObject hasLeftEyeBounds];
-[AVMetadataFaceObject maskConfidence];
-[AVMetadataFaceObject hasConfidence];
-[AVMetadataFaceObject hasSmileConfidence];
-[AVMetadataFaceObject leftEyeClosedConfidence];
-[AVMetadataFaceObject hasEyesOccludedConfidence];
-[AVMetadataFaceObject payingAttention];
-[AVMetadataFaceObject rollAngle];
-[AVMetadataFaceObject hasEyesClosedConfidence];
-[AVMetadataFaceObject description];
-[AVMetadataFaceObject faceID];
-[AVMetadataFaceObject hasDistance];
-[AVMetadataFaceObject hasOccludedFeatures];
-[AVMetadataFaceObject rawFrameProxy];
-[AVMetadataFaceObject eyesOccludedConfidence];
-[AVMetadataFaceObject smileConfidence];
-[AVMetadataFaceObject rightEyeClosedConfidence];
-[AVMetadataFaceObject copyWithZone:];
-[AVMetadataFaceObject hasLeftEyeClosedConfidence];
-[AVMetadataFaceObject isEqual:];
-[AVMetadataFaceObject hasEyesOpenConfidence];
-[AVMetadataFaceObject hasRollAngle];
-[AVMetadataFaceObject yawAngle];
-[AVMetadataFaceObject confidence];
-[AVMetadataFaceObject hasEyeWearConfidence];
-[AVMetadataFaceObject hasPitchAngle];
-[AVMetadataFaceObject leftEyeBounds];
-[AVMetadataFaceObject eyeWearConfidence];
-[AVMetadataFaceObject initWithFigEmbeddedCaptureDeviceFaceDictionary:input:timeStamp:];
-[AVMetadataFaceObject hasPayingAttentionConfidence];
-[AVMetadataFaceObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:];
-[AVMetadataFaceObject initWithFaceID:hasRollAngle:rollAngle:hasYawAngle:yawAngle:hasPitchAngle:pitchAngle:time:duration:bounds:];
-[AVMetadataFaceObject initWithFaceID:hasRollAngle:rollAngle:hasYawAngle:yawAngle:hasPitchAngle:pitchAngle:time:duration:bounds:optionalInfoDict:originalMetadataObject:sourceCaptureInput:];
-[AVMetadataFaceObject initWithType:time:duration:bounds:optionalInfoDict:originalMetadataObject:sourceCaptureInput:];
-[AVMetadataFaceObject payingAttentionConfidence];
```
