# `CLFindMyAccessoryRangingManager`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"<CLFindMyAccessoryRangingManagerDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _delegateQueue;
{unique_ptr<CLConnectionClient, std::default_delete<CLConnectionClient>>=""{?="__ptr_"^{CLConnectionClient}}} _connection;
```

## Properties

```
@property (T@"<CLFindMyAccessoryRangingManagerDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[CLFindMyAccessoryRangingManager handleMessage:];
-[CLFindMyAccessoryRangingManager init];
-[CLFindMyAccessoryRangingManager handleInterruption];
-[CLFindMyAccessoryRangingManager setDelegate:];
-[CLFindMyAccessoryRangingManager delegate];
-[CLFindMyAccessoryRangingManager initWithDelegate:delegateQueue:];
-[CLFindMyAccessoryRangingManager prepareForStartRangingOnDevice:];
-[CLFindMyAccessoryRangingManager fetchFirmwareVersionFromDevice:];
-[CLFindMyAccessoryRangingManager connectToDevice:];
-[CLFindMyAccessoryRangingManager disconnectFromDevice:];
-[CLFindMyAccessoryRangingManager initRoseWithParameters:onDevice:];
-[CLFindMyAccessoryRangingManager setRoseRangingParameters:onDevice:];
-[CLFindMyAccessoryRangingManager startEventCounterOnDevice:];
-[CLFindMyAccessoryRangingManager startRangingWithParameters:onDevice:];
-[CLFindMyAccessoryRangingManager stopEventCounterOnDevice:];
-[CLFindMyAccessoryRangingManager stopRangingOnDevice:];
-[CLFindMyAccessoryRangingManager stopRoseWithParameters:onDevice:];
```
