# `WiFiP2PUIAgent`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UNUserNotificationCenterDelegate`
- 3 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"WiFiP2PXPCConnection" _xpcConnection;
@"UNUserNotificationCenter" _notificationCenter;
@"NSObject<OS_os_log>" _logger;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WiFiP2PUIAgent userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:];
-[WiFiP2PUIAgent startConnectionUsingProxy:completionHandler:];
-[WiFiP2PUIAgent init];
-[WiFiP2PUIAgent exportedInterface];
-[WiFiP2PUIAgent invalidate];
-[WiFiP2PUIAgent exportedObject];
-[WiFiP2PUIAgent activate];
-[WiFiP2PUIAgent removeNotificationsWithIdentifiers:];
-[WiFiP2PUIAgent addNotificationRequest:completionHandler:];
-[WiFiP2PUIAgent configureNotificationsWithBundleIdentifier:];
-[WiFiP2PUIAgent showAccessoryNotificationWithUUID:deviceName:localization:completionHandler:];
-[WiFiP2PUIAgent showInfrastructureDisconnectOnRetroModeNotificationForService:localization:phoneDisconnected:uuid:completionHandler:];
```
