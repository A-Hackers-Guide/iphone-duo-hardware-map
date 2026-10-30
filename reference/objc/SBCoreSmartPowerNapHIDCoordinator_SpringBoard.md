# `SBCoreSmartPowerNapHIDCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 3 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"SBWindowSceneManager" _windowSceneManager;
@"<_SBCSPNClient>" _cspn;
@"NSObject<OS_dispatch_queue>" _callbackQueue;
@"<BSInvalidatable>" _digitizerAssertion;
B _userPresenceLatch;
C _lastState;
B _started;
```

## Properties

```
@property (T@"<BSInvalidatable>",R,N,V_digitizerAssertion) _digitizerAssertion;
@property (TB,R,N,V_userPresenceLatch) _userPresenceLatch;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_callbackQueue) _callbackQueue;
```

## Class methods

```
+[SBCoreSmartPowerNapHIDCoordinator coordinatorForWindowSceneManager:];
```

## Instance methods

```
-[SBCoreSmartPowerNapHIDCoordinator stop];
-[SBCoreSmartPowerNapHIDCoordinator start];
-[SBCoreSmartPowerNapHIDCoordinator _acquireAssertion];
-[SBCoreSmartPowerNapHIDCoordinator _callbackQueue];
-[SBCoreSmartPowerNapHIDCoordinator _digitizerAssertion];
-[SBCoreSmartPowerNapHIDCoordinator _handleState:];
-[SBCoreSmartPowerNapHIDCoordinator _handleStateForTesting:];
-[SBCoreSmartPowerNapHIDCoordinator _handleStateOnMainQueue:];
-[SBCoreSmartPowerNapHIDCoordinator _noteSmartCoverDidOpenOnMain];
-[SBCoreSmartPowerNapHIDCoordinator _userPresenceLatch];
-[SBCoreSmartPowerNapHIDCoordinator initWithWindowSceneManager:cspn:];
-[SBCoreSmartPowerNapHIDCoordinator noteSmartCoverDidOpen];
```
