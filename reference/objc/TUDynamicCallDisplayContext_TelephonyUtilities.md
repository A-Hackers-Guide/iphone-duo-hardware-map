# `TUDynamicCallDisplayContext`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TUMutableCallDisplayContext`
- 4 instance variables, 4 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"<TUDynamicCallDisplayContextDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _serialQueue;
@"TUFeatureFlags" _featureFlags;
@"CXCallDirectoryManager" _callDirectoryManager;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_serialQueue) serialQueue;
@property (T@"TUFeatureFlags",R,N,V_featureFlags) featureFlags;
@property (T@"CXCallDirectoryManager",&,N,V_callDirectoryManager) callDirectoryManager;
@property (T@"<TUDynamicCallDisplayContextDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[TUDynamicCallDisplayContext serialQueue];
-[TUDynamicCallDisplayContext init];
-[TUDynamicCallDisplayContext setSerialQueue:];
-[TUDynamicCallDisplayContext _initializeSynchronousStateWithCall:contactIdentifier:contactsDataProvider:];
-[TUDynamicCallDisplayContext callDirectoryManager];
-[TUDynamicCallDisplayContext initWithCall:contactIdentifier:serialQueue:cacheOnly:];
-[TUDynamicCallDisplayContext updatePredictedNameFromReceptionist:];
-[TUDynamicCallDisplayContext initWithCall:contactIdentifier:serialQueue:contactsDataSource:cacheOnly:];
-[TUDynamicCallDisplayContext initWithDisplayContext:call:serialQueue:cacheOnly:];
-[TUDynamicCallDisplayContext setDelegate:];
-[TUDynamicCallDisplayContext delegate];
-[TUDynamicCallDisplayContext initWithCoder:];
-[TUDynamicCallDisplayContext _initializeAsynchronousStateWithCall:cacheOnly:];
-[TUDynamicCallDisplayContext initWithCall:contactIdentifier:serialQueue:];
-[TUDynamicCallDisplayContext initWithCall:contactIdentifier:serialQueue:contactsDataSource:];
-[TUDynamicCallDisplayContext initWithDisplayContext:call:serialQueue:];
-[TUDynamicCallDisplayContext setCallDirectoryManager:];
-[TUDynamicCallDisplayContext updateDisplayContextWithBusinessConnectInfoUsingCall:];
-[TUDynamicCallDisplayContext featureFlags];
```
