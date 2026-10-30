# `BTShareAudioSessionClient`

- Image: [`/System/Library/PrivateFrameworks/BluetoothServices.framework/BluetoothServices`](../userland/System__Library__PrivateFrameworks__BluetoothServices.framework__BluetoothServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 8 instance variables, 4 properties, 19 instance methods, 1 class methods

## Instance variables

```
B _activateCalled;
B _invalidateCalled;
B _invalidateDone;
@"NSXPCConnection" _xpcCnx;
i _mode;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _progressHandler;
@"NSXPCListenerEndpoint" _testListenerEndpoint;
```

## Properties

```
@property (T@"NSXPCListenerEndpoint",&,N,V_testListenerEndpoint) testListenerEndpoint;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (Ti,N,V_mode) mode;
@property (T@?,C,N,V_progressHandler) progressHandler;
```

## Class methods

```
+[BTShareAudioSessionClient supportsSecureCoding];
```

## Instance methods

```
-[BTShareAudioSessionClient testListenerEndpoint];
-[BTShareAudioSessionClient setProgressHandler:];
-[BTShareAudioSessionClient dispatchQueue];
-[BTShareAudioSessionClient progressHandler];
-[BTShareAudioSessionClient _ensureXPCStarted];
-[BTShareAudioSessionClient setTestListenerEndpoint:];
-[BTShareAudioSessionClient init];
-[BTShareAudioSessionClient setMode:];
-[BTShareAudioSessionClient setDispatchQueue:];
-[BTShareAudioSessionClient invalidate];
-[BTShareAudioSessionClient _activate:];
-[BTShareAudioSessionClient _interrupted];
-[BTShareAudioSessionClient encodeWithCoder:];
-[BTShareAudioSessionClient mode];
-[BTShareAudioSessionClient activate];
-[BTShareAudioSessionClient initWithCoder:];
-[BTShareAudioSessionClient _invalidated];
-[BTShareAudioSessionClient shareAudioProgressEvent:info:];
-[BTShareAudioSessionClient userConfirmed:];
```
