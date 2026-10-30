# `CMDeviceStateManagerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@? fEventHandler;
@"NSOperationQueue" fEventQueue;
q fPropertyA;
q fPropertyA0;
q fPropertyA1;
q fPropertyB;
q fPropertyC;
q fPropertyD;
d fContinuousTimestamp;
d fAPArrivalTimestampSecs;
d fTimestamp;
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} fDeviceStateEventDispatcher;
B fRegisteredForNotifications;
@"NSString" fClientID;
```

## Instance methods

```
-[CMDeviceStateManagerInternal init];
-[CMDeviceStateManagerInternal dealloc];
-[CMDeviceStateManagerInternal feedDeviceStateEvent:propertyA0Type:propertyA1Type:propertyBType:propertyCType:propertyDType:timestamp:continuousTimestamp:timestampAPArrivalSecs:];
-[CMDeviceStateManagerInternal sendEventToClientPrivate];
```
