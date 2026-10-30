# `SBCarDoNotDisturbController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSExternalLockProviding`, `CSLockAlertPresenter`, `CSExternalEventHandling`, `CSExternalBehaviorProviding`, `SBLockScreenCoordinatorObserving`
- 9 instance variables, 14 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
B _queue_stateValid;
B _queue_exitConfirmationRequired;
B _queue_pendingExitConfirmationRequirement;
B _queue_screenOn;
@"CARAutomaticDNDStatus" _carAutomaticDNDStatus;
@"SBLockScreenCoordinator" _lockScreenCoordinator;
@"SBWindowSceneManager" _windowSceneManager;
@? alertDismissalHandler;
```

## Properties

```
@property (TB,R,N,GisLocked) locked;
@property (TB,R,N) showPasscode;
@property (TB,R,N) presentsAlert;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) coverSheetIdentifier;
@property (Tq,R,N) participantState;
@property (T@?,C,N,ValertDismissalHandler) alertDismissalHandler;
@property (Tq,R,N) scrollingStrategy;
@property (Tq,R,N) notificationBehavior;
@property (TQ,R,N) restrictedCapabilities;
@property (Tq,R,N) proximityDetectionMode;
```

## Instance methods

```
-[SBCarDoNotDisturbController unlockFromSource:];
-[SBCarDoNotDisturbController _setScreenOn:];
-[SBCarDoNotDisturbController handleEvent:];
-[SBCarDoNotDisturbController wouldHandleButtonEvent:];
-[SBCarDoNotDisturbController conformsToCSBehaviorProviding];
-[SBCarDoNotDisturbController isLocked];
-[SBCarDoNotDisturbController init];
-[SBCarDoNotDisturbController alertDismissalHandler];
-[SBCarDoNotDisturbController dealloc];
-[SBCarDoNotDisturbController proximityDetectionMode];
-[SBCarDoNotDisturbController _dismissAlertItemsAnimated:];
-[SBCarDoNotDisturbController _queue_setScreenOn:];
-[SBCarDoNotDisturbController _shouldExitConfirmationBeEnforced];
-[SBCarDoNotDisturbController scrollingStrategy];
-[SBCarDoNotDisturbController notificationBehavior];
-[SBCarDoNotDisturbController initWithCARAutomaticDNDStatus:windowSceneManager:lockScreenCoordinator:];
-[SBCarDoNotDisturbController lockScreenCoordinator:didAddLockScreenManager:];
-[SBCarDoNotDisturbController _queue_setExitConfirmationRequired:];
-[SBCarDoNotDisturbController initWithWindowSceneManager:lockScreenCoordinator:];
-[SBCarDoNotDisturbController presentsAlert];
-[SBCarDoNotDisturbController _isExitConfirmationRequired];
-[SBCarDoNotDisturbController conformsToCSExternalBehaviorProviding];
-[SBCarDoNotDisturbController conformsToCSEventHandling];
-[SBCarDoNotDisturbController coverSheetIdentifier];
-[SBCarDoNotDisturbController lockScreenCoordinator:didRemoveLockScreenManager:];
-[SBCarDoNotDisturbController showPasscode];
-[SBCarDoNotDisturbController setAlertDismissalHandler:];
-[SBCarDoNotDisturbController participantState];
-[SBCarDoNotDisturbController restrictedCapabilities];
```
