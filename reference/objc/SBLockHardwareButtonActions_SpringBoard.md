# `SBLockHardwareButtonActions`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBHardwareButtonGestureParametersProviderBase`
- Protocols: `SBHardwareButtonGestureParametersObserver`
- 16 instance variables, 10 properties, 49 instance methods, 0 class methods

## Instance variables

```
q _homeButtonType;
@"SBApplication" _lastLockButtonEventRecipient;
@"SBProximitySensorCoordinator" _proximitySensorCoordinator;
@"SBHardwareButtonService" _hardwareButtonService;
@"SBWalletPreArmController" _walletPreArmController;
@"SOSManager" _sosManager;
@"SBHardwareButtonGestureParameters" _accessibilityGestureParameters;
@"SBHardwareButtonGestureParameters" _siriGestureParameters;
@"SBHardwareButtonGestureParameters" _proximitySensorGestureParameters;
q _sosTriggerMechanism;
B _isButtonDown;
@"SBSiriHardwareButtonInteraction" _siriButtonInteraction;
@"SBAccessibilityHardwareButtonInteraction" _accessibilityButtonInteraction;
@"SBSleepWakeHardwareButtonInteraction" _sleepWakeButtonInteraction;
@"<SBHardwareButtonInteraction><SBHardwareButtonGestureParametersProvider>" _proximitySensorButtonInteraction;
@"SBWindowScene" _targetWindowScene;
```

## Properties

```
@property (T@"SBSiriHardwareButtonInteraction",&,N,V_siriButtonInteraction) siriButtonInteraction;
@property (T@"SBAccessibilityHardwareButtonInteraction",&,N,V_accessibilityButtonInteraction) accessibilityButtonInteraction;
@property (T@"SBSleepWakeHardwareButtonInteraction",&,N,V_sleepWakeButtonInteraction) sleepWakeButtonInteraction;
@property (T@"<SBHardwareButtonInteraction><SBHardwareButtonGestureParametersProvider>",&,N,V_proximitySensorButtonInteraction) proximitySensorButtonInteraction;
@property (T@"SBWindowScene",W,N,V_targetWindowScene) targetWindowScene;
@property (TB,R,N,V_isButtonDown) isButtonDown;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBLockHardwareButtonActions setAccessibilityButtonInteraction:];
-[SBLockHardwareButtonActions performLongPressActions];
-[SBLockHardwareButtonActions disallowsLongPressForReason:];
-[SBLockHardwareButtonActions _mesaLikePreArmsWithLock];
-[SBLockHardwareButtonActions disallowsTriplePressForReason:];
-[SBLockHardwareButtonActions performInitialButtonDownActions];
-[SBLockHardwareButtonActions _sendButtonEventToApp:down:];
-[SBLockHardwareButtonActions setProximitySensorButtonInteraction:];
-[SBLockHardwareButtonActions performSecondButtonDownActions];
-[SBLockHardwareButtonActions setTargetWindowScene:];
-[SBLockHardwareButtonActions _usesLockButtonForSecureIntent];
-[SBLockHardwareButtonActions performFinalButtonUpActions];
-[SBLockHardwareButtonActions siriButtonInteraction];
-[SBLockHardwareButtonActions _showPowerDownTransientOverlayOnForceReset];
-[SBLockHardwareButtonActions _registeredLockButtonAppsDidChange:];
-[SBLockHardwareButtonActions performSinglePressAction];
-[SBLockHardwareButtonActions _shouldWaitForDoublePress];
-[SBLockHardwareButtonActions sleepWakeButtonInteraction];
-[SBLockHardwareButtonActions _performSOSDidTriggerActions];
-[SBLockHardwareButtonActions performSOSGestureEndedActions];
-[SBLockHardwareButtonActions _sendButtonDownToRegisteredApp];
-[SBLockHardwareButtonActions hardwareButtonGestureParameters];
-[SBLockHardwareButtonActions provider:didUpdateButtonGestureParameters:];
-[SBLockHardwareButtonActions performTriplePressActions];
-[SBLockHardwareButtonActions setSleepWakeButtonInteraction:];
-[SBLockHardwareButtonActions performSinglePressDidFailActions];
-[SBLockHardwareButtonActions performSOSGestureBeganActions];
-[SBLockHardwareButtonActions isButtonDown];
-[SBLockHardwareButtonActions reverseFadeOutIfNeeded];
-[SBLockHardwareButtonActions _usesLockButtonForSiri];
-[SBLockHardwareButtonActions initWithHomeButtonType:proximitySensorCoordinator:];
-[SBLockHardwareButtonActions disallowsDoublePressForReason:];
-[SBLockHardwareButtonActions performSOSActionsWithUUID:triggerMechanism:completion:];
-[SBLockHardwareButtonActions setSiriButtonInteraction:];
-[SBLockHardwareButtonActions performInitialButtonUpActions];
-[SBLockHardwareButtonActions performButtonUpPreActions];
-[SBLockHardwareButtonActions performTerminalLockLongPressActions];
-[SBLockHardwareButtonActions accessibilityButtonInteraction];
-[SBLockHardwareButtonActions targetWindowScene];
-[SBLockHardwareButtonActions performDoublePressActions];
-[SBLockHardwareButtonActions _isSOSActive];
-[SBLockHardwareButtonActions performLongPressCancelledActions];
-[SBLockHardwareButtonActions disallowsSinglePressForReason:];
-[SBLockHardwareButtonActions performKeyboardShortcut];
-[SBLockHardwareButtonActions _sendButtonUpToRegisteredApp];
-[SBLockHardwareButtonActions shouldBeginDoublePressGestureWhileObjectWithinProximity];
-[SBLockHardwareButtonActions _foregroundAppRegisteredForLockButtonEvents];
-[SBLockHardwareButtonActions performForceResetSequenceBeganActions];
-[SBLockHardwareButtonActions proximitySensorButtonInteraction];
```
