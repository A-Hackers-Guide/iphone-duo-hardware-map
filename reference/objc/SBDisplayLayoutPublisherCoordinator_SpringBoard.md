# `SBDisplayLayoutPublisherCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSDisplayLayoutPublisherObserving`, `BLSBacklightStateObserving`, `SBDisplayContentModeTransitionObserver`
- 7 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _activeDisplayLayoutPublishers;
@"NSMutableSet" _activeLayoutElementAssertions;
@"FBMainDisplayLayoutPublisher" _targetPublisher;
@"<BSInvalidatable>" _spuriousTargetPublisherUpdatePreventionAssertion;
@"FBSDisplayConfiguration" _lastKnownDisplayConfiguration;
q _lastKnownBacklightState;
@"<FBSDisplayLayoutPublishing>" _primaryPublisher;
```

## Properties

```
@property (T@"<FBSDisplayLayoutPublishing>",&,N,V_primaryPublisher) primaryPublisher;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDisplayLayoutPublisherCoordinator init];
-[SBDisplayLayoutPublisherCoordinator displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBDisplayLayoutPublisherCoordinator displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBDisplayLayoutPublisherCoordinator publisher:didUpdateLayout:withTransition:];
-[SBDisplayLayoutPublisherCoordinator backlight:didCompleteUpdateToState:forEvent:];
-[SBDisplayLayoutPublisherCoordinator _needsUpdateLayoutForPublisher:];
-[SBDisplayLayoutPublisherCoordinator activateDisplayLayoutPublisher:];
-[SBDisplayLayoutPublisherCoordinator _needsUpdateLayoutElements:];
-[SBDisplayLayoutPublisherCoordinator _publishMultiTaskingArrangementForWindowSceneIfNeeded:];
-[SBDisplayLayoutPublisherCoordinator _targetElementsForLayout:];
-[SBDisplayLayoutPublisherCoordinator _updateLayout:withTransitionReason:];
-[SBDisplayLayoutPublisherCoordinator _windowSceneForPublisher:];
-[SBDisplayLayoutPublisherCoordinator invalidateDisplayLayoutPublisher:];
-[SBDisplayLayoutPublisherCoordinator primaryPublisher];
-[SBDisplayLayoutPublisherCoordinator setPrimaryPublisher:];
```
