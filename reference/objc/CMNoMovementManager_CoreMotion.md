# `CMNoMovementManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 8 instance methods, 1 class methods

## Instance variables

```
{unique_ptr<CLConnectionClient, std::default_delete<CLConnectionClient>>=""{?="__ptr_"^{CLConnectionClient}}} fLocationdConnection;
@"NSObject<OS_dispatch_queue>" fInternalQueue;
@"<CMNoMovementManagerDelegate>" _delegate;
```

## Properties

```
@property (T@"<CMNoMovementManagerDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[CMNoMovementManager isAvailable];
```

## Instance methods

```
-[CMNoMovementManager _connect];
-[CMNoMovementManager _disconnect];
-[CMNoMovementManager init];
-[CMNoMovementManager dealloc];
-[CMNoMovementManager setDelegate:];
-[CMNoMovementManager _handleMessage:];
-[CMNoMovementManager delegate];
-[CMNoMovementManager requestLatestStateUpdate];
```
