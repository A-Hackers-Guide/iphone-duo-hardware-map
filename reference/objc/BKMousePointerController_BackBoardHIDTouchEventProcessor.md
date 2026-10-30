# `BKMousePointerController`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKHIDEventAuthenticationMessageNamespaceResolving`, `BKOrientationObserver`, `BKDisplayBlankingObserver`, `BKSmartCoverObserver`, `BKCADisplayObserver`, `BKDisplayOrientationObserver`, `BKIOHIDServiceMatchObserver`, `BKIOHIDServiceDisappearanceObserver`, `BKGlobalKeyboardObserver`, `BKHIDEventProcessor`, `BSInvalidatable`
- 66 instance variables, 14 properties, 42 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _preferencesLock;
@"NSObject<OS_dispatch_queue>" _serviceTerminationQueue;
@"BKMousePointerControllerConfiguration" _configuration;
d _mainDisplayCornerRadius;
@"BKIOHIDServiceMatcher" _pointerHIDServiceMatcher;
@"NSMutableDictionary" _pointerHIDServiceByServiceID;
@"BKMousePointerAnalyticsReporter" _analyticsReporter;
@"BKCADisplayMonitor" _displayMonitor;
@"<BSInvalidatable>" _displayMonitorObservingAssertion;
@"NSString" _mainDisplayUUID;
@"NSString" _designatedMainDisplayUUID;
@"NSDictionary" _regionArrangementByCoalitionID;
@"NSDictionary" _regionArrangementByDisplayUUID;
@"NSDictionary" _availableDisplaysByUUID;
@"NSDictionary" _interestingDisplaysByUUID;
@"NSMutableDictionary" _displaysBecomingUninterestingByUUID;
@"NSArray" _displayArrangement;
@"BKMousePointerRegionArrangement" _regionArrangement;
@"BKMousePointerRegion" _pointerRegion;
@"NSMutableArray" _activePointerAnimations;
Q _pointerAnimationRevisionID;
{CGPoint="x"d"y"d} _pointerRegionPoint;
C _pointerRegionEdgeMask;
@"NSMutableSet" _disableEventsPIDs;
Q _interpolatedEventMask;
@"BKDisplayLink" _displayLink;
Q _displayLinkPauseTime;
Q _displayLinkUnpauseTime;
@"BSAbsoluteMachTimer" _displayLinkPauseTimer;
@"BKMouseEventAccumulator" _eventAccumulator;
@"NSSet" _lastEventContexts;
@"BKDisplayOrientationController" _displayOrientationController;
@"<BSInvalidatable>" _displayOrientationObservation;
q _rawDeviceOrientation;
@"NSMutableDictionary" _senderPropertiesBySenderID;
q _activeKeyboardModifiers;
@"BKTouchPadManager" _touchPadManager;
@"<BKGlobalKeyboardEventObserving>" _keyboardEventProcessor;
@"<BKSmartCoverObserving>" _smartCoverEventProcessor;
@"<BKDisplayRenderSpace>" _displayRenderSpace;
@"<BKOrientationProvider>" _orientationProvider;
@"<BSInvalidatable>" _orientationManagerObservationAssertion;
@"<BSInvalidatable>" _displayBlankingObservationAssertion;
@"<BSInvalidatable>" _keyboardEventObservationAssertion;
@"<BSInvalidatable>" _smartCoverObservationAssertion;
@"BKMousePointerAnnotationController" _annotationController;
@"BKMousePointerServiceServer" _ipcServer_do_not_access_directly;
@"NSMutableArray" _lifecycleObservers;
@"BKMousePointerEventStatisticsLogger" _statisticsLogger;
@"NSHashTable" _globalDevicePreferencesObservers;
@"NSMutableOrderedSet" _buttonDownRepositionAssertions;
@"NSMutableDictionary" _globalEventRoutesByDisplayID;
@"NSMutableSet" _globalContextsPinnedByMouse;
@"NSMutableSet" _hitTestContextsPinnedByMouse;
@"NSMutableDictionary" _modelUpdateSuppressionAssertionsByDisplayID;
@"NSDictionary" _interfaceOrientationByDisplayUUID;
B _debugVisualizationEnabled;
B _displayLinkDisabled;
B _readyToReceiveEvents;
B _eventsPaused;
B _displayLinkPaused;
B _haveUnassociatedMouse;
{atomic_flag="_Value"AB} _invalid;
@"BKSLocalDefaults" _localDefaults;
@"BKHIDClientConnectionManager" _HIDConnectionManager;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"BKSLocalDefaults",&,N,V_localDefaults) localDefaults;
@property (T@"BKHIDClientConnectionManager",&,N,V_HIDConnectionManager) HIDConnectionManager;
@property (T@"BKSMousePointerDevicePreferences",&,N) globalDevicePreferences;
@property (T{CGPoint=dd},R,N) globalPointerPosition;
@property (T{CGPoint=dd},R,N) normalizedGlobalPointerPosition;
@property (T@"NSArray",R,N) availableDevices;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKMousePointerController configurationWithContext:mousePointerServiceServer:];
```

## Instance methods

```
-[BKMousePointerController _displayLinkFired:];
-[BKMousePointerController displayOrientationController:interfaceOrientationDidChange:forDisplayUUID:];
-[BKMousePointerController dealloc];
-[BKMousePointerController processEvent:sender:dispatcher:];
-[BKMousePointerController initWithConfiguration:];
-[BKMousePointerController globalKeyboardModifiersDidChange:];
-[BKMousePointerController senderDisplayUUIDForAuthenticationMessage:];
-[BKMousePointerController invalidate];
-[BKMousePointerController matcher:servicesDidMatch:];
-[BKMousePointerController localDefaults];
-[BKMousePointerController serviceDidDisappear:];
-[BKMousePointerController setLocalDefaults:];
-[BKMousePointerController normalizedGlobalPointerPosition];
-[BKMousePointerController acquireButtonDownPointerRepositionAssertionForReason:contextRelativePointerPosition:onDisplay:restrictingToPID:];
-[BKMousePointerController getHitTestContextsAtPoint:withAdditionalContexts:onDisplay:withCompletion:];
-[BKMousePointerController globalDevicePreferences];
-[BKMousePointerController globalPointerPosition];
-[BKMousePointerController setDesignatedMainDisplayUUID:];
-[BKMousePointerController setGlobalDevicePreferences:];
-[BKMousePointerController smartCoverStateDidChange:];
-[BKMousePointerController availableDevices];
-[BKMousePointerController setDisplayArrangement:];
-[BKMousePointerController addLifecycleObserver:];
-[BKMousePointerController removeLifecycleObserver:];
-[BKMousePointerController HIDConnectionManager];
-[BKMousePointerController addGlobalDevicePreferencesObserver:];
-[BKMousePointerController destinationPIDMatchesHapticFeedbackRequestPID:];
-[BKMousePointerController display:didBecomeBlank:];
-[BKMousePointerController hitTestRegionsDidChange:forDisplayUUID:];
-[BKMousePointerController monitor:activeDisplaysDidChange:];
-[BKMousePointerController orientationProvider:deviceOrientationMayHaveChanged:changeSource:isDeviceOrientationLocked:];
-[BKMousePointerController removeGlobalDevicePreferencesObserver:];
-[BKMousePointerController setContextRelativePointerPosition:onDisplay:withAnimationParameters:restrictingToPID:auditPID:];
-[BKMousePointerController setContextRelativePointerPosition:withInitialVelocity:onDisplay:withDecelerationRate:restrictingToPID:auditPID:];
-[BKMousePointerController setEventsDisabled:pid:];
-[BKMousePointerController setGlobalPointerEventRoutes:forPID:displayUUID:];
-[BKMousePointerController setGlobalPointerPosition:auditToken:];
-[BKMousePointerController setGlobalPointerPosition:synthesizeEvents:auditToken:];
-[BKMousePointerController setHIDConnectionManager:];
-[BKMousePointerController setPointerPosition:onDisplay:withAnimationParameters:auditPID:];
-[BKMousePointerController stopRoutingGlobalEventsForPID:];
-[BKMousePointerController suppressPointerModelUpdatesAssertionForDisplay:reason:];
```
