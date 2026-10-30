# `BWDetectedFacesRingBuffer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWFaceDetector`
- 6 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _ringBuffer;
^{OpaqueFigSimpleMutex=} _mutex;
i _depth;
i _numConsecutiveFramesWithFaces;
{?="value"q"timescale"i"flags"I"epoch"q} _lastUpdatePTS;
{?="value"q"timescale"i"flags"I"epoch"q} _lastStableFacePTS;
```

## Properties

```
@property (T@"<BWFaceDetector>",R) faceDetector;
@property (Tf,R) secondsSinceLastFaceDetected;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWDetectedFacesRingBuffer faceDetector];
-[BWDetectedFacesRingBuffer flush];
-[BWDetectedFacesRingBuffer dealloc];
-[BWDetectedFacesRingBuffer initWithDepth:];
-[BWDetectedFacesRingBuffer addFacesFromSampleBuffer:];
-[BWDetectedFacesRingBuffer secondsSinceLastFaceDetected];
-[BWDetectedFacesRingBuffer transferFacesToSampleBuffer:transformToBufferSpace:sourceCropRect:];
```
