# `SBHardwareButtonService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemServiceServerHardwareButtonDelegate`, `SBDisplayContentModeTransitionObserver`
- 12 instance variables, 9 properties, 65 instance methods, 1 class methods

## Instance variables

```
@"SBSystemServiceServer" _systemServiceServer;
@"FBServiceClientAuthenticator" _serviceClientHomeHardwareButtonHintSuppressionEntitlementAuthenticator;
@"FBServiceClientAuthenticator" _serviceClientEventConsumerEntitlement;
@"FBServiceClientAuthenticator" _serviceClientHintViewEntitlement;
@"RBSProcessMonitor" _processMonitor;
@"NSMutableArray" _observers;
@"BSMutableIntegerMap" _eventMaskPerKind;
@"BSMutableIntegerMap" _registrationsByButtonKind;
@"BSMutableIntegerMap" _clientsByPID;
@"SBApplicationController" _applicationController;
@"NSMapTable" _coordinatorsByWindowScene;
@"NSMapTable" _buttonHintViewRegistrationsByWindowScene;
```

## Properties

```
@property (T@"BSMutableIntegerMap",&,N,V_registrationsByButtonKind) registrationsByButtonKind;
@property (T@"BSMutableIntegerMap",&,N,V_clientsByPID) clientsByPID;
@property (T@"SBApplicationController",&,N,V_applicationController) applicationController;
@property (T@"NSMapTable",&,N,V_coordinatorsByWindowScene) coordinatorsByWindowScene;
@property (T@"NSMapTable",&,N,V_buttonHintViewRegistrationsByWindowScene) buttonHintViewRegistrationsByWindowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBHardwareButtonService sharedInstance];
```

## Instance methods

```
-[SBHardwareButtonService consumeLockButtonSinglePressUpWithPriority:];
-[SBHardwareButtonService _addRegistration:toClient:];
-[SBHardwareButtonService applicationController];
-[SBHardwareButtonService setCoordinatorsByWindowScene:];
-[SBHardwareButtonService systemServiceServer:client:fetchHapticTypeForButtonKind:completion:];
-[SBHardwareButtonService systemServiceServer:client:setHapticType:buttonKind:];
-[SBHardwareButtonService systemServiceServer:client:updateHintContentVisibility:forButton:animationSettings:];
-[SBHardwareButtonService setClientsByPID:];
-[SBHardwareButtonService init];
-[SBHardwareButtonService windowSceneDidDisconnect:];
-[SBHardwareButtonService displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBHardwareButtonService consumeLockButtonDoublePressUpWithPriority:];
-[SBHardwareButtonService setApplicationController:];
-[SBHardwareButtonService buttonHintViewRegistrationsByWindowScene];
-[SBHardwareButtonService consumeVolumeDecreaseButtonSinglePressUpWithPriority:];
-[SBHardwareButtonService systemServiceServer:client:updateSystemGlowStyle:];
-[SBHardwareButtonService displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBHardwareButtonService consumeVolumeIncreaseButtonSinglePressUpWithPriority:];
-[SBHardwareButtonService registerBezelEffectsCoordinator:forWindowScene:];
-[SBHardwareButtonService clientsByPID];
-[SBHardwareButtonService _process:stateDidUpdate:];
-[SBHardwareButtonService consumeHomeButtonLongPressWithPriority:];
-[SBHardwareButtonService _setSystemServiceClient:buttonKind:eventMask:priority:];
-[SBHardwareButtonService consumeHomeButtonTriplePressUpWithPriority:];
-[SBHardwareButtonService systemServiceServer:client:requestSystemGlowEffectWithInitialStyle:clientPort:];
-[SBHardwareButtonService _sendXPCMessageForEvent:buttonKind:priority:toClient:];
-[SBHardwareButtonService systemServiceServer:client:registerAssociatedHintViewContextId:renderId:size:buttonKind:clientPort:];
-[SBHardwareButtonService _reconfigureProcessMonitorForPredicates:];
-[SBHardwareButtonService _updateAllButtonEventMasks];
-[SBHardwareButtonService hasConsumersForHomeButtonSinglePress];
-[SBHardwareButtonService consumeRingerSwitchToggleStateOffWithPriority:];
-[SBHardwareButtonService addObserver:];
-[SBHardwareButtonService consumeHeadsetPlayPauseSinglePressDownWithPriority:continuation:];
-[SBHardwareButtonService _removeRegistration:fromClient:];
-[SBHardwareButtonService _updateEventMasksForButtonKind:];
-[SBHardwareButtonService coordinatorsByWindowScene];
-[SBHardwareButtonService registrationsByButtonKind];
-[SBHardwareButtonService hasConsumersForHomeButtonPresses];
-[SBHardwareButtonService hasConsumersForLockButtonDoublePressUp];
-[SBHardwareButtonService _applicationForClientInfo:];
-[SBHardwareButtonService setButtonHintViewRegistrationsByWindowScene:];
-[SBHardwareButtonService _reconfigureProcessMonitor];
-[SBHardwareButtonService systemServiceServer:client:requestsHIDEvents:token:forButtonKind:];
-[SBHardwareButtonService _initWithSystemServiceServer:];
-[SBHardwareButtonService systemServiceServer:client:setEventMask:buttonKind:priority:];
-[SBHardwareButtonService _sendEvent:buttonKind:withPriority:];
-[SBHardwareButtonService consumeHomeButtonDoublePressDownWithPriority:];
-[SBHardwareButtonService hasConsumersForLockButtonPresses];
-[SBHardwareButtonService consumeVolumeIncreaseButtonSinglePressDownWithPriority:continuation:];
-[SBHardwareButtonService consumeHomeButtonSinglePressUpWithPriority:];
-[SBHardwareButtonService _mutableRegistrationsForButtonKind:createIfNecessary:];
-[SBHardwareButtonService _firstAvailableBezelEffectsCoordinator];
-[SBHardwareButtonService setRegistrationsByButtonKind:];
-[SBHardwareButtonService consumeLockButtonLongPressWithPriority:];
-[SBHardwareButtonService _mutableRegistrationsForButtonKind:];
-[SBHardwareButtonService _performButtonRegistrationChangeAndNotifyObservers:];
-[SBHardwareButtonService _sendEvent:buttonKind:withPriority:continuation:];
-[SBHardwareButtonService consumeRingerSwitchToggleStateOnWithPriority:];
-[SBHardwareButtonService _hwButtonHintViewsSupported];
-[SBHardwareButtonService systemServiceServer:getHintViewsSupportedForClient:];
-[SBHardwareButtonService consumeHeadsetPlayPauseSinglePressUpWithPriority:];
-[SBHardwareButtonService systemServiceServer:client:acquireAssertionOfType:forReason:withCompletion:];
-[SBHardwareButtonService systemServiceServer:clientDidDisconnect:];
-[SBHardwareButtonService _registrationsForButtonKind:];
-[SBHardwareButtonService consumeVolumeDecreaseButtonSinglePressDownWithPriority:continuation:];
```
