# `BKHIDDirectTouchEventProcessor`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKHIDEventAuthenticationMessageNamespaceResolving`, `BKIOHIDServiceMatchObserver`, `BKIOHIDServiceDisappearanceObserver`, `BKGlobalKeyboardObserver`, `BKIOHIDServicePersistentPropertyHandling`, `BKDisplayOrientationObserver`, `BSDescriptionStreamable`, `BKHIDEventProcessor`, `BSInvalidatable`
- 34 instance variables, 17 properties, 73 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"<BKHIDEventHitTestDispatcher>" _dispatcher;
@"BKIOHIDServicePersistentPropertyController" _persistentPropertyController;
@"<BKHIDEventDeliveryManagerProviding>" _deliveryManagerProvider;
@"<BKDisplayRenderSpace>" _displayRenderSpace;
@"<BKGestureProcessingWrapping>" _gestureProcessorWrapper;
@"<BKOrientationProvider>" _orientationProvider;
@"BKTouchServiceClientManager" _touchServiceClientManager;
@"BKTouchDeliveryObservationManager" _deliveryObservationManager;
@"BKHIDEventSenderCache" _senderCache;
@"NSArray" _matchers;
@"BKIOHIDServiceSimplePersistentPropertySupport" _pencilOpaqueTouchPersistentPropertySupport;
@"BKTouchPadManager" _touchPadManager;
@"BKIOHIDService" _queue_mainDisplayDigitizerService;
@"BKIOHIDService" _queue_mainDisplayAOPDigitizerService;
@"BKIOHIDService" _queue_mainDisplayPencilDigitizerService;
d _queue_startMainDisplayDigitizerMatchingTime;
@"BSContinuousMachTimer" _queue_mainDisplayDigitizerSentinelTimer;
q _queue_interfaceOrientation;
q _queue_activeModifiers;
@"<BSInvalidatable>" _globalKeyboardObserver;
@"NSMutableDictionary" _queue_perDisplayInfo;
@"NSMutableDictionary" _queue_referenceToTouchStreamClient;
I _queue_previousVendedTouchStreamReference;
@"NSMutableDictionary" _queue_slotIDToSlotRecord;
@"NSMutableOrderedSet" _queue_touchEnterSlotIDs;
@"NSString" _queue_chamoisDisplayUUID;
@"<BSInvalidatable>" _displayOrientationObservation;
@"NSMutableSet" _queue_accessoryTouchscreenServices;
@"NSMutableDictionary" _queue_serviceSenderIDToChamoisDisplayUUID;
@"NSMutableDictionary" _queue_lifecycleObserversPerDisplay;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_shouldIgnoreTouchesWhileObjectInProximity;
B _queue_invalidated;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<BKDisplayRenderSpace>",R,N) displayRenderSpace;
@property (T@"BKTouchServiceClientManager",R,N) touchServiceClientManager;
@property (T@"<BKGestureProcessingWrapping>",&,N,V_gestureProcessorWrapper) gestureProcessorWrapper;
@property (T@"BKIOHIDService",R,&) mainDisplayDigitizerService;
@property (T@"BKIOHIDService",R,&) mainDisplayAOPDigitizerService;
@property (T@"BKIOHIDService",R,&) mainDisplayPencilDigitizerService;
@property (T@"BKTouchDeliveryObservationManager",&) deliveryObservationManager;
@property (T@"NSString",C) chamoisDisplayUUID;
@property (TB,N) shouldIgnoreTouchesWhileObjectInProximity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKHIDDirectTouchEventProcessor digitizerMatchingDictionaries];
```

## Instance methods

```
-[BKHIDDirectTouchEventProcessor initWithContext:];
-[BKHIDDirectTouchEventProcessor displayOrientationController:interfaceOrientationDidChange:forDisplayUUID:];
-[BKHIDDirectTouchEventProcessor cancelAndSuppressTouchesOnDisplay:reason:];
-[BKHIDDirectTouchEventProcessor transferTouchIdentifiers:count:toTargetID:];
-[BKHIDDirectTouchEventProcessor _queue_addServicesMatchingSenderDescriptor:inPerDisplayInfo:toArray:];
-[BKHIDDirectTouchEventProcessor setSessionID:];
-[BKHIDDirectTouchEventProcessor _queue_cancelLongPressTimerForSlotID:];
-[BKHIDDirectTouchEventProcessor invalidateTouchStreamReference:];
-[BKHIDDirectTouchEventProcessor _handleDirectTouchEvent:service:];
-[BKHIDDirectTouchEventProcessor cancelTouchesOnDisplay:];
-[BKHIDDirectTouchEventProcessor shouldIgnoreTouchesWhileObjectInProximity];
-[BKHIDDirectTouchEventProcessor mainDisplayDigitizerService];
-[BKHIDDirectTouchEventProcessor appendDescriptionToFormatter:];
-[BKHIDDirectTouchEventProcessor dealloc];
-[BKHIDDirectTouchEventProcessor processEvent:sender:dispatcher:];
-[BKHIDDirectTouchEventProcessor _queue_servicesMatchingSenderDescriptor:];
-[BKHIDDirectTouchEventProcessor cancelTouchesOnAllDisplays];
-[BKHIDDirectTouchEventProcessor _queue_startLongPressTimerForSlotRecord:slotID:targetID:];
-[BKHIDDirectTouchEventProcessor _queue_resetTouchAuthenticationInitialSampleEvent];
-[BKHIDDirectTouchEventProcessor _queue_displayInfoForDisplay:createIfNeeded:];
-[BKHIDDirectTouchEventProcessor addTouchLifecycleObserver:forDisplayUUID:];
-[BKHIDDirectTouchEventProcessor _queue_windowServerDidDeleteSlotID:];
-[BKHIDDirectTouchEventProcessor globalKeyboardModifiersDidChange:];
-[BKHIDDirectTouchEventProcessor setShouldIgnoreTouchesWhileObjectInProximity:];
-[BKHIDDirectTouchEventProcessor senderDisplayUUIDForAuthenticationMessage:];
-[BKHIDDirectTouchEventProcessor _queue_hasTouchEnterSlots];
-[BKHIDDirectTouchEventProcessor invalidate];
-[BKHIDDirectTouchEventProcessor setOffset:forTouchesWithUserIdentifier:];
-[BKHIDDirectTouchEventProcessor _queue_enumerateTouchStreamsForAllDisplaysUsingBlock:];
-[BKHIDDirectTouchEventProcessor setChamoisDisplayUUID:];
-[BKHIDDirectTouchEventProcessor matcher:servicesDidMatch:];
-[BKHIDDirectTouchEventProcessor initWithHitTestDispatcher:displayRenderSpace:deliveryManager:senderCache:serviceMatcherDataProvider:];
-[BKHIDDirectTouchEventProcessor cancelTouchesWithIdentifiers:];
-[BKHIDDirectTouchEventProcessor _queue_invalidateTouchStreamClient:reason:];
-[BKHIDDirectTouchEventProcessor _queue_enumerateDigitizersForDisplay:usingBlock:];
-[BKHIDDirectTouchEventProcessor mainDisplayPencilDigitizerService];
-[BKHIDDirectTouchEventProcessor postTouchAnnotations:sourcePID:];
-[BKHIDDirectTouchEventProcessor touchServiceClientManager];
-[BKHIDDirectTouchEventProcessor applyExtendedHitTestInformationForCAScreenCoordinates:displayUUID:toPathAttributes:forEvent:secureName:excludeContextIDs:];
-[BKHIDDirectTouchEventProcessor setGestureProcessorWrapper:];
-[BKHIDDirectTouchEventProcessor _queue_displayUUIDForDigitizerService:];
-[BKHIDDirectTouchEventProcessor setDeliveryObservationManager:];
-[BKHIDDirectTouchEventProcessor authenticationSpecificationForSlotID:registrantEntitled:];
-[BKHIDDirectTouchEventProcessor chamoisDisplayUUID];
-[BKHIDDirectTouchEventProcessor _determineServiceForEvent:sender:fromTouchPad:];
-[BKHIDDirectTouchEventProcessor _queue_applyCachedPropertiesToMultitouchService:];
-[BKHIDDirectTouchEventProcessor detachTouchIdentifiers:assignUserIdentifier:policy:offset:];
-[BKHIDDirectTouchEventProcessor _persistentPropertyKeyDenylist];
-[BKHIDDirectTouchEventProcessor didInitializeRegistryWithContext:];
-[BKHIDDirectTouchEventProcessor gestureProcessorWrapper];
-[BKHIDDirectTouchEventProcessor serviceDidDisappear:];
-[BKHIDDirectTouchEventProcessor _queue_slotRecordForSlotID:];
-[BKHIDDirectTouchEventProcessor setHitTestRegions:forDisplay:];
-[BKHIDDirectTouchEventProcessor _queue_touchStreamClientForReference:];
-[BKHIDDirectTouchEventProcessor _queue_postSyntheticEventForLongPressSlotID:targetID:];
-[BKHIDDirectTouchEventProcessor setInterfaceOrientation:forDisplayUUID:];
-[BKHIDDirectTouchEventProcessor _isPossibleChamoisTouchscreen:];
-[BKHIDDirectTouchEventProcessor _queue_enumerateDigitizersForAllDisplaysUsingBlock:];
-[BKHIDDirectTouchEventProcessor _queue_touchStreamInfoForDisplayUUID:createIfNeeded:];
-[BKHIDDirectTouchEventProcessor setPersistentProperties:forServicesMatchingDescriptor:];
-[BKHIDDirectTouchEventProcessor mainDisplayAOPDigitizerService];
-[BKHIDDirectTouchEventProcessor addTouchAuthenticationSpecifications:registrantEntitled:];
-[BKHIDDirectTouchEventProcessor setEventDispatchMode:ambiguityRecommendation:lastTouchTimestamp:forTouchStreamIdentifier:];
-[BKHIDDirectTouchEventProcessor _queue_digitizerStateForService:];
-[BKHIDDirectTouchEventProcessor displayRenderSpace];
-[BKHIDDirectTouchEventProcessor gestureCancelTouchesWithIdentifiers:];
-[BKHIDDirectTouchEventProcessor cancelTouchesOnMainDisplay];
-[BKHIDDirectTouchEventProcessor deliveryObservationManager];
-[BKHIDDirectTouchEventProcessor _queue_addDigitizerStateForService:];
-[BKHIDDirectTouchEventProcessor handlesPersistentPropertiesForSenderDescriptor:];
-[BKHIDDirectTouchEventProcessor _queue_addTouchStreamClient:toDisplayUUID:versionedPID:];
-[BKHIDDirectTouchEventProcessor addTouchStreamForTargetID:display:versionedPID:identifier:shouldSendAmbiguityRecommendations:];
-[BKHIDDirectTouchEventProcessor setRoutingPolicy:forTouchesWithUserIdentifier:];
```
