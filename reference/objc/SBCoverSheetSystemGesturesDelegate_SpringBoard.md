# `SBCoverSheetSystemGesturesDelegate`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemGestureRecognizerDelegate`, `SBTouchTemplateGestureRecognizerDelegate`, `SBIndirectPanGestureRecognizerOrientationProviding`
- 13 instance variables, 17 properties, 45 instance methods, 0 class methods

## Instance variables

```
B _checkingGestureAvailabilityForNoninteractiveReason;
i _syntheticAppearState;
@"<SBCoverSheetSystemGestureDelegateContextProviding>" _contextProvider;
@"UIPanGestureRecognizer" _presentGestureRecognizer;
@"SBIndirectPanGestureRecognizer" _indirectPresentGestureRecognizer;
@"SBIndirectPanGestureRecognizer" _indirectDismissGestureRecognizer;
@"SBFluidScrunchGestureRecognizer" _scrunchDismissGestureRecognizer;
@"UIViewController" _viewController;
@"SBWindowScene" _windowScene;
@"UIGestureRecognizer" _dismissGestureRecognizer;
@"UIGestureRecognizer" _dismissAddendumGestureRecognizer;
@"UIGestureRecognizer" _preemptingGestureRecognizer;
@"CSCoverSheetDismissGestureSettings" _dismissGestureSettings;
```

## Properties

```
@property (T@"UIViewController",W,N,V_viewController) viewController;
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (T@"UIGestureRecognizer",W,N,V_dismissGestureRecognizer) dismissGestureRecognizer;
@property (T@"UIGestureRecognizer",W,N,V_dismissAddendumGestureRecognizer) dismissAddendumGestureRecognizer;
@property (T@"UIGestureRecognizer",W,N,V_preemptingGestureRecognizer) preemptingGestureRecognizer;
@property (T@"CSCoverSheetDismissGestureSettings",&,N,V_dismissGestureSettings) dismissGestureSettings;
@property (TB,N,V_checkingGestureAvailabilityForNoninteractiveReason) checkingGestureAvailabilityForNoninteractiveReason;
@property (T@"<SBCoverSheetSystemGestureDelegateContextProviding>",W,N,V_contextProvider) contextProvider;
@property (T@"UIPanGestureRecognizer",&,N,V_presentGestureRecognizer) presentGestureRecognizer;
@property (T@"SBIndirectPanGestureRecognizer",&,N,V_indirectPresentGestureRecognizer) indirectPresentGestureRecognizer;
@property (T@"SBIndirectPanGestureRecognizer",&,N,V_indirectDismissGestureRecognizer) indirectDismissGestureRecognizer;
@property (T@"SBFluidScrunchGestureRecognizer",&,N,V_scrunchDismissGestureRecognizer) scrunchDismissGestureRecognizer;
@property (Ti,N,V_syntheticAppearState) syntheticAppearState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBCoverSheetSystemGesturesDelegate setViewController:];
-[SBCoverSheetSystemGesturesDelegate preemptingGestureRecognizer];
-[SBCoverSheetSystemGesturesDelegate isAnyGestureActivelyRecognized];
-[SBCoverSheetSystemGesturesDelegate gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[SBCoverSheetSystemGesturesDelegate setWindowScene:];
-[SBCoverSheetSystemGesturesDelegate _canPresentGestureBegin];
-[SBCoverSheetSystemGesturesDelegate gestureRecognizer:shouldReceiveTouch:];
-[SBCoverSheetSystemGesturesDelegate setIndirectPresentGestureRecognizer:];
-[SBCoverSheetSystemGesturesDelegate presentGestures];
-[SBCoverSheetSystemGesturesDelegate dismissGestureRecognizer];
-[SBCoverSheetSystemGesturesDelegate _isGestureActivelyRecognized:];
-[SBCoverSheetSystemGesturesDelegate dismissGestures];
-[SBCoverSheetSystemGesturesDelegate isPresentGestureAllowedToBegin];
-[SBCoverSheetSystemGesturesDelegate setScrunchDismissGestureRecognizer:];
-[SBCoverSheetSystemGesturesDelegate setCheckingGestureAvailabilityForNoninteractiveReason:];
-[SBCoverSheetSystemGesturesDelegate setIndirectDismissGestureRecognizer:];
-[SBCoverSheetSystemGesturesDelegate setDismissGestureSettings:];
-[SBCoverSheetSystemGesturesDelegate viewForSystemGestureRecognizer:];
-[SBCoverSheetSystemGesturesDelegate syntheticAppearState];
-[SBCoverSheetSystemGesturesDelegate viewController];
-[SBCoverSheetSystemGesturesDelegate setContextProvider:];
-[SBCoverSheetSystemGesturesDelegate indirectPanEffectiveInterfaceOrientationInView:];
-[SBCoverSheetSystemGesturesDelegate isDismissGestureAllowedToBegin];
-[SBCoverSheetSystemGesturesDelegate scrunchDismissGestureRecognizer];
-[SBCoverSheetSystemGesturesDelegate isPresentGestureActive];
-[SBCoverSheetSystemGesturesDelegate gestureRecognizerShouldBegin:];
-[SBCoverSheetSystemGesturesDelegate contextProvider];
-[SBCoverSheetSystemGesturesDelegate _isGestureAllowedByTransientOverlaysOrTopmostApp];
-[SBCoverSheetSystemGesturesDelegate setPresentGestureRecognizer:];
-[SBCoverSheetSystemGesturesDelegate _areAnyGesturesRecognizedInSet:];
-[SBCoverSheetSystemGesturesDelegate gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[SBCoverSheetSystemGesturesDelegate checkingGestureAvailabilityForNoninteractiveReason];
-[SBCoverSheetSystemGesturesDelegate _canDismissGestureBegin];
-[SBCoverSheetSystemGesturesDelegate dismissAddendumGestureRecognizer];
-[SBCoverSheetSystemGesturesDelegate setSyntheticAppearState:];
-[SBCoverSheetSystemGesturesDelegate dismissGestureSettings];
-[SBCoverSheetSystemGesturesDelegate setPreemptingGestureRecognizer:];
-[SBCoverSheetSystemGesturesDelegate presentGestureRecognizer];
-[SBCoverSheetSystemGesturesDelegate isDismissGestureActive];
-[SBCoverSheetSystemGesturesDelegate setDismissAddendumGestureRecognizer:];
-[SBCoverSheetSystemGesturesDelegate indirectPresentGestureRecognizer];
-[SBCoverSheetSystemGesturesDelegate windowScene];
-[SBCoverSheetSystemGesturesDelegate initWithViewController:windowScene:dismissGestureRecognizer:dismissAddendumGestureRecognizer:dismissalPreemptingGestureRecognizer:];
-[SBCoverSheetSystemGesturesDelegate setDismissGestureRecognizer:];
-[SBCoverSheetSystemGesturesDelegate indirectDismissGestureRecognizer];
```
