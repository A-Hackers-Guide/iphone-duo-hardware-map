# `AVCMNotificationDispatcherListenerKey`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 0 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"AVWeakReference" _weakReferenceToListener;
^? _callback;
@"NSString" _name;
^v _object;
```

## Class methods

```
+[AVCMNotificationDispatcherListenerKey listenerKeyWithWeakReferenceToListener:callback:name:object:];
```

## Instance methods

```
-[AVCMNotificationDispatcherListenerKey init];
-[AVCMNotificationDispatcherListenerKey dealloc];
-[AVCMNotificationDispatcherListenerKey hash];
-[AVCMNotificationDispatcherListenerKey copyWithZone:];
-[AVCMNotificationDispatcherListenerKey isEqual:];
-[AVCMNotificationDispatcherListenerKey initWithWeakReferenceToListener:callback:name:object:];
```
