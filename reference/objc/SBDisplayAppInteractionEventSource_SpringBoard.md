# `SBDisplayAppInteractionEventSource`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSTouchDeliveryObserving`, `FBSDisplayLayoutPublisherObserving`, `SBApplicationRestrictionObserver`, `SBLayoutStateTransitionObserver`, `SBWindowSceneAttachmentObserving`, `SBAppInteractionEventSourceProviding`
- 9 instance variables, 12 properties, 37 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _appLayoutOnStage;
@"SBApplicationController" _applicationController;
@"NSString" _currentFocusedBundleID;
@"NSHashTable" _observers;
@"BKSTouchDeliveryObservationService" _touchDeliveryObservationService;
@"<FBSDisplayLayoutPublishing>" _displayLayoutPublisher;
@"SBApplicationRestrictionController" _applicationRestrictionController;
@"SBFAnalyticsClient" _analyticsClient;
@"SBLayoutStateTransitionCoordinator" _layoutStateTransitionCoordinator;
```

## Properties

```
@property (T@"NSString",C,N,V_currentFocusedBundleID) currentFocusedBundleID;
@property (T@"NSHashTable",R,N,V_observers) observers;
@property (T@"BKSTouchDeliveryObservationService",W,N,V_touchDeliveryObservationService) touchDeliveryObservationService;
@property (T@"<FBSDisplayLayoutPublishing>",&,N,V_displayLayoutPublisher) displayLayoutPublisher;
@property (T@"SBApplicationController",W,N,V_applicationController) applicationController;
@property (T@"SBApplicationRestrictionController",W,N,V_applicationRestrictionController) applicationRestrictionController;
@property (T@"SBFAnalyticsClient",W,N,V_analyticsClient) analyticsClient;
@property (T@"SBLayoutStateTransitionCoordinator",W,N,V_layoutStateTransitionCoordinator) layoutStateTransitionCoordinator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDisplayAppInteractionEventSource layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:];
-[SBDisplayAppInteractionEventSource applicationRestrictionController:didUpdateVisibleTags:hiddenTags:];
-[SBDisplayAppInteractionEventSource applicationController];
-[SBDisplayAppInteractionEventSource removeObserver:];
-[SBDisplayAppInteractionEventSource windowSceneDidDisconnect:];
-[SBDisplayAppInteractionEventSource initWithApplicationController:];
-[SBDisplayAppInteractionEventSource setApplicationController:];
-[SBDisplayAppInteractionEventSource dealloc];
-[SBDisplayAppInteractionEventSource publisher:didUpdateLayout:withTransition:];
-[SBDisplayAppInteractionEventSource layoutStateTransitionCoordinator];
-[SBDisplayAppInteractionEventSource _iconVisibilityDidChange:];
-[SBDisplayAppInteractionEventSource addObserver:];
-[SBDisplayAppInteractionEventSource layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:];
-[SBDisplayAppInteractionEventSource setDisplayLayoutPublisher:];
-[SBDisplayAppInteractionEventSource displayLayoutPublisher];
-[SBDisplayAppInteractionEventSource setLayoutStateTransitionCoordinator:];
-[SBDisplayAppInteractionEventSource analyticsClient];
-[SBDisplayAppInteractionEventSource _installedAppsDidChange:];
-[SBDisplayAppInteractionEventSource observers];
-[SBDisplayAppInteractionEventSource windowSceneDidConnect:];
-[SBDisplayAppInteractionEventSource touchDetachedForIdentifier:context:pid:];
-[SBDisplayAppInteractionEventSource touchUpOccuredForIdentifier:detached:context:pid:];
-[SBDisplayAppInteractionEventSource touchDeliveryObservationService];
-[SBDisplayAppInteractionEventSource _bundleIDsForIcons:];
-[SBDisplayAppInteractionEventSource _configureEventSourceWithAnalyticsClient:applicationController:applicationRestrictionController:iconModel:layoutStateTransitionCoordinator:displayLayoutPublisher:touchDeliveryObservationService:];
-[SBDisplayAppInteractionEventSource _initWithAnalyticsClient:applicationController:applicationRestrictionController:iconModel:layoutStateTransitionCoordinator:displayLayoutPublisher:touchDeliveryObservationService:];
-[SBDisplayAppInteractionEventSource _noteTouchForProcess:context:];
-[SBDisplayAppInteractionEventSource _notifyTransition:beginning:];
-[SBDisplayAppInteractionEventSource _userQuitApplication:];
-[SBDisplayAppInteractionEventSource _userRemovedSuggestion:];
-[SBDisplayAppInteractionEventSource _webBookmarkUninstalled:];
-[SBDisplayAppInteractionEventSource applicationRestrictionController];
-[SBDisplayAppInteractionEventSource currentFocusedBundleID];
-[SBDisplayAppInteractionEventSource setAnalyticsClient:];
-[SBDisplayAppInteractionEventSource setApplicationRestrictionController:];
-[SBDisplayAppInteractionEventSource setCurrentFocusedBundleID:];
-[SBDisplayAppInteractionEventSource setTouchDeliveryObservationService:];
```
