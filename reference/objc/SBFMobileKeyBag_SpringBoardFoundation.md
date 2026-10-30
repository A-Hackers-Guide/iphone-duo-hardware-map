# `SBFMobileKeyBag`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 7 properties, 31 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _calloutQueue;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableArray" _queue_observerStateChangedCallbackBlocks;
@"NSHashTable" _queue_observers;
@"NSMutableArray" _queue_performAfterFirstUnlockBlocks;
B _queue_hasPasscodeSet;
B _queue_hasUnlockedSinceBoot;
^{_AKSEvent=} _aksEvent;
```

## Properties

```
@property (T@"SBFMobileKeyBagState",R,C,N) state;
@property (T@"SBFMobileKeyBagState",R,C,N) extendedState;
@property (TB,R,N) hasBeenUnlockedSinceBoot;
@property (TB,R,N) hasPasscodeSet;
@property (Tq,R,N) maxUnlockAttempts;
@property (TB,R,N) isContinuityUnlocked;
@property (TB,R,N) isInStoreDemoMode;
```

## Class methods

```
+[SBFMobileKeyBag sharedInstance];
```

## Instance methods

```
-[SBFMobileKeyBag removeObserver:];
-[SBFMobileKeyBag init];
-[SBFMobileKeyBag dealloc];
-[SBFMobileKeyBag addObserver:];
-[SBFMobileKeyBag hasPasscodeSet];
-[SBFMobileKeyBag hasBeenUnlockedSinceBoot];
-[SBFMobileKeyBag state];
-[SBFMobileKeyBag extendedState];
-[SBFMobileKeyBag _queue_aksDeviceState];
-[SBFMobileKeyBag _queue_createStashBag:skipSEKeepUserDataOperation:];
-[SBFMobileKeyBag _queue_firstUnlockOccurred];
-[SBFMobileKeyBag _queue_handleKeybagStatusChanged];
-[SBFMobileKeyBag _queue_isContinuityUnlocked];
-[SBFMobileKeyBag _queue_keyBagInfo];
-[SBFMobileKeyBag _queue_lockStateExtended:];
-[SBFMobileKeyBag _queue_setHasPasscodeIfNecessary:];
-[SBFMobileKeyBag _queue_verifyExpectedStashState:];
-[SBFMobileKeyBag _shouldHandleKeyBagEventWithHandleState:];
-[SBFMobileKeyBag beginRecovery:error:];
-[SBFMobileKeyBag createStashBagWithOptions:completion:];
-[SBFMobileKeyBag createStashBagWithOptions:completion:completionQueue:];
-[SBFMobileKeyBag isContinuityUnlocked];
-[SBFMobileKeyBag isInStoreDemoMode];
-[SBFMobileKeyBag lockSkippingGracePeriod:];
-[SBFMobileKeyBag lockSkippingGracePeriod:endingContinuityUnlock:];
-[SBFMobileKeyBag maxUnlockAttempts];
-[SBFMobileKeyBag performAfterFirstUnlockSinceBootUsingBlock:];
-[SBFMobileKeyBag refreshContinuityUnlockHeartbeat];
-[SBFMobileKeyBag unlockWithOptions:error:];
-[SBFMobileKeyBag verifyWithOptions:error:];
-[SBFMobileKeyBag waitForUnlockWithTimeout:];
```
