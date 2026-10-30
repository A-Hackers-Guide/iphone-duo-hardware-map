# `HIDSession`

- Image: [`/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`](../userland/System__Library__Frameworks__IOKit.framework__Versions__A__IOKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
{?="client"^{__IOHIDEventSystem}"callback"^?"refCon"^v"queueContext"^{__IOHIDSessionQueueContext}"stateCondition"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}"state"i"stateBusy"i"eventDispatchQueueSession"@"NSObject<OS_dispatch_queue>""eventDispatchSource"@"NSObject<OS_dispatch_source>""eventDipsatchPending"^{__CFArray}"properties"^{__CFDictionary}"logLevel"I"serviceSet"^{__CFSet}"simpleSessionFilters"^{__CFArray}"sessionFilters"^{__CFArray}"pendingSessionFilters"^{__CFArray}"activityLastTimestamp"Q"activityLastTime"{timeval="tv_sec"q"tv_usec"i}"activityNotificationSet"^{__CFSet}} _session;
```

## Instance methods

```
-[HIDSession dealloc];
-[HIDSession _cfTypeID];
```
