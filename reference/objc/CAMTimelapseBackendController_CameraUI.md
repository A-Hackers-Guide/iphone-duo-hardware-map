# `CAMTimelapseBackendController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMVideoCaptureRequestDelegate`, `CAMNebulaDaemonTimelapseProtocol`, `CAMPersistenceResultDelegate`
- 13 instance variables, 17 properties, 49 instance methods, 0 class methods

## Instance variables

```
B __writingMovie;
B __capturing;
B __oldMovieWriterEnabled;
i __notifyRegisterTokenSuspendIO;
i __notifyRegisterTokenResumeIO;
@"NSMutableArray" __sessionContexts;
@"NSObject<OS_dispatch_queue>" __workQueue;
@"<CAMTimelapseMovieWriterProtocol>" __movieWriter;
@"CAMTimelapseState" __currentState;
@"CAMNebulaKeepAliveController" __keepAliveController;
@"CAMPersistenceController" __persistenceController;
@"NSMutableDictionary" __transactionForPersistenceUUID;
@"RBSProcessMonitor" __processMonitor;
```

## Properties

```
@property (T@"NSMutableArray",R,N,V__sessionContexts) _sessionContexts;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__workQueue) _workQueue;
@property (TB,R,N,V__writingMovie) _writingMovie;
@property (T@"<CAMTimelapseMovieWriterProtocol>",R,N,V__movieWriter) _movieWriter;
@property (T@"CAMTimelapseState",&,N,S_setCurrentState:,V__currentState) _currentState;
@property (TB,N,G_isCapturing,S_setCapturing:,V__capturing) _capturing;
@property (T@"CAMNebulaKeepAliveController",R,N,V__keepAliveController) _keepAliveController;
@property (T@"CAMPersistenceController",R,N,V__persistenceController) _persistenceController;
@property (TB,R,N,V__oldMovieWriterEnabled) _oldMovieWriterEnabled;
@property (T@"NSMutableDictionary",R,N,V__transactionForPersistenceUUID) _transactionForPersistenceUUID;
@property (Ti,R,N,V__notifyRegisterTokenSuspendIO) _notifyRegisterTokenSuspendIO;
@property (Ti,R,N,V__notifyRegisterTokenResumeIO) _notifyRegisterTokenResumeIO;
@property (T@"RBSProcessMonitor",R,N,V__processMonitor) _processMonitor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMTimelapseBackendController _isCapturing];
-[CAMTimelapseBackendController _workQueue];
-[CAMTimelapseBackendController _currentState];
-[CAMTimelapseBackendController init];
-[CAMTimelapseBackendController _persistenceController];
-[CAMTimelapseBackendController dealloc];
-[CAMTimelapseBackendController _setCurrentState:];
-[CAMTimelapseBackendController videoRequestDidCompleteRemotePersistence:withResponse:error:];
-[CAMTimelapseBackendController _keepAliveController];
-[CAMTimelapseBackendController _processMonitor];
-[CAMTimelapseBackendController _createPlaceholderAssetForState:];
-[CAMTimelapseBackendController _deleteItemAtPath:];
-[CAMTimelapseBackendController _dispatchToMainQueueWithBlock:];
-[CAMTimelapseBackendController _dispatchToWorkQueueAfterDelay:withBlock:];
-[CAMTimelapseBackendController _dispatchToWorkQueueWithBlock:];
-[CAMTimelapseBackendController _frameTransformForState:];
-[CAMTimelapseBackendController _getOrCreateSessionContextForTimelapseUUID:];
-[CAMTimelapseBackendController _isCameraRunning];
-[CAMTimelapseBackendController _movieWriter];
-[CAMTimelapseBackendController _movieWrittenToFilePath:duration:metadata:state:];
-[CAMTimelapseBackendController _notifyAssetsdOfIncomingMovieAtPath:duration:metadata:state:];
-[CAMTimelapseBackendController _notifyRegisterTokenResumeIO];
-[CAMTimelapseBackendController _notifyRegisterTokenSuspendIO];
-[CAMTimelapseBackendController _oldMovieWriterEnabled];
-[CAMTimelapseBackendController _performPendingWork];
-[CAMTimelapseBackendController _permanentlyFailTimelapseUUID:withState:];
-[CAMTimelapseBackendController _reserveDummyFileForTimelapseUUID:firstImageFilePath:useHEVC:];
-[CAMTimelapseBackendController _saveTimelapseDirectoryForDebuggingTimelapseUUID:];
-[CAMTimelapseBackendController _scheduleDelayedMovieWriteIfNeededForTimelapseUUID:];
-[CAMTimelapseBackendController _sessionContexts];
-[CAMTimelapseBackendController _setCapturing:];
-[CAMTimelapseBackendController _shouldSaveLastTimelapseDataForDebugging];
-[CAMTimelapseBackendController _transactionForPersistenceUUID];
-[CAMTimelapseBackendController _updatePendingWorkFromDiskForceEndLastSession:];
-[CAMTimelapseBackendController _updateSessionContext:withState:];
-[CAMTimelapseBackendController _workQueue_destroyProcessMonitor];
-[CAMTimelapseBackendController _workQueue_setupCameraProcessMonitoringIfNecessary];
-[CAMTimelapseBackendController _writeMovieForSessionContext:];
-[CAMTimelapseBackendController _writingMovie];
-[CAMTimelapseBackendController finishCaptureForTimelapseWithUUID:];
-[CAMTimelapseBackendController handleClientConnection:];
-[CAMTimelapseBackendController handleClientDisconnection];
-[CAMTimelapseBackendController initWithPersistenceController:keepAliveController:];
-[CAMTimelapseBackendController persistenceController:didGenerateVideoLocalPersistenceResult:forCaptureResult:fromRequest:];
-[CAMTimelapseBackendController resumeTimelapseWithUUID:];
-[CAMTimelapseBackendController startTimelapseWithUUID:];
-[CAMTimelapseBackendController stopTimelapseWithUUID:];
-[CAMTimelapseBackendController updatePendingWorkFromDiskForceEndLastSession:];
-[CAMTimelapseBackendController updateTimelapseWithUUID:];
```
