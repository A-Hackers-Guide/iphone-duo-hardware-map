# `AVSystemMuteObserver`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 3 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"<AVSystemMuteObserverDelegate>" _delegate;
B _observing;
B _systemMuted;
@"NSObject<OS_dispatch_queue>" _serialQueue;
i _captionsOnMutePreferenceNotifyToken;
B _cachedCaptionsOnMutePreferenceEnabled;
@"AVSystemController" _avSystemController;
@ _avSystemControllerVolumeToken;
@ _avSystemControllerRouteToken;
@ _avSystemControllerServerDiedToken;
```

## Properties

```
@property (T@"<AVSystemMuteObserverDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisSystemMuted) systemMuted;
@property (TB,R,N,GisCaptionsOnMutePreferenceEnabled) captionsOnMutePreferenceEnabled;
```

## Class methods

```
+[AVSystemMuteObserver initialize];
```

## Instance methods

```
-[AVSystemMuteObserver stopObserving];
-[AVSystemMuteObserver init];
-[AVSystemMuteObserver dealloc];
-[AVSystemMuteObserver setDelegate:];
-[AVSystemMuteObserver delegate];
-[AVSystemMuteObserver _evaluate];
-[AVSystemMuteObserver _evaluateOnSerialQueue];
-[AVSystemMuteObserver _notifyDelegateOfChange];
-[AVSystemMuteObserver _refreshCachedCaptionsOnMutePreferenceEnabled];
-[AVSystemMuteObserver _startObservingAccessibility];
-[AVSystemMuteObserver _startObservingOnIPhoneFamily];
-[AVSystemMuteObserver _stopObservingOnIPhoneFamily];
-[AVSystemMuteObserver isCaptionsOnMutePreferenceEnabled];
-[AVSystemMuteObserver isSystemMuted];
-[AVSystemMuteObserver startObservingWithDelegate:];
```
