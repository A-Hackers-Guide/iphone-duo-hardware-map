# `SBDashBoardSetupController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSExternalBehaviorProviding`, `CSExternalEventHandling`, `SBLockScreenSetupControlling`
- 6 instance variables, 12 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"CSCoverSheetViewController" _coverSheetViewController;
@"SBApplicationController" _applicationController;
@"SBSetupManager" _setupManager;
@"SBWindowScene" _windowScene;
B _isOnActiveDisplay;
@"SBDashBoardSetupViewController" _setupViewController;
```

## Properties

```
@property (T@"SBDashBoardSetupViewController",&,N,V_setupViewController) setupViewController;
@property (Tq,R,N) scrollingStrategy;
@property (Tq,R,N) notificationBehavior;
@property (TQ,R,N) restrictedCapabilities;
@property (Tq,R,N) proximityDetectionMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) coverSheetIdentifier;
@property (Tq,R,N) participantState;
@property (TB,R,N,GisPresentingSetupView) presentingSetupView;
```

## Instance methods

```
-[SBDashBoardSetupController handleEvent:];
-[SBDashBoardSetupController wouldHandleButtonEvent:];
-[SBDashBoardSetupController conformsToCSBehaviorProviding];
-[SBDashBoardSetupController init];
-[SBDashBoardSetupController dealloc];
-[SBDashBoardSetupController proximityDetectionMode];
-[SBDashBoardSetupController scrollingStrategy];
-[SBDashBoardSetupController notificationBehavior];
-[SBDashBoardSetupController conformsToCSExternalBehaviorProviding];
-[SBDashBoardSetupController conformsToCSEventHandling];
-[SBDashBoardSetupController coverSheetIdentifier];
-[SBDashBoardSetupController participantState];
-[SBDashBoardSetupController restrictedCapabilities];
-[SBDashBoardSetupController setSetupViewController:];
-[SBDashBoardSetupController setupViewController];
-[SBDashBoardSetupController quickFadeCursiveHelloToVisible:];
-[SBDashBoardSetupController _addOrRemoveSetupViewIfNecessaryAnimated:setupViewController:completion:];
-[SBDashBoardSetupController _clearSetupViewIfNecessaryAnimated:completion:];
-[SBDashBoardSetupController _configureForCurrentSetupMode];
-[SBDashBoardSetupController _setupModeChanged:];
-[SBDashBoardSetupController clearSetupViewForInactiveDisplay];
-[SBDashBoardSetupController initWithCoverSheetViewController:setupManager:applicationController:windowScene:];
-[SBDashBoardSetupController isPresentingSetupView];
-[SBDashBoardSetupController presentSetupViewIfNecessaryFromSourceController:completion:];
```
