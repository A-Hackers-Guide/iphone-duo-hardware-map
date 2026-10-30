# `AAController`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 20 instance variables, 16 properties, 70 instance methods, 0 class methods

## Instance variables

```
B _activateCalled;
B _invalidateCalled;
B _invalidateDone;
B _registeredWithManager;
I _clientID;
@? _batteryInfoMessageHandler;
@? _conversationDetectMessageHandler;
@? _rawGestureMessageHandler;
@? _sleepDetectionMessageHandler;
@? _preferenceEQMessageHandler;
@? _deviceInfoChangeHandler;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _interruptionHandler;
@? _invalidationHandler;
@? _multimodalContextMessageHandler;
@? _personalTranslationMessageHandler;
@? _pmeConfigMessageHandler;
@? _accessoryUsageSummaryMessageHandler;
@? _appleCareMessageHandler;
@? _setFeatureFlagMessageHandler;
```

## Properties

```
@property (TI,N,V_clientID) clientID;
@property (T@?,C,N,V_batteryInfoMessageHandler) batteryInfoMessageHandler;
@property (T@?,C,N,V_conversationDetectMessageHandler) conversationDetectMessageHandler;
@property (T@?,C,N,V_rawGestureMessageHandler) rawGestureMessageHandler;
@property (T@?,C,N,V_sleepDetectionMessageHandler) sleepDetectionMessageHandler;
@property (T@?,C,N,V_preferenceEQMessageHandler) preferenceEQMessageHandler;
@property (T@?,C,N,V_deviceInfoChangeHandler) deviceInfoChangeHandler;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (T@?,C,N,V_multimodalContextMessageHandler) multimodalContextMessageHandler;
@property (T@?,C,N,V_personalTranslationMessageHandler) personalTranslationMessageHandler;
@property (T@?,C,N,V_pmeConfigMessageHandler) pmeConfigMessageHandler;
@property (T@?,C,N,V_accessoryUsageSummaryMessageHandler) accessoryUsageSummaryMessageHandler;
@property (T@?,C,N,V_appleCareMessageHandler) appleCareMessageHandler;
@property (T@?,C,N,V_setFeatureFlagMessageHandler) setFeatureFlagMessageHandler;
```

## Instance methods

```
-[AAController xpcReceivedMessage:];
-[AAController _xpcReceivedMessage:];
-[AAController clientID];
-[AAController dispatchQueue];
-[AAController _accessoryUsageSummaryMessageReceived:fromDevice:];
-[AAController _registerWithSharedManager:];
-[AAController _multimodalContextMessageReceived:fromDevice:];
-[AAController activateWithCompletion:];
-[AAController setPreferenceEQMessageHandler:];
-[AAController setSleepDetectionMessageHandler:];
-[AAController sleepDetectionMessageHandler];
-[AAController setPersonalTranslationMessageHandler:];
-[AAController setSetFeatureFlagMessageHandler:];
-[AAController setClientID:];
-[AAController sendGetTipiTableMessageToDestinationIdentifier:completionHandler:];
-[AAController _sendAccessoryEventMessage:eventType:destinationIdentifier:completionHandler:];
-[AAController setInvalidationHandler:];
-[AAController setPmeConfigMessageHandler:];
-[AAController init];
-[AAController setAppleCareMessageHandler:];
-[AAController accessoryUsageSummaryMessageHandler];
-[AAController sendSleepDetectionMessage:destinationIdentifier:completionHandler:];
-[AAController sendPMEConfigData:destinationIdentifier:completionHandler:];
-[AAController interruptionHandler];
-[AAController pmeConfigMessageHandler];
-[AAController conversationDetectMessageHandler];
-[AAController personalTranslationMessageHandler];
-[AAController setDispatchQueue:];
-[AAController sendMultimodalContextMessage:destinationIdentifier:completionHandler:];
-[AAController sendPreferenceEQMessage:destinationIdentifier:completionHandler:];
-[AAController sendFeatureFlagMessage:destinationIdentifier:completionHandler:];
-[AAController _xpcReceivedAudioAccessoryDeviceInfoChange:];
-[AAController batteryInfoMessageHandler];
-[AAController invalidate];
-[AAController preferenceEQMessageHandler];
-[AAController setRawGestureMessageHandler:];
-[AAController _activate:];
-[AAController multimodalContextMessageHandler];
-[AAController _interrupted];
-[AAController rawGestureMessageHandler];
-[AAController _batteryInfoMessageReceived:fromDevice:];
-[AAController _pmeConfigDataReceived:fromDevice:];
-[AAController setFeatureFlagMessageHandler];
-[AAController setInterruptionHandler:];
-[AAController _sleepDetectionMessageReceived:fromDevice:];
-[AAController setMultimodalContextMessageHandler:];
-[AAController _rawGestureMessageReceived:fromDevice:];
-[AAController setDeviceInfoChangeHandler:];
-[AAController description];
-[AAController appleCareMessageHandler];
-[AAController _personalTranslationMessageReceived:fromDevice:];
-[AAController setAccessoryUsageSummaryMessageHandler:];
-[AAController sendAppleCareAccessoryConfig:destinationIdentifier:completionHandler:];
-[AAController _sendDeviceConfig:destinationIdentifier:completionHandler:];
-[AAController sendPTEventMessage:destinationIdentifier:completionHandler:];
-[AAController _requestAllAADeviceInfosWithCompletionHandler:];
-[AAController deviceInfoChangeHandler];
-[AAController invalidationHandler];
-[AAController _conversationDetectMessageReceived:fromDevice:];
-[AAController _preferenceEQMessageReceived:fromDevice:];
-[AAController _setFeatureFlagMessageReceived:fromDevice:];
-[AAController sendConversationDetectMessage:destinationIdentifier:completionHandler:];
-[AAController sendDEOCTempDisableIntervalMessage:destinationIdentifier:completionHandler:];
-[AAController setConversationDetectMessageHandler:];
-[AAController _invalidated];
-[AAController _xpcReceivedAccessoryEvent:];
-[AAController requestAllAADeviceInfosWithCompletionHandler:];
-[AAController setBatteryInfoMessageHandler:];
-[AAController _appleCareMessageReceived:fromDevice:];
-[AAController sendDeviceConfig:destinationIdentifier:completionHandler:];
```
