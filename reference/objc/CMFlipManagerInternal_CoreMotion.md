# `CMFlipManagerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@? fEventHandler;
@"NSOperationQueue" fEventQueue;
q fFlipState;
q fFlipReason;
d fContinuousTimestamp;
d fTimestamp;
B fNotifyAllClients;
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} fFlipDispatcher;
B fRegisteredForDistributedNotifications;
{unique_ptr<CLConnectionClient, std::default_delete<CLConnectionClient>>=""{?="__ptr_"^{CLConnectionClient}}} fConnection;
@"NSObject<OS_dispatch_queue>" fConnectionQueue;
@"NSString" fClientID;
B fUpdatesRequested;
```

## Instance methods

```
-[CMFlipManagerInternal init];
-[CMFlipManagerInternal dealloc];
```
