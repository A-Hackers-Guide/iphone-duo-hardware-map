# `SBActivityBannerObserver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBActivityBannerViewControllerDelegate`, `SBFZStackParticipantObserver`, `SBActivityObserver`
- 9 instance variables, 13 properties, 54 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _prominentAlertPresentingActivities;
@"NSMutableDictionary" _itemByActivityIdentifier;
@"NSMutableDictionary" _bannerPresentableByActivityIdentifier;
@"NSMapTable" _activityIdentifiersPerScene;
@"NSMutableDictionary" _ongoingActivityBannerPresentableByActivityIdentifier;
@"NSMutableDictionary" _revokePreventionActivityBundleIdToActivityIdentifiers;
q _activityEnvironment;
@"SBActivityBannerAuthority" _bannerAuthority;
@"SBActivityAlert" _activeAlert;
```

## Properties

```
@property (T@"NSMutableSet",&,N,V_prominentAlertPresentingActivities) prominentAlertPresentingActivities;
@property (T@"NSMutableDictionary",&,N,V_itemByActivityIdentifier) itemByActivityIdentifier;
@property (T@"NSMutableDictionary",&,N,V_bannerPresentableByActivityIdentifier) bannerPresentableByActivityIdentifier;
@property (T@"NSMapTable",&,N,V_activityIdentifiersPerScene) activityIdentifiersPerScene;
@property (T@"NSMutableDictionary",&,N,V_ongoingActivityBannerPresentableByActivityIdentifier) ongoingActivityBannerPresentableByActivityIdentifier;
@property (T@"NSMutableDictionary",&,N,V_revokePreventionActivityBundleIdToActivityIdentifiers) revokePreventionActivityBundleIdToActivityIdentifiers;
@property (Tq,N,V_activityEnvironment) activityEnvironment;
@property (T@"SBActivityBannerAuthority",&,N,V_bannerAuthority) bannerAuthority;
@property (T@"SBActivityAlert",&,N,V_activeAlert) activeAlert;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBActivityBannerObserver activityDidEnd:];
-[SBActivityBannerObserver zStackParticipantWithIdentifier:settingsDidChange:];
-[SBActivityBannerObserver _processZStackParticipantSettings:];
-[SBActivityBannerObserver init];
-[SBActivityBannerObserver zStackParticipantWithIdentifier:wasAcquiredWithSettings:];
-[SBActivityBannerObserver _sendAnalyticsEventWithPayloadBuilder:];
-[SBActivityBannerObserver dealloc];
-[SBActivityBannerObserver presentFallbackAlert:];
-[SBActivityBannerObserver activityDidDismiss:];
-[SBActivityBannerObserver setItemByActivityIdentifier:];
-[SBActivityBannerObserver presentAlert:];
-[SBActivityBannerObserver activityDidStart:];
-[SBActivityBannerObserver dismissAlert:];
-[SBActivityBannerObserver _isActivityOngoing:];
-[SBActivityBannerObserver activityEnvironmentChanged:];
-[SBActivityBannerObserver shouldHandleActivityItem:];
-[SBActivityBannerObserver itemByActivityIdentifier];
-[SBActivityBannerObserver _stopAlertingForActivityIdentifier:];
-[SBActivityBannerObserver setActiveAlert:];
-[SBActivityBannerObserver activeAlert];
-[SBActivityBannerObserver redisplayActivity:];
-[SBActivityBannerObserver activityProminenceChanged:item:];
-[SBActivityBannerObserver bannerAuthority];
-[SBActivityBannerObserver setActivityIdentifiersPerScene:];
-[SBActivityBannerObserver _addPresentable:forActivityIdentifier:];
-[SBActivityBannerObserver _createActivityBannerViewControllerForItem:payloadIdentifier:];
-[SBActivityBannerObserver _dismissBannerWithActivityIdentifier:];
-[SBActivityBannerObserver _dismissBannerWithActivityIdentifier:forceDismissal:];
-[SBActivityBannerObserver _handleActivityAlert:present:];
-[SBActivityBannerObserver _handleProminentActivityAlert:prominent:];
-[SBActivityBannerObserver _isBundleIdentifierSuppressed:];
-[SBActivityBannerObserver _postBannerWithActivityIdentifier:payloadIdentifier:prominent:completion:];
-[SBActivityBannerObserver _postBannerWithAlert:];
-[SBActivityBannerObserver _removePresentable:forActivityIdentifier:];
-[SBActivityBannerObserver _shouldShowSystemApertureUIForActivityItem:];
-[SBActivityBannerObserver _shouldSuppressPresentationForActivityIdentifier:];
-[SBActivityBannerObserver _windowSceneForActivityIdentifier:];
-[SBActivityBannerObserver activityBannerDidDisappear:activityIdentifier:];
-[SBActivityBannerObserver activityBannerWantsToBeDismissed:activityIdentifier:];
-[SBActivityBannerObserver activityBannerWillDisappear:activityIdentifier:];
-[SBActivityBannerObserver activityEnvironment];
-[SBActivityBannerObserver activityForBundleId:shouldPreventFromRevoke:];
-[SBActivityBannerObserver activityIdentifiersPerScene];
-[SBActivityBannerObserver bannerPresentableByActivityIdentifier];
-[SBActivityBannerObserver ongoingActivityBannerPresentableByActivityIdentifier];
-[SBActivityBannerObserver prominentAlertPresentingActivities];
-[SBActivityBannerObserver revokePreventionActivityBundleIdToActivityIdentifiers];
-[SBActivityBannerObserver setActivityEnvironment:];
-[SBActivityBannerObserver setBannerAuthority:];
-[SBActivityBannerObserver setBannerPresentableByActivityIdentifier:];
-[SBActivityBannerObserver setOngoingActivityBannerPresentableByActivityIdentifier:];
-[SBActivityBannerObserver setProminentAlertPresentingActivities:];
-[SBActivityBannerObserver setRevokePreventionActivityBundleIdToActivityIdentifiers:];
-[SBActivityBannerObserver shouldHandleRedisplayOfActivityItem:];
```
