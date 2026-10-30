# `BTBluetoothPairingSession`

- Image: [`/System/Library/PrivateFrameworks/BluetoothServices.framework/BluetoothServices`](../userland/System__Library__PrivateFrameworks__BluetoothServices.framework__BluetoothServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 34 instance variables, 14 properties, 35 instance methods, 0 class methods

## Instance variables

```
[32c] _btAddrStr;
B _btConfigured;
B _btConnecting;
^{BTDeviceImpl=} _btDevice;
B _btDisconnected;
^{BTPairingAgentImpl=} _btPairingAgent;
B _btPairingAgentStarted;
^{BTSessionImpl=} _btSession;
B _btSessionAddedServiceCallback;
B _btSessionAttaching;
B _btStarted;
B _invalidateCalled;
I _retryCount;
B _retryOnDetach;
@"NSObject<OS_dispatch_source>" _retryTimer;
d _startTime;
@"NSObject<OS_dispatch_source>" _timeoutTimer;
@"NSObject<OS_os_transaction>" _transaction;
^{LogCategory=ii*I**i^{LogCategory}^{LogOutput}^{LogOutput}QQII*^{LogCategoryPrivate}} _ucat;
@"WPClient" _wpClient;
B _aggregate;
B _connectOnly;
B _disconnectOnly;
B _guestMode;
B _guestPermanent;
B _softwareVolume;
B _userNotInContacts;
I _deviceVersion;
@? _completionHandler;
@"NSString" _deviceAddress;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@"NSString" _guestAddress;
@"NSData" _guestKey;
@"NSString" _name;
```

## Properties

```
@property (TB,N,V_aggregate) aggregate;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (TB,N,V_connectOnly) connectOnly;
@property (T@"NSString",C,N,V_deviceAddress) deviceAddress;
@property (TI,R,N,V_deviceVersion) deviceVersion;
@property (TB,N,V_disconnectOnly) disconnectOnly;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@"NSString",C,N,V_guestAddress) guestAddress;
@property (T@"NSData",C,N,V_guestKey) guestKey;
@property (TB,N,V_guestMode) guestMode;
@property (TB,N,V_guestPermanent) guestPermanent;
@property (T@"NSString",R,C,N,V_name) name;
@property (TB,R,N,V_softwareVolume) softwareVolume;
@property (TB,N,V_userNotInContacts) userNotInContacts;
```

## Instance methods

```
-[BTBluetoothPairingSession dispatchQueue];
-[BTBluetoothPairingSession _activate];
-[BTBluetoothPairingSession setCompletionHandler:];
-[BTBluetoothPairingSession completionHandler];
-[BTBluetoothPairingSession init];
-[BTBluetoothPairingSession _invalidate];
-[BTBluetoothPairingSession dealloc];
-[BTBluetoothPairingSession setDispatchQueue:];
-[BTBluetoothPairingSession invalidate];
-[BTBluetoothPairingSession _btEnsureStarted];
-[BTBluetoothPairingSession deviceVersion];
-[BTBluetoothPairingSession activate];
-[BTBluetoothPairingSession _btEnsureStopped];
-[BTBluetoothPairingSession name];
-[BTBluetoothPairingSession _completed:];
-[BTBluetoothPairingSession aggregate];
-[BTBluetoothPairingSession deviceAddress];
-[BTBluetoothPairingSession setAggregate:];
-[BTBluetoothPairingSession setDeviceAddress:];
-[BTBluetoothPairingSession setGuestMode:];
-[BTBluetoothPairingSession setConnectOnly:];
-[BTBluetoothPairingSession _btDeletePairingAndRetry];
-[BTBluetoothPairingSession connectOnly];
-[BTBluetoothPairingSession disconnectOnly];
-[BTBluetoothPairingSession guestAddress];
-[BTBluetoothPairingSession guestKey];
-[BTBluetoothPairingSession guestMode];
-[BTBluetoothPairingSession setDisconnectOnly:];
-[BTBluetoothPairingSession setGuestAddress:];
-[BTBluetoothPairingSession setGuestKey:];
-[BTBluetoothPairingSession setUserNotInContacts:];
-[BTBluetoothPairingSession softwareVolume];
-[BTBluetoothPairingSession userNotInContacts];
-[BTBluetoothPairingSession guestPermanent];
-[BTBluetoothPairingSession setGuestPermanent:];
```
