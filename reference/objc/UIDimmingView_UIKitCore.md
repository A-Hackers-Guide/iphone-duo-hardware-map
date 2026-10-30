# `UIDimmingView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIEventObserver`, `UIGestureRecognizerDelegate`
- 16 instance variables, 16 properties, 46 instance methods, 1 class methods

## Instance variables

```
@"UIBarButtonItem" _highlightedBarButtonItem;
@"UIImageView" _highlightedImageView;
@"UIImageView" _backgroundGlow;
@"NSArray" _passthroughViews;
B _ignoresTouches;
B _inPassthroughHitTest;
@"UIColor" _dimmingColor;
@"UITapGestureRecognizer" _singleFingerTapRecognizer;
@"UIEvent" _observedEventForAdditionalGestures;
@"NSMutableSet" _additionalEventGestureRecognizers;
B _suppressesBackdrops;
@"<UIDimmingViewDelegate>" _delegate;
d _percentDisplayed;
d _percentLightened;
@"UIBlurEffect" _blurEffect;
@"NSArray" _lowerWindowDismissalGestureViews;
```

## Properties

```
@property (T@"<UIDimmingViewDelegate>",W,N,V_delegate) delegate;
@property (T@"UIBarButtonItem",&,N) highlightedBarButtonItem;
@property (T@"NSArray",C,N,V_passthroughViews) passthroughViews;
@property (TB,N,V_ignoresTouches) ignoresTouches;
@property (TB,R,N) displayed;
@property (Td,N,V_percentDisplayed) percentDisplayed;
@property (Td,N,V_percentLightened) percentLightened;
@property (T@"UIColor",&,N,V_dimmingColor) dimmingColor;
@property (T@"UIBlurEffect",&,N,V_blurEffect) blurEffect;
@property (TB,N,V_suppressesBackdrops) suppressesBackdrops;
@property (T@"NSArray",C,N,V_lowerWindowDismissalGestureViews) lowerWindowDismissalGestureViews;
@property (TB,N) hitTestsAsOpaque;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIDimmingView defaultDimmingColor];
```

## Instance methods

```
-[UIDimmingView touchesEnded:withEvent:];
-[UIDimmingView updateBackgroundColor];
-[UIDimmingView dimmingColor];
-[UIDimmingView _dynamicUserInterfaceTraitDidChange];
-[UIDimmingView gestureRecognizer:shouldReceiveTouch:];
-[UIDimmingView dealloc];
-[UIDimmingView _gestureRecognizersForEvent:];
-[UIDimmingView hitTest:withEvent:];
-[UIDimmingView setDelegate:];
-[UIDimmingView willMoveToWindow:];
-[UIDimmingView passthroughViews];
-[UIDimmingView updateBackground];
-[UIDimmingView delegate];
-[UIDimmingView hitTestsAsOpaque];
-[UIDimmingView setHitTestsAsOpaque:];
-[UIDimmingView isTransparentFocusItem];
-[UIDimmingView setDimmingColor:];
-[UIDimmingView initWithFrame:];
-[UIDimmingView textEffectsVisibilityLevel];
-[UIDimmingView _backdropViewsToAnimate];
-[UIDimmingView _clearAdditionalEventGestures];
-[UIDimmingView _queueAdditionalEventGesturesFromView:];
-[UIDimmingView _sendDelegateDimmingViewWasTapped];
-[UIDimmingView _simulateTap];
-[UIDimmingView blurEffect];
-[UIDimmingView dimmingRemovalAnimationDidStop];
-[UIDimmingView display:];
-[UIDimmingView display:withAnimationDuration:afterDelay:];
-[UIDimmingView displayed];
-[UIDimmingView handleSingleTap:];
-[UIDimmingView highlightedBarButtonItem];
-[UIDimmingView hitTest:forEvent:];
-[UIDimmingView ignoresTouches];
-[UIDimmingView lowerWindowDismissalGestureViews];
-[UIDimmingView mouseUp:];
-[UIDimmingView percentDisplayed];
-[UIDimmingView percentLightened];
-[UIDimmingView setBlurEffect:];
-[UIDimmingView setHighlightedBarButtonItem:];
-[UIDimmingView setIgnoresTouches:];
-[UIDimmingView setLowerWindowDismissalGestureViews:];
-[UIDimmingView setPassthroughViews:];
-[UIDimmingView setPercentDisplayed:];
-[UIDimmingView setPercentLightened:];
-[UIDimmingView setSuppressesBackdrops:];
-[UIDimmingView suppressesBackdrops];
```
