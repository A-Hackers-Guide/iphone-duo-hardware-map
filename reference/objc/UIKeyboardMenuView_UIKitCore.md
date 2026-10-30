# `UIKeyboardMenuView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UITableViewDataSource`, `UITableViewDelegate`, `UIDimmingViewDelegate`
- 32 instance variables, 14 properties, 104 instance methods, 0 class methods

## Instance variables

```
@"UIInputSwitcherTableView" m_table;
@"UIInputSwitcherShadowView" m_shadowView;
@"UIInputSwitcherSelectionExtraView" m_selExtraView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} m_referenceRect;
d m_pointerOffset;
B m_scrollable;
B m_startAutoscroll;
B m_scrolling;
B m_shouldFade;
{CGPoint="x"d"y"d} m_point;
d m_scrollStartTime;
i m_scrollDirection;
@"NSTimer" m_scrollTimer;
Q m_visibleRows;
Q m_firstVisibleRow;
q m_mode;
@"UIDimmingView" m_dimmingView;
@"UIView" m_inputView;
{CGPoint="x"d"y"d} m_referenceLocation;
@"UIKBKeyView" m_backgroundKeyView;
d m_timeDismissed;
q m_initialIndexInteracted;
B m_menuDrag;
@"UISelectionFeedbackGenerator" m_slideBehavior;
B _usesStraightLeftEdge;
B _usesDarkTheme;
B _showingCapsLockSwitcher;
q _indexForSelectedFastSwitchMode;
q _indexForUnselectedFastSwitchMode;
@"UIKBTree" _referenceKey;
@"UIKeyboardLayoutStar" _layout;
@"UIGlomojiAnalyticsDispatcher" _glomojiAnalyticsInstance;
```

## Properties

```
@property (Tq,N,Vm_mode) mode;
@property (TB,R) usesTable;
@property (TB,N,V_usesStraightLeftEdge) usesStraightLeftEdge;
@property (TB,N,V_usesDarkTheme) usesDarkTheme;
@property (TB,N,V_showingCapsLockSwitcher) showingCapsLockSwitcher;
@property (Tq,N,V_indexForSelectedFastSwitchMode) indexForSelectedFastSwitchMode;
@property (Tq,N,V_indexForUnselectedFastSwitchMode) indexForUnselectedFastSwitchMode;
@property (T@"UIKBTree",N,V_referenceKey) referenceKey;
@property (T@"UIKeyboardLayoutStar",N,V_layout) layout;
@property (T@"UIGlomojiAnalyticsDispatcher",&,N,V_glomojiAnalyticsInstance) glomojiAnalyticsInstance;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIKeyboardMenuView numberOfItems];
-[UIKeyboardMenuView hide];
-[UIKeyboardMenuView tableView:numberOfRowsInSection:];
-[UIKeyboardMenuView touchesEnded:withEvent:];
-[UIKeyboardMenuView tableView:cellForRowAtIndexPath:];
-[UIKeyboardMenuView referenceKey];
-[UIKeyboardMenuView setNeedsDisplay];
-[UIKeyboardMenuView clear];
-[UIKeyboardMenuView didMoveToWindow];
-[UIKeyboardMenuView touchesCancelled:withEvent:];
-[UIKeyboardMenuView dimmingView];
-[UIKeyboardMenuView setRenderConfig:];
-[UIKeyboardMenuView dimmingViewWasTapped:];
-[UIKeyboardMenuView table];
-[UIKeyboardMenuView applicationWillSuspend:];
-[UIKeyboardMenuView dealloc];
-[UIKeyboardMenuView isVisible];
-[UIKeyboardMenuView tableView:willDisplayCell:forRowAtIndexPath:];
-[UIKeyboardMenuView touchesBegan:withEvent:];
-[UIKeyboardMenuView touchesMoved:withEvent:];
-[UIKeyboardMenuView setMode:];
-[UIKeyboardMenuView containerView];
-[UIKeyboardMenuView tableView:heightForRowAtIndexPath:];
-[UIKeyboardMenuView inputView];
-[UIKeyboardMenuView removeFromSuperview];
-[UIKeyboardMenuView tableView:willSelectRowAtIndexPath:];
-[UIKeyboardMenuView mode];
-[UIKeyboardMenuView tableView:didSelectRowAtIndexPath:];
-[UIKeyboardMenuView show];
-[UIKeyboardMenuView setFrame:];
-[UIKeyboardMenuView layout];
-[UIKeyboardMenuView font];
-[UIKeyboardMenuView setReferenceKey:];
-[UIKeyboardMenuView initWithFrame:];
-[UIKeyboardMenuView preferredSize];
-[UIKeyboardMenuView setLayout:];
-[UIKeyboardMenuView scrollViewDidScroll:];
-[UIKeyboardMenuView setShowingCapsLockSwitcher:];
-[UIKeyboardMenuView indexPathForInputSwitcherCellIncludingInteractiveInsetsAtPoint:];
-[UIKeyboardMenuView setupBackgroundKeyViewWithSize:];
-[UIKeyboardMenuView usesDimmingView];
-[UIKeyboardMenuView didShow];
-[UIKeyboardMenuView _delayedFade];
-[UIKeyboardMenuView _internationalKeyRoundedCornerInLayout:];
-[UIKeyboardMenuView _renderConfig];
-[UIKeyboardMenuView autoscrollTimerFired:];
-[UIKeyboardMenuView centerPopUpOverKey];
-[UIKeyboardMenuView customizeCell:forItemAtIndex:];
-[UIKeyboardMenuView defaultSelectedIndex];
-[UIKeyboardMenuView didSelectItemAtIndex:];
-[UIKeyboardMenuView endScrolling:];
-[UIKeyboardMenuView fade];
-[UIKeyboardMenuView fadeWithDelay:];
-[UIKeyboardMenuView fadeWithDelay:forSelectionAtIndex:];
-[UIKeyboardMenuView fontForItemAtIndex:];
-[UIKeyboardMenuView getRowFromPoint:];
-[UIKeyboardMenuView glomojiAnalyticsInstance];
-[UIKeyboardMenuView highlightRow:];
-[UIKeyboardMenuView indexForSelectedFastSwitchMode];
-[UIKeyboardMenuView indexForUnselectedFastSwitchMode];
-[UIKeyboardMenuView insertSelExtraView];
-[UIKeyboardMenuView interactiveBounds];
-[UIKeyboardMenuView isPopupMode];
-[UIKeyboardMenuView launchedFromKeyboard];
-[UIKeyboardMenuView localizedTitleForItemAtIndex:];
-[UIKeyboardMenuView maskForShadowViewBlurredBackground];
-[UIKeyboardMenuView minYOfLastTableCellForSelectionExtraView];
-[UIKeyboardMenuView performShowAnimation];
-[UIKeyboardMenuView popupRect];
-[UIKeyboardMenuView returnToKeyboardIfNeeded];
-[UIKeyboardMenuView selectItemAtPoint:];
-[UIKeyboardMenuView setGlomojiAnalyticsInstance:];
-[UIKeyboardMenuView setHighlightForRowAtIndexPath:highlight:];
-[UIKeyboardMenuView setIndexForSelectedFastSwitchMode:];
-[UIKeyboardMenuView setIndexForUnselectedFastSwitchMode:];
-[UIKeyboardMenuView setKeyboardDimmed:];
-[UIKeyboardMenuView setNeedsDisplayForCell:];
-[UIKeyboardMenuView setNeedsDisplayForTopBottomCells];
-[UIKeyboardMenuView setUsesDarkTheme:];
-[UIKeyboardMenuView setUsesStraightLeftEdge:];
-[UIKeyboardMenuView setupShadowViewWithSize:];
-[UIKeyboardMenuView shouldSelectItemAtIndex:];
-[UIKeyboardMenuView shouldShow];
-[UIKeyboardMenuView shouldShowSelectionExtraViewForIndexPath:];
-[UIKeyboardMenuView showAsHUD];
-[UIKeyboardMenuView showAsHUDFromLocation:withInputView:touchBegan:];
-[UIKeyboardMenuView showAsPopupForKey:inLayout:];
-[UIKeyboardMenuView showingCapsLockSwitcher];
-[UIKeyboardMenuView stopAnyAutoscrolling];
-[UIKeyboardMenuView subtitleFont];
-[UIKeyboardMenuView subtitleFontForItemAtIndex:];
-[UIKeyboardMenuView subtitleForItemAtIndex:];
-[UIKeyboardMenuView supplementalVisibleFramesInView:];
-[UIKeyboardMenuView tableView:willDeselectRowAtIndexPath:];
-[UIKeyboardMenuView titleForItemAtIndex:];
-[UIKeyboardMenuView updateSelectionWithPoint:];
-[UIKeyboardMenuView usesDarkTheme];
-[UIKeyboardMenuView usesDeviceLanguageForItemAtIndex:];
-[UIKeyboardMenuView usesShadowView];
-[UIKeyboardMenuView usesStraightLeftEdge];
-[UIKeyboardMenuView usesTable];
-[UIKeyboardMenuView willFade];
-[UIKeyboardMenuView willFadeForSelectionAtIndex:];
-[UIKeyboardMenuView willShow];
```
