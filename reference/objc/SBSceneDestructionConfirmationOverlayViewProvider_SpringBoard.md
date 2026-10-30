# `SBSceneDestructionConfirmationOverlayViewProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBDeviceApplicationSceneOverlayViewProvider`
- Protocols: `SBSceneDestructionConfirmationViewControllerDelegate`, `SBDeviceApplicationSceneHandleObserver`
- 2 instance variables, 6 properties, 20 instance methods, 2 class methods

## Instance variables

```
@? _pendingCompletionHandler;
@"SBSceneDestructionConfirmationViewController" _confirmationViewController;
```

## Properties

```
@property (T@?,C,N,V_pendingCompletionHandler) pendingCompletionHandler;
@property (T@"SBSceneDestructionConfirmationViewController",&,N,V_confirmationViewController) confirmationViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSceneDestructionConfirmationOverlayViewProvider _providersByHandle];
+[SBSceneDestructionConfirmationOverlayViewProvider providerForSceneHandle:];
```

## Instance methods

```
-[SBSceneDestructionConfirmationOverlayViewProvider sceneHandle:didCreateScene:];
-[SBSceneDestructionConfirmationOverlayViewProvider priority];
-[SBSceneDestructionConfirmationOverlayViewProvider _realOverlayViewController];
-[SBSceneDestructionConfirmationOverlayViewProvider contentWantsSimplifiedOrientationBehavior];
-[SBSceneDestructionConfirmationOverlayViewProvider dealloc];
-[SBSceneDestructionConfirmationOverlayViewProvider initWithSceneHandle:delegate:];
-[SBSceneDestructionConfirmationOverlayViewProvider _activateIfPossible];
-[SBSceneDestructionConfirmationOverlayViewProvider invalidate];
-[SBSceneDestructionConfirmationOverlayViewProvider wantsResignActiveAssertion];
-[SBSceneDestructionConfirmationOverlayViewProvider shouldSuppressKeyboard];
-[SBSceneDestructionConfirmationOverlayViewProvider pendingCompletionHandler];
-[SBSceneDestructionConfirmationOverlayViewProvider setPendingCompletionHandler:];
-[SBSceneDestructionConfirmationOverlayViewProvider confirmationViewController];
-[SBSceneDestructionConfirmationOverlayViewProvider setConfirmationViewController:];
-[SBSceneDestructionConfirmationOverlayViewProvider _closureConfirmation];
-[SBSceneDestructionConfirmationOverlayViewProvider _finalizeSceneSessionWithActionIdentifier:completion:];
-[SBSceneDestructionConfirmationOverlayViewProvider _tearDownConfirmationViewController];
-[SBSceneDestructionConfirmationOverlayViewProvider confirmationViewController:didFinishWithResult:chosenAction:];
-[SBSceneDestructionConfirmationOverlayViewProvider confirmationViewControllerDidFinishDismissAnimation:];
-[SBSceneDestructionConfirmationOverlayViewProvider requestConfirmationWithCompletionHandler:];
```
