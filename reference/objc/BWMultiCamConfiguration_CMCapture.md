# `BWMultiCamConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 0 properties, 4 instance methods, 3 class methods

## Instance variables

```
@"NSArray" _portTypesPrioritizedForCameraControls;
@"NSArray" _unsynchronizedActiveStreamsPortTypes;
@"NSArray" _synchronizedActiveStreamsGroupsPortTypes;
@"NSArray" _mutuallyExclusiveUnsynchronizedStreamsPortTypes;
B _stereoVideoCaptureEnabled;
B _multiCamClientCompositingEnabled;
B _colorAssistedSecureFaceIDEnabled;
B _secureProcessingCoexEnabled;
B _builtInMicrophoneIsRecording;
B _exclusivelyForSecureProcessing;
```

## Class methods

```
+[BWMultiCamConfiguration initialize];
+[BWMultiCamConfiguration configurationWithCurrentStateFromCaptureDevice:];
+[BWMultiCamConfiguration configurationWithUnsynchronizedActiveStreamsPortTypes:synchronizedActiveStreamsGroupsPortTypes:mutuallyExclusiveUnsynchronizedStreamsPortTypes:stereoVideoCaptureEnabled:multiCamClientCompositingEnabled:colorAssistedSecureFaceIDEnabled:secureProcessingCoexEnabled:exclusivelyForSecureProcessing:builtInMicrophoneIsRecording:];
```

## Instance methods

```
-[BWMultiCamConfiguration dealloc];
-[BWMultiCamConfiguration isEqual:];
-[BWMultiCamConfiguration copyActiveSynchronizedStreamsGroupsForDevice:errorOut:];
-[BWMultiCamConfiguration multiCamConfigurationForDevice:errorOut:];
```
