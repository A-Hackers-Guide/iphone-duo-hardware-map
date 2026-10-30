# `SBWorkspaceTransientOverlayTransitionContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWorkspaceTransitionContext`
- 9 instance variables, 9 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _animated;
B _shouldDismissSiriUponPresentation;
B _shouldPreserveAppSwitcher;
@"<SBTransientOverlayPresenting>" _scenePresenter;
@"SBTransientOverlayPresentationManager" _presentationManager;
@"SBWorkspaceTransientOverlay" _transientOverlay;
q _transitionType;
@"BSProcessHandle" _originatingProcess;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (TB,N,GisAnimated,V_animated) animated;
@property (TB,N,V_shouldDismissSiriUponPresentation) shouldDismissSiriUponPresentation;
@property (TB,N,V_shouldPreserveAppSwitcher) shouldPreserveAppSwitcher;
@property (T@"<SBTransientOverlayPresenting>",&,N,V_scenePresenter) scenePresenter;
@property (T@"SBTransientOverlayPresentationManager",&,N,V_presentationManager) presentationManager;
@property (T@"SBWorkspaceTransientOverlay",&,N,V_transientOverlay) transientOverlay;
@property (Tq,N,V_transitionType) transitionType;
@property (T@"BSProcessHandle",&,N,V_originatingProcess) originatingProcess;
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
```

## Instance methods

```
-[SBWorkspaceTransientOverlayTransitionContext setTransitionType:];
-[SBWorkspaceTransientOverlayTransitionContext scenePresenter];
-[SBWorkspaceTransientOverlayTransitionContext transitionType];
-[SBWorkspaceTransientOverlayTransitionContext transientOverlay];
-[SBWorkspaceTransientOverlayTransitionContext setWindowScene:];
-[SBWorkspaceTransientOverlayTransitionContext setShouldDismissSiriUponPresentation:];
-[SBWorkspaceTransientOverlayTransitionContext compactDescriptionBuilderWithMultilinePrefix:];
-[SBWorkspaceTransientOverlayTransitionContext init];
-[SBWorkspaceTransientOverlayTransitionContext isAnimated];
-[SBWorkspaceTransientOverlayTransitionContext shouldDismissSiriUponPresentation];
-[SBWorkspaceTransientOverlayTransitionContext originatingProcess];
-[SBWorkspaceTransientOverlayTransitionContext presentationManager];
-[SBWorkspaceTransientOverlayTransitionContext setAnimated:];
-[SBWorkspaceTransientOverlayTransitionContext setTransientOverlay:];
-[SBWorkspaceTransientOverlayTransitionContext setPresentationManager:];
-[SBWorkspaceTransientOverlayTransitionContext setScenePresenter:];
-[SBWorkspaceTransientOverlayTransitionContext windowScene];
-[SBWorkspaceTransientOverlayTransitionContext shouldPreserveAppSwitcher];
-[SBWorkspaceTransientOverlayTransitionContext setOriginatingProcess:];
-[SBWorkspaceTransientOverlayTransitionContext setShouldPreserveAppSwitcher:];
-[SBWorkspaceTransientOverlayTransitionContext descriptionBuilderWithMultilinePrefix:];
```
