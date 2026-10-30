# `FBSDisplaySource`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`, `BSDescriptionProviding`
- 25 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"CADisplay" _display;
@"FBSDisplayMonitor" _lock_monitor;
@"NSObject<OS_dispatch_queue>" _callOutQueue;
@"FBSDisplayConfiguration" _lock_rawConfiguration;
@"FBSDisplayConfiguration" _lock_rawConfigurationOfLastTransition;
@"FBSDisplayConfiguration" _lock_reportedRawConfiguration;
@"NSSet" _lock_reportedEffectiveConfigurations;
@"FBSDisplayConfiguration" _evlock_rawConfiguration;
@"FBSDisplayConfiguration" _evlock_reportedRawConfiguration;
@"NSSet" _evlock_reportedEffectiveConfigurations;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _externallyVisibleLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _updateTransformsLock;
I _displayID;
I _instanceID;
i _lock_attachment;
i _evlock_attachment;
I _lock_debounceToken;
B _isMainDisplay;
B _updatable;
B _observing;
B _lock_initialized;
B _lock_allowsUnknown;
B _lock_invalidated;
B _alwaysConnected;
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
-[FBSDisplaySource observeValueForKeyPath:ofObject:change:context:];
-[FBSDisplaySource debugDescription];
-[FBSDisplaySource succinctDescriptionBuilder];
-[FBSDisplaySource init];
-[FBSDisplaySource dealloc];
-[FBSDisplaySource descriptionWithMultilinePrefix:];
-[FBSDisplaySource succinctDescription];
-[FBSDisplaySource invalidate];
-[FBSDisplaySource description];
-[FBSDisplaySource descriptionBuilderWithMultilinePrefix:];
```
