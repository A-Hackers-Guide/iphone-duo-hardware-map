# `AVCaptureDataOutputSynchronizer`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVCaptureVideoDataOutputSampleBufferDelegate`, `AVCaptureAudioDataOutputSampleBufferDelegate`, `AVCaptureMetadataOutputObjectsDelegateInternal`, `AVCaptureDepthDataOutputDelegate`, `AVCaptureVisionDataOutputDelegate`, `AVCapturePointCloudDataOutputDelegate`, `AVCaptureCameraCalibrationDataOutputDelegate`
- 1 instance variables, 7 properties, 26 instance methods, 1 class methods

## Instance variables

```
@"AVCaptureDataOutputSynchronizerInternal" _internal;
```

## Properties

```
@property (T@"NSArray",R,&) dataOutputs;
@property (T@"<AVCaptureDataOutputSynchronizerDelegate>",R,N) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateCallbackQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVCaptureDataOutputSynchronizer initialize];
```

## Instance methods

```
-[AVCaptureDataOutputSynchronizer setDelegate:queue:];
-[AVCaptureDataOutputSynchronizer dealloc];
-[AVCaptureDataOutputSynchronizer captureOutput:didOutputSampleBuffer:fromConnection:];
-[AVCaptureDataOutputSynchronizer delegate];
-[AVCaptureDataOutputSynchronizer delegateCallbackQueue];
-[AVCaptureDataOutputSynchronizer captureOutput:didDropSampleBuffer:fromConnection:];
-[AVCaptureDataOutputSynchronizer _adjustSynchronizedDataTimestamps];
-[AVCaptureDataOutputSynchronizer _allFollowerSynchronizedDataOutputsContainTimestampEqualToOrGreaterThanLeaderTimestamp:];
-[AVCaptureDataOutputSynchronizer _appendSynchronizedData:forCaptureOutput:];
-[AVCaptureDataOutputSynchronizer _assignTimestampAdjustmentQueueToDataOutputStorageWithCommonProvenance];
-[AVCaptureDataOutputSynchronizer _computedLeaderSynchronizedDataQueueMaxDepthForDataOutputs:];
-[AVCaptureDataOutputSynchronizer _dispatchRipenedSynchronizedData];
-[AVCaptureDataOutputSynchronizer _dispatchSynchronizedDataWithTimestamp:];
-[AVCaptureDataOutputSynchronizer _earliestFollowerSynchronizedDataQueueTimestamp];
-[AVCaptureDataOutputSynchronizer _overrideDataOutputDelegatesForDelegateCallbackQueue:];
-[AVCaptureDataOutputSynchronizer cameraCalibrationDataOutput:didDropCameraCalibrationDataAtTimestamp:connection:reason:];
-[AVCaptureDataOutputSynchronizer cameraCalibrationDataOutput:didOutputCameraCalibrationData:timestamp:connection:];
-[AVCaptureDataOutputSynchronizer captureOutput:didOutputMetadataObjectCollections:fromConnection:];
-[AVCaptureDataOutputSynchronizer dataOutputs];
-[AVCaptureDataOutputSynchronizer depthDataOutput:didDropDepthData:timestamp:connection:reason:];
-[AVCaptureDataOutputSynchronizer depthDataOutput:didOutputDepthData:timestamp:connection:];
-[AVCaptureDataOutputSynchronizer initWithDataOutputs:];
-[AVCaptureDataOutputSynchronizer pointCloudDataOutput:didDropPointCloudData:timestamp:connection:reason:];
-[AVCaptureDataOutputSynchronizer pointCloudDataOutput:didOutputPointCloudData:timestamp:connection:];
-[AVCaptureDataOutputSynchronizer visionDataOutput:didDropVisionDataPixelBufferForTimestamp:connection:reason:];
-[AVCaptureDataOutputSynchronizer visionDataOutput:didOutputVisionDataPixelBuffer:timestamp:connection:];
```
