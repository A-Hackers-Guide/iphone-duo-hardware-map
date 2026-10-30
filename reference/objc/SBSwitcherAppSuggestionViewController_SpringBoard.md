# `SBSwitcherAppSuggestionViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 10 instance variables, 4 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"SBBestAppSuggestion" _bestAppSuggestion;
B _showSuggestions;
@"SBSwitcherAppSuggestionBannerView" _bannerView;
@"UITapGestureRecognizer" _tapGestureRecognizer;
@"UILongPressGestureRecognizer" _longPressGestureRecognizer;
B _presentingOrDismissingBanner;
@"NSObject<OS_dispatch_queue>" _setSuggestionQueue;
@"NSMutableSet" _pauseSuggestionUpdateReasons;
B _suggestionQueueSuspended;
@"<SBSwitcherAppSuggestionViewControllerDelegate>" _delegate;
```

## Properties

```
@property (TB,N,G_isSuggestionQueueSuspended,S_setSuggestionQueueSuspended:,V_suggestionQueueSuspended) suggestionQueueSuspended;
@property (T@"SBBestAppSuggestion",&,N,V_bestAppSuggestion) bestAppSuggestion;
@property (TB,N,V_showSuggestions) showSuggestions;
@property (T@"<SBSwitcherAppSuggestionViewControllerDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[SBSwitcherAppSuggestionViewController _insertAndAnimateInBottomBannerForSuggestion:completion:];
-[SBSwitcherAppSuggestionViewController _handleLongPress:];
-[SBSwitcherAppSuggestionViewController _animateOutAndRemoveCurrentBottomBannerWithCompletion:];
-[SBSwitcherAppSuggestionViewController setBestAppSuggestion:];
-[SBSwitcherAppSuggestionViewController _idleOnscreenRectForBottomBanner];
-[SBSwitcherAppSuggestionViewController dealloc];
-[SBSwitcherAppSuggestionViewController willMoveToParentViewController:];
-[SBSwitcherAppSuggestionViewController viewDidLoad];
-[SBSwitcherAppSuggestionViewController _bannerStyle];
-[SBSwitcherAppSuggestionViewController setShowSuggestions:];
-[SBSwitcherAppSuggestionViewController initWithNibName:bundle:];
-[SBSwitcherAppSuggestionViewController _setBestAppSuggestion:animationCompletion:];
-[SBSwitcherAppSuggestionViewController _evaluateSuggestionQueueSuspension];
-[SBSwitcherAppSuggestionViewController setDelegate:];
-[SBSwitcherAppSuggestionViewController _hasSuggestionBannerView];
-[SBSwitcherAppSuggestionViewController bestAppSuggestion];
-[SBSwitcherAppSuggestionViewController loadView];
-[SBSwitcherAppSuggestionViewController _handleBannerTap:];
-[SBSwitcherAppSuggestionViewController _activateBestAppSuggestion];
-[SBSwitcherAppSuggestionViewController delegate];
-[SBSwitcherAppSuggestionViewController _updateBottomBannerWithCompletion:];
-[SBSwitcherAppSuggestionViewController viewWillLayoutSubviews];
-[SBSwitcherAppSuggestionViewController _setSuggestionQueueSuspended:];
-[SBSwitcherAppSuggestionViewController showSuggestions];
-[SBSwitcherAppSuggestionViewController _offscreenRectForBottomBanner];
-[SBSwitcherAppSuggestionViewController _activateCurrentSuggestion];
-[SBSwitcherAppSuggestionViewController endPausingSuggestionUpdatesForReason:];
-[SBSwitcherAppSuggestionViewController beginPausingSuggestionUpdatesForReason:];
-[SBSwitcherAppSuggestionViewController _isSuggestionQueueSuspended];
```
