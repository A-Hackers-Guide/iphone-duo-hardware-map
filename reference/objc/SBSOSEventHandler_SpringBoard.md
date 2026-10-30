# `SBSOSEventHandler`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SOSManagerClientObserver`, `BSInvalidatable`
- 6 instance variables, 8 properties, 13 instance methods, 1 class methods

## Instance variables

```
@ _coversheetObserverToken;
@"BSCompoundAssertion" _observers;
B _isValid;
B _running;
@"SBFUserAuthenticationController" _override_authenticationController;
@"SOSManager" _override_sosManager;
```

## Properties

```
@property (TB,N,G_isRunning,S_setRunning:,V_running) running;
@property (T@"SBFUserAuthenticationController",R,N,G_authenticationController,V_override_authenticationController) authenticationController;
@property (T@"SOSManager",R,N,G_sosManager,V_override_sosManager) sosManager;
@property (TB,R,N,GisSOSActive) SOSActive;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSOSEventHandler sharedInstance];
```

## Instance methods

```
-[SBSOSEventHandler init];
-[SBSOSEventHandler dealloc];
-[SBSOSEventHandler _authenticationController];
-[SBSOSEventHandler addObserver:];
-[SBSOSEventHandler invalidate];
-[SBSOSEventHandler run];
-[SBSOSEventHandler _isRunning];
-[SBSOSEventHandler _setRunning:];
-[SBSOSEventHandler _forceBioAuthenticationLockoutIfAvailableWithSource:showingPasscode:];
-[SBSOSEventHandler _sosManager];
-[SBSOSEventHandler didDismissSOSBeforeSOSCall:];
-[SBSOSEventHandler didUpdateCurrentSOSInitiationState:];
-[SBSOSEventHandler isSOSActive];
```
