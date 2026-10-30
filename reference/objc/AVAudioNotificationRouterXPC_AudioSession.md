# `AVAudioNotificationRouterXPC`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVAudioNotificationCenterServer`
- 1 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
{synchronized<NotificationDelegateCollectionXPC, caulk::mach::unfair_lock, caulk::empty_atomic_interface<NotificationDelegateCollectionXPC>>="mMutex"{unfair_lock="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}}"mObject"{NotificationDelegateCollectionXPC="mDelegates"{unordered_map<unsigned long long, NotificationDelegateCollectionXPC::NotificationDelegates, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, NotificationDelegateCollectionXPC::NotificationDelegates>>>="__table_"{__hash_table<std::__hash_value_type<unsigned long long, NotificationDelegateCollectionXPC::NotificationDelegates>, std::__unordered_map_hasher<unsigned long long, std::pair<const unsigned long long, NotificationDelegateCollectionXPC::NotificationDelegates>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::pair<const unsigned long long, NotificationDelegateCollectionXPC::NotificationDelegates>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::pair<const unsigned long long, NotificationDelegateCollectionXPC::NotificationDelegates>>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, NotificationDelegateCollectionXPC::NotificationDelegates>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, NotificationDelegateCollectionXPC::NotificationDelegates>, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, NotificationDelegateCollectionXPC::NotificationDelegates>, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, NotificationDelegateCollectionXPC::NotificationDelegates>, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}}"mIsAudioServiceTerminated"B}} _delegates;
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
+[AVAudioNotificationRouterXPC sharedInstance];
```

## Instance methods

```
-[AVAudioNotificationRouterXPC init];
-[AVAudioNotificationRouterXPC handleNotification:payload:];
-[AVAudioNotificationRouterXPC addNotificationDelegate:error:];
-[AVAudioNotificationRouterXPC createRemoteNotificationCenter];
-[AVAudioNotificationRouterXPC destroyRemoteNotificationCenter:];
-[AVAudioNotificationRouterXPC handleAudiomxdReset];
-[AVAudioNotificationRouterXPC handleAudiomxdTermination];
-[AVAudioNotificationRouterXPC isAudioServiceTerminated];
-[AVAudioNotificationRouterXPC removeNotificationDelegate:];
-[AVAudioNotificationRouterXPC setAudioServiceTerminated:];
-[AVAudioNotificationRouterXPC startObservingNotifications:forDelegate:];
-[AVAudioNotificationRouterXPC stopObservingNotifications:forDelegate:];
```
