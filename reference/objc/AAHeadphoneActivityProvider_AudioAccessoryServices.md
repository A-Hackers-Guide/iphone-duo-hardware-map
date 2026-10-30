# `AAHeadphoneActivityProvider`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 16 instance variables, 10 properties, 41 instance methods, 1 class methods

## Instance variables

```
B _activateCalled;
@? _activateCompletion;
B _direct;
B _invalidateCalled;
B _invalidateDone;
@"NSXPCConnection" _xpcCnx;
I _headphoneActivityProviderFlags;
I _clientID;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _interruptionHandler;
@? _invalidationHandler;
@? _sleepStateUpdateHandler;
@? _conversationAwarenessStateUpdateHandler;
@? _detailedCASignalStateUpdateHandler;
@? _activityFlagUpdateHandler;
@"NSXPCListenerEndpoint" _testListenerEndpoint;
```

## Properties

```
@property (TI,N,V_clientID) clientID;
@property (T@"NSXPCListenerEndpoint",&,N,V_testListenerEndpoint) testListenerEndpoint;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (T@?,C,N,V_sleepStateUpdateHandler) sleepStateUpdateHandler;
@property (T@?,C,N,V_conversationAwarenessStateUpdateHandler) conversationAwarenessStateUpdateHandler;
@property (T@?,C,N,V_detailedCASignalStateUpdateHandler) detailedCASignalStateUpdateHandler;
@property (T@?,C,N,V_activityFlagUpdateHandler) activityFlagUpdateHandler;
@property (TI,N,V_headphoneActivityProviderFlags) headphoneActivityProviderFlags;
```

## Class methods

```
+[AAHeadphoneActivityProvider supportsSecureCoding];
```

## Instance methods

```
-[AAHeadphoneActivityProvider detailedCASignalStateUpdated:forDeviceAddress:];
-[AAHeadphoneActivityProvider testListenerEndpoint];
-[AAHeadphoneActivityProvider _invalidateDirect];
-[AAHeadphoneActivityProvider clientID];
-[AAHeadphoneActivityProvider dispatchQueue];
-[AAHeadphoneActivityProvider _ensureXPCStarted];
-[AAHeadphoneActivityProvider activateWithCompletion:];
-[AAHeadphoneActivityProvider setTestListenerEndpoint:];
-[AAHeadphoneActivityProvider setClientID:];
-[AAHeadphoneActivityProvider activityFlagUpdated:forDeviceAddress:];
-[AAHeadphoneActivityProvider setConversationAwarenessStateUpdateHandler:];
-[AAHeadphoneActivityProvider setInvalidationHandler:];
-[AAHeadphoneActivityProvider init];
-[AAHeadphoneActivityProvider setDetailedCASignalStateUpdateHandler:];
-[AAHeadphoneActivityProvider sleepStateUpdateHandler];
-[AAHeadphoneActivityProvider _activateXPC:reactivate:];
-[AAHeadphoneActivityProvider _activateDirect:];
-[AAHeadphoneActivityProvider getDetailedCASignalStateForDeviceAddress:completion:];
-[AAHeadphoneActivityProvider activityFlagUpdateHandler];
-[AAHeadphoneActivityProvider getActivityFlagStateForDeviceAddress:completion:];
-[AAHeadphoneActivityProvider getConversationAwarenessStateForDeviceAddress:completion:];
-[AAHeadphoneActivityProvider interruptionHandler];
-[AAHeadphoneActivityProvider setDispatchQueue:];
-[AAHeadphoneActivityProvider detailedCASignalStateUpdateHandler];
-[AAHeadphoneActivityProvider getSleepStateForDeviceAddress:completion:];
-[AAHeadphoneActivityProvider invalidate];
-[AAHeadphoneActivityProvider _activate:];
-[AAHeadphoneActivityProvider conversationAwarenessStateUpdateHandler];
-[AAHeadphoneActivityProvider _interrupted];
-[AAHeadphoneActivityProvider encodeWithCoder:];
-[AAHeadphoneActivityProvider setInterruptionHandler:];
-[AAHeadphoneActivityProvider _reportError:];
-[AAHeadphoneActivityProvider setActivityFlagUpdateHandler:];
-[AAHeadphoneActivityProvider initWithCoder:];
-[AAHeadphoneActivityProvider setSleepStateUpdateHandler:];
-[AAHeadphoneActivityProvider invalidationHandler];
-[AAHeadphoneActivityProvider setHeadphoneActivityProviderFlags:];
-[AAHeadphoneActivityProvider sleepStateUpdated:sleepTimestamp:forDeviceAddress:];
-[AAHeadphoneActivityProvider headphoneActivityProviderFlags];
-[AAHeadphoneActivityProvider _invalidated];
-[AAHeadphoneActivityProvider conversationAwarenessStateUpdated:forDeviceAddress:];
```
