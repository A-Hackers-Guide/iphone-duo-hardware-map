# `SAUILayoutSpecifying` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 9 properties, 19 instance methods, 0 class methods

## Properties

```
@property (Tq,R,N) layoutMode;
@property (Tq,R,N) minimumSupportedLayoutMode;
@property (Tq,R,N) maximumSupportedLayoutMode;
@property (Tq,R,N) preferredLayoutMode;
@property (T@"<SAUILayoutHosting>",?,W,N) layoutHost;
@property (TB,?,R,N,GisInteractiveDismissalEnabled) interactiveDismissalEnabled;
@property (TB,?,R,N,GisMinimalPresentationPossible) minimalPresentationPossible;
@property (TB,?,R,N,GisRequestingMenuPresentation) requestingMenuPresentation;
@property (TB,?,N,GisDisplayedWithLimitedSize) displayedWithLimitedSize;
```

## Instance methods

```
-[SAUILayoutSpecifying setLayoutMode:reason:];
-[SAUILayoutSpecifying layoutMode];
-[SAUILayoutSpecifying preferredLayoutMode];
-[SAUILayoutSpecifying minimumSupportedLayoutMode];
-[SAUILayoutSpecifying maximumSupportedLayoutMode];
-[SAUILayoutSpecifying setDisplayedWithLimitedSize:];
-[SAUILayoutSpecifying layoutHost];
-[SAUILayoutSpecifying setLayoutHost:];
-[SAUILayoutSpecifying isRequestingMenuPresentation];
-[SAUILayoutSpecifying isProvidedViewConcentric:inLayoutMode:];
-[SAUILayoutSpecifying preferredEdgeOutsetsForLayoutMode:suggestedOutsets:maximumOutsets:];
-[SAUILayoutSpecifying isDisplayedWithLimitedSize];
-[SAUILayoutSpecifying isInteractiveDismissalEnabled];
-[SAUILayoutSpecifying sizeThatFitsSize:forProvidedView:inLayoutMode:];
-[SAUILayoutSpecifying isMinimalPresentationPossible];
-[SAUILayoutSpecifying layoutHostContainerViewDidLayoutSubviews:];
-[SAUILayoutSpecifying layoutHostContainerViewWillLayoutSubviews:];
-[SAUILayoutSpecifying layoutHostContextDidUpdateTo:withPreviousLayoutHostContext:];
-[SAUILayoutSpecifying layoutHostMetricsDidUpdateTo:withPreviousLayoutHostMetrics:];
```
