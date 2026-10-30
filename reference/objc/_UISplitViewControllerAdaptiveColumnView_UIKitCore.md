# `_UISplitViewControllerAdaptiveColumnView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIPassthroughScrollInteractionDelegate`
- 18 instance variables, 21 properties, 58 instance methods, 0 class methods

## Instance variables

```
q splitViewControllerColumn;
? interactionDelegate;
@"_TtCE5UIKitCSo40_UISplitViewControllerAdaptiveColumnViewP33_E55D530921B5D45A8EA231E2252C983512ClippingView" clippingView;
@"_TtCE5UIKitCSo40_UISplitViewControllerAdaptiveColumnViewP33_E55D530921B5D45A8EA231E2252C983511DimmingView" dimmingView;
@"UIFocusContainerGuide" focusContainerGuide;
@"UIView" ownedContentView;
@"_UIPassthroughScrollInteraction" passthroughScrollInteraction;
B previousPassthroughScrollInteractionHitTestPassedSelf;
passthroughScrollInteractionEnabled;
prepared;
@"<_UIViewMaterial>" background;
Q maskedCorners;
{UIEdgeInsets=dddd} contentInsets;
d dimmingLevel;
B dimmingBackgroundEnabled;
d fallbackCornerRadius;
q userInterfaceLevel;
B glassBackgroundContentDimmingEnabled;
```

## Properties

```
@property (Tq,N,R,VsplitViewControllerColumn) splitViewControllerColumn;
@property (T@"<_UISplitViewControllerAdaptiveColumnInteractionDelegate>",N,W,VinteractionDelegate) interactionDelegate;
@property (T@"_TtCE5UIKitCSo40_UISplitViewControllerAdaptiveColumnViewP33_E55D530921B5D45A8EA231E2252C983512ClippingView",N,&,VclippingView) clippingView;
@property (T@"_TtCE5UIKitCSo40_UISplitViewControllerAdaptiveColumnViewP33_E55D530921B5D45A8EA231E2252C983511DimmingView",N,&,VdimmingView) dimmingView;
@property (T@"UIFocusContainerGuide",N,&,VfocusContainerGuide) focusContainerGuide;
@property (T@"UIView",N,&,VownedContentView) ownedContentView;
@property (T@"_UIPassthroughScrollInteraction",N,&,VpassthroughScrollInteraction) passthroughScrollInteraction;
@property (TB,N,VpreviousPassthroughScrollInteractionHitTestPassedSelf) previousPassthroughScrollInteractionHitTestPassedSelf;
@property (T@"<_UIViewMaterial>",N,&,Vbackground) background;
@property (TQ,N,VmaskedCorners) maskedCorners;
@property (T{UIEdgeInsets=dddd},N,VcontentInsets) contentInsets;
@property (T@"UIView",N,&) contentView;
@property (Td,N,VdimmingLevel) dimmingLevel;
@property (TB,N,VdimmingBackgroundEnabled) dimmingBackgroundEnabled;
@property (Td,N,VfallbackCornerRadius) fallbackCornerRadius;
@property (TB,N) passthroughScrollInteractionEnabled;
@property (TB,N) prepared;
@property (Tq,N,VuserInterfaceLevel) userInterfaceLevel;
@property (TB,N,VglassBackgroundContentDimmingEnabled) glassBackgroundContentDimmingEnabled;
@property (T@"UIView",N,R) containerView;
@property (T@"NSString",N,R) description;
```

## Instance methods

```
-[_UISplitViewControllerAdaptiveColumnView isPrepared];
-[_UISplitViewControllerAdaptiveColumnView focusContainerGuide];
-[_UISplitViewControllerAdaptiveColumnView isPassthroughScrollInteractionEnabled];
-[_UISplitViewControllerAdaptiveColumnView setPassthroughScrollInteraction:];
-[_UISplitViewControllerAdaptiveColumnView interactionDelegate];
-[_UISplitViewControllerAdaptiveColumnView setContentView:];
-[_UISplitViewControllerAdaptiveColumnView prepareDimmingView];
-[_UISplitViewControllerAdaptiveColumnView setPassthroughScrollInteractionEnabled:];
-[_UISplitViewControllerAdaptiveColumnView dimmingView];
-[_UISplitViewControllerAdaptiveColumnView configurePassthroughScrollInteraction];
-[_UISplitViewControllerAdaptiveColumnView setGlassBackgroundContentDimmingEnabled:];
-[_UISplitViewControllerAdaptiveColumnView setOwnedContentView:];
-[_UISplitViewControllerAdaptiveColumnView setBackground:];
-[_UISplitViewControllerAdaptiveColumnView setContentInsets:];
-[_UISplitViewControllerAdaptiveColumnView updateSubviewsForChangeInMaskedCorners];
-[_UISplitViewControllerAdaptiveColumnView setInteractionDelegate:];
-[_UISplitViewControllerAdaptiveColumnView dimmingBackgroundEnabled];
-[_UISplitViewControllerAdaptiveColumnView updateCornerConfiguration];
-[_UISplitViewControllerAdaptiveColumnView setFocusContainerGuide:];
-[_UISplitViewControllerAdaptiveColumnView userInterfaceLevel];
-[_UISplitViewControllerAdaptiveColumnView layoutSubviews];
-[_UISplitViewControllerAdaptiveColumnView hitTest:withEvent:];
-[_UISplitViewControllerAdaptiveColumnView maskedCorners];
-[_UISplitViewControllerAdaptiveColumnView tapGestureDidChange:];
-[_UISplitViewControllerAdaptiveColumnView fallbackCornerRadius];
-[_UISplitViewControllerAdaptiveColumnView background];
-[_UISplitViewControllerAdaptiveColumnView updateProperties];
-[_UISplitViewControllerAdaptiveColumnView passthroughScrollInteractionDidRecognize:atLocation:];
-[_UISplitViewControllerAdaptiveColumnView setDimmingView:];
-[_UISplitViewControllerAdaptiveColumnView containerView];
-[_UISplitViewControllerAdaptiveColumnView prepareClippingView];
-[_UISplitViewControllerAdaptiveColumnView setDimmingLevel:];
-[_UISplitViewControllerAdaptiveColumnView setMaskedCorners:];
-[_UISplitViewControllerAdaptiveColumnView passthroughScrollInteraction:shouldInteractAtLocation:withEvent:];
-[_UISplitViewControllerAdaptiveColumnView dimmingLevel];
-[_UISplitViewControllerAdaptiveColumnView splitViewControllerColumn];
-[_UISplitViewControllerAdaptiveColumnView clippingView];
-[_UISplitViewControllerAdaptiveColumnView updateTraitTransformsForChangeInUserInterfaceLevel];
-[_UISplitViewControllerAdaptiveColumnView updateFocusContainerGuide];
-[_UISplitViewControllerAdaptiveColumnView contentView];
-[_UISplitViewControllerAdaptiveColumnView setDimmingBackgroundEnabled:];
-[_UISplitViewControllerAdaptiveColumnView contentInsets];
-[_UISplitViewControllerAdaptiveColumnView setClippingView:];
-[_UISplitViewControllerAdaptiveColumnView description];
-[_UISplitViewControllerAdaptiveColumnView initWithCoder:];
-[_UISplitViewControllerAdaptiveColumnView setFallbackCornerRadius:];
-[_UISplitViewControllerAdaptiveColumnView setUserInterfaceLevel:];
-[_UISplitViewControllerAdaptiveColumnView updateDimmingBackground];
-[_UISplitViewControllerAdaptiveColumnView initWithSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveColumnView setPrepared:];
-[_UISplitViewControllerAdaptiveColumnView updateGlassBackgroundContentDimming];
-[_UISplitViewControllerAdaptiveColumnView ownedContentView];
-[_UISplitViewControllerAdaptiveColumnView initWithFrame:];
-[_UISplitViewControllerAdaptiveColumnView updateDimmingView];
-[_UISplitViewControllerAdaptiveColumnView glassBackgroundContentDimmingEnabled];
-[_UISplitViewControllerAdaptiveColumnView passthroughScrollInteraction];
-[_UISplitViewControllerAdaptiveColumnView setPreviousPassthroughScrollInteractionHitTestPassedSelf:];
-[_UISplitViewControllerAdaptiveColumnView previousPassthroughScrollInteractionHitTestPassedSelf];
```
