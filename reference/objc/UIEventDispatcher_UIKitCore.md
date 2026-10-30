# `UIEventDispatcher`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIEventFetcherSink`
- 4 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"UIEventFetcher" _eventFetcher;
^{__CFRunLoopSource=} _collectHIDEventsRunLoopSource;
^{__CFRunLoop=} _runLoop;
@"UIEventEnvironment" _mainEnvironment;
```

## Instance methods

```
-[UIEventDispatcher dealloc];
-[UIEventDispatcher eventFetcherDidReceiveEvents:];
```
