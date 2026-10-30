# `CCUIContentModuleContentViewController` (protocol)

- Image: [`/System/Library/ControlCenter/Bundles/DisplayModule.bundle/DisplayModule`](../userland/System__Library__ControlCenter__Bundles__DisplayModule.bundle__DisplayModule.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 20 properties, 41 instance methods, 0 class methods

## Properties

```
@property (Td,R,N) preferredExpandedContentHeight;
@property (TB,?,N,GisResizing) resizing;
@property (Tq,?,N) gridSizeClass;
@property (TB,?,N) suppressesContentTransitions;
@property (Tq,?,N) userVisibilityStatus;
@property (Td,?,R,N) preferredExpandedContentWidth;
@property (TB,?,R,N) prefersExpandedContentSizeMatchesGridSize;
@property (Td,?,R,N) preferredExpandedContinuousCornerRadius;
@property (Td,?,N) compactContinuousCornerRadius;
@property (TQ,?,N) contentRenderingMode;
@property (T@"CCUIModuleContentMetrics",?,&,N) contentMetrics;
@property (TB,?,R,N) providesOwnPlatter;
@property (T@"NSArray",?,R,N) containerViewsForPlatterTreatment;
@property (T@"UIViewPropertyAnimator",?,R,N) customAnimator;
@property (TB,?,R,N) shouldPerformHoverInteraction;
@property (TB,?,R,N) shouldPerformClickInteraction;
@property (TB,?,R,N) wantsConfigurationIntent;
@property (TB,?,R,N) promptsForUserConfiguration;
@property (T@"INIntent",?,R,N) defaultConfigurationIntent;
@property (TQ,?,R,N) implicitlyExpandedGridSizeClasses;
```

## Instance methods

```
-[CCUIContentModuleContentViewController preferredExpandedContentHeight];
-[CCUIContentModuleContentViewController displayWillTurnOff];
-[CCUIContentModuleContentViewController canDismissPresentedContent];
-[CCUIContentModuleContentViewController setSuppressesContentTransitions:];
-[CCUIContentModuleContentViewController contentRenderingMode];
-[CCUIContentModuleContentViewController gridSizeClass];
-[CCUIContentModuleContentViewController prefersExpandedContentSizeMatchesGridSize];
-[CCUIContentModuleContentViewController userVisibilityStatus];
-[CCUIContentModuleContentViewController setContentRenderingMode:];
-[CCUIContentModuleContentViewController setResizing:];
-[CCUIContentModuleContentViewController shouldBeginTransitionToExpandedContentModule];
-[CCUIContentModuleContentViewController dismissPresentedContentAnimated:completion:];
-[CCUIContentModuleContentViewController setGridSizeClass:];
-[CCUIContentModuleContentViewController shouldExpandModuleOnTouch:];
-[CCUIContentModuleContentViewController preferredExpandedContentWidth];
-[CCUIContentModuleContentViewController setUserVisibilityStatus:];
-[CCUIContentModuleContentViewController containerViewsForPlatterTreatment];
-[CCUIContentModuleContentViewController suppressesContentTransitions];
-[CCUIContentModuleContentViewController interpretsLocationAsContent:inView:];
-[CCUIContentModuleContentViewController isResizing];
-[CCUIContentModuleContentViewController willTransitionToExpandedContentMode:];
-[CCUIContentModuleContentViewController shouldFinishTransitionToExpandedContentModule];
-[CCUIContentModuleContentViewController compactContinuousCornerRadius];
-[CCUIContentModuleContentViewController setCompactContinuousCornerRadius:];
-[CCUIContentModuleContentViewController providesOwnPlatter];
-[CCUIContentModuleContentViewController contentMetrics];
-[CCUIContentModuleContentViewController shouldPerformClickInteraction];
-[CCUIContentModuleContentViewController implicitlyExpandedGridSizeClasses];
-[CCUIContentModuleContentViewController shouldPerformHoverInteraction];
-[CCUIContentModuleContentViewController didTransitionToExpandedContentMode:];
-[CCUIContentModuleContentViewController preferredExpandedContinuousCornerRadius];
-[CCUIContentModuleContentViewController setContentMetrics:];
-[CCUIContentModuleContentViewController customAnimator];
-[CCUIContentModuleContentViewController promptsForUserConfiguration];
-[CCUIContentModuleContentViewController moduleLayoutSizeForOrientation:];
-[CCUIContentModuleContentViewController controlCenterDidDismiss];
-[CCUIContentModuleContentViewController controlCenterWillPresent];
-[CCUIContentModuleContentViewController defaultConfigurationIntent];
-[CCUIContentModuleContentViewController setConfigurationIntent:];
-[CCUIContentModuleContentViewController shouldUseCompactContentFrameForExpandedContent];
-[CCUIContentModuleContentViewController wantsConfigurationIntent];
```
