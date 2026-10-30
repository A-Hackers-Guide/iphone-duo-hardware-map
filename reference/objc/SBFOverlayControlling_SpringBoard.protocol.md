# `SBFOverlayControlling` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 6 properties, 23 instance methods, 0 class methods

## Properties

```
@property (Td,R,N) contentWidth;
@property (Td,N) presentationProgress;
@property (TB,R,N,GisPresented) presented;
@property (TB,R,N,GisAnimatingPresentationProgress) animatingPresentationProgress;
@property (T@"<SBFOverlayDismissalDelegate>",W,N) dismissalDelegate;
@property (Td,R,N) leadingViewScrollFraction;
```

## Instance methods

```
-[SBFOverlayControlling dismissAnimated:completionHandler:];
-[SBFOverlayControlling presentAnimated:completionHandler:];
-[SBFOverlayControlling isPresented];
-[SBFOverlayControlling setPresentationProgress:];
-[SBFOverlayControlling presentAnimated:];
-[SBFOverlayControlling contentWidth];
-[SBFOverlayControlling dismissalDelegate];
-[SBFOverlayControlling setDismissalDelegate:];
-[SBFOverlayControlling presentationProgress];
-[SBFOverlayControlling setPresentationProgress:interactive:animated:completionHandler:];
-[SBFOverlayControlling addHomeScreenOverlayObserver:];
-[SBFOverlayControlling finalPresentationProgressForTranslation:velocity:initialPresentationProgress:fromLeading:];
-[SBFOverlayControlling layerPresentationProgress];
-[SBFOverlayControlling leadingViewScrollFraction];
-[SBFOverlayControlling presentationProgressForTranslation:initialPresentationProgress:fromLeading:];
-[SBFOverlayControlling setLeadingViewScrollFraction:animated:];
-[SBFOverlayControlling setPresentationProgress:fromLeading:interactive:animated:completionHandler:];
-[SBFOverlayControlling isAnimatingPresentationProgress];
-[SBFOverlayControlling dismissUsingViewControllerTransitionCoordinator:];
-[SBFOverlayControlling presentAnimated:fromLeading:];
-[SBFOverlayControlling presentAnimated:fromLeading:completionHandler:];
-[SBFOverlayControlling removeHomeScreenOverlayObserver:];
-[SBFOverlayControlling setPresentationProgress:fromLeading:];
```
