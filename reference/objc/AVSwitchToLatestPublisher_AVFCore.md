# `AVSwitchToLatestPublisher`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVPublisher`
- 4 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
^{OpaqueFigReentrantMutex=} _callbackMutex;
@"AVPublisher" _upstream;
@"AVNotificationSubscription" _outputPublisherSubscription;
i _publisherIndex;
```

## Class methods

```
+[AVSwitchToLatestPublisher switchToLatestPublisherWithUpstream:];
```

## Instance methods

```
-[AVSwitchToLatestPublisher initWithUpstream:];
-[AVSwitchToLatestPublisher dealloc];
-[AVSwitchToLatestPublisher description];
-[AVSwitchToLatestPublisher subscribeRequestingInitialValue:block:];
```
