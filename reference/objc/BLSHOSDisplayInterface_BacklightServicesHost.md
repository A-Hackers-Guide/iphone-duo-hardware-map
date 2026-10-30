# `BLSHOSDisplayInterface`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDisplayStateClientDelegate`, `BLSHOSDisplayInterfaceProviding`, `BLSHTransparentFlipbookProvider`, `BLSHWatchdogDelegate`
- 32 instance variables, 24 properties, 39 instance methods, 0 class methods

## Instance variables

```
@"<BLSHBacklightPlatformProvider>" _platformProvider;
@"<BLSHBacklightOSInterfaceProviding>" _osInterfaceProvider;
@"NSString" _identifier;
Q _referenceId;
@"<BLSDisplayStateDelegate>" _displayStateDelegate;
@"CBDisplayStateClient" _displayStateClient;
@"CADisplayStateControl" _displayStateControl;
@"CMSuppressionManager" _suppressionManager;
@"BLSHSuppressionEvent" _lock_lastSuppressionEvent;
@"BSContinuousMachTimer" _setCBDisplayModeTimer;
@"NSString" _loggingName;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
q _lock_caDisplayState;
q _lock_notifiedCADisplayState;
q _lock_cbDisplayMode;
q _lock_cbFlipbookState;
i _surfaceType;
f _backlightDimmedFactor;
B _displayStateClientSupported;
B _highLuminanceAODsupportedInCB;
B _deviceSupportsAlwaysOn;
B _deviceSupportsAlwaysOnFlipbook;
B _lock_suppressionServiceActive;
B _lock_flipbookTransparent;
B _lock_cloningDisabled;
@"<BLSHWatchdogInvalidatable>" _lock_CBWatchdogTimer;
@"<BLSHWatchdogInvalidatable>" _lock_CAWatchdogTimer;
Q _lock_CBWatchdogType;
Q _lock_CAWatchdogType;
d _cbTransitionsDelayForTesting;
d _caTransitionsDelayForTesting;
@"CADisplay" _caDisplay;
```

## Properties

```
@property (T@"CADisplay",R,N,V_caDisplay) caDisplay;
@property (T@"<BLSHBacklightOSInterfaceProviding>",R,N) osInterfaceProvider;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<BLSDisplayStateDelegate>",&,SsetDisplayStateDelegate:) displayStateDelegate;
@property (Tq,R,N) cbDisplayMode;
@property (TB,R,N) highLuminanceAODsupportedInCB;
@property (TB,R,N) supportsFlipbookState;
@property (Tq,R,N) cbFlipbookState;
@property (Tq,R,N) caDisplayState;
@property (Tq,R,N) caDisplayPowerState;
@property (TB,N,GisCloningDisabled) cloningDisabled;
@property (TB,R,N,GisSuppressionServiceActive) suppressionServiceActive;
@property (T@"BLSHSuppressionEvent",R,N) lastSuppressionEvent;
@property (Ti,R,N) surfaceType;
@property (TQ,R,N) referenceId;
@property (T@"NSString",R,C,N) loggingName;
@property (TB,N,GisFlipbookTransparent) flipbookTransparent;
@property (T@"<BLSDisplay>",R,N) display;
@property (Td,?,N,SsetCBTransitionsDelayForTesting:) cbTransitionsDelayForTesting;
@property (Td,?,N,SsetCATransitionsDelayForTesting:) caTransitionsDelayForTesting;
```

## Instance methods

```
-[BLSHOSDisplayInterface cbDisplayMode];
-[BLSHOSDisplayInterface loggingName];
-[BLSHOSDisplayInterface display];
-[BLSHOSDisplayInterface setCATransitionsDelayForTesting:];
-[BLSHOSDisplayInterface registerHandlersForService:];
-[BLSHOSDisplayInterface didCompleteSwitchToFlipbookState:withError:];
-[BLSHOSDisplayInterface createFlipbook];
-[BLSHOSDisplayInterface surfaceType];
-[BLSHOSDisplayInterface didCompleteTransitionToDisplayMode:withError:];
-[BLSHOSDisplayInterface identifier];
-[BLSHOSDisplayInterface isCloningDisabled];
-[BLSHOSDisplayInterface displayStateDelegate];
-[BLSHOSDisplayInterface setCBTransitionsDelayForTesting:];
-[BLSHOSDisplayInterface setCloningDisabled:];
-[BLSHOSDisplayInterface cbFlipbookState];
-[BLSHOSDisplayInterface isSuppressionServiceActive];
-[BLSHOSDisplayInterface transitionToCADisplayState:];
-[BLSHOSDisplayInterface transitionToDisplayMode:withDuration:didChangeAlwaysOnBrightnessCurve:];
-[BLSHOSDisplayInterface highLuminanceAODsupportedInCB];
-[BLSHOSDisplayInterface caDisplayState];
-[BLSHOSDisplayInterface abortContextForTimer:];
-[BLSHOSDisplayInterface supportsFlipbookState];
-[BLSHOSDisplayInterface switchToFlipbookState:];
-[BLSHOSDisplayInterface doesMatchCADisplay:];
-[BLSHOSDisplayInterface caDisplay];
-[BLSHOSDisplayInterface caDisplayPowerState];
-[BLSHOSDisplayInterface createDisplayPowerResourceHintWithState:];
-[BLSHOSDisplayInterface referenceId];
-[BLSHOSDisplayInterface lastSuppressionEvent];
-[BLSHOSDisplayInterface delegateQueue];
-[BLSHOSDisplayInterface acquireDisplayPowerAssertionForReason:];
-[BLSHOSDisplayInterface osInterfaceProvider];
-[BLSHOSDisplayInterface setDisplayStateDelegate:];
-[BLSHOSDisplayInterface endSuppressionService];
-[BLSHOSDisplayInterface startSuppressionServiceWithHandler:];
-[BLSHOSDisplayInterface initWithCADisplay:platformProvider:osInterfaceProvider:];
-[BLSHOSDisplayInterface didDetectSignificantUserInteraction];
-[BLSHOSDisplayInterface isFlipbookTransparent];
-[BLSHOSDisplayInterface setFlipbookTransparent:];
```
