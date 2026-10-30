# `AVContentKeySessionInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 25 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
@"AVWeakReferencingDelegateStorage" _delegateStorage;
@"AVWeakReference" _weakReference;
@"NSURL" _storageURL;
@"NSData" _appIdentifier;
B _isExpired;
B _internal;
B _supportsAdvisoryKeys;
@"AVContentKeyReportGroup" _defaultContentKeyGroup;
@"NSObject<OS_dispatch_queue>" _threadSafetyQ;
@"NSHashTable" _contentKeyRecipients;
@"NSString" _keySystem;
@"NSMutableDictionary" keyRequestsByRequestID;
@"NSMutableArray" _contentKeyGroups;
@"NSMapTable" cryptorUUIDToContentKeyRequestMap;
@"NSMutableDictionary" keyRequestParamsByRequestID;
@"NSMutableDictionary" keyRequestTrackerByRequestID;
@"NSMutableDictionary" cryptorsByIdentifier;
@"NSMapTable" contentKeyRequestByKeySpecifierMap;
@"NSMapTable" contentKeyByKeySpecifierMap;
@"NSData" _protectorSessionIdentifier;
@"NSMapTable" recipientsByRecipientID;
@"NSObject<OS_dispatch_queue>" _delegateReadWriteQueue;
@"NSObject<OS_dispatch_queue>" _delegateQueue;
^{OpaqueFigContentKeyBoss=} _contentKeyBoss;
B _useContentKeyBoss;
```
