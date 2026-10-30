# `UISApplicationSupportClient`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 3 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
B _queue_invalidated;
@"BSServiceConnection" _queue_connection;
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
-[UISApplicationSupportClient init];
-[UISApplicationSupportClient dealloc];
-[UISApplicationSupportClient invalidate];
-[UISApplicationSupportClient _remoteTarget];
-[UISApplicationSupportClient requestPasscodeUnlockUIWithCompletion:];
-[UISApplicationSupportClient _applicationSupportServiceEndpoint];
-[UISApplicationSupportClient applicationInitializationContextWithParameters:];
-[UISApplicationSupportClient destroyScenesWithPersistentIdentifiers:animationType:destroySessions:completion:];
```
