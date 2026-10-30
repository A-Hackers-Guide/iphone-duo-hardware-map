# `SBContinuitySessionSystemEventMonitor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSCoverSheetViewControllerObserver`, `SOSManagerClientObserver`, `SBTodayViewControllerObserver`, `CSExternalEventHandling`, `SBRemoteTransientOverlaySessionManagerObserver`, `SBRemoteTransientOverlaySessionObserver`, `FBSDisplayObserving`
- 10 instance variables, 16 properties, 49 instance methods, 1 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"FBSDisplayMonitor" _displayMonitor;
B _isUILocked;
B _isUIBlocked;
B _inCall;
B _isPasscodeVisible;
B _isSOSActive;
B _lockScreenSearchPresented;
B _usingSecureApp;
B _userInitiatedRemoteTransientOverlayPresented;
```

## Properties

```
@property (TB,R,N,GisUIBlocked) uiBlocked;
@property (TB,R,N,GisUILocked) uiLocked;
@property (TB,R,N,GisInCall) inCall;
@property (TB,R,N,GisSOSActive) sosActive;
@property (TB,R,N,GisLockScreenSearchPresented,V_lockScreenSearchPresented) lockScreenSearchPresented;
@property (TB,R,N,GisUsingSecureApp) usingSecureApp;
@property (TB,R,N,GisAirplayMirroring) airplayMirroring;
@property (TB,R,N,GisUserInitiatedRemoteTransientOverlayPresented) userInitiatedRemoteTransientOverlayPresented;
@property (TB,R,N,GisInStoreDemoMode) storeDemoMode;
@property (TB,R,N,GisPresentingStoreDemoLoop) presentingStoreDemoLoop;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) coverSheetIdentifier;
@property (Tq,R,N) participantState;
```

## Class methods

```
+[SBContinuitySessionSystemEventMonitor _enumerateInterestingWindowScenesFromSet:block:];
```

## Instance methods

```
-[SBContinuitySessionSystemEventMonitor handleEvent:];
-[SBContinuitySessionSystemEventMonitor wouldHandleButtonEvent:];
-[SBContinuitySessionSystemEventMonitor todayViewControllerDidDismissSearch:];
-[SBContinuitySessionSystemEventMonitor remoteTransientOverlaySession:didInvalidateWithReason:error:];
-[SBContinuitySessionSystemEventMonitor removeObserver:];
-[SBContinuitySessionSystemEventMonitor init];
-[SBContinuitySessionSystemEventMonitor dealloc];
-[SBContinuitySessionSystemEventMonitor todayViewControllerDidPresentSearch:];
-[SBContinuitySessionSystemEventMonitor addObserver:];
-[SBContinuitySessionSystemEventMonitor remoteTransientOverlaySessionManager:didActivateSession:];
-[SBContinuitySessionSystemEventMonitor isInCall];
-[SBContinuitySessionSystemEventMonitor remoteTransientOverlaySessionDidDeactivate:];
-[SBContinuitySessionSystemEventMonitor conformsToCSEventHandling];
-[SBContinuitySessionSystemEventMonitor displayMonitor:willDisconnectIdentity:];
-[SBContinuitySessionSystemEventMonitor _setUILocked:];
-[SBContinuitySessionSystemEventMonitor displayMonitor:didConnectIdentity:withConfiguration:];
-[SBContinuitySessionSystemEventMonitor isUILocked];
-[SBContinuitySessionSystemEventMonitor coverSheetIdentifier];
-[SBContinuitySessionSystemEventMonitor participantState];
-[SBContinuitySessionSystemEventMonitor _postEvent:];
-[SBContinuitySessionSystemEventMonitor isInStoreDemoMode];
-[SBContinuitySessionSystemEventMonitor _callStatusChanged:];
-[SBContinuitySessionSystemEventMonitor coverSheetViewControllerDidDismissSearch:];
-[SBContinuitySessionSystemEventMonitor coverSheetViewControllerDidPresentModalView:];
-[SBContinuitySessionSystemEventMonitor coverSheetViewControllerDidPresentSearch:];
-[SBContinuitySessionSystemEventMonitor coverSheetViewControllerDidSettleOnPage:mainPage:];
-[SBContinuitySessionSystemEventMonitor _aggregateLockStateChanged:];
-[SBContinuitySessionSystemEventMonitor _calculateIsInCall];
-[SBContinuitySessionSystemEventMonitor _calculateLockScreenSearchPresented];
-[SBContinuitySessionSystemEventMonitor _calculateUserInitiatedRemoteTransientOverlayPresented];
-[SBContinuitySessionSystemEventMonitor _coverSheetSecureAppChanged:];
-[SBContinuitySessionSystemEventMonitor _coverSheetTodayViewController];
-[SBContinuitySessionSystemEventMonitor _passcodeVisibilityUpdated:];
-[SBContinuitySessionSystemEventMonitor _reevaluateSecureAppUsage];
-[SBContinuitySessionSystemEventMonitor _setInCall:];
-[SBContinuitySessionSystemEventMonitor _setLockScreenSearchPresented:];
-[SBContinuitySessionSystemEventMonitor _setPasscodeVisible:];
-[SBContinuitySessionSystemEventMonitor _setSOSActive:];
-[SBContinuitySessionSystemEventMonitor _setUIBlocked:];
-[SBContinuitySessionSystemEventMonitor _setUserInitiatedRemoteTransientOverlayPresented:];
-[SBContinuitySessionSystemEventMonitor _setUsingSecureApp:];
-[SBContinuitySessionSystemEventMonitor didUpdateCurrentSOSInitiationState:];
-[SBContinuitySessionSystemEventMonitor isAirplayMirroring];
-[SBContinuitySessionSystemEventMonitor isLockScreenSearchPresented];
-[SBContinuitySessionSystemEventMonitor isPresentingStoreDemoLoop];
-[SBContinuitySessionSystemEventMonitor isSOSActive];
-[SBContinuitySessionSystemEventMonitor isUIBlocked];
-[SBContinuitySessionSystemEventMonitor isUserInitiatedRemoteTransientOverlayPresented];
-[SBContinuitySessionSystemEventMonitor isUsingSecureApp];
```
