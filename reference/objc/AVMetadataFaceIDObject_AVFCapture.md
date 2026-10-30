# `AVMetadataFaceIDObject`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetadataObject`
- Protocols: `NSCopying`
- 11 instance variables, 11 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"AVMetadataFaceIDFrameProxy" _rawFrameProxy;
@"AVMetadataFaceIDFrameProxy" _metadataFrameProxy;
@"AVMetadataFaceIDFrameProxy" _referenceFrameProxy;
Q _contextIndex;
q _frameType;
q _lightSourceProjectorMode;
B _ready;
q _coachingStatus;
Q _bracketProbePatternType;
@"NSDictionary" _metadata;
q _userEngagementStatus;
```

## Properties

```
@property (T@"AVMetadataFaceIDFrameProxy",R,V_rawFrameProxy) rawFrameProxy;
@property (T@"AVMetadataFaceIDFrameProxy",R,V_metadataFrameProxy) metadataFrameProxy;
@property (T@"AVMetadataFaceIDFrameProxy",R,V_referenceFrameProxy) referenceFrameProxy;
@property (TQ,R,V_contextIndex) contextIndex;
@property (Tq,R,V_frameType) frameType;
@property (Tq,R,V_lightSourceProjectorMode) lightSourceProjectorMode;
@property (TB,R,GisReady,V_ready) ready;
@property (Tq,R,V_coachingStatus) coachingStatus;
@property (TQ,R,V_bracketProbePatternType) bracketProbePatternType;
@property (Tq,R,V_userEngagementStatus) userEngagementStatus;
@property (T@"NSDictionary",R,V_metadata) metadata;
```

## Class methods

```
+[AVMetadataFaceIDObject faceIDObjectWithFaceIDResultDictionary:metadataDictionary:input:time:];
```

## Instance methods

```
-[AVMetadataFaceIDObject isReady];
-[AVMetadataFaceIDObject dealloc];
-[AVMetadataFaceIDObject metadataFrameProxy];
-[AVMetadataFaceIDObject metadata];
-[AVMetadataFaceIDObject description];
-[AVMetadataFaceIDObject rawFrameProxy];
-[AVMetadataFaceIDObject copyWithZone:];
-[AVMetadataFaceIDObject bracketProbePatternType];
-[AVMetadataFaceIDObject coachingStatus];
-[AVMetadataFaceIDObject contextIndex];
-[AVMetadataFaceIDObject frameType];
-[AVMetadataFaceIDObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:];
-[AVMetadataFaceIDObject initWithFaceIDResultDictionary:metadataDictionary:time:sourceCaptureInput:];
-[AVMetadataFaceIDObject lightSourceProjectorMode];
-[AVMetadataFaceIDObject referenceFrameProxy];
-[AVMetadataFaceIDObject userEngagementStatus];
```
