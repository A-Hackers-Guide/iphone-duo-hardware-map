# `CMCallHandednessManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" fPrivateQueue;
^{Dispatcher=^^?@} fDispatcher;
@"<CMCallHandednessDelegate>" _delegate;
```

## Properties

```
@property (T@"<CMCallHandednessDelegate>",N,V_delegate) delegate;
```

## Class methods

```
+[CMCallHandednessManager isCallHandednessAvailable];
```

## Instance methods

```
-[CMCallHandednessManager init];
-[CMCallHandednessManager dealloc];
-[CMCallHandednessManager setDelegate:];
-[CMCallHandednessManager delegate];
-[CMCallHandednessManager onCallHandednessStateUpdated:];
-[CMCallHandednessManager startCallHandednessUpdates];
-[CMCallHandednessManager stopCallHandednessUpdates];
```
