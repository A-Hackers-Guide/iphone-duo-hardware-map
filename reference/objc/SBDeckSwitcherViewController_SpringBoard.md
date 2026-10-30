# `SBDeckSwitcherViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFluidSwitcherViewController`
- Protocols: `SBSwitcherAppSuggestionViewControllerDelegate`
- 2 instance variables, 6 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"SBSwitcherAppSuggestionViewController" _appSuggestionController;
@"SBAppSuggestionManager" _appSuggestionManager;
```

## Properties

```
@property (T@"SBSwitcherAppSuggestionViewController",&,N,V_appSuggestionController) appSuggestionController;
@property (T@"SBAppSuggestionManager",W,N,V_appSuggestionManager) appSuggestionManager;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDeckSwitcherViewController layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:];
-[SBDeckSwitcherViewController setBestAppSuggestion:];
-[SBDeckSwitcherViewController _setBestAppSuggestion:animationCompletion:];
-[SBDeckSwitcherViewController invalidate];
-[SBDeckSwitcherViewController layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:];
-[SBDeckSwitcherViewController bestAppSuggestion];
-[SBDeckSwitcherViewController viewWillLayoutSubviews];
-[SBDeckSwitcherViewController handleFluidSwitcherGestureManager:didBeginGesture:];
-[SBDeckSwitcherViewController performTransitionWithContext:animated:completion:];
-[SBDeckSwitcherViewController _assertionReason];
-[SBDeckSwitcherViewController appSuggestionController];
-[SBDeckSwitcherViewController appSuggestionManager];
-[SBDeckSwitcherViewController initWithPersonality:liveContentOverlayCoordinator:dataSource:delegate:applicationController:pictureInPictureCoordinator:debugName:];
-[SBDeckSwitcherViewController orientationForSuggestionViewController:];
-[SBDeckSwitcherViewController setAppSuggestionController:];
-[SBDeckSwitcherViewController setAppSuggestionManager:];
-[SBDeckSwitcherViewController suggestionViewController:activatedSuggestion:];
```
