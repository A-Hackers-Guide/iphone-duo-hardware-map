# `CAMSmartStyleSettingsResourceLoadingManager`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMSmartStyleSettingsResourceLoaderDelegate`
- 7 instance variables, 11 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"<CAMSmartStyleSettingsResourceLoadingManagerDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" __loadingQueue;
@"NSMutableDictionary" __allResourceLoaders;
@"NSMutableArray" __pendingResourceLoaders;
@"CAMSmartStyleSettingsResourceLoader" __activeResourceLoader;
d __activeLoadStartTime;
@"NSMutableDictionary" __logIdentifiers;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__loadingQueue) _loadingQueue;
@property (T@"NSMutableDictionary",R,N,V__allResourceLoaders) _allResourceLoaders;
@property (T@"NSMutableArray",R,N,V__pendingResourceLoaders) _pendingResourceLoaders;
@property (T@"CAMSmartStyleSettingsResourceLoader",&,N,V__activeResourceLoader) _activeResourceLoader;
@property (Td,N,V__activeLoadStartTime) _activeLoadStartTime;
@property (T@"NSMutableDictionary",R,N,V__logIdentifiers) _logIdentifiers;
@property (T@"<CAMSmartStyleSettingsResourceLoadingManagerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMSmartStyleSettingsResourceLoadingManager init];
-[CAMSmartStyleSettingsResourceLoadingManager setDelegate:];
-[CAMSmartStyleSettingsResourceLoadingManager delegate];
-[CAMSmartStyleSettingsResourceLoadingManager _loadingQueue];
-[CAMSmartStyleSettingsResourceLoadingManager _logIdentifiers];
-[CAMSmartStyleSettingsResourceLoadingManager _activeLoadStartTime];
-[CAMSmartStyleSettingsResourceLoadingManager _activeResourceLoader];
-[CAMSmartStyleSettingsResourceLoadingManager _allResourceLoaders];
-[CAMSmartStyleSettingsResourceLoadingManager _loadNextResourceIfPossible];
-[CAMSmartStyleSettingsResourceLoadingManager _pendingResourceLoaders];
-[CAMSmartStyleSettingsResourceLoadingManager _unloadResourcesForAssetIdentifier:allowLoadingNextResource:];
-[CAMSmartStyleSettingsResourceLoadingManager isWaitingOnLoadingForAssetIdentifiers:];
-[CAMSmartStyleSettingsResourceLoadingManager loadResourcesForAssetIdentifier:];
-[CAMSmartStyleSettingsResourceLoadingManager loadResourcesForAssetIdentifiers:unloadAllOthers:];
-[CAMSmartStyleSettingsResourceLoadingManager logIdentifierForAssetIdentifier:];
-[CAMSmartStyleSettingsResourceLoadingManager logIdentifierForAssetIdentifiers:];
-[CAMSmartStyleSettingsResourceLoadingManager resourceLoaderForAssetIdentifier:];
-[CAMSmartStyleSettingsResourceLoadingManager set_activeLoadStartTime:];
-[CAMSmartStyleSettingsResourceLoadingManager set_activeResourceLoader:];
-[CAMSmartStyleSettingsResourceLoadingManager smartStyleSettingsResourceLoaderDidFinishLoading:];
-[CAMSmartStyleSettingsResourceLoadingManager unloadResourcesForAssetIdentifier:];
```
