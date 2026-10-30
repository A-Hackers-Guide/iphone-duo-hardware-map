# `SBAssistantIslandActivityElementViewProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemApertureLayoutCustomizing`, `SBSystemApertureContextProviding`, `SAUIElementViewProviding`, `SAUIContentTransitioning`, `SAUILayoutSpecifying`, `SAUICooperativeTransitioning`
- 16 instance variables, 33 properties, 42 instance methods, 0 class methods

## Instance variables

```
@"SBAssistantIslandActivityElement" _element;
@"SBSystemApertureSceneElementAccessoryView" _portalView;
@"SBSystemApertureSceneElementAccessoryView" _minimalPortalView;
Q _sourceLayerRenderingId;
I _sourceLayerContextId;
d _accessoryViewSize;
@"<SAInvalidatable>" _cooperativeTransitionAssertionToken;
B _displayedWithLimitedSize;
B _hasPortalContent;
q _layoutMode;
q _preferredLayoutMode;
@"<SAUILayoutHosting>" _layoutHost;
@"<SAUICooperativeTransitionHosting>" _cooperativeTransitionHost;
@"<SBAssistantIslandActivityElementViewProviderDelegate>" _delegate;
d _preferredAvoidanceCornerRadius;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _preferredAvoidanceRect;
```

## Properties

```
@property (T@"<SBAssistantIslandActivityElementViewProviderDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,V_hasPortalContent) hasPortalContent;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_preferredAvoidanceRect) preferredAvoidanceRect;
@property (Td,N,V_preferredAvoidanceCornerRadius) preferredAvoidanceCornerRadius;
@property (Tq,?,R,N) systemApertureCustomLayout;
@property (Tq,?,R,N) customLayoutRequestingSpecialFlowerBoundsResizingAnimation;
@property (Tq,?,R,N) systemApertureLayoutCustomizingOptions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,?,R,N,GisAffiliatedWithSessionMonitor) affiliatedWithSessionMonitor;
@property (T@"UIColor",?,R,N) keyColor;
@property (T@"FBScene",?,R,N) scene;
@property (TB,?,R,N) preventsSwipeToHide;
@property (TB,?,R,N) inhibitsIndicatorMitosis;
@property (Td,?,R,N) preferredSystemClipPadding;
@property (T@"UIView",R,N) leadingView;
@property (T@"UIView",R,N) trailingView;
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
-[SBAssistantIslandActivityElementViewProvider setDisplayedWithLimitedSize:];
-[SBAssistantIslandActivityElementViewProvider layoutHost];
-[SBAssistantIslandActivityElementViewProvider minimalView];
-[SBAssistantIslandActivityElementViewProvider trailingView];
-[SBAssistantIslandActivityElementViewProvider overridesConcentricPaddingForView:inLayoutMode:];
-[SBAssistantIslandActivityElementViewProvider requestCooperativeTransitionAssertionIfNeeded];
-[SBAssistantIslandActivityElementViewProvider setLayoutMode:reason:];
-[SBAssistantIslandActivityElementViewProvider concentricPaddingOverrideForView:inLayoutMode:];
-[SBAssistantIslandActivityElementViewProvider layoutMode];
-[SBAssistantIslandActivityElementViewProvider leadingView];
-[SBAssistantIslandActivityElementViewProvider setLayoutHost:];
-[SBAssistantIslandActivityElementViewProvider isFixedInOrientation];
-[SBAssistantIslandActivityElementViewProvider systemApertureCustomLayout];
-[SBAssistantIslandActivityElementViewProvider preferredAvoidanceCornerRadius];
-[SBAssistantIslandActivityElementViewProvider preferredAlertingDuration:];
-[SBAssistantIslandActivityElementViewProvider setPreferredAvoidanceRect:];
-[SBAssistantIslandActivityElementViewProvider element];
-[SBAssistantIslandActivityElementViewProvider preferredLayoutMode];
-[SBAssistantIslandActivityElementViewProvider preferredEdgeOutsetsForLayoutMode:suggestedOutsets:maximumOutsets:];
-[SBAssistantIslandActivityElementViewProvider isDisplayedWithLimitedSize];
-[SBAssistantIslandActivityElementViewProvider requestCooperativeTransitionAssertion];
-[SBAssistantIslandActivityElementViewProvider initWithElement:];
-[SBAssistantIslandActivityElementViewProvider preferredAvoidanceRect];
-[SBAssistantIslandActivityElementViewProvider handleElementViewEvent:];
-[SBAssistantIslandActivityElementViewProvider setSourceLayerRenderingId:contextId:];
-[SBAssistantIslandActivityElementViewProvider sizeThatFitsSize:forProvidedView:inLayoutMode:];
-[SBAssistantIslandActivityElementViewProvider cooperativeTransitionHost];
-[SBAssistantIslandActivityElementViewProvider beginCooperativeDismissal];
-[SBAssistantIslandActivityElementViewProvider _canShowWhileLocked];
-[SBAssistantIslandActivityElementViewProvider setDelegate:];
-[SBAssistantIslandActivityElementViewProvider _updatePortalContents];
-[SBAssistantIslandActivityElementViewProvider delegate];
-[SBAssistantIslandActivityElementViewProvider hasPortalContent];
-[SBAssistantIslandActivityElementViewProvider description];
-[SBAssistantIslandActivityElementViewProvider minimumSupportedLayoutMode];
-[SBAssistantIslandActivityElementViewProvider setPreferredAvoidanceCornerRadius:];
-[SBAssistantIslandActivityElementViewProvider invalidateCooperativeTransitionAssertion];
-[SBAssistantIslandActivityElementViewProvider contentProviderWillTransitionToSize:inContainerView:transitionCoordinator:];
-[SBAssistantIslandActivityElementViewProvider layoutHostContainerViewWillLayoutSubviews:];
-[SBAssistantIslandActivityElementViewProvider maximumSupportedLayoutMode];
-[SBAssistantIslandActivityElementViewProvider setCooperativeTransitionHost:];
-[SBAssistantIslandActivityElementViewProvider setAccessoryViewSize:];
```
