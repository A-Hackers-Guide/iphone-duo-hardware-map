# `CAMTimelapseController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMStillImageCaptureRequestDelegate`, `CAMNebulaDaemonTimelapseClientProtocol`
- 23 instance variables, 29 properties, 70 instance methods, 2 class methods

## Instance variables

```
B __ignoringTimerCallbacksForTearDown;
B __ignoringTimerCallbacksWaitingForCaptureResponse;
B __shouldUpdateFocusAndExposureWhenContrastDetectionCompletes;
B __backendRecoveryNeeded;
B __previewStarted;
B __focusAndExposureAdjusted;
@"CAMCaptureGraphConfiguration" __graphConfigurationForCurrentState;
@"<CAMTimelapseControllerDelegate>" _delegate;
@"CAMFocusResult" _lastFocusResult;
@"CAMTimelapseState" __state;
@"NSObject<OS_dispatch_source>" __captureTimer;
@"NSCountedSet" __inFlightTimelapseUUIDs;
@"NSMutableSet" __pendingCompletedStates;
^{ct_green_tea_logger_s=} __greenTeaLogger;
@"NSTimer" __focusLockTimeoutTimer;
@"CAMCaptureAttributeManager" __captureAttributeManager;
@"CUCaptureController" __captureController;
@"CAMLocationController" __locationController;
@"CAMMotionController" __motionController;
@"CAMPersistenceController" __persistenceController;
@"CAMStorageController" __storageController;
@"CAMLibrarySelectionController" __librarySelectionController;
@"CAMNebulaDaemonProxyManager" __nebulaDaemonProxyManager;
```

## Properties

```
@property (T@"CAMTimelapseState",R,N,V__state) _state;
@property (T@"CAMCaptureGraphConfiguration",R,N,G_graphConfigurationForCurrentState,V__graphConfigurationForCurrentState) _graphConfigurationForCurrentState;
@property (T@"NSObject<OS_dispatch_source>",R,N,V__captureTimer) _captureTimer;
@property (TB,R,N,V__ignoringTimerCallbacksForTearDown) _ignoringTimerCallbacksForTearDown;
@property (TB,R,N,V__ignoringTimerCallbacksWaitingForCaptureResponse) _ignoringTimerCallbacksWaitingForCaptureResponse;
@property (T@"NSCountedSet",R,N,V__inFlightTimelapseUUIDs) _inFlightTimelapseUUIDs;
@property (T@"NSMutableSet",R,N,V__pendingCompletedStates) _pendingCompletedStates;
@property (TB,N,S_setShouldUpdateFocusAndExposureWhenContrastDetectionCompletes:,V__shouldUpdateFocusAndExposureWhenContrastDetectionCompletes) _shouldUpdateFocusAndExposureWhenContrastDetectionCompletes;
@property (T^{ct_green_tea_logger_s=},R,N,V__greenTeaLogger) _greenTeaLogger;
@property (TB,N,S_setBackendRecoveryNeeded:,V__backendRecoveryNeeded) _backendRecoveryNeeded;
@property (TB,N,S_setPreviewStarted:,V__previewStarted) _previewStarted;
@property (TB,N,G_isFocusAndExposureAdjusted,S_setFocusAndExposureAdjusted:,V__focusAndExposureAdjusted) _focusAndExposureAdjusted;
@property (T@"NSTimer",&,N,V__focusLockTimeoutTimer) _focusLockTimeoutTimer;
@property (T@"CAMCaptureAttributeManager",R,N,V__captureAttributeManager) _captureAttributeManager;
@property (T@"CUCaptureController",R,N,V__captureController) _captureController;
@property (T@"CAMLocationController",R,N,V__locationController) _locationController;
@property (T@"CAMMotionController",R,N,V__motionController) _motionController;
@property (T@"CAMPersistenceController",R,N,V__persistenceController) _persistenceController;
@property (T@"CAMStorageController",R,N,V__storageController) _storageController;
@property (T@"CAMLibrarySelectionController",R,N,V__librarySelectionController) _librarySelectionController;
@property (T@"CAMNebulaDaemonProxyManager",R,N,V__nebulaDaemonProxyManager) _nebulaDaemonProxyManager;
@property (T@"<CAMTimelapseControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisCapturing) capturing;
@property (T@"NSDate",R,N) captureStartTime;
@property (T@"CAMFocusResult",N,V_lastFocusResult) lastFocusResult;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAMTimelapseController _newVideoPreviewSurfaceForTimelapseState:];
+[CAMTimelapseController createPlaceholderResultForTimelapseState:];
```

## Instance methods

```
-[CAMTimelapseController _applicationWillEnterForeground:];
-[CAMTimelapseController stillImageRequestDidCompleteStillImageCapture:withResponse:error:];
-[CAMTimelapseController _locationController];
-[CAMTimelapseController _storageController];
-[CAMTimelapseController _state];
-[CAMTimelapseController _applicationDidEnterBackground:];
-[CAMTimelapseController _librarySelectionController];
-[CAMTimelapseController _sessionStarted:];
-[CAMTimelapseController _motionController];
-[CAMTimelapseController _captureController];
-[CAMTimelapseController _captureAttributeManager];
-[CAMTimelapseController isCapturing];
-[CAMTimelapseController stillImageRequestDidCompleteStillImageLocalPersistence:withResponse:error:];
-[CAMTimelapseController _captureTimerFired];
-[CAMTimelapseController _startCaptureTimer];
-[CAMTimelapseController _focusLockTimeoutTimer];
-[CAMTimelapseController _enqueueCaptureRequest];
-[CAMTimelapseController _prepareForTimelapseCaptureSetModeAndDevice:];
-[CAMTimelapseController _triggerBackendCrashRecoveryIfNeeded];
-[CAMTimelapseController lastFocusResult];
-[CAMTimelapseController captureStartTime];
-[CAMTimelapseController init];
-[CAMTimelapseController _persistenceController];
-[CAMTimelapseController _captureTimer];
-[CAMTimelapseController _saveStateToDisk:];
-[CAMTimelapseController dealloc];
-[CAMTimelapseController _invalidateCachedGraphConfiguration];
-[CAMTimelapseController forceStopTimelapseCaptureWithReasons:];
-[CAMTimelapseController initWithCaptureController:locationController:motionController:persistenceController:storageController:librarySelectionController:nebulaDaemonProxyManager:];
-[CAMTimelapseController _restoreCaptureStateFromDisk];
-[CAMTimelapseController set_focusLockTimeoutTimer:];
-[CAMTimelapseController _ignoringTimerCallbacksWaitingForCaptureResponse];
-[CAMTimelapseController _graphConfigurationForCurrentState];
-[CAMTimelapseController _nebulaDaemonProxyManager];
-[CAMTimelapseController _setBackendRecoveryNeeded:];
-[CAMTimelapseController _resetFocusLockTimeoutTimer];
-[CAMTimelapseController _setPreviewStarted:];
-[CAMTimelapseController setLastFocusResult:];
-[CAMTimelapseController _backendRecoveryNeeded];
-[CAMTimelapseController _updateLocationIfNecessary];
-[CAMTimelapseController _createThumbnailImageFromPlaceholderResult:];
-[CAMTimelapseController _resetIgnoringTimerCallbacksWaitingForCaptureResponse];
-[CAMTimelapseController _shouldUpdateFocusAndExposureWhenContrastDetectionCompletes];
-[CAMTimelapseController _stillImageCaptureRequestWithCurrentSettings];
-[CAMTimelapseController setDelegate:];
-[CAMTimelapseController _inFlightTimelapseUUIDs];
-[CAMTimelapseController _updateFocusAndExposureForStartCapturing];
-[CAMTimelapseController _setShouldUpdateFocusAndExposureWhenContrastDetectionCompletes:];
-[CAMTimelapseController _startCapturingWithCaptureDevice:deviceDirection:captureSession:];
-[CAMTimelapseController _greenTeaLogger];
-[CAMTimelapseController startCapturingWithCaptureDevice:deviceDirection:captureSession:];
-[CAMTimelapseController _sessionRuntimeErrored:];
-[CAMTimelapseController _ignoringTimerCallbacksForTearDown];
-[CAMTimelapseController _reserveDiskSpaceForTimelapseUUID:preferHEVC:withCompletionBlock:];
-[CAMTimelapseController _setNewCaptureStateForCaptureDevice:deviceDirection:captureSession:];
-[CAMTimelapseController delegate];
-[CAMTimelapseController _stopCapturingWithReasons:];
-[CAMTimelapseController _deviceStarted:];
-[CAMTimelapseController _previewStarted];
-[CAMTimelapseController restoreConfiguration];
-[CAMTimelapseController _isFocusAndExposureAdjusted];
-[CAMTimelapseController _setFocusAndExposureAdjusted:];
-[CAMTimelapseController _teardownCaptureTimer];
-[CAMTimelapseController _pendingCompletedStates];
-[CAMTimelapseController stopCapturingWithReasons:];
-[CAMTimelapseController _previewStarted:];
-[CAMTimelapseController _notifyInsufficientDiskSpaceForContinuingCapture];
-[CAMTimelapseController _notifyInsufficientDiskSpaceForStartingCaptureWithNeededBytes:availableBytes:];
-[CAMTimelapseController _updateFocusLensPosition:forTimelapseUUID:forceUpdate:];
-[CAMTimelapseController _canCapturePhotoWithUnavailableReasons:];
```
