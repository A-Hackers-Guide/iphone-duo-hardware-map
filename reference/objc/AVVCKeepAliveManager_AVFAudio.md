# `AVVCKeepAliveManager`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
^{AVVCKeepAliveImpl=^^?} _impl;
@"NSObject<OS_dispatch_queue>" mKeepAliveDispatchQueue;
```

## Class methods

```
+[AVVCKeepAliveManager sharedManager];
```

## Instance methods

```
-[AVVCKeepAliveManager stopWithCompletion:];
-[AVVCKeepAliveManager init];
-[AVVCKeepAliveManager dealloc];
-[AVVCKeepAliveManager startWithCompletion:];
-[AVVCKeepAliveManager createWithCompletion:];
-[AVVCKeepAliveManager destroyWithCompletion:];
-[AVVCKeepAliveManager getDispatchQueue];
```
