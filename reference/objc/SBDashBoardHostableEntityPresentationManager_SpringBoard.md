# `SBDashBoardHostableEntityPresentationManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDashBoardHostableEntityHostingFluidSwitcherViewControllerDelegate`
- 4 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"SBDashBoardHostableEntityHostingFluidSwitcherViewController" _switcherViewController;
B _isDismissingEntity;
@"NSMutableOrderedSet" _pendingPresentationRequests;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (TB,R,N) isPresentingEntity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDashBoardHostableEntityPresentationManager coverSheetViewController];
-[SBDashBoardHostableEntityPresentationManager setWindowScene:];
-[SBDashBoardHostableEntityPresentationManager initWithWindowScene:];
-[SBDashBoardHostableEntityPresentationManager windowScene];
-[SBDashBoardHostableEntityPresentationManager _canTransferFromSourceManager:];
-[SBDashBoardHostableEntityPresentationManager coordinateStateWithSourceHostableEntityPresentationManager:completion:];
-[SBDashBoardHostableEntityPresentationManager dashBoardHostableEntityFluidSwitcherViewControllerDidDismiss:];
-[SBDashBoardHostableEntityPresentationManager dismissEntity:completion:];
-[SBDashBoardHostableEntityPresentationManager isPresentingEntity];
-[SBDashBoardHostableEntityPresentationManager presentEntityWithRequest:];
```
