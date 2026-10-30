# `SBDashBoardApplicationHostableEntity`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSceneHandleObserver`, `CSAppHostContextProviding`, `SBDashBoardHostedAppViewControllerDelegate`, `CSHostableEntity`
- 2 instance variables, 11 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"_SBDashBoardHostedAppEntityViewController" _hostedAppViewController;
@"SBApplicationSceneEntity" _applicationSceneEntity;
```

## Properties

```
@property (T@"SBApplicationSceneEntity",R,N,V_applicationSceneEntity) applicationSceneEntity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,N) hostedAppBundleIdentifier;
@property (TB,R,N) hostedAppShouldHideHomeGrabberView;
@property (T@"CSCoverSheetViewControllerBase<CSCoverSheetViewPresenting><CSHostableEntityPresenting><BSInvalidatable>",R,N) hostingViewController;
@property (Tq,R,N) presentationPriority;
@property (T@"SBDisplayItem",R,N) displayItemRepresentation;
@property (T@"NSString",R,C,N) applicationBundleIdentifier;
```

## Instance methods

```
-[SBDashBoardApplicationHostableEntity sceneHandle:didDestroyScene:];
-[SBDashBoardApplicationHostableEntity sceneHandle:clientConnectedForScene:];
-[SBDashBoardApplicationHostableEntity hostedAppBundleIdentifier];
-[SBDashBoardApplicationHostableEntity initWithApplicationSceneEntity:];
-[SBDashBoardApplicationHostableEntity hostedAppShouldHideHomeGrabberView];
-[SBDashBoardApplicationHostableEntity dashBoardHostedAppViewControllerDidFailToActivateApplication:];
-[SBDashBoardApplicationHostableEntity applicationSceneEntity];
-[SBDashBoardApplicationHostableEntity presentationPriority];
-[SBDashBoardApplicationHostableEntity hostingContainerViewController];
-[SBDashBoardApplicationHostableEntity displayItemRepresentation];
-[SBDashBoardApplicationHostableEntity applicationBundleIdentifier];
-[SBDashBoardApplicationHostableEntity hostingViewController];
```
