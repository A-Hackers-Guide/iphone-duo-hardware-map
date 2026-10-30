# `SBBulletinSpokenObserverGateway`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BBObserverDelegate`, `AFSiriAnnouncementRequestCapabilityObserving`
- 5 instance variables, 4 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"BBObserver" _bbObserver;
@"DNDEventBehaviorResolutionService" _dndEventBehaviorResolutionService;
@"AFSiriAnnouncementRequestCapabilityManager" _announcementRequestCapabilityManager;
B _canAnnounceNotifications;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBBulletinSpokenObserverGateway sharedInstance];
```

## Instance methods

```
-[SBBulletinSpokenObserverGateway init];
-[SBBulletinSpokenObserverGateway observer:addBulletin:forFeed:playLightsAndSirens:withReply:];
-[SBBulletinSpokenObserverGateway eligibleAnnouncementRequestTypesChanged:onPlatform:];
-[SBBulletinSpokenObserverGateway availableAnnouncementRequestTypesChanged:onPlatform:];
```
