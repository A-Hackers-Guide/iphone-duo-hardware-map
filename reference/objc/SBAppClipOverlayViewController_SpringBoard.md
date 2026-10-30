# `SBAppClipOverlayViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFTouchPassThroughViewController`
- Protocols: `SBAppClipOverlayCoordinatorParticipant`, `SBAppClipOverlayViewDelegate`, `BSInvalidatable`
- 8 instance variables, 12 properties, 31 instance methods, 0 class methods

## Instance variables

```
B _displayedOverPlaceholder;
B _needsUpdate;
@"NSString" _bundleIdentifier;
@"NSString" _sceneIdentifier;
@"NSString" _webClipIdentifier;
@"SBAppClipOverlayCoordinator" _coordinator;
@"CPSClipOverlayViewController" _overlayViewController;
q _sceneActivationState;
```

## Properties

```
@property (T@"NSString",&,N,V_webClipIdentifier) webClipIdentifier;
@property (T@"SBAppClipOverlayCoordinator",&,N,V_coordinator) coordinator;
@property (T@"CPSClipOverlayViewController",&,N,V_overlayViewController) overlayViewController;
@property (TB,N,V_displayedOverPlaceholder) displayedOverPlaceholder;
@property (Tq,N,V_sceneActivationState) sceneActivationState;
@property (TB,N,V_needsUpdate) needsUpdate;
@property (T@"NSString",R,C,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSString",R,C,N,V_sceneIdentifier) sceneIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAppClipOverlayViewController needsUpdate];
-[SBAppClipOverlayViewController bundleIdentifier];
-[SBAppClipOverlayViewController setCoordinator:];
-[SBAppClipOverlayViewController viewDidLayoutSubviews];
-[SBAppClipOverlayViewController initWithNibName:bundle:];
-[SBAppClipOverlayViewController webClipIdentifier];
-[SBAppClipOverlayViewController viewWillAppear:];
-[SBAppClipOverlayViewController sceneIdentifier];
-[SBAppClipOverlayViewController invalidate];
-[SBAppClipOverlayViewController view];
-[SBAppClipOverlayViewController loadView];
-[SBAppClipOverlayViewController description];
-[SBAppClipOverlayViewController viewDidDisappear:];
-[SBAppClipOverlayViewController participantName];
-[SBAppClipOverlayViewController initWithCoder:];
-[SBAppClipOverlayViewController setNeedsUpdate];
-[SBAppClipOverlayViewController preferredStatusBarStyle];
-[SBAppClipOverlayViewController coordinator];
-[SBAppClipOverlayViewController setNeedsUpdate:];
-[SBAppClipOverlayViewController overlayViewController];
-[SBAppClipOverlayViewController setWebClipIdentifier:];
-[SBAppClipOverlayViewController setSceneActivationState:animated:];
-[SBAppClipOverlayViewController appClipOverlayCoordinator:requestsSurrenderOfViewController:];
-[SBAppClipOverlayViewController appClipPlaceholderViewDidInvalidate:];
-[SBAppClipOverlayViewController displayedOverPlaceholder];
-[SBAppClipOverlayViewController initWithCoordinator:bundleIdentifier:sceneIdentifier:];
-[SBAppClipOverlayViewController sceneActivationState];
-[SBAppClipOverlayViewController setDisplayedOverPlaceholder:];
-[SBAppClipOverlayViewController setDisplayedOverPlaceholder:animated:];
-[SBAppClipOverlayViewController setOverlayViewController:];
-[SBAppClipOverlayViewController setSceneActivationState:];
```
