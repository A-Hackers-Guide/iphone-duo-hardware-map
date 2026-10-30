# `LACDTOSensorRepairStateProviderTaskDecorator`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOSensorRepairStateProvider`
- 3 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"<LACDTOSensorRepairStateProvider>" _provider;
@"NSObject<OS_dispatch_queue>" _replyQueue;
@"LACBackgroundTask" _backgroundTask;
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
-[LACDTOSensorRepairStateProviderTaskDecorator dealloc];
-[LACDTOSensorRepairStateProviderTaskDecorator fetchRepairStateWithCompletion:];
-[LACDTOSensorRepairStateProviderTaskDecorator _repairStateBackgroundTask];
-[LACDTOSensorRepairStateProviderTaskDecorator initWithProvider:replyQueue:];
```
