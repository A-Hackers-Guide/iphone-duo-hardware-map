# `FigCaptureSessionStateManager`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 23 instance variables, 24 properties, 51 instance methods, 1 class methods

## Instance variables

```
@"NSString" _loggingPrefix;
B _clientStartedSession;
B _clientRequestedStartSession;
B _clientRequestedStopRunning;
B _systemRequestedPrewarming;
B _backgrounded;
B _inMultitaskingMode;
B _inWindow;
B _inPictureInPicture;
B _cameraStolen;
@"NSString" _cameraStolenInterruptor;
B _cameraShutDownDueToSystemPressure;
B _micStolen;
@"NSMutableArray" _interruptionStatuses;
i _sessionStatus;
B _sessionUsesCamera;
B _sessionUsesMic;
B _multitaskingModeAllowed;
i _runtimeError;
B _sessionStopRequired;
i _sessionWasInterruptedWithError;
i _sessionWasStoppedWithRuntimeError;
B _didSuppressAutoResume;
```

## Properties

```
@property (TB,R,N) sessionShouldRun;
@property (TB,R,N) sessionShouldStart;
@property (TB,R,N) sessionShouldStop;
@property (TB,R,N) sessionHasUpdatedError;
@property (TB,R,N) sessionShouldUpdate;
@property (TB,R,N,V_systemRequestedPrewarming) systemRequestedPrewarming;
@property (TB,R,N,V_clientStartedSession) clientStartedSession;
@property (TB,R,N,V_clientRequestedStartSession) clientRequestedStartSession;
@property (TB,R,N) isSessionRunning;
@property (Ti,R,N,V_sessionStatus) sessionStatus;
@property (Ti,R,N) interruptionError;
@property (Ti,R,N,V_sessionWasInterruptedWithError) sessionWasInterruptedWithError;
@property (Ti,R,N,V_sessionWasStoppedWithRuntimeError) sessionWasStoppedWithRuntimeError;
@property (Ti,R,N,V_runtimeError) runtimeError;
@property (TB,R,N,V_cameraStolen) cameraStolen;
@property (T@"NSString",R,N,V_cameraStolenInterruptor) cameraStolenInterruptor;
@property (TB,R,N,V_cameraShutDownDueToSystemPressure) cameraShutDownDueToSystemPressure;
@property (TB,R,N,V_micStolen) micStolen;
@property (TB,R,N,V_backgrounded) backgrounded;
@property (TB,R,N,V_inMultitaskingMode) inMultitaskingMode;
@property (TB,R,N,V_inWindow) inWindow;
@property (TB,R,N,V_inPictureInPicture) inPictureInPicture;
@property (TB,R,N,V_didSuppressAutoResume) didSuppressAutoResume;
@property (T@"NSString",&,N,V_loggingPrefix) loggingPrefix;
```

## Class methods

```
+[FigCaptureSessionStateManager initialize];
```

## Instance methods

```
-[FigCaptureSessionStateManager osStatePropertyList];
-[FigCaptureSessionStateManager runtimeError];
-[FigCaptureSessionStateManager sessionUpdatedRunningStatus:withError:];
-[FigCaptureSessionStateManager clientRequestedSetConfigurationWithUsesCamera:usesMic:multitaskingModeAllowed:];
-[FigCaptureSessionStateManager microphoneDeviceInterrupted:];
-[FigCaptureSessionStateManager micStolen];
-[FigCaptureSessionStateManager didSuppressAutoResume];
-[FigCaptureSessionStateManager clientRequestedStopRunning];
-[FigCaptureSessionStateManager sessionShouldUpdate];
-[FigCaptureSessionStateManager sessionWasInterruptedWithError];
-[FigCaptureSessionStateManager sessionClearNonSystemInterruption];
-[FigCaptureSessionStateManager sessionHasUpdatedError];
-[FigCaptureSessionStateManager loggingPrefix];
-[FigCaptureSessionStateManager cancelPrewarm];
-[FigCaptureSessionStateManager clientRequestedStartSession];
-[FigCaptureSessionStateManager dealloc];
-[FigCaptureSessionStateManager checkSessionAllowedToRunWithConfigurationUsesCamera:usesMic:];
-[FigCaptureSessionStateManager audioSessionReset];
-[FigCaptureSessionStateManager audiomxdDied];
-[FigCaptureSessionStateManager systemRequestedPrewarming];
-[FigCaptureSessionStateManager cameraStolenInterruptor];
-[FigCaptureSessionStateManager sessionInterruptionTriggered:];
-[FigCaptureSessionStateManager sessionInterruptionResolved:];
-[FigCaptureSessionStateManager sessionWasStoppedWithRuntimeError];
-[FigCaptureSessionStateManager inWindow];
-[FigCaptureSessionStateManager inMultitaskingMode];
-[FigCaptureSessionStateManager sessionSentDidStopRunningWithInterruptionError:runtimeError:];
-[FigCaptureSessionStateManager sessionShouldStart];
-[FigCaptureSessionStateManager clientRequestedStartRunning];
-[FigCaptureSessionStateManager systemRequestedPrewarm];
-[FigCaptureSessionStateManager sessionWillStopWithInterruptionError:runtimeError:];
-[FigCaptureSessionStateManager interruptionError];
-[FigCaptureSessionStateManager sessionWillStartRunning];
-[FigCaptureSessionStateManager sessionRequestedResetRunningCondition];
-[FigCaptureSessionStateManager cameraDeviceAvailabilityChangedWithReason:available:interruptor:];
-[FigCaptureSessionStateManager sessionRequestedStopAttachedSession];
-[FigCaptureSessionStateManager sessionGraphFailedToStartWithError:];
-[FigCaptureSessionStateManager description];
-[FigCaptureSessionStateManager isSessionRunning];
-[FigCaptureSessionStateManager clientStartedSession];
-[FigCaptureSessionStateManager sessionStatus];
-[FigCaptureSessionStateManager cameraStolen];
-[FigCaptureSessionStateManager systemApplicationStateChangedToBackgrounded:inMultitaskingMode:windowed:pictureInPicture:foregroundAutoResumeDisabled:];
-[FigCaptureSessionStateManager sessionShouldStop];
-[FigCaptureSessionStateManager backgrounded];
-[FigCaptureSessionStateManager sessionWillHandleClientRequestedStopRunning];
-[FigCaptureSessionStateManager inPictureInPicture];
-[FigCaptureSessionStateManager setLoggingPrefix:];
-[FigCaptureSessionStateManager cameraShutDownDueToSystemPressure];
-[FigCaptureSessionStateManager sessionRequestedStartDetachedSession];
-[FigCaptureSessionStateManager sessionShouldRun];
```
