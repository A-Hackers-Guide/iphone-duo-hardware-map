# `_TtC22AccessoryNotifications33NotificationsForwardingConnection`

- Image: [`/System/Library/Frameworks/AccessoryNotifications.framework/AccessoryNotifications`](../userland/System__Library__Frameworks__AccessoryNotifications.framework__AccessoryNotifications.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_TtP22AccessoryNotifications38NotificationsForwardingHostXPCProtocol_`
- 8 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
_$sSo21_EXCapabilityEndpointCSg capabilityEndpoint;
_$sSo8DADeviceC device;
_$sSo18DAExtensionSessionC extensionSession;
AccessoryNotifications.AccessoryNotification function type (escaping) storeActiveNotification;
AccessoryNotifications.AccessoryNotification.Identifier function type (escaping) removeActiveNotification;
AccessoryNotifications.AccessoryNotification ? AccessoryNotifications.AccessoryNotification.Identifier function type (escaping) lookupActiveNotification;
_$sSo15NSXPCConnectionCSg xpcConnection;
AccessoryNotifications.NotificationsForwardingConnectionDelegate ? delegate;
```

## Instance methods

```
-[_TtC22AccessoryNotifications33NotificationsForwardingConnection init];
-[_TtC22AccessoryNotifications33NotificationsForwardingConnection dealloc];
-[_TtC22AccessoryNotifications33NotificationsForwardingConnection notificationResponse:completion:];
-[_TtC22AccessoryNotifications33NotificationsForwardingConnection removeNotificationsWithIdentifiersAdapter:completion:];
-[_TtC22AccessoryNotifications33NotificationsForwardingConnection requestFileWithSourceIdentifier:notificationIdentifier:fileIdentifierAdapter:completion:];
```
