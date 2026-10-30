# `BWDeviceMotionActivityDetector`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"BWMotionSampleRingBuffer" _motionDataRingBuffer;
^{OpaqueFigSimpleMutex=} _ringMutex;
B _stationary;
B _newMotionDataAvailable;
B _robustMethodEnabled;
B _motionMetadataStatusChecked;
B _directionalMotionDetectionEnabled;
d _directionalMotionDetectionAngularRotationThreshold;
{?="doingBiasEstimation"B"timestamp"d"quaternion"{?="w"d"x"d"y"d"z"d}} _directionalMotionDetectionReferenceDirection;
```

## Properties

```
@property (TB,R,N,GisStationary) stationary;
@property (TB,GisDirectionalMotionDetectionEnabled) directionalMotionDetectionEnabled;
```

## Class methods

```
+[BWDeviceMotionActivityDetector initialize];
```

## Instance methods

```
-[BWDeviceMotionActivityDetector init];
-[BWDeviceMotionActivityDetector dealloc];
-[BWDeviceMotionActivityDetector isStationary];
-[BWDeviceMotionActivityDetector isDirectionalMotionDetectionEnabled];
-[BWDeviceMotionActivityDetector processSampleBuffer:];
-[BWDeviceMotionActivityDetector setDirectionalMotionDetectionEnabled:];
```
