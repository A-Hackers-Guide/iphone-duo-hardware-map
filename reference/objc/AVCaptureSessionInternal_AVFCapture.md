# `AVCaptureSessionInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 75 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
@"AVWeakReference" weakReference;
@"NSString" sessionPreset;
@"NSObject<OS_tcc_identity>" tccIdentity;
@"NSString" mediaEnvironment;
i beginConfigRefCount;
i graphRebuildFromCommitConfigRefCount;
@"FigCaptureSessionConfiguration" sessionConfig;
^{OpaqueFigCaptureSession=} figCaptureSession;
B figCaptureSessionRunning;
B figCaptureSessionStarted;
@"NSMutableArray" inputs;
@"NSMutableArray" outputs;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} outputsLock;
@"NSMutableArray" controls;
@"AVWeakReference" weakReferenceControlsDelegate;
@"NSObject<OS_dispatch_queue>" clientControlsQueue;
@"AVCaptureControlsOverlay" controlsOverlay;
@"NSPointerArray" videoPreviewLayers;
@"NSMutableArray" connections;
@"NSMutableArray" committedAVCaptureSessionConfigurations;
@"AVCaptureSessionConfiguration" liveAVCaptureSessionConfiguration;
@"NSError" stopError;
B running;
B interrupted;
B usesApplicationAudioSession;
B automaticallyConfiguresApplicationAudioSession;
B configuresApplicationAudioSessionToMixWithOthers;
B configuresApplicationAudioSessionForBluetoothHighQualityRecording;
B automaticallyConfiguresCaptureDeviceForWideColor;
@"AVRunLoopCondition" runLoopCondition;
B waitingForFigCaptureSessionToStart;
B waitingForFigCaptureSessionToStop;
B waitingForFigCaptureSessionConfigurationToBecomeLive;
B graphRebuildCancelledWait;
@"AVRunLoopCondition" singleGraphBuilderGateCondition;
q graphBuildInProgressCount;
f hardwareCost;
^{OpaqueCMClock=} synchronizationClock;
B notifiesOnMainThread;
@"NSMutableArray" devicesToResetVideoZoomFactorAndMinMaxFrameDurations;
B authorizedToUseCameraInMultipleForegroundAppLayout;
B xctestAuthorizedToStealDevice;
B continuityCameraIsWired;
i continuityCameraClientDeviceClass;
B clientIsVOIP;
B suppressVideoEffects;
@"NSObject<OS_dispatch_semaphore>" captureServerConnectionDiedSemaphore;
@ serverConnectionDiedNotificationToken;
^{ct_green_tea_logger_s=} greenTeaLogger;
B videoInputDeviceUsed;
^{OpaqueFigReentrantMutex=} figCaptureSourceConfigChangeCacheMutex;
@"NSThread" threadWhichBeganConfiguration;
@"NSMutableArray" _devicesObservingVideoZoomFactor;
B checkIfFileAlreadyExistForMFO;
@"NSMutableArray" recordingMovieFileOutputs;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} recordingMovieFileOutputsLock;
B smartStyleRenderingSupported;
B smartStyleRenderingEnabled;
@ systemSmartStyleObserver;
@"AVCaptureSmartStyle" smartStyleSetByClient;
B smartStyleRenderingOptedOut;
B smartStyleRenderingOptedOutDefault;
@"NSString" smartStyleAlertBundleName;
@"NSString" smartStyleAlertOptOutDescription;
q smartStyleControlMode;
@"AVCaptureSystemStylePicker" automaticallyAddedSystemStylePicker;
@"AVCaptureSystemStyleSlider" automaticallyAddedSystemParameterSlider;
B textureStyleEnabled;
B textureStyleSupported;
@"AVCaptureTextureStyle" textureStyleSetByClient;
B automaticallyRunsDeferredStart;
@"AVWeakReferencingDelegateStorage" deferredStartDelegateStorage;
B clientLaunchTelemetryEnabled;
B visualIntelligenceCameraEnabled;
@"NSMutableDictionary" thirdPartyCompatibilityRotationCoordinatorsByDeviceUniqueID;
```
