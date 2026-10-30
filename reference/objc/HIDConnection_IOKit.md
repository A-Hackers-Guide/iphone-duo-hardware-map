# `HIDConnection`

- Image: [`/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`](../userland/System__Library__Frameworks__IOKit.framework__Versions__A__IOKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
{?="system"^{__IOHIDEventSystem}"notifications"^{__CFDictionary}"queue"^{__IOHIDEventQueue}"port"^{__IOMIGMachPort}"reply_port"I"demuxCallback"^?"demuxRefcon"^v"terminationCallback"^?"terminationRefcon"^v"services"^{__CFSet}"pid"i"dispatchQueue"@"NSObject<OS_dispatch_queue>""sendPossiblePort"I"sendPossibleSource"@"NSObject<OS_dispatch_source>""replySendPossibleSource"@"NSObject<OS_dispatch_source>""sendPossible"i"propertySet"^{__CFSet}"caller"^{__CFString}"procName"^{__CFString}"uuid"^{__CFString}"uuidStr"*"type"i"attributes"^{__CFDictionary}"task_name_port"I"audit_token"{?="val"[8I]}"lock"{os_unfair_recursive_lock_s="ourl_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"ourl_count"I}"entitlements"^(IOHIDEventSystemConnectionEntitlements)"connectionEntitlements"@"NSObject<OS_xpc_object>""disableProtectedServices"i"filterPriority"i"state"I"notificationsLock"{os_unfair_recursive_lock_s="ourl_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"ourl_count"I}"virtualServices"^{__CFDictionary}"eventFilterMask"Q"eventFilteredCount"I"eventFilterTimeoutCount"I"droppedEventCount"I"currentDroppedEventCount"I"droppedEventTypeMask"Q"eventCount"I"eventMask"Q"lastDroppedEventTime"{timeval="tv_sec"q"tv_usec"i}"firstDroppedEventTime"{timeval="tv_sec"q"tv_usec"i}"maxEventLatency"Q"droppedEventStatus"i"propertyChangeNotificationHandlingTime"Q"eventLog"^{__CFData}"eventTypeCnt"^I"activityState"I"activityStateChangeCount"I"idleNotificationTime"Q"activityDispatchSource"@"NSObject<OS_dispatch_source>""activityNotification"^{__IOHIDNotification}"activityLog"^{__CFData}"filter"^{__IOHIDConnectionFilter}"serverDied"i} _connection;
```

## Instance methods

```
-[HIDConnection dealloc];
-[HIDConnection _cfTypeID];
-[HIDConnection description];
```
