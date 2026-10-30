# `AVCaptureFaceIDConfiguration`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 6 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
q _mode;
B _frameMetadataEnabled;
B _frameLogEnabled;
B _periocularEnabled;
B _attentionRequired;
q _retryType;
```

## Properties

```
@property (Tq,N,V_mode) mode;
@property (TB,N,GisFrameMetadataEnabled,V_frameMetadataEnabled) frameMetadataEnabled;
@property (TB,N,GisFrameLogEnabled,V_frameLogEnabled) frameLogEnabled;
@property (TB,N,GisPeriocularEnabled,V_periocularEnabled) periocularEnabled;
@property (TB,N,GisAttentionRequired,V_attentionRequired) attentionRequired;
@property (Tq,N,V_retryType) retryType;
```

## Instance methods

```
-[AVCaptureFaceIDConfiguration setMode:];
-[AVCaptureFaceIDConfiguration mode];
-[AVCaptureFaceIDConfiguration copyWithZone:];
-[AVCaptureFaceIDConfiguration isEqual:];
-[AVCaptureFaceIDConfiguration faceIDConfigurationDictionary];
-[AVCaptureFaceIDConfiguration isAttentionRequired];
-[AVCaptureFaceIDConfiguration isFrameLogEnabled];
-[AVCaptureFaceIDConfiguration isFrameMetadataEnabled];
-[AVCaptureFaceIDConfiguration isPeriocularEnabled];
-[AVCaptureFaceIDConfiguration retryType];
-[AVCaptureFaceIDConfiguration setAttentionRequired:];
-[AVCaptureFaceIDConfiguration setFrameLogEnabled:];
-[AVCaptureFaceIDConfiguration setFrameMetadataEnabled:];
-[AVCaptureFaceIDConfiguration setPeriocularEnabled:];
-[AVCaptureFaceIDConfiguration setRetryType:];
```
