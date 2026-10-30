# `SBPrototypeAdvancedActivityElementViewProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemApertureContextProviding`, `SAUIElementViewProviding`, `SAUIContentTransitioning`, `SAUILayoutSpecifying`
- 11 instance variables, 28 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"SBPrototypeAdvancedActivityElement" _element;
@ _destinationToken;
q _viewProviderIndex;
B _layoutCondensed;
B _displayedWithLimitedSize;
B _needsDistinction;
@"UIView" _leadingView;
@"UIView" _trailingView;
q _layoutMode;
q _preferredLayoutMode;
@"<SAUILayoutHosting>" _layoutHost;
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
```

## Instance methods

```
-[SBPrototypeAdvancedActivityElementViewProvider setDisplayedWithLimitedSize:];
-[SBPrototypeAdvancedActivityElementViewProvider layoutHost];
-[SBPrototypeAdvancedActivityElementViewProvider keyColor];
-[SBPrototypeAdvancedActivityElementViewProvider minimalView];
-[SBPrototypeAdvancedActivityElementViewProvider trailingView];
-[SBPrototypeAdvancedActivityElementViewProvider setLayoutMode:reason:];
-[SBPrototypeAdvancedActivityElementViewProvider layoutMode];
-[SBPrototypeAdvancedActivityElementViewProvider leadingView];
-[SBPrototypeAdvancedActivityElementViewProvider setLayoutHost:];
-[SBPrototypeAdvancedActivityElementViewProvider element];
-[SBPrototypeAdvancedActivityElementViewProvider preferredLayoutMode];
-[SBPrototypeAdvancedActivityElementViewProvider preferredEdgeOutsetsForLayoutMode:suggestedOutsets:maximumOutsets:];
-[SBPrototypeAdvancedActivityElementViewProvider isDisplayedWithLimitedSize];
-[SBPrototypeAdvancedActivityElementViewProvider handleElementViewEvent:];
-[SBPrototypeAdvancedActivityElementViewProvider _updateLabel];
-[SBPrototypeAdvancedActivityElementViewProvider sizeThatFitsSize:forProvidedView:inLayoutMode:];
-[SBPrototypeAdvancedActivityElementViewProvider _canShowWhileLocked];
-[SBPrototypeAdvancedActivityElementViewProvider minimumSupportedLayoutMode];
-[SBPrototypeAdvancedActivityElementViewProvider contentProviderWillTransitionToSize:inContainerView:transitionCoordinator:];
-[SBPrototypeAdvancedActivityElementViewProvider layoutHostContainerViewWillLayoutSubviews:];
-[SBPrototypeAdvancedActivityElementViewProvider maximumSupportedLayoutMode];
-[SBPrototypeAdvancedActivityElementViewProvider _currentTrailingTitle];
-[SBPrototypeAdvancedActivityElementViewProvider _decrementLayoutMode];
-[SBPrototypeAdvancedActivityElementViewProvider _incrementLayoutMode];
-[SBPrototypeAdvancedActivityElementViewProvider _newTrailingLabel];
-[SBPrototypeAdvancedActivityElementViewProvider _requestSignificantTransition];
-[SBPrototypeAdvancedActivityElementViewProvider _updateLabel:forLayoutMode:];
-[SBPrototypeAdvancedActivityElementViewProvider initWithElement:index:destinationToken:];
-[SBPrototypeAdvancedActivityElementViewProvider needsDistinction];
-[SBPrototypeAdvancedActivityElementViewProvider setNeedsDistinction:];
```
