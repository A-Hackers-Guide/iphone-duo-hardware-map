# `MobileAccessoryUpdater`

- Image: [`/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/MobileAccessoryUpdater`](../userland/System__Library__PrivateFrameworks__MobileAccessoryUpdater.framework__MobileAccessoryUpdater.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 0 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"<MobileAccessoryUpdaterDelegate>" _delegate;
@"<FudConnection>" _connection;
@"NSString" _bundleIdentifier;
@"NSString" _clientIdentifier;
* _cClientIdentifier;
@"NSObject<OS_dispatch_queue>" _sessionQueue;
@"NSObject<OS_dispatch_queue>" _callbackQueue;
@"NSObject<OS_dispatch_queue_attr>" _attr;
@"NSString" _activeFilter;
B _isInternalClient;
B _didUnregister;
```

## Instance methods

```
-[MobileAccessoryUpdater createConnection];
-[MobileAccessoryUpdater clientIdentifier];
-[MobileAccessoryUpdater dealloc];
-[MobileAccessoryUpdater bundleIdentifier];
-[MobileAccessoryUpdater unregister];
-[MobileAccessoryUpdater activeFilter];
-[MobileAccessoryUpdater doneWithOptions:];
-[MobileAccessoryUpdater getActiveDeviceClass];
-[MobileAccessoryUpdater getActiveDeviceClassCString];
-[MobileAccessoryUpdater getPluginsList];
-[MobileAccessoryUpdater initWithDelegate:isInternalClient:options:error:];
-[MobileAccessoryUpdater initWithGroupIdentifer:delegate:options:error:];
-[MobileAccessoryUpdater initWithPluginIdentifier:delegate:options:error:];
-[MobileAccessoryUpdater initWithPluginIdentifier:isGroupIdentifier:delegate:isInternalClient:options:error:];
-[MobileAccessoryUpdater loadPluginWithAccessoryInfo:options:];
-[MobileAccessoryUpdater performNextStepWithOptions:];
-[MobileAccessoryUpdater performStep:withOptions:];
-[MobileAccessoryUpdater queryNextStep:];
-[MobileAccessoryUpdater registerForIdentifier:isGroupIdentifier:];
-[MobileAccessoryUpdater sendMessageForCommand:withOptions:replyHandler:];
-[MobileAccessoryUpdater setActiveDeviceClass:];
-[MobileAccessoryUpdater setLastRemoteFindDate:];
```
