# `AVAudioNotificationRouter`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/libSessionUtility.dylib`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__libSessionUtility.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVAudioNotificationCenterServer`, `SASSpatialBehaviorUnitDelegate`
- 5 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
{ObjectRef<opaqueCMNotificationCenter *>="mCFObject"^{opaqueCMNotificationCenter}} _notificationCenter;
^{ISessionCollectionProvider=^^?} _sessionCollectionProvider;
{synchronized<avas::NotificationDelegateCollection, caulk::mach::unfair_lock, caulk::empty_atomic_interface<avas::NotificationDelegateCollection>>="mMutex"{unfair_lock="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}}"mObject"{NotificationDelegateCollection="_delegates"{unordered_map<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>>>="__table_"{__hash_table<std::__hash_value_type<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>, std::__unordered_map_hasher<unsigned long long, std::pair<const unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::pair<const unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::pair<const unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, avas::NotificationDelegateCollection::NotificationDelegates>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}}"_currentDelegateID"Q}} _delegates;
@"NSSet" _propertyNotificationsOfInterest;
^? _sessionNotificationHandler;
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
-[AVAudioNotificationRouter handleInterruptionForPid:audioSessionID:mxSessionID:interruptionState:interruptionInfo:];
-[AVAudioNotificationRouter handleInterruptionForPid:audioSessionID:interruptionState:interruptionInfo:];
-[AVAudioNotificationRouter addNotificationDelegate:error:];
-[AVAudioNotificationRouter removeNotificationDelegate:];
-[AVAudioNotificationRouter updateDelegate:notificationFilter:error:];
-[AVAudioNotificationRouter handleCMNotification:object:payload:];
-[AVAudioNotificationRouter initWithNotificationCenter:sessionCollectionProvider:sessionNotificationHandler:];
-[AVAudioNotificationRouter internal_UpdateNotificationCenterSubscriptions:];
-[AVAudioNotificationRouter internal_findSessionsBelongingToAudioSessionID:outMatches:];
-[AVAudioNotificationRouter internal_findSessionsMatchingAudioSessionID:outMatches:];
-[AVAudioNotificationRouter internal_findSessionsMatchingMXSessionID:outMatches:];
-[AVAudioNotificationRouter internal_findSessionsMatchingObject:outMatches:];
-[AVAudioNotificationRouter internal_publishInterruptions:];
-[AVAudioNotificationRouter internal_publishPropertyNotifications:];
-[AVAudioNotificationRouter spatialBehaviorUnit:updatedDerivedProperties:];
```
