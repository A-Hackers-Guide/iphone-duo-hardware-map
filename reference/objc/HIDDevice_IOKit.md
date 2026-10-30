# `HIDDevice`

- Image: [`/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`](../userland/System__Library__Frameworks__IOKit.framework__Versions__A__IOKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
{?="service"I"regID"Q"deviceInterface"^^{IOHIDDeviceDeviceInterface}"deviceTimeStampedInterface"^^{IOHIDDeviceTimeStampedDeviceInterface}"plugInInterface"^^{IOCFPlugInInterfaceStruct}"deviceLock"{os_unfair_recursive_lock_s="ourl_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"ourl_count"I}"properties"^{__CFDictionary}"elements"^{__CFSet}"rootKey"^{__CFString}"UUIDKey"^{__CFString}"notificationPort"^{IONotificationPort}"notification"I"asyncEventSource"^{__CFRunLoopSource}"sourceContext"{?="version"q"info"^v"retain"^?"release"^?"copyDescription"^?"equal"^?"hash"^?"getPort"^?"perform"^?}"queuePort"^{__CFMachPort}"runLoop"^{__CFRunLoop}"runLoopMode"^{__CFString}"dispatchQueue"@"NSObject<OS_dispatch_queue>""dispatchMach"@"NSObject<OS_dispatch_mach>""dispatchStateMask"AI"cancelHandler"@?"queue"^{__IOHIDQueue}"inputMatchingMultiple"^{__CFArray}"loadProperties"C"isDirty"C"transaction"^v"callbackLock"{os_unfair_recursive_lock_s="ourl_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"ourl_count"I}"reportBuffer"^{__CFData}"batchElements"^{__CFArray}"removalCallbackSet"^{__CFSet}"inputReportCallbackSet"^{__CFSet}"inputValueCallbackSet"^{__CFSet}"asyncCommitCallbacks"^{__CFDictionary}"asyncElementCallbacks"^{__CFDictionary}"asyncReportCallbacks"^{__CFDictionary}"elementHandler"A^v"removalHandler"A^v"inputReportHandler"A^v"propertyNotificationHandler"A^v"propertyNotificationKeys"^{__CFArray}"previousPropertyValues"^{__CFDictionary}"propertyPort"^{IONotificationPort}"propertyNotify"I} _device;
```

## Instance methods

```
-[HIDDevice dealloc];
-[HIDDevice _cfTypeID];
-[HIDDevice description];
```
