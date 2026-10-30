# `UIStatusBarForegroundView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIAccessibilityHUDGestureDelegate`
- 11 instance variables, 7 properties, 44 instance methods, 0 class methods

## Instance variables

```
B _usesVerticalLayout;
[52B] _itemIsEnabled;
[3@"UIStatusBarLayoutManager"] _layoutManagers;
i _ignoreDataLevel;
@"NSMutableArray" _actionAnimationStack;
@"UIStatusBarComposedData" _currentData;
@"UIStatusBarComposedData" _pendedData;
i _pendedActions;
@"UIAccessibilityHUDGestureManager" _accessibilityHUDGestureManager;
q _idiom;
@"UIStatusBarForegroundStyleAttributes" _foregroundStyle;
```

## Properties

```
@property (Tq,N,V_idiom) idiom;
@property (T@"UIStatusBarForegroundStyleAttributes",R,N,V_foregroundStyle) foregroundStyle;
@property (T@"UIStatusBar",R,N) statusBar;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIStatusBarForegroundView jiggleLockIcon];
-[UIStatusBarForegroundView statusBar];
-[UIStatusBarForegroundView _accessibilityHUDGestureManager:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[UIStatusBarForegroundView didMoveToWindow];
-[UIStatusBarForegroundView _accessibilityHUDGestureManager:HUDItemForPoint:];
-[UIStatusBarForegroundView _accessibilityHUDGestureManager:gestureLiftedAtPoint:];
-[UIStatusBarForegroundView _accessibilityHUDGestureManager:showHUDItem:];
-[UIStatusBarForegroundView setIdiom:];
-[UIStatusBarForegroundView dealloc];
-[UIStatusBarForegroundView setBounds:];
-[UIStatusBarForegroundView _statusBarWindowForAccessibilityHUD];
-[UIStatusBarForegroundView setFrame:];
-[UIStatusBarForegroundView pointInside:withEvent:];
-[UIStatusBarForegroundView _dismissAccessibilityHUDForGestureManager:];
-[UIStatusBarForegroundView idiom];
-[UIStatusBarForegroundView foregroundStyle];
-[UIStatusBarForegroundView leftEdgePadding];
-[UIStatusBarForegroundView setPersistentAnimationsEnabled:];
-[UIStatusBarForegroundView _accessibilityHUDGestureManager:canCancelGestureRecognizer:];
-[UIStatusBarForegroundView _animateUnlockCompletionBlock:];
-[UIStatusBarForegroundView _cleanUpAfterDataChange];
-[UIStatusBarForegroundView _cleanUpAfterSimpleReflow];
-[UIStatusBarForegroundView _computeVisibleItemsPreservingHistory:];
-[UIStatusBarForegroundView _reflowItemViewsCrossfadingCenterWithDuration:timeWasEnabled:];
-[UIStatusBarForegroundView _reflowItemViewsWithDuration:preserveHistory:];
-[UIStatusBarForegroundView _setStatusBarData:actions:animated:];
-[UIStatusBarForegroundView _statusBarItemViewAtPoint:];
-[UIStatusBarForegroundView _tryToPlaceItem:inItemArray:layoutManager:roomRemaining:allowSwap:swappedItem:];
-[UIStatusBarForegroundView animateUnlock];
-[UIStatusBarForegroundView frameForAllItemsInRegion:];
-[UIStatusBarForegroundView frameForItemOfType:];
-[UIStatusBarForegroundView ignoringData];
-[UIStatusBarForegroundView initWithFrame:foregroundStyle:usesVerticalLayout:];
-[UIStatusBarForegroundView isShowingBreadcrumb];
-[UIStatusBarForegroundView rectIntersectsBatteryItem:];
-[UIStatusBarForegroundView rectIntersectsTimeItem:];
-[UIStatusBarForegroundView reflowItemViews:];
-[UIStatusBarForegroundView reflowItemViewsCrossfadingCenter:duration:];
-[UIStatusBarForegroundView reflowItemViewsForgettingEitherSideItemHistory];
-[UIStatusBarForegroundView rightEdgePadding];
-[UIStatusBarForegroundView setStatusBarData:actions:animated:];
-[UIStatusBarForegroundView startIgnoringData];
-[UIStatusBarForegroundView stopIgnoringData:];
-[UIStatusBarForegroundView willChangeNavigationItemDisplayWithSystemNavigationAction:];
```
