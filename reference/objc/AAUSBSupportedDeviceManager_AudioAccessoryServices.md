# `AAUSBSupportedDeviceManager`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 2 properties, 15 instance methods, 1 class methods

## Instance variables

```
@? _activateCompletion;
B _invalidateCalled;
B _invalidateDone;
@"NSXPCConnection" _xpcCnx;
I _clientID;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
```

## Properties

```
@property (TI,N,V_clientID) clientID;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
```

## Class methods

```
+[AAUSBSupportedDeviceManager supportsSecureCoding];
```

## Instance methods

```
-[AAUSBSupportedDeviceManager clientID];
-[AAUSBSupportedDeviceManager dispatchQueue];
-[AAUSBSupportedDeviceManager _ensureXPCStarted];
-[AAUSBSupportedDeviceManager setClientID:];
-[AAUSBSupportedDeviceManager init];
-[AAUSBSupportedDeviceManager setDispatchQueue:];
-[AAUSBSupportedDeviceManager invalidate];
-[AAUSBSupportedDeviceManager _interrupted];
-[AAUSBSupportedDeviceManager encodeWithCoder:];
-[AAUSBSupportedDeviceManager _reportError:];
-[AAUSBSupportedDeviceManager description];
-[AAUSBSupportedDeviceManager initWithCoder:];
-[AAUSBSupportedDeviceManager _invalidated];
-[AAUSBSupportedDeviceManager _handleServerDied];
-[AAUSBSupportedDeviceManager proxCardUserActionOnHeadphone:withAction:completion:];
```
