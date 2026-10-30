# `CAMBufferNotificationObservance`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMBufferObservance`
- 3 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSString" _notification;
@"NSObject" _object;
@"NSNotificationCenter" _notificationCenter;
```

## Properties

```
@property (T@"NSString",R,C,N,V_notification) notification;
@property (T@"NSObject",R,W,N,V_object) object;
@property (T@"NSNotificationCenter",R,N,V_notificationCenter) notificationCenter;
```

## Instance methods

```
-[CAMBufferNotificationObservance notificationCenter];
-[CAMBufferNotificationObservance notification];
-[CAMBufferNotificationObservance object];
-[CAMBufferNotificationObservance fulfillWithChange:];
-[CAMBufferNotificationObservance initWithNotification:object:center:removeOnceEnabled:];
-[CAMBufferNotificationObservance setupObservanceForBuffer:];
-[CAMBufferNotificationObservance teardownObservanceForBuffer:];
```
