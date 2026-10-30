# `IOKPowerNotifier`

- Image: [`/System/Library/PrivateFrameworks/IOKitten.framework/IOKitten`](../userland/System__Library__PrivateFrameworks__IOKitten.framework__IOKitten.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 9 instance methods, 0 class methods

## Instance variables

```
^{IONotificationPort=} _notificationPort;
I _connection;
I _notifier;
@"<IOKPowerNotifierDelegate>" _delegate;
```

## Properties

```
@property (T@"<IOKPowerNotifierDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[IOKPowerNotifier dealloc];
-[IOKPowerNotifier setDelegate:];
-[IOKPowerNotifier delegate];
-[IOKPowerNotifier systemWillSleep];
-[IOKPowerNotifier systemHasPoweredOn];
-[IOKPowerNotifier initWithDispatchQueue:];
-[IOKPowerNotifier _handlePowerNotificationWithMessageType:andArgument:];
-[IOKPowerNotifier systemWillNotSleep];
-[IOKPowerNotifier systemWillPowerOn];
```
