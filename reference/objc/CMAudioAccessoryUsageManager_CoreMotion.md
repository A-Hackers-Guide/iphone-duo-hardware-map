# `CMAudioAccessoryUsageManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 9 instance methods, 2 class methods

## Instance variables

```
{unique_ptr<CLConnectionClient, std::default_delete<CLConnectionClient>>=""{?="__ptr_"^{CLConnectionClient}}} _locationConnection;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@"<CMAudioAccessoryUsageDelegate>" _delegate;
q _authorizationStatus;
```

## Properties

```
@property (T@"<CMAudioAccessoryUsageDelegate>",W,N,V_delegate) delegate;
@property (Tq,R,N,GisAuthorized,V_authorizationStatus) authorizationStatus;
```

## Class methods

```
+[CMAudioAccessoryUsageManager isAvailable];
+[CMAudioAccessoryUsageManager isAuthorized];
```

## Instance methods

```
-[CMAudioAccessoryUsageManager _connect];
-[CMAudioAccessoryUsageManager _disconnect];
-[CMAudioAccessoryUsageManager init];
-[CMAudioAccessoryUsageManager dealloc];
-[CMAudioAccessoryUsageManager setDelegate:];
-[CMAudioAccessoryUsageManager _handleMessage:];
-[CMAudioAccessoryUsageManager delegate];
-[CMAudioAccessoryUsageManager isAuthorized];
-[CMAudioAccessoryUsageManager requestAudioAccessoryUsageUpdatesWithHandler:];
```
