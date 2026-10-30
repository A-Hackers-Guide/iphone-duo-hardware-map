# `ACCAssistiveTouchProvider`

- Image: [`/System/Library/PrivateFrameworks/AccessoryAssistiveTouch.framework/AccessoryAssistiveTouch`](../userland/System__Library__PrivateFrameworks__AccessoryAssistiveTouch.framework__AccessoryAssistiveTouch.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _cachedState;
@"NSString" _providerUID;
@"<ACCAssistiveTouchProviderProtocol>" _delegate;
@"NSXPCConnection" _serverConnection;
@"<ACCAssistiveTouchXPCServerProtocol>" _remoteObject;
@"NSMutableDictionary" _accessories;
```

## Properties

```
@property (T@"NSString",&,N,V_providerUID) providerUID;
@property (T@"<ACCAssistiveTouchProviderProtocol>",&,N,V_delegate) delegate;
@property (T@"NSXPCConnection",&,N,V_serverConnection) serverConnection;
@property (T@"<ACCAssistiveTouchXPCServerProtocol>",&,N,V_remoteObject) remoteObject;
@property (T@"NSMutableDictionary",&,N,V_accessories) accessories;
@property (TB,N,V_cachedState) cachedState;
```

## Instance methods

```
-[ACCAssistiveTouchProvider connectToServer];
-[ACCAssistiveTouchProvider setRemoteObject:];
-[ACCAssistiveTouchProvider serverConnection];
-[ACCAssistiveTouchProvider dealloc];
-[ACCAssistiveTouchProvider accessories];
-[ACCAssistiveTouchProvider providerUID];
-[ACCAssistiveTouchProvider remoteObject];
-[ACCAssistiveTouchProvider setDelegate:];
-[ACCAssistiveTouchProvider setAccessories:];
-[ACCAssistiveTouchProvider delegate];
-[ACCAssistiveTouchProvider setServerConnection:];
-[ACCAssistiveTouchProvider setProviderUID:];
-[ACCAssistiveTouchProvider setCachedState:];
-[ACCAssistiveTouchProvider cachedState];
-[ACCAssistiveTouchProvider accessoryAssistiveTouchAttached:];
-[ACCAssistiveTouchProvider accessoryAssistiveTouchDetachAll];
-[ACCAssistiveTouchProvider accessoryAssistiveTouchDetached:];
-[ACCAssistiveTouchProvider calculateDesiredState:];
-[ACCAssistiveTouchProvider initWithDelegate:initialState:];
-[ACCAssistiveTouchProvider notifyAssistiveTouchEnabledState:];
-[ACCAssistiveTouchProvider requestState:];
-[ACCAssistiveTouchProvider setEnabled:flag:];
```
