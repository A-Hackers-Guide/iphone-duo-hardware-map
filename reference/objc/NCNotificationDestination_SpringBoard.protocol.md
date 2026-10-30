# `NCNotificationDestination` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 12 instance methods, 0 class methods

## Properties

```
@property (T@"<NCNotificationDestinationDelegate>",W,N) delegate;
@property (T@"NSString",R,N) identifier;
@property (T@"BSServiceConnectionEndpoint",R,N) endpoint;
```

## Instance methods

```
-[NCNotificationDestination identifier];
-[NCNotificationDestination endpoint];
-[NCNotificationDestination withdrawNotificationRequest:];
-[NCNotificationDestination postNotificationRequest:];
-[NCNotificationDestination setDelegate:];
-[NCNotificationDestination modifyNotificationRequest:];
-[NCNotificationDestination canReceiveNotificationRequest:];
-[NCNotificationDestination delegate];
-[NCNotificationDestination interceptsQueueRequest:];
-[NCNotificationDestination updateNotificationSystemSettings:previousSystemSettings:];
-[NCNotificationDestination updateNotificationSectionSettings:previousSectionSettings:];
-[NCNotificationDestination notificationsLoadedForSectionIdentifier:];
```
