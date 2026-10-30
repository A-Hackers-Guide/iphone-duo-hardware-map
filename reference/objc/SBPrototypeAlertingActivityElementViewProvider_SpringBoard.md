# `SBPrototypeAlertingActivityElementViewProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemApertureContextProviding`, `SAUIElementViewProviding`, `SAUIContentTransitioning`, `SAUILayoutSpecifying`, `SAUICooperativeTransitioning`
- 16 instance variables, 29 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"SBPrototypeAlertingActivityElement" _element;
@ _destinationToken;
q _viewProviderIndex;
@"UIView" _leadingView;
@"UIView" _trailingView;
@"UIView" _minimalView;
@"UIView" _redSquareView;
B _pendingFadeIn;
B _isFadingOut;
@"<SAInvalidatable>" _cooperativeTransitionAssertionToken;
B _displayedWithLimitedSize;
B _needsDistinction;
q _layoutMode;
q _preferredLayoutMode;
@"<SAUILayoutHosting>" _layoutHost;
@"<SAUICooperativeTransitionHosting>" _cooperativeTransitionHost;
```

## Properties

```
@property (TB,N,V_needsDistinction) needsDistinction;
@property (TB,?,R,N,GisAffiliatedWithSessionMonitor) affiliatedWithSessionMonitor;
@property (T@"UIColor",?,R,N) keyColor;
@property (T@"FBScene",?,R,N) scene;
@property (TB,?,R,N) preventsSwipeToHide;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) preferredAvoidanceRect;
@property (Td,?,R,N) preferredAvoidanceCornerRadius;
@property (TB,?,R,N) inhibitsIndicatorMitosis;
@property (Td,?,R,N) preferredSystemClipPadding;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,N,V_leadingView) leadingView;
@property (T@"UIView",R,N,V_trailingView) trailingView;
@property (T@"UIView",R,N) minimalView;
@property (T@"UIView",?,R,N) detachedMinimalView;
@property (T@"<SAElement>",R,W,N) element;
@property (TQ,?,N) layoutAxis;
@property (Tq,R,N,V_layoutMode) layoutMode;
@property (Tq,R,N) minimumSupportedLayoutMode;
@property (Tq,R,N) maximumSupportedLayoutMode;
@property (Tq,R,N,V_preferredLayoutMode) preferredLayoutMode;
@property (T@"<SAUILayoutHosting>",?,W,N,V_layoutHost) layoutHost;
@property (TB,?,R,N,GisInteractiveDismissalEnabled) interactiveDismissalEnabled;
@property (TB,?,R,N,GisMinimalPresentationPossible) minimalPresentationPossible;
@property (TB,?,R,N,GisRequestingMenuPresentation) requestingMenuPresentation;
@property (TB,?,N,GisDisplayedWithLimitedSize,V_displayedWithLimitedSize) displayedWithLimitedSize;
@property (T@"<SAUICooperativeTransitionHosting>",W,N,V_cooperativeTransitionHost) cooperativeTransitionHost;
```

## Instance methods

```
-[SBPrototypeAlertingActivityElementViewProvider setDisplayedWithLimitedSize:];
-[SBPrototypeAlertingActivityElementViewProvider layoutHost];
-[SBPrototypeAlertingActivityElementViewProvider keyColor];
-[SBPrototypeAlertingActivityElementViewProvider minimalView];
-[SBPrototypeAlertingActivityElementViewProvider trailingView];
-[SBPrototypeAlertingActivityElementViewProvider setLayoutMode:reason:];
-[SBPrototypeAlertingActivityElementViewProvider layoutMode];
-[SBPrototypeAlertingActivityElementViewProvider leadingView];
-[SBPrototypeAlertingActivityElementViewProvider setLayoutHost:];
-[SBPrototypeAlertingActivityElementViewProvider isRequestingMenuPresentation];
-[SBPrototypeAlertingActivityElementViewProvider element];
-[SBPrototypeAlertingActivityElementViewProvider preferredLayoutMode];
-[SBPrototypeAlertingActivityElementViewProvider preferredEdgeOutsetsForLayoutMode:suggestedOutsets:maximumOutsets:];
-[SBPrototypeAlertingActivityElementViewProvider isDisplayedWithLimitedSize];
-[SBPrototypeAlertingActivityElementViewProvider handleElementViewEvent:];
-[SBPrototypeAlertingActivityElementViewProvider sizeThatFitsSize:forProvidedView:inLayoutMode:];
-[SBPrototypeAlertingActivityElementViewProvider cooperativeTransitionHost];
-[SBPrototypeAlertingActivityElementViewProvider beginCooperativeDismissal];
-[SBPrototypeAlertingActivityElementViewProvider _canShowWhileLocked];
-[SBPrototypeAlertingActivityElementViewProvider minimumSupportedLayoutMode];
-[SBPrototypeAlertingActivityElementViewProvider contentProviderWillTransitionToSize:inContainerView:transitionCoordinator:];
-[SBPrototypeAlertingActivityElementViewProvider layoutHostContainerViewWillLayoutSubviews:];
-[SBPrototypeAlertingActivityElementViewProvider maximumSupportedLayoutMode];
-[SBPrototypeAlertingActivityElementViewProvider setCooperativeTransitionHost:];
-[SBPrototypeAlertingActivityElementViewProvider initWithElement:index:destinationToken:];
-[SBPrototypeAlertingActivityElementViewProvider needsDistinction];
-[SBPrototypeAlertingActivityElementViewProvider preventsSwipeToHide];
-[SBPrototypeAlertingActivityElementViewProvider setNeedsDistinction:];
```
