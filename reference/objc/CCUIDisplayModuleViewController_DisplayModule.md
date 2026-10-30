# `CCUIDisplayModuleViewController`

- Image: [`/System/Library/ControlCenter/Bundles/DisplayModule.bundle/DisplayModule`](../userland/System__Library__ControlCenter__Bundles__DisplayModule.bundle__DisplayModule.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `CBPropertyObserver`, `CCUIGroupRendering`, `CCUIContentModuleContentViewController`
- 8 instance variables, 32 properties, 46 instance methods, 0 class methods

## Instance variables

```
^{BKSDisplayBrightnessTransaction=} _brightnessTransaction;
@"CBClient" _cbClient;
@"CBDisplayClient" _cbDisplayClient;
B _expanded;
d _compactContinuousCornerRadius;
@"<CCUIDisplayModuleViewControllerDelegate>" _delegate;
@"CCUIContentModuleContext" _contentModuleContext;
@"CCUIContinuousSliderView" _sliderView;
```

## Properties

```
@property (T@"CCUIContentModuleContext",&,N,V_contentModuleContext) contentModuleContext;
@property (T@"CCUIContinuousSliderView",&,N,V_sliderView) sliderView;
@property (T@"<CCUIDisplayModuleViewControllerDelegate>",W,N,V_delegate) delegate;
@property (Tf,R,N) currentBrightness;
@property (T@"NSSet",R) properties;
@property (T@"NSObject<OS_dispatch_queue>",R) notifyQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N,GisGroupRenderingRequired) groupRenderingRequired;
@property (T@"NSArray",R,N) punchOutRenderingViews;
@property (Td,R,N) preferredExpandedContentHeight;
@property (TB,?,N,GisResizing) resizing;
@property (Tq,?,N) gridSizeClass;
@property (TB,?,N) suppressesContentTransitions;
@property (Tq,?,N) userVisibilityStatus;
@property (Td,?,R,N) preferredExpandedContentWidth;
@property (TB,?,R,N) prefersExpandedContentSizeMatchesGridSize;
@property (Td,?,R,N) preferredExpandedContinuousCornerRadius;
@property (Td,?,N,V_compactContinuousCornerRadius) compactContinuousCornerRadius;
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
-[CCUIDisplayModuleViewController properties];
-[CCUIDisplayModuleViewController punchOutRenderingViews];
-[CCUIDisplayModuleViewController contentModuleContext];
-[CCUIDisplayModuleViewController sliderView];
-[CCUIDisplayModuleViewController viewWillDisappear:];
-[CCUIDisplayModuleViewController shouldExpandModuleOnTouch:];
-[CCUIDisplayModuleViewController setContentModuleContext:];
-[CCUIDisplayModuleViewController dealloc];
-[CCUIDisplayModuleViewController preferredExpandedContentWidth];
-[CCUIDisplayModuleViewController containerViewsForPlatterTreatment];
-[CCUIDisplayModuleViewController viewDidLoad];
-[CCUIDisplayModuleViewController isGroupRenderingRequired];
-[CCUIDisplayModuleViewController _backlightLevel];
-[CCUIDisplayModuleViewController _noteScreenBrightnessDidChange:];
-[CCUIDisplayModuleViewController _sliderPresentationValueDidChange:];
-[CCUIDisplayModuleViewController _updateBrightnessControlInteractionEnabled];
-[CCUIDisplayModuleViewController _updateWithCurrentBrightnessAnimated:];
-[CCUIDisplayModuleViewController _sliderEditingDidEnd:];
-[CCUIDisplayModuleViewController initWithContentModuleContext:];
-[CCUIDisplayModuleViewController willTransitionToExpandedContentMode:];
-[CCUIDisplayModuleViewController notifyQueue];
-[CCUIDisplayModuleViewController viewWillAppear:];
-[CCUIDisplayModuleViewController compactContinuousCornerRadius];
-[CCUIDisplayModuleViewController setCompactContinuousCornerRadius:];
-[CCUIDisplayModuleViewController providesOwnPlatter];
-[CCUIDisplayModuleViewController preferredExpandedContentHeight];
-[CCUIDisplayModuleViewController _canShowWhileLocked];
-[CCUIDisplayModuleViewController setDelegate:];
-[CCUIDisplayModuleViewController viewDidAppear:];
-[CCUIDisplayModuleViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[CCUIDisplayModuleViewController loadView];
-[CCUIDisplayModuleViewController delegate];
-[CCUIDisplayModuleViewController viewWillLayoutSubviews];
-[CCUIDisplayModuleViewController viewDidDisappear:];
-[CCUIDisplayModuleViewController setGlyphPackageDescription:];
-[CCUIDisplayModuleViewController _canAdjustBrightness];
-[CCUIDisplayModuleViewController _sliderEditingDidBegin:];
-[CCUIDisplayModuleViewController _updateBrightnessControlAvailability];
-[CCUIDisplayModuleViewController setGlyphState:];
-[CCUIDisplayModuleViewController currentBrightness];
-[CCUIDisplayModuleViewController observeValue:forKey:andHandle:withContext:];
-[CCUIDisplayModuleViewController preferredExpandedContinuousCornerRadius];
-[CCUIDisplayModuleViewController setSliderView:];
-[CCUIDisplayModuleViewController viewForTouchContinuation];
-[CCUIDisplayModuleViewController _setBacklightLevel:];
-[CCUIDisplayModuleViewController setContentMetrics:];
```
