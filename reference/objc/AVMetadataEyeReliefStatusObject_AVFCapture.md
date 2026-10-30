# `AVMetadataEyeReliefStatusObject`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetadataObject`
- Protocols: `NSCopying`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
Q _eyeReliefStatus;
d _distance;
B _hasDistance;
```

## Properties

```
@property (TQ,R) eyeReliefStatus;
@property (TB,R) hasDistance;
@property (Td,R) distance;
```

## Class methods

```
+[AVMetadataEyeReliefStatusObject eyeReliefStatusObjectWithEyeReliefStatus:input:time:optionalInfoDict:];
```

## Instance methods

```
-[AVMetadataEyeReliefStatusObject distance];
-[AVMetadataEyeReliefStatusObject description];
-[AVMetadataEyeReliefStatusObject hasDistance];
-[AVMetadataEyeReliefStatusObject copyWithZone:];
-[AVMetadataEyeReliefStatusObject eyeReliefStatus];
-[AVMetadataEyeReliefStatusObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:];
-[AVMetadataEyeReliefStatusObject initWithEyeReliefStatus:time:sourceCaptureInput:optionalInfoDict:];
```
