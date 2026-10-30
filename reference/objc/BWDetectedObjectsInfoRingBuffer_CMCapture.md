# `BWDetectedObjectsInfoRingBuffer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWObjectDetector`
- 6 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _ringBuffer;
^{OpaqueFigSimpleMutex=} _mutex;
i _depth;
i _numConsecutiveFramesWithObjects;
{?="value"q"timescale"i"flags"I"epoch"q} _lastUpdatePTS;
{?="value"q"timescale"i"flags"I"epoch"q} _lastStableObjectPTS;
```

## Properties

```
@property (T@"<BWObjectDetector>",R) objectDetector;
@property (Tf,R) secondsSinceLastObjectDetected;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWDetectedObjectsInfoRingBuffer flush];
-[BWDetectedObjectsInfoRingBuffer dealloc];
-[BWDetectedObjectsInfoRingBuffer objectDetector];
-[BWDetectedObjectsInfoRingBuffer addObjectsFromSampleBuffer:];
-[BWDetectedObjectsInfoRingBuffer initWithRingBufferDepth:];
-[BWDetectedObjectsInfoRingBuffer objectsForPTS:];
-[BWDetectedObjectsInfoRingBuffer secondsSinceLastObjectDetected];
-[BWDetectedObjectsInfoRingBuffer transferObjectsToSampleBuffer:transformToBufferSpace:sourceCropRect:];
```
