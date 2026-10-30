# `FBSApplicationPlaceholder`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSBundleInfo`
- 8 instance variables, 8 properties, 53 instance methods, 2 class methods

## Instance variables

```
@"LSApplicationProxy" _proxy;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_queue>" _callOutQueue;
@"FBSApplicationPlaceholderProgress" _queue_progress;
@"NSMutableSet" _queue_observers;
Q _installType;
@"LSApplicationIdentity" _applicationIdentity;
@"FBSApplicationLibrary" _appLibrary;
```

## Properties

```
@property (T@"LSApplicationProxy",&,N,G_proxy,S_setProxy:) proxy;
@property (T@"FBSApplicationLibrary",W,N,V_appLibrary) appLibrary;
@property (T@"LSApplicationIdentity",R,C,N,V_applicationIdentity) applicationIdentity;
@property (T@"<FBSApplicationPlaceholderProgress>",R,N) progress;
@property (TB,R,N,GisPrioritizable) prioritizable;
@property (TB,R,N,GisPausable) pausable;
@property (TB,R,N,GisResumable) resumable;
@property (TB,R,N,GisCancellable) cancellable;
```

## Class methods

```
+[FBSApplicationPlaceholder _sharedQueue];
+[FBSApplicationPlaceholder _callOutQueue];
```

## Instance methods

```
-[FBSApplicationPlaceholder installType];
-[FBSApplicationPlaceholder isRestricted];
-[FBSApplicationPlaceholder pause];
-[FBSApplicationPlaceholder percentComplete];
-[FBSApplicationPlaceholder succinctDescriptionBuilder];
-[FBSApplicationPlaceholder removeObserver:];
-[FBSApplicationPlaceholder installPhase];
-[FBSApplicationPlaceholder add:];
-[FBSApplicationPlaceholder remove:];
-[FBSApplicationPlaceholder prioritize];
-[FBSApplicationPlaceholder dealloc];
-[FBSApplicationPlaceholder progress];
-[FBSApplicationPlaceholder addObserver:];
-[FBSApplicationPlaceholder expectedFinalInstallPhase];
-[FBSApplicationPlaceholder _proxy];
-[FBSApplicationPlaceholder installState];
-[FBSApplicationPlaceholder cancel];
-[FBSApplicationPlaceholder isResumable];
-[FBSApplicationPlaceholder resume];
-[FBSApplicationPlaceholder descriptionBuilderWithMultilinePrefix:];
-[FBSApplicationPlaceholder isPrioritizable];
-[FBSApplicationPlaceholder isCancellable];
-[FBSApplicationPlaceholder isPausable];
-[FBSApplicationPlaceholder _reloadProgress];
-[FBSApplicationPlaceholder _canPerformAction:];
-[FBSApplicationPlaceholder _cancelWithResult:];
-[FBSApplicationPlaceholder _dispatchToObserversWithBlock:];
-[FBSApplicationPlaceholder _initWithApplicationProxy:identity:];
-[FBSApplicationPlaceholder _initWithBundleIdentifier:url:];
-[FBSApplicationPlaceholder _initWithBundleProxy:url:];
-[FBSApplicationPlaceholder _noteChangedSignificantly];
-[FBSApplicationPlaceholder _pauseWithResult:];
-[FBSApplicationPlaceholder _performAction:withResult:];
-[FBSApplicationPlaceholder _prioritizeWithResult:];
-[FBSApplicationPlaceholder _queue_canPerformAction:];
-[FBSApplicationPlaceholder _queue_isCloudDemoted];
-[FBSApplicationPlaceholder _queue_noteChangedSignificantly:];
-[FBSApplicationPlaceholder _queue_setProxy:force:];
-[FBSApplicationPlaceholder _queue_supportedActions];
-[FBSApplicationPlaceholder _reloadFromProxy:];
-[FBSApplicationPlaceholder _reloadFromRecord:];
-[FBSApplicationPlaceholder _resumeWithResult:];
-[FBSApplicationPlaceholder _sendToObserversPlaceholderDidChangeSignificantly];
-[FBSApplicationPlaceholder _sendToObserversPlaceholderProgressDidUpdate];
-[FBSApplicationPlaceholder _setProxy:];
-[FBSApplicationPlaceholder _setProxy:force:];
-[FBSApplicationPlaceholder appLibrary];
-[FBSApplicationPlaceholder applicationIdentity];
-[FBSApplicationPlaceholder cancelWithResult:];
-[FBSApplicationPlaceholder pauseWithResult:];
-[FBSApplicationPlaceholder prioritizeWithResult:];
-[FBSApplicationPlaceholder resumeWithResult:];
-[FBSApplicationPlaceholder setAppLibrary:];
```
