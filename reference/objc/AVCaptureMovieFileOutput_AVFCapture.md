# `AVCaptureMovieFileOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureFileOutput`
- 1 instance variables, 15 properties, 103 instance methods, 7 class methods

## Instance variables

```
@"AVCaptureMovieFileOutputInternal" _internal;
```

## Properties

```
@property (TB,R,N,GisProVideoStorageSupported) proVideoStorageSupported;
@property (TB,N) usesProVideoStorage;
@property (TB,R,N,GisTrueVideoCaptureSupported) trueVideoCaptureSupported;
@property (TB,N,GisTrueVideoCaptureEnabled) trueVideoCaptureEnabled;
@property (T{?=qiIq},N) movieFragmentInterval;
@property (T@"NSArray",C,N) metadata;
@property (T@"NSArray",R,N) availableVideoCodecTypes;
@property (TB,N,GisPrimaryConstituentDeviceSwitchingBehaviorForRecordingEnabled) primaryConstituentDeviceSwitchingBehaviorForRecordingEnabled;
@property (Tq,R,N) primaryConstituentDeviceSwitchingBehaviorForRecording;
@property (TQ,R,N) primaryConstituentDeviceRestrictedSwitchingBehaviorConditionsForRecording;
@property (TB,R,N,GisSpatialVideoCaptureSupported) spatialVideoCaptureSupported;
@property (TB,N,GisSpatialVideoCaptureEnabled) spatialVideoCaptureEnabled;
@property (TB,R,N,GisCinematicVideoMetadataCaptureSupported) cinematicVideoMetadataCaptureSupported;
@property (TB,N) automaticallyAdjustsCinematicVideoMetadataCaptureEnabled;
@property (TB,N,GisCinematicVideoMetadataCaptureEnabled) cinematicVideoMetadataCaptureEnabled;
```

## Class methods

```
+[AVCaptureMovieFileOutput initialize];
+[AVCaptureMovieFileOutput uniqueID];
+[AVCaptureMovieFileOutput new];
+[AVCaptureMovieFileOutput consolidateMovieFragmentsInFile:error:];
+[AVCaptureMovieFileOutput makeTimelapseMovieFromTimewarpTimelapseClassicIntermediateMovie:timelapseMovie:error:];
+[AVCaptureMovieFileOutput _makeTimelapseMovieFromTimewarpTimelapseClassicIntermediateMovie:timelapseMovie:timelapseDestinationFrameRate:error:];
+[AVCaptureMovieFileOutput updateMovieMetadataInFile:withMetadata:error:];
```

## Instance methods

```
-[AVCaptureMovieFileOutput setTrueVideoCaptureEnabled:];
-[AVCaptureMovieFileOutput setTimewarpEnabled:];
-[AVCaptureMovieFileOutput stopRecording];
-[AVCaptureMovieFileOutput canAddConnection:failureReason:];
-[AVCaptureMovieFileOutput setCinematicVideoMetadataCaptureEnabled:];
-[AVCaptureMovieFileOutput setMultiCamClientCompositingPrimaryConnection:secondaryConnection:];
-[AVCaptureMovieFileOutput setMovieFragmentInterval:];
-[AVCaptureMovieFileOutput isRecording];
-[AVCaptureMovieFileOutput movieFragmentInterval];
-[AVCaptureMovieFileOutput isMultiCamClientCompositingSupported];
-[AVCaptureMovieFileOutput isMultiCamClientCompositingEnabled];
-[AVCaptureMovieFileOutput init];
-[AVCaptureMovieFileOutput timewarpDestinationFrameRate];
-[AVCaptureMovieFileOutput safelyHandleServerConnectionDeathForFigCaptureSession:];
-[AVCaptureMovieFileOutput isStereoVideoCaptureSupported];
-[AVCaptureMovieFileOutput setStereoVideoCaptureEnabled:];
-[AVCaptureMovieFileOutput detachSafelyFromFigCaptureSession:];
-[AVCaptureMovieFileOutput timewarpMode];
-[AVCaptureMovieFileOutput dealloc];
-[AVCaptureMovieFileOutput cinematicVideoMetadataCaptureEnabledByClient];
-[AVCaptureMovieFileOutput _updateSupportedPropertiesForSourceDevice:];
-[AVCaptureMovieFileOutput handleNotification:payload:];
-[AVCaptureMovieFileOutput availableVideoCodecTypes];
-[AVCaptureMovieFileOutput resumeRecording];
-[AVCaptureMovieFileOutput isCinematicVideoMetadataCaptureEnabled];
-[AVCaptureMovieFileOutput metadata];
-[AVCaptureMovieFileOutput _updateDepthDataDeliverySupportedForSourceDevice:];
-[AVCaptureMovieFileOutput setMultiCamClientCompositingEnabled:];
-[AVCaptureMovieFileOutput handleChangedActiveFormat:forDevice:];
-[AVCaptureMovieFileOutput isTimewarpEnabled];
-[AVCaptureMovieFileOutput multiCamClientCompositingPrimaryConnection];
-[AVCaptureMovieFileOutput setMetadata:];
-[AVCaptureMovieFileOutput startRecordingToOutputFileURL:recordingDelegate:];
-[AVCaptureMovieFileOutput connectionMediaTypes];
-[AVCaptureMovieFileOutput removeConnection:];
-[AVCaptureMovieFileOutput attachSafelyToFigCaptureSession:];
-[AVCaptureMovieFileOutput setTimewarpDestinationFrameRate:];
-[AVCaptureMovieFileOutput outputSizeForSourceFormat:];
-[AVCaptureMovieFileOutput setTimewarpMode:];
-[AVCaptureMovieFileOutput addConnection:error:];
-[AVCaptureMovieFileOutput pauseRecording];
-[AVCaptureMovieFileOutput _invokeClientCompositingCallbackForSettingsID:compositingData:];
-[AVCaptureMovieFileOutput outputFileURL];
-[AVCaptureMovieFileOutput isProVideoStorageSupported];
-[AVCaptureMovieFileOutput setUsesProVideoStorage:];
-[AVCaptureMovieFileOutput usesProVideoStorage];
-[AVCaptureMovieFileOutput _stopRecording];
-[AVCaptureMovieFileOutput _avErrorUserInfoDictionaryForError:wrapper:payload:];
-[AVCaptureMovieFileOutput _cleanupDelegateWrappers:];
-[AVCaptureMovieFileOutput _cleanupDelegateWrappersPendingDidStopRecordingUnregistration];
-[AVCaptureMovieFileOutput _delegateWrapperForSettingsID:];
-[AVCaptureMovieFileOutput _finishHandlingDidStopRecordingNotificationForWrapper:withPayload:demoof:addMetadata:errorCode:];
-[AVCaptureMovieFileOutput _hasBroadcastVideoOutputForSourceDevice:];
-[AVCaptureMovieFileOutput _isProResRawRecordingAndAWBIsNotLockedForWrapper:];
-[AVCaptureMovieFileOutput _propagateBravoSwitchingBehaviorWhenRecording];
-[AVCaptureMovieFileOutput _removeRecordingDelegateWrapper:];
-[AVCaptureMovieFileOutput _startRecording:];
-[AVCaptureMovieFileOutput _totalNANDBandwidthAllowed:videoCodecType:];
-[AVCaptureMovieFileOutput _updateAvailableVideoCodecTypesForSourceDevice:];
-[AVCaptureMovieFileOutput _updateCinematicVideoMetadataCaptureSupportedForSourceDevice:];
-[AVCaptureMovieFileOutput _updateConstituentDeviceSwitchingBehaviorForSourceDevice:];
-[AVCaptureMovieFileOutput _updateSpatialVideoCaptureSupportedForSourceDevice:];
-[AVCaptureMovieFileOutput automaticallyAdjustsCinematicVideoMetadataCaptureEnabled];
-[AVCaptureMovieFileOutput bravoCameraSelectionBehaviorForRecording];
-[AVCaptureMovieFileOutput handleChangedBroadcastVideoOutputForDevice:];
-[AVCaptureMovieFileOutput handleChangedDynamicAspectRatio:forFormat:];
-[AVCaptureMovieFileOutput handleChangedMSGPulseDurationForDevice:];
-[AVCaptureMovieFileOutput handleDidDropFrameWhileRecordingNotificationForWrapper:withPayload:];
-[AVCaptureMovieFileOutput handleDidPauseRecordingNotificationForWrapper:withPayload:];
-[AVCaptureMovieFileOutput handleDidResumeRecordingNotificationForWrapper:withPayload:];
-[AVCaptureMovieFileOutput handleDidStartRecordingNotificationForWrapper:withPayload:];
-[AVCaptureMovieFileOutput handleDidStopRecordingNotificationForMomentCaptureWrapper:withPayload:demoof:addMetadata:];
-[AVCaptureMovieFileOutput handleDidStopRecordingNotificationForWrapper:withPayload:demoof:addMetadata:];
-[AVCaptureMovieFileOutput handleVideoStabilizationModeChangedForConnection:];
-[AVCaptureMovieFileOutput handleVideoStabilizationStrengthChangedForDevice:];
-[AVCaptureMovieFileOutput isCinematicVideoMetadataCaptureSupported];
-[AVCaptureMovieFileOutput isDepthCaptureEnabled];
-[AVCaptureMovieFileOutput isPrimaryConstituentDeviceSwitchingBehaviorForRecordingEnabled];
-[AVCaptureMovieFileOutput isRecordingPaused];
-[AVCaptureMovieFileOutput isSpatialVideoCaptureEnabled];
-[AVCaptureMovieFileOutput isSpatialVideoCaptureSupported];
-[AVCaptureMovieFileOutput isStereoVideoCaptureEnabled];
-[AVCaptureMovieFileOutput isTimewarpSupported];
-[AVCaptureMovieFileOutput isTrueVideoCaptureEnabled];
-[AVCaptureMovieFileOutput isTrueVideoCaptureSupported];
-[AVCaptureMovieFileOutput outputSettingsForConnection:];
-[AVCaptureMovieFileOutput primaryConstituentDeviceRestrictedSwitchingBehaviorConditionsForRecording];
-[AVCaptureMovieFileOutput primaryConstituentDeviceSwitchingBehaviorForRecording];
-[AVCaptureMovieFileOutput recordingInProgress];
-[AVCaptureMovieFileOutput recordsVideoOrientationAndMirroringChangesAsMetadataTrackForConnection:];
-[AVCaptureMovieFileOutput sendsLastVideoPreviewFrame];
-[AVCaptureMovieFileOutput setAutomaticallyAdjustsCinematicVideoMetadataCaptureEnabled:];
-[AVCaptureMovieFileOutput setBravoCameraSelectionBehaviorForRecording:];
-[AVCaptureMovieFileOutput setConnectionsActive:];
-[AVCaptureMovieFileOutput setDepthCaptureEnabled:];
-[AVCaptureMovieFileOutput setOutputSettings:forConnection:];
-[AVCaptureMovieFileOutput setPrimaryConstituentDeviceSwitchingBehaviorForRecording:restrictedSwitchingBehaviorConditions:];
-[AVCaptureMovieFileOutput setPrimaryConstituentDeviceSwitchingBehaviorForRecordingEnabled:];
-[AVCaptureMovieFileOutput setRecordsVideoOrientationAndMirroringChanges:asMetadataTrackForConnection:];
-[AVCaptureMovieFileOutput setSendsLastVideoPreviewFrame:];
-[AVCaptureMovieFileOutput setSpatialVideoCaptureEnabled:];
-[AVCaptureMovieFileOutput startRecordingMovieWithSettings:delegate:];
-[AVCaptureMovieFileOutput supportedOutputSettingsKeysForConnection:];
```
