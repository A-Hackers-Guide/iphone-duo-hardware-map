# `TUCallCenterXPCServer` (protocol)

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `TUCallServicesProxyCallActions`
- 0 instance variables, 0 properties, 26 instance methods, 0 class methods

## Instance methods

```
-[TUCallCenterXPCServer fetchAnonymousXPCEndpoint:];
-[TUCallCenterXPCServer performSmartHoldingRequest:completion:];
-[TUCallCenterXPCServer performRecordingRequest:completion:];
-[TUCallCenterXPCServer _performSmartHoldingRequest:completion:];
-[TUCallCenterXPCServer startReceptionistReply];
-[TUCallCenterXPCServer registerAnonymousXPCEndpoint:];
-[TUCallCenterXPCServer pullPersistedChannel:];
-[TUCallCenterXPCServer requestTranslationReportAConcernForCallUUID:];
-[TUCallCenterXPCServer deleteCustomGreetingForAccountUUID:];
-[TUCallCenterXPCServer sendReceptionistReply:];
-[TUCallCenterXPCServer screenWithRequest:];
-[TUCallCenterXPCServer stopTransmissionForBargeCall:sourceIsHandsfreeAccessory:];
-[TUCallCenterXPCServer performTranslationRequest:completion:];
-[TUCallCenterXPCServer joinConversationWithRequest:];
-[TUCallCenterXPCServer shouldAllowRingingCallStatusIndicator:];
-[TUCallCenterXPCServer shouldSuppressInCallStatusBar:];
-[TUCallCenterXPCServer startTransmissionForBargeCall:sourceIsHandsfreeAccessory:];
-[TUCallCenterXPCServer reportLocalPreviewStoppedForCallWithUniqueProxyIdentifier:];
-[TUCallCenterXPCServer dialWithRequest:displayContext:];
-[TUCallCenterXPCServer customSandboxedURLGreetingForAccountUUID:withCompletion:];
-[TUCallCenterXPCServer defaultGreeting:];
-[TUCallCenterXPCServer dialWithRequest:reply:];
-[TUCallCenterXPCServer fetchCurrentCallUpdates:];
-[TUCallCenterXPCServer pullCallFromClientUsingHandoffActivityUserInfo:reply:];
-[TUCallCenterXPCServer requestInitialState:];
-[TUCallCenterXPCServer saveCustomSandboxedURLGreeting:forAccountUUID:];
```
