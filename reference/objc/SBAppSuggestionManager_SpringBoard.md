# `SBAppSuggestionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UABestAppSuggestionManagerDelegate`, `SBAttentionAwarenessClientDelegate`, `SBBacklightCoordinatorObserver`
- 13 instance variables, 4 properties, 28 instance methods, 1 class methods

## Instance variables

```
@"UABestAppSuggestionManager" _continuitySuggestionManager;
@"UABestAppSuggestion" _continuityCurrentBestSuggestion;
@"ATXProactiveSuggestionClient" _proactiveSuggestionClient;
@"ATXProactiveSuggestion" _currentProactiveBestSuggestion;
i _proactiveSuggestionNotificationToken;
@"SBBestAppSuggestion" _currentBestSuggestion;
@"NSCountedSet" _listeningReasons;
B _isListeningForContinuitySuggestion;
B _isListeningForExpertCenterSuggestion;
B _screenOnDueToUserEvent;
B _screenOnAndLookingForEvent;
@"SBAttentionAwarenessClient" _idleTouchAwarenessClient;
@"SBApplicationController" _applicationController;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBAppSuggestionManager sharedInstance];
```

## Instance methods

```
-[SBAppSuggestionManager clientDidResetForUserAttention:withEvent:];
-[SBAppSuggestionManager _screenDidDim];
-[SBAppSuggestionManager noteActivatingForAppSuggestion:fromSource:];
-[SBAppSuggestionManager _createSuggestionSources];
-[SBAppSuggestionManager _stopListeningForNotifications];
-[SBAppSuggestionManager _handleInitialSpringBoardLaunch];
-[SBAppSuggestionManager client:attentionLostTimeoutDidExpire:forConfigurationGeneration:withAssociatedObject:];
-[SBAppSuggestionManager _setContinuitySuggestionUpdatesEnabled:expertCenterSuggestionUpdatesEnabled:];
-[SBAppSuggestionManager enableListeningForUpdatesForReason:];
-[SBAppSuggestionManager _destroySuggestionSources];
-[SBAppSuggestionManager disableListeningForUpdatesForReason:];
-[SBAppSuggestionManager initWithApplicationController:];
-[SBAppSuggestionManager dealloc];
-[SBAppSuggestionManager noteNotActivatingForAppSuggestion:fromSource:];
-[SBAppSuggestionManager startFetchingPayloadForAppSuggestion:];
-[SBAppSuggestionManager performWithCurrentSuggestedAppAndApplication:];
-[SBAppSuggestionManager _calculateBestSuggestionAndNotifyListeners];
-[SBAppSuggestionManager bestAppSuggestionChanged:];
-[SBAppSuggestionManager backlightCoordinator:didUpdateAggregateBacklightState:fromSource:];
-[SBAppSuggestionManager _registerForProactiveSuggestionNotifications];
-[SBAppSuggestionManager proactiveSuggestionChanged];
-[SBAppSuggestionManager _deregisterFromProactiveSuggestionNotifications];
-[SBAppSuggestionManager _listenForNotifications];
-[SBAppSuggestionManager _evaluateSuggestionUpdates];
-[SBAppSuggestionManager currentSuggestedApp];
-[SBAppSuggestionManager backlightCoordinator:willUpdateAggregateBacklightState:fromSource:];
-[SBAppSuggestionManager _handleAppUninstall:];
-[SBAppSuggestionManager _screenDidUndim:];
```
