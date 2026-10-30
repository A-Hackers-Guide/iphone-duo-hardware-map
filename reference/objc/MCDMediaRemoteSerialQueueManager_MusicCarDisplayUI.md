# `MCDMediaRemoteSerialQueueManager`

- Image: [`/System/Library/PrivateFrameworks/MusicCarDisplayUI.framework/MusicCarDisplayUI`](../userland/System__Library__PrivateFrameworks__MusicCarDisplayUI.framework__MusicCarDisplayUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSOperationQueue" _mediaRemoteSerialQueue;
```

## Properties

```
@property (T@"NSOperationQueue",&,N,V_mediaRemoteSerialQueue) mediaRemoteSerialQueue;
```

## Class methods

```
+[MCDMediaRemoteSerialQueueManager sharedInstance];
```

## Instance methods

```
-[MCDMediaRemoteSerialQueueManager init];
-[MCDMediaRemoteSerialQueueManager cancelAllOperations];
-[MCDMediaRemoteSerialQueueManager addOperation:cancelAllOperations:];
-[MCDMediaRemoteSerialQueueManager mediaRemoteSerialQueue];
-[MCDMediaRemoteSerialQueueManager setMediaRemoteSerialQueue:];
```
