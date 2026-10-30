# `LACDTOLocationController`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOLocationMonitorDelegate`, `LACDTOLocationController`, `LACDTOLocationProvider`, `LACDTOPendingPolicyEvaluationControllerObserver`, `LACDTOEventProducer`
- 7 instance variables, 8 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"<LACDTOLocationProvider>" locationProvider;
@"<LACDTOLocationMonitor>" monitor;
@"<LACDTOKVStore>" store;
@"<LACFeatureFlagsProviderDTO>" featureFlags;
@"OS_dispatch_queue" workQueue;
@"LACDTOLocationState" locationState;
@"<LACDTOEventBus>" eventBus;
```

## Properties

```
@property (T@"<LACDTOLocationProvider>",N,&,VlocationProvider) locationProvider;
@property (T@"<LACDTOLocationMonitor>",N,&,Vmonitor) monitor;
@property (T@"<LACDTOKVStore>",N,&,Vstore) store;
@property (T@"<LACFeatureFlagsProviderDTO>",N,&,VfeatureFlags) featureFlags;
@property (T@"OS_dispatch_queue",N,&,VworkQueue) workQueue;
@property (T@"LACDTOLocationState",N,&,VlocationState) locationState;
@property (T@"<LACDTOEventBus>",N,&,VeventBus) eventBus;
@property (T@"NSString",N,R) description;
```

## Instance methods

```
-[LACDTOLocationController setWorkQueue:];
-[LACDTOLocationController monitor];
-[LACDTOLocationController store];
-[LACDTOLocationController setLocationProvider:];
-[LACDTOLocationController setLocationState:];
-[LACDTOLocationController init];
-[LACDTOLocationController setMonitor:];
-[LACDTOLocationController locationState];
-[LACDTOLocationController workQueue];
-[LACDTOLocationController description];
-[LACDTOLocationController setStore:];
-[LACDTOLocationController setFeatureFlags:];
-[LACDTOLocationController locationProvider];
-[LACDTOLocationController featureFlags];
-[LACDTOLocationController checkIsInFamiliarLocationWithCompletion:];
-[LACDTOLocationController eventBus];
-[LACDTOLocationController initWithLocationProvider:monitor:store:featureFlags:workQueue:];
-[LACDTOLocationController locationMonitor:didReceiveLocationState:];
-[LACDTOLocationController pendingEvaluationController:updatedPendingEvaluation:];
-[LACDTOLocationController pendingEvaluationControllerDidStartTrackingPendingEvaluations:];
-[LACDTOLocationController pendingEvaluationControllerDidStopTrackingPendingEvaluations:];
-[LACDTOLocationController setEventBus:];
```
