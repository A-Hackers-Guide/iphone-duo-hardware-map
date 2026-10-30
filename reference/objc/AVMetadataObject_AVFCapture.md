# `AVMetadataObject`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 6 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"AVMetadataObjectInternal" _objectInternal;
```

## Properties

```
@property (T{?=qiIq},R) time;
@property (T{?=qiIq},R) duration;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R) bounds;
@property (T@"NSString",R) type;
@property (Tq,R) groupID;
@property (Tq,R) objectID;
```

## Class methods

```
+[AVMetadataObject derivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:];
```

## Instance methods

```
-[AVMetadataObject groupID];
-[AVMetadataObject input];
-[AVMetadataObject init];
-[AVMetadataObject setDetectionSource:];
-[AVMetadataObject detectionSource];
-[AVMetadataObject syntheticFocusMode];
-[AVMetadataObject dealloc];
-[AVMetadataObject mask];
-[AVMetadataObject duration];
-[AVMetadataObject objectID];
-[AVMetadataObject cinematicVideoFocusMode];
-[AVMetadataObject type];
-[AVMetadataObject originalMetadataObject];
-[AVMetadataObject bounds];
-[AVMetadataObject isFixedFocus];
-[AVMetadataObject isEqual:];
-[AVMetadataObject sentToPerceptionThumbnailChannel];
-[AVMetadataObject time];
-[AVMetadataObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:];
-[AVMetadataObject initWithType:time:duration:bounds:optionalInfoDict:originalMetadataObject:sourceCaptureInput:];
```
