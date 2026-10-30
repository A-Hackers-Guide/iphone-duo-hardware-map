# `FigExternalSyncDevice`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
Q _hpmentid;
Q _ssamentid;
Q _pid;
Q _vid;
I _serviceNotification;
^{IONotificationPort=} _ioServiceNotificationPort;
@"NSObject<OS_dispatch_queue>" _queue;
B _usbConnected;
B _ssamEnabled;
@"NSString" _externalSyncDeviceDeviceIdentifer;
```

## Properties

```
@property (TB,R,N,GisConnected,V_usbConnected) usbConnected;
@property (TB,R,N,GisSSAMEnabled,V_ssamEnabled) ssamEnabled;
@property (T@"NSString",R,N,V_externalSyncDeviceDeviceIdentifer) externalSyncDeviceDeviceIdentifer;
```

## Instance methods

```
-[FigExternalSyncDevice isConnected];
-[FigExternalSyncDevice dealloc];
-[FigExternalSyncDevice forceCleanup];
-[FigExternalSyncDevice _SSAMDeivceTerminatedService:];
-[FigExternalSyncDevice _setSSAMPortEnabled:];
-[FigExternalSyncDevice _setupSSAMInterestNotification];
-[FigExternalSyncDevice _teardownSSAMInterestNotification];
-[FigExternalSyncDevice externalSyncDeviceDeviceIdentifer];
-[FigExternalSyncDevice getDeviceInfoDict];
-[FigExternalSyncDevice initWithHpmEntID:ssamEntID:connectionState:vid:pid:];
-[FigExternalSyncDevice isSSAMEnabled];
```
