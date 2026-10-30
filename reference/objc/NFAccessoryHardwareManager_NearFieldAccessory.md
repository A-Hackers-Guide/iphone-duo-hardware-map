# `NFAccessoryHardwareManager`

- Image: [`/System/Library/PrivateFrameworks/NearFieldAccessory.framework/NearFieldAccessory`](../userland/System__Library__PrivateFrameworks__NearFieldAccessory.framework__NearFieldAccessory.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NFXPCServiceClientDelegate`
- 4 instance variables, 0 properties, 26 instance methods, 1 class methods

## Instance variables

```
@"NSMutableSet" _sessions;
@"NFXPCServiceClient" _xpcClient;
Q _xpcConnectionID;
I _hwSupport;
```

## Class methods

```
+[NFAccessoryHardwareManager sharedHardwareManager];
```

## Instance methods

```
-[NFAccessoryHardwareManager connect];
-[NFAccessoryHardwareManager init];
-[NFAccessoryHardwareManager dealloc];
-[NFAccessoryHardwareManager sessionDidEnd:];
-[NFAccessoryHardwareManager synchronousRemoteObjectProxyWithErrorHandler:];
-[NFAccessoryHardwareManager remoteObjectProxyWithErrorHandler:];
-[NFAccessoryHardwareManager startReaderSession:];
-[NFAccessoryHardwareManager didInterrupt:connectionID:];
-[NFAccessoryHardwareManager didInvalidate:];
-[NFAccessoryHardwareManager getPowerCounters:];
-[NFAccessoryHardwareManager pushSignedRF:];
-[NFAccessoryHardwareManager triggerDelayedWake:];
-[NFAccessoryHardwareManager enableMultiTag:];
-[NFAccessoryHardwareManager clearMultiTagState];
-[NFAccessoryHardwareManager getMultiTagState:];
-[NFAccessoryHardwareManager _connectIfNeeded:];
-[NFAccessoryHardwareManager getInfo];
-[NFAccessoryHardwareManager restartMultiTag];
-[NFAccessoryHardwareManager _cleanupSessions];
-[NFAccessoryHardwareManager enableLPCD:];
-[NFAccessoryHardwareManager getDieId:];
-[NFAccessoryHardwareManager getHwSupport:error:];
-[NFAccessoryHardwareManager getLastDetectedTags:];
-[NFAccessoryHardwareManager getRfSettings:];
-[NFAccessoryHardwareManager setClientName:onConnection:];
-[NFAccessoryHardwareManager updateHWSupport:error:];
```
