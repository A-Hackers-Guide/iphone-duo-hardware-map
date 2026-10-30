# `BWVideoOrientationMetadataNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 16 instance variables, 1 properties, 20 instance methods, 1 class methods

## Instance variables

```
^{OpaqueCMClock=} _clock;
^{OpaqueCMClock=} _masterClock;
i _rotationDegrees;
B _videoMirrored;
i _sourcePosition;
i _sourceDeviceType;
^{opaqueCMFormatDescription=} _boxedMetadataFormatDescription;
I _localIDOfOrientationMetadata;
B _recordVideoOrientationAndMirroringChanges;
B _physicalMirroringForMovieRecordingEnabled;
B _flipMetadataHorizontally;
B _recording;
i _exifOrientation;
[8^{OpaqueCMBlockBuffer}] _bbufCache;
@"BWVideoOrientationTimeMachine" _videoOrientationTimeMachine;
@"NSObject<OS_dispatch_queue>" _emitSamplesDispatchQueue;
```

## Properties

```
@property (T@"BWVideoOrientationTimeMachine",R,N) videoOrientationTimeMachine;
```

## Class methods

```
+[BWVideoOrientationMetadataNode initialize];
```

## Instance methods

```
-[BWVideoOrientationMetadataNode videoOrientationTimeMachine];
-[BWVideoOrientationMetadataNode prepareForCurrentConfigurationToBecomeLive];
-[BWVideoOrientationMetadataNode sourcePosition];
-[BWVideoOrientationMetadataNode setMasterClock:];
-[BWVideoOrientationMetadataNode renderSampleBuffer:forInput:];
-[BWVideoOrientationMetadataNode init];
-[BWVideoOrientationMetadataNode setSourcePosition:];
-[BWVideoOrientationMetadataNode dealloc];
-[BWVideoOrientationMetadataNode hasNonLiveConfigurationChanges];
-[BWVideoOrientationMetadataNode masterClock];
-[BWVideoOrientationMetadataNode setPhysicalMirroringForMovieRecordingEnabled:];
-[BWVideoOrientationMetadataNode sourceDeviceType];
-[BWVideoOrientationMetadataNode physicalMirroringForMovieRecordingEnabled];
-[BWVideoOrientationMetadataNode setSourceDeviceType:];
-[BWVideoOrientationMetadataNode didReachEndOfDataForConfigurationID:input:];
-[BWVideoOrientationMetadataNode updateVideoMirrored:];
-[BWVideoOrientationMetadataNode updateRotationDegrees:];
-[BWVideoOrientationMetadataNode nodeSubType];
-[BWVideoOrientationMetadataNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWVideoOrientationMetadataNode nodeType];
```
