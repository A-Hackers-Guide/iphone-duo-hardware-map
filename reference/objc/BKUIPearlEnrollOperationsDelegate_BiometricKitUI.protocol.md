# `BKUIPearlEnrollOperationsDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 1 properties, 26 instance methods, 0 class methods

## Properties

```
@property (Ti,R,N) state;
```

## Instance methods

```
-[BKUIPearlEnrollOperationsDelegate presentViewController:animated:completion:];
-[BKUIPearlEnrollOperationsDelegate setState:animated:];
-[BKUIPearlEnrollOperationsDelegate substate];
-[BKUIPearlEnrollOperationsDelegate previousState];
-[BKUIPearlEnrollOperationsDelegate view];
-[BKUIPearlEnrollOperationsDelegate setStatus:];
-[BKUIPearlEnrollOperationsDelegate state];
-[BKUIPearlEnrollOperationsDelegate updateButtonsVisibility];
-[BKUIPearlEnrollOperationsDelegate audioManager];
-[BKUIPearlEnrollOperationsDelegate setProgressString:];
-[BKUIPearlEnrollOperationsDelegate percentOfPillsCompleted];
-[BKUIPearlEnrollOperationsDelegate _updateDebugLabel];
-[BKUIPearlEnrollOperationsDelegate setSubstate:];
-[BKUIPearlEnrollOperationsDelegate removeGlassesUI];
-[BKUIPearlEnrollOperationsDelegate _endEnrollFlowWithError:];
-[BKUIPearlEnrollOperationsDelegate cleanupEnrollView];
-[BKUIPearlEnrollOperationsDelegate clearPendingStateWorkItems];
-[BKUIPearlEnrollOperationsDelegate endEnrollFlowWithError:];
-[BKUIPearlEnrollOperationsDelegate enrollOperation:finishedWithIdentity:animateImmediately:];
-[BKUIPearlEnrollOperationsDelegate getEnrollview];
-[BKUIPearlEnrollOperationsDelegate invalidateSubstateTimer];
-[BKUIPearlEnrollOperationsDelegate pearlEnrollControllerCompleted];
-[BKUIPearlEnrollOperationsDelegate refreshEscapeHatchForCurrentState];
-[BKUIPearlEnrollOperationsDelegate setState:animated:afterDelay:];
-[BKUIPearlEnrollOperationsDelegate setSubstate:animated:afterDelay:];
-[BKUIPearlEnrollOperationsDelegate showMaskAndGlassesTutorialWithCompletion:];
```
