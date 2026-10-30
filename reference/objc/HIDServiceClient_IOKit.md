# `HIDServiceClient`

- Image: [`/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`](../userland/System__Library__Frameworks__IOKit.framework__Versions__A__IOKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
{?="system"^{__IOHIDEventSystemClient}"serviceID"^v"callbackLock"{os_unfair_recursive_lock_s="ourl_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"ourl_count"I}"removal"{?="callback"^?"block"@?"target"^v"refcon"^v}"virtualService"{?="callbacks"^{__IOHIDVirtualServiceClientCallbacksV2}"target"^v"refcon"^v}"serviceLock"{os_unfair_recursive_lock_s="ourl_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"ourl_count"I}"cachedProperties"^{__CFDictionary}"fastPathInterface"^^{IOHIDServiceFastPathInterface}"plugInInterface"^^{IOCFPlugInInterfaceStruct}"removalHandler"^v"primaryUsagePage"I"primaryUsage"I"usagePairs"^{_IOHIDServiceClientUsagePair}"usagePairsCount"I} _client;
```

## Instance methods

```
-[HIDServiceClient dealloc];
-[HIDServiceClient _cfTypeID];
-[HIDServiceClient description];
```
