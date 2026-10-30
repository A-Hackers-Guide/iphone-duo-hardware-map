# `AccessoryHIDClient`

- Image: [`/System/Library/PrivateFrameworks/AccessoryHID.framework/AccessoryHID`](../userland/System__Library__PrivateFrameworks__AccessoryHID.framework__AccessoryHID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AccessoryHIDXPCClientProtocol`
- 5 instance variables, 9 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"<AccessoryHIDClientProtocol>" _delegate;
@"NSXPCConnection" _serverConnection;
@"<AccessoryHIDXPCServerProtocol>" _remoteObject;
@"NSMutableDictionary" _registeredHIDDescriptors;
@"NSLock" _registeredHIDDescriptorsLock;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_serverConnection) serverConnection;
@property (T@"<AccessoryHIDXPCServerProtocol>",&,N,V_remoteObject) remoteObject;
@property (T@"NSMutableDictionary",&,V_registeredHIDDescriptors) registeredHIDDescriptors;
@property (T@"NSLock",&,N,V_registeredHIDDescriptorsLock) registeredHIDDescriptorsLock;
@property (T@"<AccessoryHIDClientProtocol>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AccessoryHIDClient initWithDelegate:];
-[AccessoryHIDClient connectToServer];
-[AccessoryHIDClient setRemoteObject:];
-[AccessoryHIDClient serverConnection];
-[AccessoryHIDClient dealloc];
-[AccessoryHIDClient remoteObject];
-[AccessoryHIDClient setDelegate:];
-[AccessoryHIDClient delegate];
-[AccessoryHIDClient setServerConnection:];
-[AccessoryHIDClient getReportResponse:componentID:reportType:reportID:report:withReply:];
-[AccessoryHIDClient hidDescriptor:active:];
-[AccessoryHIDClient inReport:componentID:report:withReply:];
-[AccessoryHIDClient registerHIDDescriptor:componentID:dictionary:withReply:];
-[AccessoryHIDClient registeredHIDDescriptors];
-[AccessoryHIDClient registeredHIDDescriptorsLock];
-[AccessoryHIDClient sendGetReportForType:andID:fromUUID:];
-[AccessoryHIDClient sendOutReport:fromUUID:];
-[AccessoryHIDClient setRegisteredHIDDescriptors:];
-[AccessoryHIDClient setRegisteredHIDDescriptorsLock:];
-[AccessoryHIDClient unregisterAllDescriptors:withReply:];
-[AccessoryHIDClient unregisterHIDDescriptor:componentID:withReply:];
```
