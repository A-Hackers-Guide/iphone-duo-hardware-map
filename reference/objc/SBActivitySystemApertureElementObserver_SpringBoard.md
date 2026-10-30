# `SBActivitySystemApertureElementObserver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBActivitySystemApertureSceneHandleDelegate`, `SBSystemApertureSceneElementDelegate`, `SBActivityObserver`
- 16 instance variables, 4 properties, 64 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _sceneHandleByActivityIdentifier;
@"NSMutableDictionary" _alertSceneHandlesByActivityIdentifier;
@"NSMutableDictionary" _elementAssertionByActivityIdentifier;
@"NSMutableDictionary" _elementByActivityIdentifier;
@"NSMutableDictionary" _activeItemByActivityIdentifier;
@"NSMutableDictionary" _contentPayloadIDsByActivityIdentifier;
@"NSMutableDictionary" _prominenceStateByActivityIdentifier;
@"NSMutableArray" _pendingItems;
@"NSMutableSet" _activeWidgetActivitiesWithSceneHandles;
@"NSMutableOrderedSet" _pendingAlerts;
@"NSMutableSet" _ongoingActivities;
@"NSMutableSet" _activitiesWithSwappedScenes;
@"NSMutableDictionary" _alertingAssertionsByActivityIdentifier;
B _preparingElementForPendingAlert;
q _activityEnvironment;
@"SBActivityAlert" _activeAlert;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBActivitySystemApertureElementObserver _updateSceneHandleForActivityIdentifier:withDestinationToken:layoutDirection:];
-[SBActivitySystemApertureElementObserver systemApertureSceneElement:layoutDirectionDidChange:];
-[SBActivitySystemApertureElementObserver _prepareAndPresentActivityAlert:];
-[SBActivitySystemApertureElementObserver activityDidEnd:];
-[SBActivitySystemApertureElementObserver _checkForPossibleSwapsForActivatedItem:];
-[SBActivitySystemApertureElementObserver _swapActivityItem:withItem:];
-[SBActivitySystemApertureElementObserver _updateSystemApertureElementProminence:item:];
-[SBActivitySystemApertureElementObserver _presentOrPendActivityAlert:];
-[SBActivitySystemApertureElementObserver _addPendingAlert:];
-[SBActivitySystemApertureElementObserver _unlockAndLaunchAppIfPossible:withAction:];
-[SBActivitySystemApertureElementObserver _registerSystemApertureElementForPendingActivityIfNecessary];
-[SBActivitySystemApertureElementObserver init];
-[SBActivitySystemApertureElementObserver _hasValidAlertingAssertion];
-[SBActivitySystemApertureElementObserver _sendAnalyticsEventWithPayloadBuilder:];
-[SBActivitySystemApertureElementObserver _activityIsPendingForIdentifier:];
-[SBActivitySystemApertureElementObserver _swapItemWithRegisteredItemIfNecessary:itemAlerting:];
-[SBActivitySystemApertureElementObserver _removeSystemApertureSceneHandleWithItem:];
-[SBActivitySystemApertureElementObserver presentFallbackAlert:];
-[SBActivitySystemApertureElementObserver _activityAlertIsPendingForIdentifier:];
-[SBActivitySystemApertureElementObserver activityDidDismiss:];
-[SBActivitySystemApertureElementObserver _addPendingItemIfNecessary:];
-[SBActivitySystemApertureElementObserver _registeredElementExistsForBundleIdentifier:];
-[SBActivitySystemApertureElementObserver presentAlert:];
-[SBActivitySystemApertureElementObserver activityDidStart:];
-[SBActivitySystemApertureElementObserver _invalidateSystemApertureElementForItem:completion:];
-[SBActivitySystemApertureElementObserver _createSceneHandle:forAlerting:];
-[SBActivitySystemApertureElementObserver _storeSceneHandle:item:];
-[SBActivitySystemApertureElementObserver _createAndActivateElementForActivityItem:forAlerting:completion:];
-[SBActivitySystemApertureElementObserver _removePendingItem:withPendingAlerts:];
-[SBActivitySystemApertureElementObserver _cleanUpInvalidRegisteredElements];
-[SBActivitySystemApertureElementObserver _restoreOngoingActivityElementIfNecessaryForDismissingAlert:];
-[SBActivitySystemApertureElementObserver _removePendingAlertForItem:];
-[SBActivitySystemApertureElementObserver _presentPendingAlertIfNecessary];
-[SBActivitySystemApertureElementObserver _activityHasDifferentAlertSceneTarget:];
-[SBActivitySystemApertureElementObserver dismissAlert:];
-[SBActivitySystemApertureElementObserver _shouldSwapActivityItem:withOtherItem:itemAlerting:];
-[SBActivitySystemApertureElementObserver _activityHasSwappedScene:];
-[SBActivitySystemApertureElementObserver _forwardElementContextChangesFromElement:forActivityIdentifier:];
-[SBActivitySystemApertureElementObserver _canRegisterElementForActivityItem:];
-[SBActivitySystemApertureElementObserver _createSystemApertureSceneHandleWithItem:forAlerting:];
-[SBActivitySystemApertureElementObserver _isActivityOngoing:];
-[SBActivitySystemApertureElementObserver _pendingItemForAlert:];
-[SBActivitySystemApertureElementObserver activityDidUpdate:];
-[SBActivitySystemApertureElementObserver _presentAlert:];
-[SBActivitySystemApertureElementObserver _sceneHandleForActivityIdentifier:];
-[SBActivitySystemApertureElementObserver _presentPendingAlertIfNecessaryForActivityIdentifier:];
-[SBActivitySystemApertureElementObserver activityEnvironmentChanged:];
-[SBActivitySystemApertureElementObserver systemApertureSceneElement:destinationTokenDidChange:];
-[SBActivitySystemApertureElementObserver _updatePendingItemWithItem:];
-[SBActivitySystemApertureElementObserver shouldHandleActivityItem:];
-[SBActivitySystemApertureElementObserver systemApertureSceneHandle:updatedContentPayloadID:];
-[SBActivitySystemApertureElementObserver _stopAlertingForActivityIdentifier:];
-[SBActivitySystemApertureElementObserver _activatedElementItemForBundleIdentifier:];
-[SBActivitySystemApertureElementObserver _canPresentAlert:];
-[SBActivitySystemApertureElementObserver systemApertureSceneHandle:requestsLaunchWithAction:];
-[SBActivitySystemApertureElementObserver _swapToAlertSceneForActivityItem:completion:];
-[SBActivitySystemApertureElementObserver activityProminenceChanged:item:];
-[SBActivitySystemApertureElementObserver _prepareForAlertingActivityIfNecessary:completion:];
-[SBActivitySystemApertureElementObserver _cleanUpAlertPresentation:completion:];
-[SBActivitySystemApertureElementObserver _systemApertureElementAssertionExistsForBundleIdentifier:];
-[SBActivitySystemApertureElementObserver activityWasBlockedForItem:];
-[SBActivitySystemApertureElementObserver _isContentReadyForAlert:];
-[SBActivitySystemApertureElementObserver _createAndActivateSystemApertureElementWithScene:item:forAlerting:completion:];
-[SBActivitySystemApertureElementObserver activityWasUnblockedForItem:];
```
