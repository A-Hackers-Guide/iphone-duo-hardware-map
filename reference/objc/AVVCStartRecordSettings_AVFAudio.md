# `AVVCStartRecordSettings`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _skipAlert;
I _startAnchorPoint;
Q _streamID;
Q _startHostTime;
q _startAlert;
q _stopAlert;
q _stopOnErrorAlert;
```

## Properties

```
@property (TQ,N,V_streamID) streamID;
@property (TQ,N,V_startHostTime) startHostTime;
@property (Tq,N,V_startAlert) startAlert;
@property (Tq,N,V_stopAlert) stopAlert;
@property (Tq,N,V_stopOnErrorAlert) stopOnErrorAlert;
@property (TB,N,V_skipAlert) skipAlert;
@property (TI,N,V_startAnchorPoint) startAnchorPoint;
```

## Instance methods

```
-[AVVCStartRecordSettings streamID];
-[AVVCStartRecordSettings initWithStreamID:atStartHostTime:];
-[AVVCStartRecordSettings setStartAlert:];
-[AVVCStartRecordSettings setStreamID:];
-[AVVCStartRecordSettings setSkipAlert:];
-[AVVCStartRecordSettings setStartAnchorPoint:];
-[AVVCStartRecordSettings setStartHostTime:];
-[AVVCStartRecordSettings setStopAlert:];
-[AVVCStartRecordSettings setStopOnErrorAlert:];
-[AVVCStartRecordSettings skipAlert];
-[AVVCStartRecordSettings startAlert];
-[AVVCStartRecordSettings startAnchorPoint];
-[AVVCStartRecordSettings startHostTime];
-[AVVCStartRecordSettings stopAlert];
-[AVVCStartRecordSettings stopOnErrorAlert];
```
