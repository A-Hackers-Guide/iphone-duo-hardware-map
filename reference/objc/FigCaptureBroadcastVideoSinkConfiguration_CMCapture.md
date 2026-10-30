# `FigCaptureBroadcastVideoSinkConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureSinkConfiguration`
- 3 instance variables, 3 properties, 13 instance methods, 0 class methods

## Instance variables

```
q _maxBufferedFrameCount;
Q _testPatternToInject;
Q _droppedFrameReplacementPolicy;
```

## Properties

```
@property (Tq,N,V_maxBufferedFrameCount) maxBufferedFrameCount;
@property (TQ,N,V_testPatternToInject) testPatternToInject;
@property (TQ,N,V_droppedFrameReplacementPolicy) droppedFrameReplacementPolicy;
```

## Instance methods

```
-[FigCaptureBroadcastVideoSinkConfiguration sinkType];
-[FigCaptureBroadcastVideoSinkConfiguration reasonForNotEqualingConfiguration:];
-[FigCaptureBroadcastVideoSinkConfiguration copyXPCEncoding];
-[FigCaptureBroadcastVideoSinkConfiguration description];
-[FigCaptureBroadcastVideoSinkConfiguration initWithXPCEncoding:];
-[FigCaptureBroadcastVideoSinkConfiguration copyWithZone:];
-[FigCaptureBroadcastVideoSinkConfiguration isEqual:];
-[FigCaptureBroadcastVideoSinkConfiguration droppedFrameReplacementPolicy];
-[FigCaptureBroadcastVideoSinkConfiguration maxBufferedFrameCount];
-[FigCaptureBroadcastVideoSinkConfiguration setDroppedFrameReplacementPolicy:];
-[FigCaptureBroadcastVideoSinkConfiguration setMaxBufferedFrameCount:];
-[FigCaptureBroadcastVideoSinkConfiguration setTestPatternToInject:];
-[FigCaptureBroadcastVideoSinkConfiguration testPatternToInject];
```
