# `AVMetadataSceneClassificationObject`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetadataObject`
- Protocols: `NSCopying`
- 1 instance variables, 14 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _confidences;
```

## Properties

```
@property (T@"NSDictionary",R,V_confidences) confidences;
@property (Tf,R) appCodeSceneConfidence;
@property (Tf,R) otherCodeSceneConfidence;
@property (Tf,R) qrSceneConfidence;
@property (Tf,R) brightStageSceneConfidence;
@property (Tf,R) documentSceneConfidence;
@property (Tf,R) foodSceneConfidence;
@property (Tf,R) indoorSceneConfidence;
@property (Tf,R) outdoorSceneConfidence;
@property (Tf,R) lynxGiftCardSceneConfidence;
@property (Tf,R) standardGiftCardSceneConfidence;
@property (Tf,R) sunsetSceneConfidence;
@property (Tf,R) textSceneConfidence;
@property (Tf,R) waterBodySceneConfidence;
```

## Class methods

```
+[AVMetadataSceneClassificationObject sceneClassificationObjectWithConfidences:input:time:];
```

## Instance methods

```
-[AVMetadataSceneClassificationObject dealloc];
-[AVMetadataSceneClassificationObject documentSceneConfidence];
-[AVMetadataSceneClassificationObject description];
-[AVMetadataSceneClassificationObject copyWithZone:];
-[AVMetadataSceneClassificationObject standardGiftCardSceneConfidence];
-[AVMetadataSceneClassificationObject _confidenceForKey:];
-[AVMetadataSceneClassificationObject appCodeSceneConfidence];
-[AVMetadataSceneClassificationObject brightStageSceneConfidence];
-[AVMetadataSceneClassificationObject confidences];
-[AVMetadataSceneClassificationObject foodSceneConfidence];
-[AVMetadataSceneClassificationObject indoorSceneConfidence];
-[AVMetadataSceneClassificationObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:];
-[AVMetadataSceneClassificationObject initSceneClassificationObjectWithConfidences:time:sourceCaptureInput:];
-[AVMetadataSceneClassificationObject lynxGiftCardSceneConfidence];
-[AVMetadataSceneClassificationObject otherCodeSceneConfidence];
-[AVMetadataSceneClassificationObject outdoorSceneConfidence];
-[AVMetadataSceneClassificationObject qrSceneConfidence];
-[AVMetadataSceneClassificationObject sunsetSceneConfidence];
-[AVMetadataSceneClassificationObject textSceneConfidence];
-[AVMetadataSceneClassificationObject waterBodySceneConfidence];
```
