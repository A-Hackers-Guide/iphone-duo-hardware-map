# `SAAudioAccessory`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 23 instance methods, 0 class methods

## Instance variables

```
I _fProductID;
i _fBTSessionAttachRetryCount;
@"NSObject<OS_dispatch_queue>" _queue;
^{BTSessionImpl=} _fBTSession;
^{BTAccessoryManagerImpl=} _fBTAccessoryManager;
^{BTDeviceImpl=} _fBTDevice;
@"NSString" _fBTAddress;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T^{BTSessionImpl=},N,V_fBTSession) fBTSession;
@property (T^{BTAccessoryManagerImpl=},N,V_fBTAccessoryManager) fBTAccessoryManager;
@property (T^{BTDeviceImpl=},N,V_fBTDevice) fBTDevice;
@property (T@"NSString",&,N,V_fBTAddress) fBTAddress;
@property (TI,N,V_fProductID) fProductID;
@property (Ti,N,V_fBTSessionAttachRetryCount) fBTSessionAttachRetryCount;
```

## Instance methods

```
-[SAAudioAccessory initWithQueue:];
-[SAAudioAccessory reset];
-[SAAudioAccessory queue];
-[SAAudioAccessory setQueue:];
-[SAAudioAccessory attachBTSession];
-[SAAudioAccessory refreshBTDevice];
-[SAAudioAccessory btSessionEventHandler:event:result:];
-[SAAudioAccessory convertToSAInEarStatus:];
-[SAAudioAccessory fBTAccessoryManager];
-[SAAudioAccessory fBTAddress];
-[SAAudioAccessory fBTDevice];
-[SAAudioAccessory fBTSession];
-[SAAudioAccessory fBTSessionAttachRetryCount];
-[SAAudioAccessory fProductID];
-[SAAudioAccessory getInEarStatus:secondary:];
-[SAAudioAccessory getPrimaryBudSide];
-[SAAudioAccessory setBTAddress:];
-[SAAudioAccessory setFBTAccessoryManager:];
-[SAAudioAccessory setFBTAddress:];
-[SAAudioAccessory setFBTDevice:];
-[SAAudioAccessory setFBTSession:];
-[SAAudioAccessory setFBTSessionAttachRetryCount:];
-[SAAudioAccessory setFProductID:];
```
