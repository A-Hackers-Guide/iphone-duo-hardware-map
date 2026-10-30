# `SBActivityManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ACUISActivityAlertClientDelegate`, `PTSettingsKeyPathObserver`, `SBActivityObservable`
- 17 instance variables, 18 properties, 66 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _bannerPresentableByActivityIdentifier;
@"NSHashTable" _observers;
@"NSObject<OS_dispatch_queue>" _activityProminenceQueue;
@"ACActivityProminenceListener" _queue_prominenceListener;
@"NSMutableDictionary" _queue_prominenceAssertionByActivityIdentifier;
q _environment;
@"ACActivityCenter" _activityCenter;
@"ACUISActivityAlertClient" _activityAlertClient;
@"<BSInvalidatable>" _activitySubscription;
@"<BSInvalidatable>" _activityExceedingReducedPushBudgetSubscription;
@"<BSInvalidatable>" _activityAlertSubscription;
@"DMFApplicationPolicyMonitor" _applicationPolicyMonitor;
@"NSMutableDictionary" _itemByActivityIdentifier;
@"NSMutableDictionary" _itemsByBundleIdentifier;
@"SBActivityAlert" _activeAlert;
@"SBLiveActivitySettings" _activitySettings;
@"NSMutableDictionary" _prominenceStateByActivityIdentifier;
```

## Properties

```
@property (T@"ACActivityCenter",&,N,V_activityCenter) activityCenter;
@property (T@"ACUISActivityAlertClient",&,N,V_activityAlertClient) activityAlertClient;
@property (T@"<BSInvalidatable>",&,N,V_activitySubscription) activitySubscription;
@property (T@"<BSInvalidatable>",&,N,V_activityExceedingReducedPushBudgetSubscription) activityExceedingReducedPushBudgetSubscription;
@property (T@"<BSInvalidatable>",&,N,V_activityAlertSubscription) activityAlertSubscription;
@property (T@"DMFApplicationPolicyMonitor",R,N,V_applicationPolicyMonitor) applicationPolicyMonitor;
@property (T@"NSMutableDictionary",&,N,V_itemByActivityIdentifier) itemByActivityIdentifier;
@property (T@"NSMutableDictionary",&,N,V_itemsByBundleIdentifier) itemsByBundleIdentifier;
@property (T@"NSMutableDictionary",&,N,V_queue_prominenceAssertionByActivityIdentifier) prominenceAssertionByActivityIdentifier;
@property (T@"SBActivityAlert",&,N,V_activeAlert) activeAlert;
@property (T@"ACActivityProminenceListener",&,N,V_queue_prominenceListener) prominenceListener;
@property (T@"SBLiveActivitySettings",&,N,V_activitySettings) activitySettings;
@property (T@"NSMutableDictionary",&,N,V_prominenceStateByActivityIdentifier) prominenceStateByActivityIdentifier;
@property (Tq,N,V_environment) environment;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBActivityManager startObservingActivityUpdates];
-[SBActivityManager _publishProminenceUpdate:item:];
-[SBActivityManager activities];
-[SBActivityManager setEnvironment:];
-[SBActivityManager setProminenceListener:];
-[SBActivityManager setActivityCenter:];
-[SBActivityManager _updateForScreenTimeLimitForBundleId:policy:];
-[SBActivityManager setItemsByBundleIdentifier:];
-[SBActivityManager removeObserver:];
-[SBActivityManager init];
-[SBActivityManager _sendAnalyticsEventWithPayloadBuilder:];
-[SBActivityManager _activityBlocked:item:];
-[SBActivityManager activityAlertClient:dismissAlertProvider:];
-[SBActivityManager isActivitySupported];
-[SBActivityManager _activityStartedOrUpdatedWithContentUpdate:];
-[SBActivityManager setProminenceStateByActivityIdentifier:];
-[SBActivityManager dealloc];
-[SBActivityManager itemsByBundleIdentifier];
-[SBActivityManager applicationPolicyMonitor];
-[SBActivityManager _addAppActivitiesRecordForBundleId:item:];
-[SBActivityManager setItemByActivityIdentifier:];
-[SBActivityManager _updateAllApplicationMonitoringPolicies];
-[SBActivityManager _presentActivityAlert:];
-[SBActivityManager _removeAppActivitiesRecordForBundleId:item:];
-[SBActivityManager setActivityAlertClient:];
-[SBActivityManager activityExceedingReducedPushBudgetSubscription];
-[SBActivityManager alertPresentationFailed:];
-[SBActivityManager setActivitySubscription:];
-[SBActivityManager _hideAllActivities:];
-[SBActivityManager firstPartyActivityGroupingIdentifiers];
-[SBActivityManager setActivityAlertSubscription:];
-[SBActivityManager setActivityExceedingReducedPushBudgetSubscription:];
-[SBActivityManager _activityLifecyclePayloadWithContentUpdate:];
-[SBActivityManager addObserver:];
-[SBActivityManager prominenceAssertionByActivityIdentifier];
-[SBActivityManager _stopActiveAlertForActivityIdentifier:];
-[SBActivityManager _activityHasDifferentAlertSceneTarget:];
-[SBActivityManager activityAlertClient];
-[SBActivityManager activitySubscription];
-[SBActivityManager prominenceListener];
-[SBActivityManager _sendAnalyticsLifecycleEventIfNecessaryWithContentUpdate:];
-[SBActivityManager lastRedisplayableActivityForBundleId:];
-[SBActivityManager activitySettings];
-[SBActivityManager _handleActivityWithContentUpdate:];
-[SBActivityManager _handleActivityExceedingReducedPushBudgetWithIdentifier:];
-[SBActivityManager itemByActivityIdentifier];
-[SBActivityManager setActiveAlert:];
-[SBActivityManager activeAlert];
-[SBActivityManager prominenceStateByActivityIdentifier];
-[SBActivityManager activityCenter];
-[SBActivityManager activityAlertClient:presentAlertProvider:completion:];
-[SBActivityManager _activityFinishedWithContentUpdate:];
-[SBActivityManager redisplayActivity:];
-[SBActivityManager _invalidateAllProminenceAssertion];
-[SBActivityManager _activityDismissedWithContentUpdate:];
-[SBActivityManager _queue_invalidateProminenceAssertionForActivityIdenfier:];
-[SBActivityManager cancelObservingActivityUpdates];
-[SBActivityManager _removeAllObservers];
-[SBActivityManager setActivitySettings:];
-[SBActivityManager _dismissActivityAlert:];
-[SBActivityManager _invalidateProminenceAssertionForActivityIdenfier:];
-[SBActivityManager activityAlertSubscription];
-[SBActivityManager preventPresentableFromRevoke:forBundleId:];
-[SBActivityManager settings:changedValueForKeyPath:];
-[SBActivityManager environment];
-[SBActivityManager setProminenceAssertionByActivityIdentifier:];
```
