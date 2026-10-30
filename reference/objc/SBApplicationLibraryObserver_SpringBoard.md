# `SBApplicationLibraryObserver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MCProfileConnectionObserver`
- 7 instance variables, 5 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"XBApplicationController" _splashBoardController;
@"FBSApplicationLibrary" _appLibrary;
@"NSMutableSet" _suspendCalloutsAssertionReasons;
@"NSObject<OS_dispatch_queue>" _mainQueueProxy;
@"NSMutableDictionary" _placeholdersByBundleID;
@"NSHashTable" _applicationObservers;
@"NSHashTable" _placeholderObservers;
```

## Properties

```
@property (T@"NSArray",R,C,N) placeholders;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBApplicationLibraryObserver new];
```

## Instance methods

```
-[SBApplicationLibraryObserver profileConnectionDidReceiveEffectiveSettingsChangedNotification:userInfo:];
-[SBApplicationLibraryObserver init];
-[SBApplicationLibraryObserver profileConnectionDidReceiveProfileListChangedNotification:userInfo:];
-[SBApplicationLibraryObserver placeholders];
-[SBApplicationLibraryObserver _didAddPlaceholders:];
-[SBApplicationLibraryObserver _addObserver:table:];
-[SBApplicationLibraryObserver _appBundleIDsForApplications:];
-[SBApplicationLibraryObserver _didAddApplications:];
-[SBApplicationLibraryObserver _didCancelPlaceholders:];
-[SBApplicationLibraryObserver _didChangeNetworkUsage:];
-[SBApplicationLibraryObserver _didDemoteApplications:];
-[SBApplicationLibraryObserver _didRemoveApplications:];
-[SBApplicationLibraryObserver _didReplaceApplications:];
-[SBApplicationLibraryObserver _didUpdateApplications:];
-[SBApplicationLibraryObserver _removeObserver:table:];
-[SBApplicationLibraryObserver _waitForLaunchImageGenerationForApplications:];
-[SBApplicationLibraryObserver addApplicationLifecycleObserver:];
-[SBApplicationLibraryObserver addPlaceholderLifecycleObserver:];
-[SBApplicationLibraryObserver initWithAppLibrary:splashBoardController:];
-[SBApplicationLibraryObserver removeApplicationLifecycleObserver:];
-[SBApplicationLibraryObserver removePlaceholderLifecycleObserver:];
-[SBApplicationLibraryObserver suspendCalloutsAssertionWithReason:];
```
