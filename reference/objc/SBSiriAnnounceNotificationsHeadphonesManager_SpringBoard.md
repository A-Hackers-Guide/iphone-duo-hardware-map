# `SBSiriAnnounceNotificationsHeadphonesManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AFSiriAnnouncementRequestCapabilityObserving`
- 2 instance variables, 5 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"AFSiriAnnouncementRequestCapabilityManager" _capabilityManager;
B _headphonesNotificationAnnouncementsAvailable;
```

## Properties

```
@property (TB,V_headphonesNotificationAnnouncementsAvailable) headphonesNotificationAnnouncementsAvailable;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSiriAnnounceNotificationsHeadphonesManager sharedInstance];
```

## Instance methods

```
-[SBSiriAnnounceNotificationsHeadphonesManager init];
-[SBSiriAnnounceNotificationsHeadphonesManager dealloc];
-[SBSiriAnnounceNotificationsHeadphonesManager eligibleAnnouncementRequestTypesChanged:onPlatform:];
-[SBSiriAnnounceNotificationsHeadphonesManager availableAnnouncementRequestTypesChanged:onPlatform:];
-[SBSiriAnnounceNotificationsHeadphonesManager canAnnounce];
-[SBSiriAnnounceNotificationsHeadphonesManager headphonesNotificationAnnouncementsAvailable];
-[SBSiriAnnounceNotificationsHeadphonesManager setHeadphonesNotificationAnnouncementsAvailable:];
```
