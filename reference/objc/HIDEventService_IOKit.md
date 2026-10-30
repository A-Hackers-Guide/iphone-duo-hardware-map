# `HIDEventService`

- Image: [`/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`](../userland/System__Library__Frameworks__IOKit.framework__Versions__A__IOKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
{?="session"^{__IOHIDSession}"service"I"serviceInterface"^^{IOHIDServiceInterface}"serviceInterface2"^^{IOHIDServiceInterface2}"plugInInterface"^^{IOCFPlugInInterfaceStruct}"registryID"^{__CFNumber}"locationID"^v"entitlements"^{__CFArray}"queueContext"^{__IOHIDServiceQueueContext}"dispatchQueue"@"NSObject<OS_dispatch_queue>""notificationPort"^{IONotificationPort}"notification"I"removalNotificationSet"^{__CFSet}"propertyNotificationSet"^{__CFSet}"requestTerminationNotificationSet"^{__CFSet}"eventTarget"^v"eventRefcon"^v"eventCallback"^?"lastLEDMask"I"lastButtonMask"I"currentReportInterval"I"currentBatchInterval"I"defaultReportInterval"I"defaultBatchInterval"I"primaryUsagePage"I"primaryUsage"I"transport"[32c]"queueSize"I"containsReportInterval"i"state"I"eventCount"I"eventMask"Q"clientCacheDict"^{__CFDictionary}"simpleFilters"^{__CFArray}"filters"^{__CFArray}"keyboardEventInProgress"^{__CFSet}"nullEventMask"Q"displayIntegratedDigitizer"i"builtIn"i"inMomentumPhase"i"inDigitizerPhase"i"sensorControlOptions"C"registered"i"protectedAccess"i"tccService"^{__CFString}"propertyCache"^{__CFDictionary}"propertyCacheHit"I"propertyCacheMiss"I"activityLastTimestamp"Q"virtualService"{?="connection"^v"target"^v"refcon"^v"callbacks"^{IOHIDServiceVirtualCallbacksV2}}"connections"^^v"propertySetTime"Q"propertyGetTime"Q"elementSetTime"Q"regID"Q"eventLog"^{__CFData}"eventTypeCnt"^Q"pluginCancelHandler"@?"filterCancelHandler"@?"pendingPluginCancel"B"pendingFilterCancels"I"cancelTimer"@"NSObject<OS_dispatch_source>""dataLock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"hidAnalyticsEvent"^v"hidAnalyticsDispatchEvent"^v"propertiesRequiredForMatching"^{__CFArray}"objc"{?="interface"^v"name"^{__CFString}"getProperty":"setProperty":"eventMatching":"setEventDispatcher":"setCancelHandler":"activate":"cancel":"setDispatchQueue":"clientNotification":"copyEvent":"setOutputEvent":"setHIDEventService":}"virtualDelegate"@} _service;
```

## Instance methods

```
-[HIDEventService dealloc];
-[HIDEventService _cfTypeID];
-[HIDEventService description];
```
