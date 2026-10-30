# `SBIconRepositoryInfoProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBHApplicationInfoProviding`
- 4 instance variables, 10 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"SBApplicationController" _applicationController;
@"SBApplicationPlaceholderController" _applicationPlaceholderController;
@"NSArray" _cachedApplications;
```

## Properties

```
@property (T@"NSArray",C,N,V_cachedApplications) cachedApplications;
@property (T@"SBApplicationController",&,N,V_applicationController) applicationController;
@property (T@"SBApplicationPlaceholderController",&,N,V_applicationPlaceholderController) applicationPlaceholderController;
@property (T@"NSArray",R,N) applications;
@property (T@"NSArray",?,R,N) applicationPlaceholders;
@property (T@"NSArray",?,R,N) webClips;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBIconRepositoryInfoProvider applications];
-[SBIconRepositoryInfoProvider applicationController];
-[SBIconRepositoryInfoProvider init];
-[SBIconRepositoryInfoProvider setApplicationController:];
-[SBIconRepositoryInfoProvider dealloc];
-[SBIconRepositoryInfoProvider applicationPlaceholderController];
-[SBIconRepositoryInfoProvider webClips];
-[SBIconRepositoryInfoProvider addApplicationInfoProviderObserver:];
-[SBIconRepositoryInfoProvider applicationPlaceholders];
-[SBIconRepositoryInfoProvider removeApplicationInfoProviderObserver:];
-[SBIconRepositoryInfoProvider initWithApplicationController:applicationPlaceholderController:];
-[SBIconRepositoryInfoProvider _notifyObserversDidAddApplicationPlaceholders:];
-[SBIconRepositoryInfoProvider _notifyObserversDidAddApplications:];
-[SBIconRepositoryInfoProvider _notifyObserversDidRemoveApplicationPlaceholders:];
-[SBIconRepositoryInfoProvider _notifyObserversDidRemoveApplications:];
-[SBIconRepositoryInfoProvider _notifyObserversDidUpdateApplicationPlaceholders:];
-[SBIconRepositoryInfoProvider _notifyObserversDidUpdateApplications:];
-[SBIconRepositoryInfoProvider cachedApplications];
-[SBIconRepositoryInfoProvider installedAppPlaceholdersDidChange:];
-[SBIconRepositoryInfoProvider installedAppsDidChange:];
-[SBIconRepositoryInfoProvider setApplicationPlaceholderController:];
-[SBIconRepositoryInfoProvider setCachedApplications:];
```
