# `BTAudioSession`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 18 instance variables, 11 properties, 34 instance methods, 1 class methods

## Instance variables

```
B _activateCalled;
@? _activateCompletion;
B _invalidateCalled;
B _invalidateDone;
@"NSObject<OS_dispatch_source>" _timeoutTimer;
^{LogCategory=ii*I**i^{LogCategory}^{LogOutput}^{LogOutput}QQII*^{LogCategoryPrivate}} _ucat;
@"NSXPCConnection" _xpcCnx;
B _inAppRouting;
i _audioArbitrationResult;
i _category;
I _flags;
i _mode;
I _clientID;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _invalidationHandler;
@"NSString" _label;
d _timeoutSeconds;
@"NSXPCListenerEndpoint" _testListenerEndpoint;
```

## Properties

```
@property (TI,N,V_clientID) clientID;
@property (T@"NSXPCListenerEndpoint",&,N,V_testListenerEndpoint) testListenerEndpoint;
@property (Ti,N,V_audioArbitrationResult) audioArbitrationResult;
@property (Ti,N,V_category) category;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (TI,N,V_flags) flags;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (TB,N,V_inAppRouting) inAppRouting;
@property (T@"NSString",C,N,V_label) label;
@property (Td,N,V_timeoutSeconds) timeoutSeconds;
@property (Ti,N,V_mode) mode;
```

## Class methods

```
+[BTAudioSession supportsSecureCoding];
```

## Instance methods

```
-[BTAudioSession testListenerEndpoint];
-[BTAudioSession clientID];
-[BTAudioSession dispatchQueue];
-[BTAudioSession _activate];
-[BTAudioSession _ensureXPCStarted];
-[BTAudioSession setCategory:];
-[BTAudioSession activateWithCompletion:];
-[BTAudioSession setFlags:];
-[BTAudioSession setTestListenerEndpoint:];
-[BTAudioSession setClientID:];
-[BTAudioSession flags];
-[BTAudioSession setInvalidationHandler:];
-[BTAudioSession init];
-[BTAudioSession label];
-[BTAudioSession category];
-[BTAudioSession setLabel:];
-[BTAudioSession dealloc];
-[BTAudioSession setMode:];
-[BTAudioSession setDispatchQueue:];
-[BTAudioSession invalidate];
-[BTAudioSession _interrupted];
-[BTAudioSession encodeWithCoder:];
-[BTAudioSession mode];
-[BTAudioSession _reportError:];
-[BTAudioSession description];
-[BTAudioSession initWithCoder:];
-[BTAudioSession invalidationHandler];
-[BTAudioSession timeoutSeconds];
-[BTAudioSession _invalidated];
-[BTAudioSession setTimeoutSeconds:];
-[BTAudioSession audioArbitrationResult];
-[BTAudioSession inAppRouting];
-[BTAudioSession setAudioArbitrationResult:];
-[BTAudioSession setInAppRouting:];
```
