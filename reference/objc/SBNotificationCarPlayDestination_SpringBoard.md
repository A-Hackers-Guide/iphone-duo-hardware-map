# `SBNotificationCarPlayDestination`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BNBannerHostMonitorListenerObserving`, `BNPresentableObserving`, `NCCarPlayBannerPresentableViewControllerDelegate`, `AFUserNotificationAnnouncementSpeakingStateDelegate`, `SiriDirectActionSourceDelegate`, `NCNotificationAlertDestination`
- 26 instance variables, 14 properties, 101 instance methods, 0 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
@"BNBannerHostMonitorListener" _bannerHostMonitorListener;
@"NSHashTable" _presentables;
@"CRCarPlayAppPolicyEvaluator" _appPolicyEvaluator;
@"NSMutableDictionary" _appPolicyForBundleID;
@"<BNPresentable>" _presentablePresentingAlertController;
@"NSMutableArray" _notificationRequestsForAnnounce;
@"NSMutableArray" _notificationRequestsPendingAnnounce;
@"NSMutableArray" _notificationRequestsPendingAVSession;
@"NCNotificationRequest" _notificationRequestPendingDeactivation;
@"NSMutableArray" _notificationRequestsPendingPreprocess;
@"NCNotificationRequest" _notificationRequestPreprocessed;
B _preprocessCompleted;
B _canActivateSiri;
B _fallbackBannerInFlight;
@"SiriDirectActionSource" _siriNotificationBannerActivationSource;
@"NSMutableSet" _notificationIdentifiersWithPresentedBanner;
@"NSMutableArray" _pendingFallbackBannerRequests;
@"AFUserNotificationAnnouncementSpeakingStateObserver" _announcementStateObserver;
@"NSMutableDictionary" _announceRequestsForNotificationRequests;
@"<NCNotificationAlertDestinationDelegate>" _delegate;
@"NCCarPlayBannerSource" _carPlayBannerSource;
@"SBNCAlertingController" _alertingController;
@"BSAbsoluteMachTimer" _announceTimeoutTimer;
@"NCNotificationRequest" _notificationRequestCurrentlyAnnouncing;
@"BSAbsoluteMachTimer" _preprocessTimeoutTimer;
```

## Properties

```
@property (T@"NCCarPlayBannerSource",R,N,G_carPlayBannerSource,V_carPlayBannerSource) carPlayBannerSource;
@property (T@"BSAbsoluteMachTimer",&,N,G_announceTimeoutTimer,S_setAnnounceTimeoutTimer:,V_announceTimeoutTimer) announceTimeoutTimer;
@property (T@"NCNotificationRequest",&,N,G_notificationRequestCurrentlyAnnouncing,S_setNotificationRequestCurrentlyAnnouncing:,V_notificationRequestCurrentlyAnnouncing) notificationRequestCurrentlyAnnouncing;
@property (T@"BSAbsoluteMachTimer",&,N,G_preprocessTimeoutTimer,S_setPreprocessTimeoutTimer:,V_preprocessTimeoutTimer) preprocessTimeoutTimer;
@property (TB,R,N,GisActive) active;
@property (T@"SBNCAlertingController",W,N,V_alertingController) alertingController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<NCNotificationAlertDestinationDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisAlertDestination) alertDestination;
@property (T@"NSString",R,N) identifier;
@property (T@"BSServiceConnectionEndpoint",R,N) endpoint;
```

## Instance methods

```
-[SBNotificationCarPlayDestination isAlertDestination];
-[SBNotificationCarPlayDestination presentableDidAppearAsBanner:];
-[SBNotificationCarPlayDestination identifier];
-[SBNotificationCarPlayDestination initWithApplicationController:];
-[SBNotificationCarPlayDestination dealloc];
-[SBNotificationCarPlayDestination endpoint];
-[SBNotificationCarPlayDestination _addPresentable:];
-[SBNotificationCarPlayDestination withdrawNotificationRequest:];
-[SBNotificationCarPlayDestination postNotificationRequest:];
-[SBNotificationCarPlayDestination setAlertingController:];
-[SBNotificationCarPlayDestination alertingController];
-[SBNotificationCarPlayDestination setDelegate:];
-[SBNotificationCarPlayDestination presentableWillAppearAsBanner:];
-[SBNotificationCarPlayDestination modifyNotificationRequest:];
-[SBNotificationCarPlayDestination canReceiveNotificationRequest:];
-[SBNotificationCarPlayDestination delegate];
-[SBNotificationCarPlayDestination _removePresentable:];
-[SBNotificationCarPlayDestination isActive];
-[SBNotificationCarPlayDestination presentableDidDisappearAsBanner:withReason:];
-[SBNotificationCarPlayDestination keyWindowForScreen:];
-[SBNotificationCarPlayDestination presentableWillNotAppearAsBanner:withReason:];
-[SBNotificationCarPlayDestination notificationAnnouncementObserver:announcementSpeakingStateDidUpdate:forNotificationRequestIdentifiers:];
-[SBNotificationCarPlayDestination canActivateChangedTo:];
-[SBNotificationCarPlayDestination bannerHostDidBecomeAvailableForMonitorListener:];
-[SBNotificationCarPlayDestination bannerHostDidBecomeUnavailableForMonitorListener:];
-[SBNotificationCarPlayDestination _isLinwoodCarPlayPreprocessEnabled];
-[SBNotificationCarPlayDestination didCancelBannerOfPresentableViewController:reason:];
-[SBNotificationCarPlayDestination didSelectBannerOfPresentableViewController:];
-[SBNotificationCarPlayDestination presentableViewControllerClosesByDefault:];
-[SBNotificationCarPlayDestination _invalidateAnnounceTimeoutTimer];
-[SBNotificationCarPlayDestination _preprocessNotificationRequest:];
-[SBNotificationCarPlayDestination _actionForNotificationRequest:];
-[SBNotificationCarPlayDestination _allNotificationActionsForNotificationRequest:];
-[SBNotificationCarPlayDestination _announceDeactivationReasonForBannerRevocationReason:];
-[SBNotificationCarPlayDestination _announceTimeoutTimer];
-[SBNotificationCarPlayDestination _announcementStateObserver];
-[SBNotificationCarPlayDestination _appPolicyEvaluator];
-[SBNotificationCarPlayDestination _bulletinForNotificationRequest:];
-[SBNotificationCarPlayDestination _callOrFaceTimeStateChanged];
-[SBNotificationCarPlayDestination _cancelAnnounceForNotificationRequest:withReason:deactivateAnnounce:];
-[SBNotificationCarPlayDestination _cancelCurrentPreprocessedSiriSession];
-[SBNotificationCarPlayDestination _cancelPreprocessOnWithdrawForRequest:];
-[SBNotificationCarPlayDestination _carPlayBannerSource];
-[SBNotificationCarPlayDestination _carPlayLaunchPolicyForNotificationRequest:];
-[SBNotificationCarPlayDestination _cleanupQueuesOnWithdrawForRequest:];
-[SBNotificationCarPlayDestination _clearCurrentPreprocessRequest];
-[SBNotificationCarPlayDestination _clearNotificationRequestPendingAnnounceDeactivationIfNecessaryDeactivatingAnnounce:];
-[SBNotificationCarPlayDestination _closeNotificationActionForNotificationRequest:];
-[SBNotificationCarPlayDestination _defaultActionTypeForNotificationRequest:];
-[SBNotificationCarPlayDestination _drainPendingFallbackBannerRequestsIfPossible];
-[SBNotificationCarPlayDestination _effectiveDefaultActionTypeForNotificationRequest:];
-[SBNotificationCarPlayDestination _enqueueFallbackBannerForRequest:];
-[SBNotificationCarPlayDestination _flushAnnounceNotificationRequestsShouldAnnounce:];
-[SBNotificationCarPlayDestination _flushNotificationRequestsPendingAnnounce];
-[SBNotificationCarPlayDestination _flushPreprocessRequests];
-[SBNotificationCarPlayDestination _handleAnnounceTimeoutForLinwoodPreprocess];
-[SBNotificationCarPlayDestination _hasRequestPreprocessed];
-[SBNotificationCarPlayDestination _hasRequestPreprocessing];
-[SBNotificationCarPlayDestination _ignoreActionForNotificationRequest:];
-[SBNotificationCarPlayDestination _inCallOrFaceTime];
-[SBNotificationCarPlayDestination _invalidatePreprocessTimeoutTimer];
-[SBNotificationCarPlayDestination _isCurrentlyAnnouncing];
-[SBNotificationCarPlayDestination _isSiriExcludedForNotificationRequest:];
-[SBNotificationCarPlayDestination _modifyNotificationRequest:inStore:];
-[SBNotificationCarPlayDestination _newPresentableForNotificationRequest:layoutDescription:];
-[SBNotificationCarPlayDestination _notificationRequestCurrentlyAnnouncing];
-[SBNotificationCarPlayDestination _notificationRequestForAnnounceWithIdentifier:];
-[SBNotificationCarPlayDestination _notificationRequestShouldShowModalSubActions:];
-[SBNotificationCarPlayDestination _notificationRequestSupportsSubActions:];
-[SBNotificationCarPlayDestination _policyForApp:];
-[SBNotificationCarPlayDestination _postCarPlayBannerForRequest:];
-[SBNotificationCarPlayDestination _postNotificationRequest:shouldAnnounce:shouldPreprocess:];
-[SBNotificationCarPlayDestination _preprocessTimeoutTimer];
-[SBNotificationCarPlayDestination _presentBannerForRequest:];
-[SBNotificationCarPlayDestination _presentSuccessBannerForRequest:];
-[SBNotificationCarPlayDestination _presentablesWithRequestIdentifier:];
-[SBNotificationCarPlayDestination _processNextPreprocessRequest];
-[SBNotificationCarPlayDestination _queueNotificationRequestWhileAnnouncing:];
-[SBNotificationCarPlayDestination _registerBannerPresentedForRequest:skipReasonForLogging:];
-[SBNotificationCarPlayDestination _removeNotificationRequestFromPendingAVSessionWithIdentifier:];
-[SBNotificationCarPlayDestination _requestAnnounceForNotificationRequest:];
-[SBNotificationCarPlayDestination _requestPreprocessForNotificationRequest:];
-[SBNotificationCarPlayDestination _setAnnounceTimeoutTimer:];
-[SBNotificationCarPlayDestination _setNotificationRequestCurrentlyAnnouncing:];
-[SBNotificationCarPlayDestination _setPreprocessTimeoutTimer:];
-[SBNotificationCarPlayDestination _setSuspended:forPresentingAlertControllerForPresentable:];
-[SBNotificationCarPlayDestination _shouldAnnounceNotificationForActiveAVSession:];
-[SBNotificationCarPlayDestination _shouldAnnounceNotificationRequest:];
-[SBNotificationCarPlayDestination _shouldDeactivateSiriSessionForNotificationRequest:bannerRevocationReason:];
-[SBNotificationCarPlayDestination _shouldDeferPostingNotificationRequestForAnnounce:];
-[SBNotificationCarPlayDestination _shouldPreprocessNotificationRequest:];
-[SBNotificationCarPlayDestination _startAnnounceTimeoutTimer];
-[SBNotificationCarPlayDestination _startPreprocessTimeoutTimer];
-[SBNotificationCarPlayDestination _subActionLabelsForNotificationRequest:];
-[SBNotificationCarPlayDestination _subActionsForNotificationRequest:];
-[SBNotificationCarPlayDestination _supplementaryActionsForNotificationRequest:];
-[SBNotificationCarPlayDestination _tearDownAnnounceOnWithdrawForLinwoodPreprocessForRequest:];
-[SBNotificationCarPlayDestination _tearDownAnnounceOnWithdrawForRequest:revokeSucceeded:];
-[SBNotificationCarPlayDestination _voicePromptStyleChanged:];
-[SBNotificationCarPlayDestination _withdrawNotificationRequest:inStore:];
-[SBNotificationCarPlayDestination _withdrawNotificationRequest:tearDownAnnounceForLinwoodPreprocess:];
```
