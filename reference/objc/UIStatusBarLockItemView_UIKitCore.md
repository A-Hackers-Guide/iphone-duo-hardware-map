# `UIStatusBarLockItemView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIStatusBarItemView`
- Protocols: `CAAnimationDelegate`
- 12 instance variables, 16 properties, 35 instance methods, 1 class methods

## Instance variables

```
B _alongsideViewIsBecomingVisible;
i _animationCount;
@"UIView" _viewToAnimateAlongside;
@"_UIStatusBarLockItemPadlockView" _padlockView;
@"UIView" _textClippingView;
@"_UIExpandingGlyphsView" _textView;
d _padlockViewCenterOffsetFromForegroundViewCenter;
@"UIView" _timeItemSnapshot;
d _timeItemSnapshotCenterOffsetFromForegroundViewCenter;
d _widthNeededDuringAnimation;
d _widthNeededForFinalState;
@? _animationCompletionBlock;
```

## Properties

```
@property (T@"_UIStatusBarLockItemPadlockView",&,N,V_padlockView) padlockView;
@property (T@"UIView",&,N,V_textClippingView) textClippingView;
@property (T@"_UIExpandingGlyphsView",&,N,V_textView) textView;
@property (Td,N,V_padlockViewCenterOffsetFromForegroundViewCenter) padlockViewCenterOffsetFromForegroundViewCenter;
@property (T@"UIView",&,N,V_timeItemSnapshot) timeItemSnapshot;
@property (Td,N,V_timeItemSnapshotCenterOffsetFromForegroundViewCenter) timeItemSnapshotCenterOffsetFromForegroundViewCenter;
@property (Td,N,V_widthNeededDuringAnimation) widthNeededDuringAnimation;
@property (Td,N,V_widthNeededForFinalState) widthNeededForFinalState;
@property (Ti,N,V_animationCount) animationCount;
@property (T@?,C,N,V_animationCompletionBlock) animationCompletionBlock;
@property (T@"UIView",W,N,V_viewToAnimateAlongside) viewToAnimateAlongside;
@property (TB,N,V_alongsideViewIsBecomingVisible) alongsideViewIsBecomingVisible;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIStatusBarLockItemView lockSlideAnimationDuration];
```

## Instance methods

```
-[UIStatusBarLockItemView _isAnimating];
-[UIStatusBarLockItemView setTextView:];
-[UIStatusBarLockItemView animationCount];
-[UIStatusBarLockItemView accessibilityHUDRepresentation];
-[UIStatusBarLockItemView animationDidStop:finished:];
-[UIStatusBarLockItemView textView];
-[UIStatusBarLockItemView setAnimationCount:];
-[UIStatusBarLockItemView isExclusive];
-[UIStatusBarLockItemView _beginAnimation];
-[UIStatusBarLockItemView setPadlockView:];
-[UIStatusBarLockItemView _endAnimation];
-[UIStatusBarLockItemView alongsideViewIsBecomingVisible];
-[UIStatusBarLockItemView animateUnlockForegroundView:timeItemSnapshot:completionBlock:];
-[UIStatusBarLockItemView animationCompletionBlock];
-[UIStatusBarLockItemView jiggleCompletionBlock:];
-[UIStatusBarLockItemView padlockView];
-[UIStatusBarLockItemView padlockViewCenterOffsetFromForegroundViewCenter];
-[UIStatusBarLockItemView setAlongsideViewIsBecomingVisible:];
-[UIStatusBarLockItemView setAnimationCompletionBlock:];
-[UIStatusBarLockItemView setPadlockViewCenterOffsetFromForegroundViewCenter:];
-[UIStatusBarLockItemView setTextClippingView:];
-[UIStatusBarLockItemView setTimeItemSnapshot:];
-[UIStatusBarLockItemView setTimeItemSnapshotCenterOffsetFromForegroundViewCenter:];
-[UIStatusBarLockItemView setViewToAnimateAlongside:];
-[UIStatusBarLockItemView setVisible:frame:duration:];
-[UIStatusBarLockItemView setWidthNeededDuringAnimation:];
-[UIStatusBarLockItemView setWidthNeededForFinalState:];
-[UIStatusBarLockItemView textClippingView];
-[UIStatusBarLockItemView timeItemSnapshot];
-[UIStatusBarLockItemView timeItemSnapshotCenterOffsetFromForegroundViewCenter];
-[UIStatusBarLockItemView updateContentsAndWidth];
-[UIStatusBarLockItemView updateForNewData:actions:];
-[UIStatusBarLockItemView viewToAnimateAlongside];
-[UIStatusBarLockItemView widthNeededDuringAnimation];
-[UIStatusBarLockItemView widthNeededForFinalState];
```
