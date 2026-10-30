# `AVCaptureReactionEffectState`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSString" _reactionType;
{?="value"q"timescale"i"flags"I"epoch"q} _startTime;
{?="value"q"timescale"i"flags"I"epoch"q} _endTime;
```

## Properties

```
@property (T{?=qiIq},N,V_endTime) endTime;
@property (T@"NSString",R,N,V_reactionType) reactionType;
@property (T{?=qiIq},R,N,V_startTime) startTime;
```

## Instance methods

```
-[AVCaptureReactionEffectState endTime];
-[AVCaptureReactionEffectState setEndTime:];
-[AVCaptureReactionEffectState startTime];
-[AVCaptureReactionEffectState dealloc];
-[AVCaptureReactionEffectState initFromDictionary:];
-[AVCaptureReactionEffectState description];
-[AVCaptureReactionEffectState dictionaryRepresentation];
-[AVCaptureReactionEffectState reactionType];
-[AVCaptureReactionEffectState initWithReactionType:startTime:];
-[AVCaptureReactionEffectState initWithReactionType:startTime:endTime:];
```
