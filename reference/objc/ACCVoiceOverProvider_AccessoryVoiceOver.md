# `ACCVoiceOverProvider`

- Image: [`/System/Library/PrivateFrameworks/AccessoryVoiceOver.framework/AccessoryVoiceOver`](../userland/System__Library__PrivateFrameworks__AccessoryVoiceOver.framework__AccessoryVoiceOver.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"<ACCVoiceOverProviderProtocol>" _delegate;
@"NSString" _providerUID;
@"NSXPCConnection" _serverConnection;
@"<ACCVoiceOverXPCServerProtocol>" _remoteObject;
@"NSMutableDictionary" _accessories;
```

## Properties

```
@property (T@"NSString",&,N,V_providerUID) providerUID;
@property (T@"NSXPCConnection",&,N,V_serverConnection) serverConnection;
@property (T@"<ACCVoiceOverXPCServerProtocol>",&,N,V_remoteObject) remoteObject;
@property (T@"NSMutableDictionary",&,N,V_accessories) accessories;
@property (T@"<ACCVoiceOverProviderProtocol>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[ACCVoiceOverProvider initWithDelegate:];
-[ACCVoiceOverProvider connectToServer];
-[ACCVoiceOverProvider setRemoteObject:];
-[ACCVoiceOverProvider serverConnection];
-[ACCVoiceOverProvider dealloc];
-[ACCVoiceOverProvider accessories];
-[ACCVoiceOverProvider providerUID];
-[ACCVoiceOverProvider remoteObject];
-[ACCVoiceOverProvider setDelegate:];
-[ACCVoiceOverProvider setAccessories:];
-[ACCVoiceOverProvider delegate];
-[ACCVoiceOverProvider setServerConnection:];
-[ACCVoiceOverProvider setProviderUID:];
-[ACCVoiceOverProvider calculateDesiredState:];
-[ACCVoiceOverProvider accessoryVoiceOver:performAction:parameters:];
-[ACCVoiceOverProvider accessoryVoiceOver:requestConfiguration:param:];
-[ACCVoiceOverProvider accessoryVoiceOver:setContext:];
-[ACCVoiceOverProvider accessoryVoiceOver:setEnabled:];
-[ACCVoiceOverProvider accessoryVoiceOverAttached:];
-[ACCVoiceOverProvider accessoryVoiceOverDetachAll];
-[ACCVoiceOverProvider accessoryVoiceOverDetached:];
-[ACCVoiceOverProvider accessoryVoiceOverStartCursorInformationUpdate:];
-[ACCVoiceOverProvider accessoryVoiceOverStartInformationUpdate:];
-[ACCVoiceOverProvider accessoryVoiceOverStopCursorInformationUpdate:];
-[ACCVoiceOverProvider accessoryVoiceOverStopInformationUpdate:];
-[ACCVoiceOverProvider updateVoiceOverCursorInfo:];
-[ACCVoiceOverProvider updateVoiceOverInfo:];
```
