# `BWFigVideoCaptureSynchronizedStreamsGroup`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 9 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"BWFigCaptureSynchronizedStreamsGroup" _synchronizedStreamsGroup;
@"NSArray" _activeStreams;
@"NSArray" _activePortTypes;
@"NSDictionary" _cameraViewMatricesByPortType;
@"NSDictionary" _cameraPoseMatricesByPortType;
@"NSDictionary" _baseZoomFactorsByPortType;
@"NSDictionary" _clientBaseZoomFactorsByPortType;
@"NSDictionary" _ispBaseZoomFactorsByPortType;
B _readOnly;
B _atomicMasterSlaveReconfigurationSupported;
B _masterConfigurationSupported;
@"BWFigVideoCaptureStream" _currentMasterStream;
@"NSDictionary" _currentSlaveConfigurationsByPortType;
i _maximumNumberOfSlaveStreamsWithoutFrameSkipping;
i _maximumNumberOfSlaveStreamsWithFrameProcessingEnabled;
i _maximumNumberOfEnabledSlaveTimeMachines;
@"BWFigVideoCaptureStream" _cameraControlsStatisticsMasterStream;
B _statsMasterHasBeenSet;
```

## Properties

```
@property (T@"BWFigCaptureSynchronizedStreamsGroup",R,N,V_synchronizedStreamsGroup) syncGroup;
@property (T@"NSArray",R,N,V_activePortTypes) activePortTypes;
@property (TB,R,N) minimumMasterToSlaveFrameRateRatioSupported;
@property (TB,R,N) maximumNumberOfSlaveStreamsWithoutFrameSkippingSupported;
@property (TB,R,N) maximumNumberOfSlaveStreamsWithFrameProcessingEnabledSupported;
@property (T@"NSDictionary",R,N,V_clientBaseZoomFactorsByPortType) clientBaseZoomFactorsByPortType;
@property (T@"NSDictionary",C,N,V_baseZoomFactorsByPortType) baseZoomFactorsByPortType;
@property (T@"NSDictionary",R,N,V_ispBaseZoomFactorsByPortType) ispBaseZoomFactorsByPortType;
@property (T@"BWFigVideoCaptureStream",R,N,V_cameraControlsStatisticsMasterStream) cameraControlsStatisticsMasterStream;
```

## Class methods

```
+[BWFigVideoCaptureSynchronizedStreamsGroup initialize];
```

## Instance methods

```
-[BWFigVideoCaptureSynchronizedStreamsGroup setBaseZoomFactorsByPortType:];
-[BWFigVideoCaptureSynchronizedStreamsGroup setMaximumNumberOfSlaveStreamsWithoutFrameSkipping:];
-[BWFigVideoCaptureSynchronizedStreamsGroup ispBaseZoomFactorsByPortType];
-[BWFigVideoCaptureSynchronizedStreamsGroup cameraControlsStatisticsMasterStream];
-[BWFigVideoCaptureSynchronizedStreamsGroup maximumNumberOfSlaveStreamsWithFrameProcessingEnabledSupported];
-[BWFigVideoCaptureSynchronizedStreamsGroup setMaximumNumberOfSlaveStreamsWithFrameProcessingEnabled:];
-[BWFigVideoCaptureSynchronizedStreamsGroup dealloc];
-[BWFigVideoCaptureSynchronizedStreamsGroup initWithSynchronizedStreamsGroup:activeStreams:readOnly:baseZoomFactorOverrides:clientBaseZoomFactorsByPortType:error:];
-[BWFigVideoCaptureSynchronizedStreamsGroup setMinimumMasterToSlaveFrameRateRatio:];
-[BWFigVideoCaptureSynchronizedStreamsGroup setMaximumNumberOfEnabledSlaveTimeMachines:];
-[BWFigVideoCaptureSynchronizedStreamsGroup cameraPoseMatrixForPortType:];
-[BWFigVideoCaptureSynchronizedStreamsGroup minimumMasterToSlaveFrameRateRatio];
-[BWFigVideoCaptureSynchronizedStreamsGroup maximumNumberOfSlaveStreamsWithoutFrameSkippingSupported];
-[BWFigVideoCaptureSynchronizedStreamsGroup activePortTypes];
-[BWFigVideoCaptureSynchronizedStreamsGroup cameraViewMatrixForPortType:];
-[BWFigVideoCaptureSynchronizedStreamsGroup setCameraControlsStatisticsMasterStream:];
-[BWFigVideoCaptureSynchronizedStreamsGroup setMasterStream:allStreams:];
-[BWFigVideoCaptureSynchronizedStreamsGroup minimumMasterToSlaveFrameRateRatioSupported];
-[BWFigVideoCaptureSynchronizedStreamsGroup clientBaseZoomFactorsByPortType];
-[BWFigVideoCaptureSynchronizedStreamsGroup baseZoomFactorsByPortType];
-[BWFigVideoCaptureSynchronizedStreamsGroup syncGroup];
```
