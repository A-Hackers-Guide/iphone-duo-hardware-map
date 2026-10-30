# `AVCMNotificationDispatcher`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 7 instance methods, 2 class methods

## Instance variables

```
^{opaqueCMNotificationCenter=} _cmNotificationCenter;
@"NSObject<OS_dispatch_queue>" _listenerObjectsQueue;
@"NSMutableDictionary" _observersForListenerKeys;
```

## Properties

```
@property (T^{opaqueCMNotificationCenter=},R,N) CMNotificationCenter;
```

## Class methods

```
+[AVCMNotificationDispatcher initialize];
+[AVCMNotificationDispatcher notificationDispatcherForCMNotificationCenter:];
```

## Instance methods

```
-[AVCMNotificationDispatcher removeListenerWithWeakReference:callback:name:object:];
-[AVCMNotificationDispatcher init];
-[AVCMNotificationDispatcher dealloc];
-[AVCMNotificationDispatcher addListenerWithWeakReference:callback:name:object:flags:];
-[AVCMNotificationDispatcher _copyAndRemoveObserverForWeakReferenceToListener:callback:name:object:];
-[AVCMNotificationDispatcher CMNotificationCenter];
-[AVCMNotificationDispatcher initWithCMNotificationCenter:];
```
