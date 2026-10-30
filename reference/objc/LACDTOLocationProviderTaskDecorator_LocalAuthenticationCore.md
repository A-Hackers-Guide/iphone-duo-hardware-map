# `LACDTOLocationProviderTaskDecorator`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOLocationProvider`
- 3 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<LACDTOLocationProvider>" _locationProvider;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"LACBackgroundTaskQueued" _locationStateBackgroundTask;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_workQueue) workQueue;
@property (T@"LACBackgroundTaskQueued",&,N,V_locationStateBackgroundTask) locationStateBackgroundTask;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACDTOLocationProviderTaskDecorator setWorkQueue:];
-[LACDTOLocationProviderTaskDecorator workQueue];
-[LACDTOLocationProviderTaskDecorator description];
-[LACDTOLocationProviderTaskDecorator setLocationStateBackgroundTask:];
-[LACDTOLocationProviderTaskDecorator _locationStateFromBackgroundTaskResult:];
-[LACDTOLocationProviderTaskDecorator _runLocationStateBackgroundTask:completion:];
-[LACDTOLocationProviderTaskDecorator checkIsInFamiliarLocationWithCompletion:];
-[LACDTOLocationProviderTaskDecorator initWithLocationProvider:workQueue:];
-[LACDTOLocationProviderTaskDecorator locationStateBackgroundTask];
```
