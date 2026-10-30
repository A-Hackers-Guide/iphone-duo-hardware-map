# `SBNoticePresentableElement`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SAUIElementViewProviding`, `SAUIContentTransitioning`, `SBSystemApertureContextProviding`, `SBPresentableElement`, `SAAlertBehavior`
- 9 instance variables, 34 properties, 34 instance methods, 1 class methods

## Instance variables

```
@"UIView" _primaryView;
@"UIView" _secondaryView;
@"NSHashTable" _observers;
@"<BNPresentable>" _presentable;
@"UIView" _leadingView;
@"UIView" _trailingView;
q _layoutMode;
q _preferredLayoutMode;
@"<SAUILayoutHosting>" _layoutHost;
```

## Properties

```
@property (T@"<BNPresentable><BNTemplateContentProviding>",R,N) templatePresentable;
@property (T@"UIView",R,N,V_leadingView) leadingView;
@property (T@"UIView",R,N,V_trailingView) trailingView;
@property (T@"UIView",R,N) minimalView;
@property (T@"UIView",?,R,N) detachedMinimalView;
@property (T@"<SAElement>",R,W,N) element;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,?,N) layoutAxis;
@property (TB,?,R,N,GisAffiliatedWithSessionMonitor) affiliatedWithSessionMonitor;
@property (T@"UIColor",?,R,N) keyColor;
@property (T@"FBScene",?,R,N) scene;
@property (TB,?,R,N) preventsSwipeToHide;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) preferredAvoidanceRect;
@property (Td,?,R,N) preferredAvoidanceCornerRadius;
@property (TB,?,R,N) inhibitsIndicatorMitosis;
@property (Td,?,R,N) preferredSystemClipPadding;
@property (T@"<BNPresentable>",R,N,V_presentable) presentable;
@property (T@"<SAElementHosting>",?,W,N) elementHost;
@property (T@"NSString",R,C,N) clientIdentifier;
@property (T@"NSString",R,C,N) elementIdentifier;
@property (TB,?,N,GisSuppressed) suppressed;
@property (Tq,R,N,V_layoutMode) layoutMode;
@property (Tq,R,N) minimumSupportedLayoutMode;
@property (Tq,R,N) maximumSupportedLayoutMode;
@property (Tq,R,N,V_preferredLayoutMode) preferredLayoutMode;
@property (T@"<SAUILayoutHosting>",?,W,N,V_layoutHost) layoutHost;
@property (TB,?,R,N,GisInteractiveDismissalEnabled) interactiveDismissalEnabled;
@property (TB,?,R,N,GisMinimalPresentationPossible) minimalPresentationPossible;
@property (TB,?,R,N,GisRequestingMenuPresentation) requestingMenuPresentation;
@property (TB,?,N,GisDisplayedWithLimitedSize) displayedWithLimitedSize;
@property (T@"<SAAlertHosting>",?,W,N) alertHost;
```

## Class methods

```
+[SBNoticePresentableElement _preferredFont:textStyle:weight:additionalTraits:];
```

## Instance methods

```
-[SBNoticePresentableElement layoutHost];
-[SBNoticePresentableElement keyColor];
-[SBNoticePresentableElement minimalView];
-[SBNoticePresentableElement trailingView];
-[SBNoticePresentableElement setLayoutMode:reason:];
-[SBNoticePresentableElement removeElementLayoutSpecifierObserver:];
-[SBNoticePresentableElement layoutMode];
-[SBNoticePresentableElement leadingView];
-[SBNoticePresentableElement setLayoutHost:];
-[SBNoticePresentableElement clientIdentifier];
-[SBNoticePresentableElement element];
-[SBNoticePresentableElement preferredLayoutMode];
-[SBNoticePresentableElement preferredEdgeOutsetsForLayoutMode:suggestedOutsets:maximumOutsets:];
-[SBNoticePresentableElement elementIdentifier];
-[SBNoticePresentableElement viewProvider];
-[SBNoticePresentableElement addElementLayoutSpecifierObserver:];
-[SBNoticePresentableElement handleElementViewEvent:];
-[SBNoticePresentableElement _canShowWhileLocked];
-[SBNoticePresentableElement presentable];
-[SBNoticePresentableElement _enumerateObserversRespondingToSelector:usingBlock:];
-[SBNoticePresentableElement description];
-[SBNoticePresentableElement minimumSupportedLayoutMode];
-[SBNoticePresentableElement shouldSuppressElementWhileOnCoversheet];
-[SBNoticePresentableElement layoutHostContainerViewDidLayoutSubviews:];
-[SBNoticePresentableElement hasAlertBehavior];
-[SBNoticePresentableElement contentProviderWillTransitionToSize:inContainerView:transitionCoordinator:];
-[SBNoticePresentableElement maximumSupportedLayoutMode];
-[SBNoticePresentableElement _primaryView];
-[SBNoticePresentableElement _secondaryView];
-[SBNoticePresentableElement _templateItemViewFromProvider:isPrimary:];
-[SBNoticePresentableElement _updateVisualStlyingOfView:fromProvider:];
-[SBNoticePresentableElement elementDescription];
-[SBNoticePresentableElement initWithTemplatePresentable:];
-[SBNoticePresentableElement templatePresentable];
```
