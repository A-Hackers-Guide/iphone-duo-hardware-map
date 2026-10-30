# `BWFigCaptureDeviceClient`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 11 properties, 19 instance methods, 0 class methods

## Instance variables

```
i _clientID;
i _pid;
@"NSString" _applicationID;
{?="val"[8I]} _auditToken;
@"NSString" _clientDescription;
i _clientPriority;
B _canStealFromClientsWithSamePriority;
B _deviceSharingWithOtherClientsAllowed;
i _clientType;
@? _deviceAvailabilityChangedHandler;
```

## Properties

```
@property (Ti,R,N,V_clientID) clientID;
@property (Ti,R,N,V_pid) pid;
@property (T{?=[8I]},R,N,V_auditToken) auditToken;
@property (T@"NSString",R,N,V_applicationID) applicationID;
@property (T@"NSString",R,N,V_clientDescription) clientDescription;
@property (Ti,N,V_clientPriority) clientPriority;
@property (TB,R,N,V_canStealFromClientsWithSamePriority) canStealFromClientsWithSamePriority;
@property (TB,R,N,V_deviceSharingWithOtherClientsAllowed) deviceSharingWithOtherClientsAllowed;
@property (Ti,R,N,V_clientType) clientType;
@property (T@?,C,N,V_deviceAvailabilityChangedHandler) deviceAvailabilityChangedHandler;
@property (TB,R,N) canShareWithFlashlightAndVibeMitigation;
```

## Instance methods

```
-[BWFigCaptureDeviceClient clientType];
-[BWFigCaptureDeviceClient applicationID];
-[BWFigCaptureDeviceClient setClientPriority:];
-[BWFigCaptureDeviceClient clientID];
-[BWFigCaptureDeviceClient initWithClientAuditToken:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:clientType:deviceAvailabilityChangedHandler:];
-[BWFigCaptureDeviceClient debugDescription];
-[BWFigCaptureDeviceClient clientDescription];
-[BWFigCaptureDeviceClient dealloc];
-[BWFigCaptureDeviceClient deviceAvailabilityChangedHandler];
-[BWFigCaptureDeviceClient canShareWithFlashlightAndVibeMitigation];
-[BWFigCaptureDeviceClient pid];
-[BWFigCaptureDeviceClient deviceSharingWithOtherClientsAllowed];
-[BWFigCaptureDeviceClient setDeviceAvailabilityChangedHandler:];
-[BWFigCaptureDeviceClient description];
-[BWFigCaptureDeviceClient auditToken];
-[BWFigCaptureDeviceClient clientPriority];
-[BWFigCaptureDeviceClient canShareRegistrationWithClientPID:deviceAvailabilityChangedHandler:];
-[BWFigCaptureDeviceClient isEqual:];
-[BWFigCaptureDeviceClient canStealFromClientsWithSamePriority];
```
