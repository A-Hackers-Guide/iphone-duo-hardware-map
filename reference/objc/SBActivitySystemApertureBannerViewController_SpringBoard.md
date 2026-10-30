# `SBActivitySystemApertureBannerViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBActivityBannerViewController`
- Protocols: `SBSystemApertureBackgroundActivitiesSuppressing`, `SAUILayoutHosting`
- 7 instance variables, 12 properties, 41 instance methods, 0 class methods

## Instance variables

```
B _invalidated;
@"ACUISSystemApertureSceneHandle" _sceneHandle;
@"SBSystemApertureSceneElement" _sceneElement;
@"UIView" _sceneElementContainerView;
@? _ensureContentHandler;
@"NSSet" _backgroundActivityIdentifiersToSuppress;
@"NSString" _backgroundActivitySuppressionReason;
```

## Properties

```
@property (T@"ACUISSystemApertureSceneHandle",&,N,V_sceneHandle) sceneHandle;
@property (TB,N,GisInvalidated,V_invalidated) invalidated;
@property (T@"SBSystemApertureSceneElement",&,N,V_sceneElement) sceneElement;
@property (T@"UIView",&,N,V_sceneElementContainerView) sceneElementContainerView;
@property (T@?,C,N,V_ensureContentHandler) ensureContentHandler;
@property (T@"NSSet",C,N,V_backgroundActivityIdentifiersToSuppress) backgroundActivityIdentifiersToSuppress;
@property (T@"NSString",C,N,V_backgroundActivitySuppressionReason) backgroundActivitySuppressionReason;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,?,N) layoutDirection;
```

## Instance methods

```
-[SBActivitySystemApertureBannerViewController isTouchOutsideDismissalEnabled];
-[SBActivitySystemApertureBannerViewController sceneHandle];
-[SBActivitySystemApertureBannerViewController presentableDidAppearAsBanner:];
-[SBActivitySystemApertureBannerViewController _updatePreferredContentSize];
-[SBActivitySystemApertureBannerViewController preferredEdgeOutsetsDidInvalidateForLayoutSpecifier:];
-[SBActivitySystemApertureBannerViewController ensureContent:queue:completion:];
-[SBActivitySystemApertureBannerViewController dealloc];
-[SBActivitySystemApertureBannerViewController viewDidLayoutSubviews];
-[SBActivitySystemApertureBannerViewController isInvalidated];
-[SBActivitySystemApertureBannerViewController setInvalidated:];
-[SBActivitySystemApertureBannerViewController invalidate];
-[SBActivitySystemApertureBannerViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[SBActivitySystemApertureBannerViewController presentableWillAppearAsBanner:];
-[SBActivitySystemApertureBannerViewController acquireActiveElementAssertionForApplication:reason:];
-[SBActivitySystemApertureBannerViewController layoutMetricsForLayoutSpecifier:];
-[SBActivitySystemApertureBannerViewController menuPresentationRequestDidChangeForLayoutSpecifier:];
-[SBActivitySystemApertureBannerViewController preferredPromotionDidInvalidateForLayoutSpecifier:];
-[SBActivitySystemApertureBannerViewController preferredLayoutModeDidInvalidateForLayoutSpecifier:];
-[SBActivitySystemApertureBannerViewController viewWillLayoutSubviews];
-[SBActivitySystemApertureBannerViewController edgeOutsetsForSize:];
-[SBActivitySystemApertureBannerViewController setSceneHandle:];
-[SBActivitySystemApertureBannerViewController presentableDidDisappearAsBanner:withReason:];
-[SBActivitySystemApertureBannerViewController acquireSuppressionAssertionForBackgroundActivities:reason:];
-[SBActivitySystemApertureBannerViewController presentableWillDisappearAsBanner:withReason:];
-[SBActivitySystemApertureBannerViewController initWithActivityItem:];
-[SBActivitySystemApertureBannerViewController _createSystemApertureSceneHandleWithItem:];
-[SBActivitySystemApertureBannerViewController _sauiLayoutMetricsForLayoutMetrics:];
-[SBActivitySystemApertureBannerViewController _updateSceneElementLayoutWithCoordinator:preAlongsideActions:];
-[SBActivitySystemApertureBannerViewController _updateSceneElementLayoutWithCoordinator:size:preAlongsideActions:];
-[SBActivitySystemApertureBannerViewController backgroundActivityIdentifiersToSuppress];
-[SBActivitySystemApertureBannerViewController backgroundActivitySuppressionReason];
-[SBActivitySystemApertureBannerViewController ensureContentHandler];
-[SBActivitySystemApertureBannerViewController preferredActivityContentSize];
-[SBActivitySystemApertureBannerViewController sceneElement];
-[SBActivitySystemApertureBannerViewController sceneElementContainerView];
-[SBActivitySystemApertureBannerViewController setBackgroundActivityIdentifiersToSuppress:];
-[SBActivitySystemApertureBannerViewController setBackgroundActivitySuppressionReason:];
-[SBActivitySystemApertureBannerViewController setEnsureContentHandler:];
-[SBActivitySystemApertureBannerViewController setSceneElement:];
-[SBActivitySystemApertureBannerViewController setSceneElementContainerView:];
-[SBActivitySystemApertureBannerViewController systemApertureLayoutMetrics];
```
