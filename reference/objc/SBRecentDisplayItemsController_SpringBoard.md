# `SBRecentDisplayItemsController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAppInteractionEventSourceObserving`
- 11 instance variables, 6 properties, 42 instance methods, 0 class methods

## Instance variables

```
@"NSMutableOrderedSet" _recentDisplayItems;
q _removalPersonality;
q _movePersonality;
@"NSSet" _relevantTransitionFromSources;
Q _maxDisplayItems;
@"SBApplicationController" _appController;
@"<SBIconModelProviding>" _iconModelProvider;
@"<BSInvalidatable>" _stateCaptureInvalidatable;
@"NSTimer" _delayAfterTransitionTimer;
@"SBHomeGestureSettings" _homeGestureSettings;
@"<SBRecentDisplayItemsControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"NSOrderedSet",C,N) recentDisplayItems;
@property (T@"<SBRecentDisplayItemsControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBRecentDisplayItemsController eventSource:userTouchedApplication:];
-[SBRecentDisplayItemsController init];
-[SBRecentDisplayItemsController dealloc];
-[SBRecentDisplayItemsController reset];
-[SBRecentDisplayItemsController setDelegate:];
-[SBRecentDisplayItemsController delegate];
-[SBRecentDisplayItemsController eventSource:userDeletedWebBookmark:];
-[SBRecentDisplayItemsController _addStateCaptureHandler];
-[SBRecentDisplayItemsController _clearDelayAfterTransitionTimer];
-[SBRecentDisplayItemsController _addDisplayItemToFront:];
-[SBRecentDisplayItemsController _addOrMoveDisplayItemToFront:];
-[SBRecentDisplayItemsController _allDisplayItemsForBundleID:];
-[SBRecentDisplayItemsController _allDisplayItemsForUniqueID:];
-[SBRecentDisplayItemsController _allDisplayItemsForWebClipID:];
-[SBRecentDisplayItemsController _allDisplayItemsPassingTest:];
-[SBRecentDisplayItemsController _allowAppToAppearWhileHidden:];
-[SBRecentDisplayItemsController _applicationsBecameHidden:];
-[SBRecentDisplayItemsController _associatedWebClipIdentifierForAppClipIdentifier:sceneIdentifier:];
-[SBRecentDisplayItemsController _disallowAppFromAppearingWhileHidden:];
-[SBRecentDisplayItemsController _displayItem:matchesBundleID:];
-[SBRecentDisplayItemsController _displayItemForLayoutElement:];
-[SBRecentDisplayItemsController _displayItemIsExecutableOnCurrentPlatform:];
-[SBRecentDisplayItemsController _displayItemRepresentsAppClip:];
-[SBRecentDisplayItemsController _firstDisplayItemForBundleID:];
-[SBRecentDisplayItemsController _firstDisplayItemForUniqueID:];
-[SBRecentDisplayItemsController _isDisallowedDisplayItem:];
-[SBRecentDisplayItemsController _moveDisplayItemToFront:];
-[SBRecentDisplayItemsController _removeDisplayItem:];
-[SBRecentDisplayItemsController _setupDelayAfterTransitionTimerForActivatingElement:];
-[SBRecentDisplayItemsController _webClipForIdentifier:];
-[SBRecentDisplayItemsController eventSource:applicationsBecameHidden:];
-[SBRecentDisplayItemsController eventSource:applicationsBecameVisible:];
-[SBRecentDisplayItemsController eventSource:didBeginTransitionToMode:withLayoutState:activatingElement:triggeredBy:];
-[SBRecentDisplayItemsController eventSource:didFinishTransitionToMode:withLayoutState:activatingElement:triggeredBy:];
-[SBRecentDisplayItemsController eventSource:keyboardFocusChangedToApplication:];
-[SBRecentDisplayItemsController eventSource:userDeletedApplications:];
-[SBRecentDisplayItemsController eventSource:userQuitApplicationInSwitcher:];
-[SBRecentDisplayItemsController eventSource:userRemovedSuggestions:];
-[SBRecentDisplayItemsController initWithRemovalPersonality:movePersonality:transitionFromSources:maxDisplayItems:eventSource:applicationController:iconModelProvider:];
-[SBRecentDisplayItemsController recentDisplayItems];
-[SBRecentDisplayItemsController removeDisplayItem:];
-[SBRecentDisplayItemsController setRecentDisplayItems:];
```
