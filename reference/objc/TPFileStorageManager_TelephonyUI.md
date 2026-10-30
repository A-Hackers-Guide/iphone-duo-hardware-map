# `TPFileStorageManager`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _hasClearedLegacyStorage;
@"NSURL" _urlForFileSystem;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (TB,N,V_hasClearedLegacyStorage) hasClearedLegacyStorage;
@property (T@"NSURL",R,N,V_urlForFileSystem) urlForFileSystem;
```

## Class methods

```
+[TPFileStorageManager sharedInstance];
```

## Instance methods

```
-[TPFileStorageManager localeChanged];
-[TPFileStorageManager init];
-[TPFileStorageManager dealloc];
-[TPFileStorageManager queue];
-[TPFileStorageManager setQueue:];
-[TPFileStorageManager imageWithName:];
-[TPFileStorageManager clearCacheWithCompletion:];
-[TPFileStorageManager clearLegacyStorageIfNecessary];
-[TPFileStorageManager deleteStorageAtURLs:];
-[TPFileStorageManager hasClearedLegacyStorage];
-[TPFileStorageManager saveImage:withName:];
-[TPFileStorageManager setHasClearedLegacyStorage:];
-[TPFileStorageManager urlForFileSystem];
-[TPFileStorageManager urlsForLegacyFileSystem];
```
