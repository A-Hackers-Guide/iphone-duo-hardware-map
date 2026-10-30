# `SBSystemApertureProvidedContentElement`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SAUIElementViewProviding`, `SBUISystemApertureContentViewContaining`, `SBSystemActionCoordinatedElementPreviewing`, `SBSystemApertureElement`, `SAUIContentTransitioning`, `SAUILayoutObservable`, `SAUILayoutSpecifying`, `SBSystemApertureSuppressible`, `SBSystemApertureLayoutCustomizing`, `SBSystemActionElementPreviewing`
- 23 instance variables, 31 properties, 56 instance methods, 0 class methods

## Instance variables

```
@"<SBUISystemApertureContentProviding>" _contentProvider;
@"SBSystemActionElementPreviewingCoordinator" _previewingCoordinator;
@"NSHashTable" _observers;
@"UIView" _primaryView;
@"UIView" _secondaryView;
@"UIView" _actionView;
B _displayedWithLimitedSize;
B _previewing;
B _urgent;
B _expanding;
B _prominent;
@"NSString" _elementIdentifier;
@"NSString" _clientIdentifier;
@"<SAElementHosting>" _elementHost;
@"UIView" _leadingView;
@"UIView" _trailingView;
@"UIView" _minimalView;
q _layoutMode;
q _minimumSupportedLayoutMode;
q _maximumSupportedLayoutMode;
q _preferredLayoutMode;
@"<SAUILayoutHosting>" _layoutHost;
@"<SBSystemAperturePlatformElementHosting>" _platformElementHost;
```

## Properties

```
@property (Tq,N,V_minimumSupportedLayoutMode) minimumSupportedLayoutMode;
@property (Tq,N,V_maximumSupportedLayoutMode) maximumSupportedLayoutMode;
@property (Tq,N,V_preferredLayoutMode) preferredLayoutMode;
@property (T@"UIView",R,N,V_leadingView) leadingView;
@property (T@"UIView",R,N,V_trailingView) trailingView;
@property (T@"UIView",R,N,V_minimalView) minimalView;
@property (T@"UIView",?,R,N) detachedMinimalView;
@property (T@"<SAElement>",R,W,N) element;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,?,N) layoutAxis;
@property (TB,R,N,GisPreviewing) previewing;
@property (TB,R,N,GisUrgent) urgent;
@property (TB,R,N,GisExpanding) expanding;
@property (Tq,R,N,V_layoutMode) layoutMode;
@property (T@"<SBSystemAperturePlatformElementHosting>",?,W,N,V_platformElementHost) platformElementHost;
@property (T@"<SAElementHosting>",?,W,N,V_elementHost) elementHost;
@property (T@"NSString",R,C,N,V_clientIdentifier) clientIdentifier;
@property (T@"NSString",R,C,N,V_elementIdentifier) elementIdentifier;
@property (T@"<SAUILayoutHosting>",?,W,N,V_layoutHost) layoutHost;
@property (TB,?,R,N,GisInteractiveDismissalEnabled) interactiveDismissalEnabled;
@property (TB,?,R,N,GisMinimalPresentationPossible) minimalPresentationPossible;
@property (TB,?,R,N,GisRequestingMenuPresentation) requestingMenuPresentation;
@property (TB,?,N,GisDisplayedWithLimitedSize,V_displayedWithLimitedSize) displayedWithLimitedSize;
@property (TB,?,N,GisSuppressed) suppressed;
@property (Tq,?,R,N) systemApertureCustomLayout;
@property (Tq,?,R,N) customLayoutRequestingSpecialFlowerBoundsResizingAnimation;
@property (Tq,?,R,N) systemApertureLayoutCustomizingOptions;
@property (TB,N,GisProminent,V_prominent) prominent;
```

## Instance methods

```
-[SBSystemApertureProvidedContentElement pop];
-[SBSystemApertureProvidedContentElement setDisplayedWithLimitedSize:];
-[SBSystemApertureProvidedContentElement systemApertureLayoutCustomizingOptions];
-[SBSystemApertureProvidedContentElement layoutHost];
-[SBSystemApertureProvidedContentElement minimalView];
-[SBSystemApertureProvidedContentElement trailingView];
-[SBSystemApertureProvidedContentElement setLayoutMode:reason:];
-[SBSystemApertureProvidedContentElement removeElementLayoutSpecifierObserver:];
-[SBSystemApertureProvidedContentElement layoutMode];
-[SBSystemApertureProvidedContentElement leadingView];
-[SBSystemApertureProvidedContentElement setLayoutHost:];
-[SBSystemApertureProvidedContentElement isUrgent];
-[SBSystemApertureProvidedContentElement clientIdentifier];
-[SBSystemApertureProvidedContentElement element];
-[SBSystemApertureProvidedContentElement preferredLayoutMode];
-[SBSystemApertureProvidedContentElement preferredEdgeOutsetsForLayoutMode:suggestedOutsets:maximumOutsets:];
-[SBSystemApertureProvidedContentElement isDisplayedWithLimitedSize];
-[SBSystemApertureProvidedContentElement elementIdentifier];
-[SBSystemApertureProvidedContentElement viewProvider];
-[SBSystemApertureProvidedContentElement addElementLayoutSpecifierObserver:];
-[SBSystemApertureProvidedContentElement sizeThatFitsSize:forProvidedView:inLayoutMode:];
-[SBSystemApertureProvidedContentElement setPlatformElementHost:];
-[SBSystemApertureProvidedContentElement _canShowWhileLocked];
-[SBSystemApertureProvidedContentElement elementHost];
-[SBSystemApertureProvidedContentElement description];
-[SBSystemApertureProvidedContentElement minimumSupportedLayoutMode];
-[SBSystemApertureProvidedContentElement shouldSuppressElementWhileOnCoversheet];
-[SBSystemApertureProvidedContentElement layoutHostContainerViewDidLayoutSubviews:];
-[SBSystemApertureProvidedContentElement setUrgent:];
-[SBSystemApertureProvidedContentElement setProminent:];
-[SBSystemApertureProvidedContentElement contentProviderWillTransitionToSize:inContainerView:transitionCoordinator:];
-[SBSystemApertureProvidedContentElement isProminent];
-[SBSystemApertureProvidedContentElement isPreviewing];
-[SBSystemApertureProvidedContentElement setElementHost:];
-[SBSystemApertureProvidedContentElement maximumSupportedLayoutMode];
-[SBSystemApertureProvidedContentElement setPreviewing:];
-[SBSystemApertureProvidedContentElement platformElementHost];
-[SBSystemApertureProvidedContentElement setPreferredLayoutMode:];
-[SBSystemApertureProvidedContentElement isExpanding];
-[SBSystemApertureProvidedContentElement setExpanding:];
-[SBSystemApertureProvidedContentElement _actionView];
-[SBSystemApertureProvidedContentElement preferredContentSizeDidInvalidateForContentViewProvider:];
-[SBSystemApertureProvidedContentElement _edgeSpacingWithConcentricPositioningIfNecessaryForView:withFrame:inContainerView:];
-[SBSystemApertureProvidedContentElement _primaryView];
-[SBSystemApertureProvidedContentElement _secondaryView];
-[SBSystemApertureProvidedContentElement _sizeForEdgeView:thatFits:layoutMode:];
-[SBSystemApertureProvidedContentElement customEdgeSpacing];
-[SBSystemApertureProvidedContentElement dodgeSensorAreaOnIntrinsicContentSize];
-[SBSystemApertureProvidedContentElement elementDescription];
-[SBSystemApertureProvidedContentElement horizontalSpacingBetweenLeadingAndCenter];
-[SBSystemApertureProvidedContentElement horizontalSpacingBetweenTrailingAndCenter];
-[SBSystemApertureProvidedContentElement initWithIdentifier:contentProvider:];
-[SBSystemApertureProvidedContentElement setMaximumSupportedLayoutMode:];
-[SBSystemApertureProvidedContentElement setMinimumSupportedLayoutMode:];
-[SBSystemApertureProvidedContentElement verticalItemSpacing];
-[SBSystemApertureProvidedContentElement verticalSpacingBetweenPrimaryAndSecondary];
```
