# `DSDeviceManager`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"<DSDeviceListDelegate>" _delegate;
@"NSArray" _remoteDevices;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"AKAppleIDAuthenticationController" _authController;
@"AIDAAccountManager" _accountManager;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_workQueue) workQueue;
@property (T@"AKAppleIDAuthenticationController",&,N,V_authController) authController;
@property (T@"AIDAAccountManager",&,N,V_accountManager) accountManager;
@property (T@"<DSDeviceListDelegate>",W,N,V_delegate) delegate;
@property (T@"NSArray",R,N,V_remoteDevices) remoteDevices;
```

## Class methods

```
+[DSDeviceManager sharedInstance];
```

## Instance methods

```
-[DSDeviceManager accountManager];
-[DSDeviceManager setWorkQueue:];
-[DSDeviceManager init];
-[DSDeviceManager setAccountManager:];
-[DSDeviceManager workQueue];
-[DSDeviceManager refresh];
-[DSDeviceManager remoteDevices];
-[DSDeviceManager setDelegate:];
-[DSDeviceManager delegate];
-[DSDeviceManager authController];
-[DSDeviceManager setAuthController:];
-[DSDeviceManager _setRemoteDeviceList:];
-[DSDeviceManager appDidLaunch];
-[DSDeviceManager refreshRemoteDeviceList];
```
