# `SBSearchPresenter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PTSettingsKeyObserver`, `SBHSearchPresenting`
- 16 instance variables, 21 properties, 62 instance methods, 0 class methods

## Instance variables

```
B _usesTransitionDistanceAsStartOffset;
B _scrollViewBeganScrollingFromTop;
@"<SBSearchPresenterDelegate>" _searchPresenterDelegate;
@"NSString" _identifier;
@"NSHashTable" _observers;
@"UIScrollView" _trackingScrollView;
@"SBHHomePullToSearchSettings" _pullToSearchSettings;
@"SBFFluidBehaviorSettings" _searchAnimationSettings;
q _presentationState;
d _presentationProgress;
d _presentationOffset;
d _presentationVelocity;
d _topOffset;
@"NSArray" _presentables;
@"NSArray" _interactionCompletions;
{SBHSearchInteractivePresentationMetrics="interactiveTransitionStartOffset"d"interactiveTransitionDistance"d"interactiveTransitionBeganFromTopLeeway"d"interactiveActivationThreshold"d} _interactivePresentationMetrics;
```

## Properties

```
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T@"NSHashTable",R,C,N,V_observers) observers;
@property (T@"UIScrollView",&,N,V_trackingScrollView) trackingScrollView;
@property (T@"SBHHomePullToSearchSettings",&,N,V_pullToSearchSettings) pullToSearchSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_searchAnimationSettings) searchAnimationSettings;
@property (Tq,N,V_presentationState) presentationState;
@property (Td,N,V_presentationProgress) presentationProgress;
@property (Td,N,V_presentationOffset) presentationOffset;
@property (Td,N,V_presentationVelocity) presentationVelocity;
@property (TB,N,V_scrollViewBeganScrollingFromTop) scrollViewBeganScrollingFromTop;
@property (Td,N,V_topOffset) topOffset;
@property (T@"NSArray",C,N,V_presentables) presentables;
@property (T@"NSArray",C,N,V_interactionCompletions) interactionCompletions;
@property (T@"<SBSearchPresenterDelegate>",W,N,V_searchPresenterDelegate) searchPresenterDelegate;
@property (T{SBHSearchInteractivePresentationMetrics=dddd},N,V_interactivePresentationMetrics) interactivePresentationMetrics;
@property (TB,N) usesTransitionDistanceAsStartOffset;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N,GisPresenting) presenting;
```

## Instance methods

```
-[SBSearchPresenter topOffset];
-[SBSearchPresenter pullToSearchSettings];
-[SBSearchPresenter presentationState];
-[SBSearchPresenter identifier];
-[SBSearchPresenter _searchPresentationProgressForOffset:];
-[SBSearchPresenter _didPresentSearch];
-[SBSearchPresenter setPresentationState:];
-[SBSearchPresenter settings:changedValueForKey:];
-[SBSearchPresenter _willPresentSearchAnimated:];
-[SBSearchPresenter setScrollViewBeganScrollingFromTop:];
-[SBSearchPresenter _didDismissSearch];
-[SBSearchPresenter setPresentationProgress:];
-[SBSearchPresenter scrollViewWillBeginDragging:];
-[SBSearchPresenter setTopOffset:];
-[SBSearchPresenter layout];
-[SBSearchPresenter setSearchAnimationSettings:];
-[SBSearchPresenter observers];
-[SBSearchPresenter scrollViewBeganScrollingFromTop];
-[SBSearchPresenter scrollViewWillEndDragging:withVelocity:];
-[SBSearchPresenter scrollViewDidScroll:];
-[SBSearchPresenter _rubberbandingOffsetForContentOffset:];
-[SBSearchPresenter isPresenting];
-[SBSearchPresenter _willDismissSearchAnimated:];
-[SBSearchPresenter searchAnimationSettings];
-[SBSearchPresenter setTrackingScrollView:];
-[SBSearchPresenter trackingScrollView];
-[SBSearchPresenter addSearchPresenterObserver:];
-[SBSearchPresenter dismissSearchAnimated:];
-[SBSearchPresenter interactivePresentationMetrics];
-[SBSearchPresenter presentSearchAnimated:];
-[SBSearchPresenter presentationOffset];
-[SBSearchPresenter removeSearchPresenterObserver:];
-[SBSearchPresenter presentationProgress];
-[SBSearchPresenter _canPresent];
-[SBSearchPresenter _noteWillBeginModifyingPresentationProgressForState:animated:];
-[SBSearchPresenter _sendDidDismissSearchToDelegateAndObservers];
-[SBSearchPresenter _sendDidDismissSearchToObserver:];
-[SBSearchPresenter _sendDidPresentSearchToDelegateAndObservers];
-[SBSearchPresenter _sendDidPresentSearchToObserver:];
-[SBSearchPresenter _sendWillDismissSearch:toObserver:];
-[SBSearchPresenter _sendWillDismissSearchToDelegateAndObservers:];
-[SBSearchPresenter _sendWillPresentSearch:toObserver:];
-[SBSearchPresenter _sendWillPresentSearchToDelegateAndObservers:];
-[SBSearchPresenter _setUpInteractivePresentationMetrics];
-[SBSearchPresenter _setUpSearchAnimationSettings];
-[SBSearchPresenter _updatePresentables:withMode:];
-[SBSearchPresenter _updatePresentables:withMode:withCompletion:];
-[SBSearchPresenter _updatePresentablesWithMode:withCompletion:];
-[SBSearchPresenter initWithSettings:identifier:];
-[SBSearchPresenter interactionCompletions];
-[SBSearchPresenter presentables];
-[SBSearchPresenter presentationVelocity];
-[SBSearchPresenter searchPresenterDelegate];
-[SBSearchPresenter setInteractionCompletions:];
-[SBSearchPresenter setInteractivePresentationMetrics:];
-[SBSearchPresenter setPresentables:];
-[SBSearchPresenter setPresentationOffset:];
-[SBSearchPresenter setPresentationVelocity:];
-[SBSearchPresenter setPullToSearchSettings:];
-[SBSearchPresenter setSearchPresenterDelegate:];
-[SBSearchPresenter setUsesTransitionDistanceAsStartOffset:];
-[SBSearchPresenter usesTransitionDistanceAsStartOffset];
```
