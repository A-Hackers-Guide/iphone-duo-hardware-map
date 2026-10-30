# `WiFiPasswordSharingSimulator`

- Image: [`/System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi`](../userland/System__Library__PrivateFrameworks__MobileWiFi.framework__MobileWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SFPasswordSharingServiceDelegate`
- 3 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"SFPasswordSharingService" _service;
@? _replyHandler;
```

## Instance methods

```
-[WiFiPasswordSharingSimulator init];
-[WiFiPasswordSharingSimulator dealloc];
-[WiFiPasswordSharingSimulator service:receivedNetworkInfo:];
-[WiFiPasswordSharingSimulator service:shouldPromptForNetwork:];
-[WiFiPasswordSharingSimulator runWithSSID:reply:];
```
