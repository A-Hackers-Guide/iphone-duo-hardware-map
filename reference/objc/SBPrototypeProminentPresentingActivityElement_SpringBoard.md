# `SBPrototypeProminentPresentingActivityElement`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemApertureSuppressible`, `SAAlertBehavior`, `SAUIElementViewProviding`, `SAUILayoutSpecifying`, `SAElement`
- 8 instance variables, 26 properties, 26 instance methods, 0 class methods

## Instance variables

```
B _prominent;
B _showsTrailing;
B _displayedWithLimitedSize;
q _layoutMode;
q _preferredLayoutMode;
@"<SAUILayoutHosting>" _layoutHost;
@"UIView" _leadingView;
@"UIView" _trailingView;
```

## Properties

```
@property (TB,N,GisProminent) prominent;
@property (TB,N) showsTrailing;
@property (TB,?,N,GisSuppressed) suppressed;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SAAlertHosting>",?,W,N) alertHost;
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
@property (T@"<SAElementHosting>",?,W,N) elementHost;
@property (T@"NSString",R,C,N) clientIdentifier;
@property (T@"NSString",R,C,N) elementIdentifier;
```

## Instance methods

```
-[SBPrototypeProminentPresentingActivityElement setDisplayedWithLimitedSize:];
-[SBPrototypeProminentPresentingActivityElement systemApertureLayoutCustomizingOptions];
-[SBPrototypeProminentPresentingActivityElement layoutHost];
-[SBPrototypeProminentPresentingActivityElement minimalView];
-[SBPrototypeProminentPresentingActivityElement trailingView];
-[SBPrototypeProminentPresentingActivityElement setLayoutMode:reason:];
-[SBPrototypeProminentPresentingActivityElement layoutMode];
-[SBPrototypeProminentPresentingActivityElement leadingView];
-[SBPrototypeProminentPresentingActivityElement setLayoutHost:];
-[SBPrototypeProminentPresentingActivityElement clientIdentifier];
-[SBPrototypeProminentPresentingActivityElement element];
-[SBPrototypeProminentPresentingActivityElement preferredLayoutMode];
-[SBPrototypeProminentPresentingActivityElement preferredEdgeOutsetsForLayoutMode:suggestedOutsets:maximumOutsets:];
-[SBPrototypeProminentPresentingActivityElement isDisplayedWithLimitedSize];
-[SBPrototypeProminentPresentingActivityElement elementIdentifier];
-[SBPrototypeProminentPresentingActivityElement init];
-[SBPrototypeProminentPresentingActivityElement viewProvider];
-[SBPrototypeProminentPresentingActivityElement handleElementViewEvent:];
-[SBPrototypeProminentPresentingActivityElement _canShowWhileLocked];
-[SBPrototypeProminentPresentingActivityElement minimumSupportedLayoutMode];
-[SBPrototypeProminentPresentingActivityElement setProminent:];
-[SBPrototypeProminentPresentingActivityElement hasAlertBehavior];
-[SBPrototypeProminentPresentingActivityElement isProminent];
-[SBPrototypeProminentPresentingActivityElement maximumSupportedLayoutMode];
-[SBPrototypeProminentPresentingActivityElement setShowsTrailing:];
-[SBPrototypeProminentPresentingActivityElement showsTrailing];
```
