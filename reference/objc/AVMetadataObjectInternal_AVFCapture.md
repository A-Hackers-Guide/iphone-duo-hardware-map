# `AVMetadataObjectInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 14 properties, 30 instance methods, 0 class methods

## Instance variables

```
{?="value"q"timescale"i"flags"I"epoch"q} _time;
{?="value"q"timescale"i"flags"I"epoch"q} _duration;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _bounds;
^{__CVBuffer=} _mask;
@"NSString" _type;
@"AVCaptureInput" _input;
B _sentToPerceptionThumbnailChannel;
@"AVMetadataObject" _originalMetadataObject;
q _groupID;
q _objectID;
Q _syntheticFocusMode;
q _detectionSource;
q _cinematicVideoFocusMode;
B _fixedFocus;
```

## Properties

```
@property (T{?=qiIq},V_time) time;
@property (T{?=qiIq},V_duration) duration;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},V_bounds) bounds;
@property (T^{__CVBuffer=},&,V_mask) mask;
@property (T@"NSString",&,V_type) type;
@property (T@"AVCaptureInput",&,V_input) input;
@property (TB,V_sentToPerceptionThumbnailChannel) sentToPerceptionThumbnailChannel;
@property (T@"AVMetadataObject",&,V_originalMetadataObject) originalMetadataObject;
@property (Tq,V_groupID) groupID;
@property (Tq,V_objectID) objectID;
@property (TQ,V_syntheticFocusMode) syntheticFocusMode;
@property (Tq,V_detectionSource) detectionSource;
@property (Tq,V_cinematicVideoFocusMode) cinematicVideoFocusMode;
@property (TB,GisFixedFocus,V_fixedFocus) fixedFocus;
```

## Instance methods

```
-[AVMetadataObjectInternal setGroupID:];
-[AVMetadataObjectInternal groupID];
-[AVMetadataObjectInternal setObjectID:];
-[AVMetadataObjectInternal input];
-[AVMetadataObjectInternal init];
-[AVMetadataObjectInternal setCinematicVideoFocusMode:];
-[AVMetadataObjectInternal setSentToPerceptionThumbnailChannel:];
-[AVMetadataObjectInternal setInput:];
-[AVMetadataObjectInternal setDetectionSource:];
-[AVMetadataObjectInternal detectionSource];
-[AVMetadataObjectInternal syntheticFocusMode];
-[AVMetadataObjectInternal dealloc];
-[AVMetadataObjectInternal mask];
-[AVMetadataObjectInternal setMask:];
-[AVMetadataObjectInternal setBounds:];
-[AVMetadataObjectInternal duration];
-[AVMetadataObjectInternal objectID];
-[AVMetadataObjectInternal cinematicVideoFocusMode];
-[AVMetadataObjectInternal setType:];
-[AVMetadataObjectInternal type];
-[AVMetadataObjectInternal originalMetadataObject];
-[AVMetadataObjectInternal setFixedFocus:];
-[AVMetadataObjectInternal bounds];
-[AVMetadataObjectInternal setSyntheticFocusMode:];
-[AVMetadataObjectInternal isFixedFocus];
-[AVMetadataObjectInternal setTime:];
-[AVMetadataObjectInternal setDuration:];
-[AVMetadataObjectInternal sentToPerceptionThumbnailChannel];
-[AVMetadataObjectInternal setOriginalMetadataObject:];
-[AVMetadataObjectInternal time];
```
