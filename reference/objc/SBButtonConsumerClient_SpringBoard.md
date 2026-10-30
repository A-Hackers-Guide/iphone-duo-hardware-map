# `SBButtonConsumerClient`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 8 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _entitledToConsumeButtonsInBackground;
B _application;
B _runningVisible;
B _suspended;
@"<FBSServiceFacilityClientHandle>" _systemServiceClient;
@"NSMutableSet" _registrations;
@"SBApplicationController" _applicationController;
```

## Properties

```
@property (T@"<FBSServiceFacilityClientHandle>",&,N,V_systemServiceClient) systemServiceClient;
@property (TB,N,GisEntitledToConsumeButtonsInBackground,V_entitledToConsumeButtonsInBackground) entitledToConsumeButtonsInBackground;
@property (TB,N,GisApplication,V_application) application;
@property (TB,N,GisRunningVisible,V_runningVisible) runningVisible;
@property (TB,N,GisSuspended,V_suspended) suspended;
@property (TB,R,N) canReceiveEvents;
@property (T@"NSMutableSet",&,N,V_registrations) registrations;
@property (T@"SBApplicationController",R,N,V_applicationController) applicationController;
```

## Instance methods

```
-[SBButtonConsumerClient setSuspended:];
-[SBButtonConsumerClient isApplication];
-[SBButtonConsumerClient setRegistrations:];
-[SBButtonConsumerClient applicationController];
-[SBButtonConsumerClient isSuspended];
-[SBButtonConsumerClient registrations];
-[SBButtonConsumerClient setApplication:];
-[SBButtonConsumerClient setSystemServiceClient:];
-[SBButtonConsumerClient setEntitledToConsumeButtonsInBackground:];
-[SBButtonConsumerClient canReceiveEvents];
-[SBButtonConsumerClient isEntitledToConsumeButtonsInBackground];
-[SBButtonConsumerClient setRunningVisible:];
-[SBButtonConsumerClient hash];
-[SBButtonConsumerClient description];
-[SBButtonConsumerClient systemServiceClient];
-[SBButtonConsumerClient isEqual:];
-[SBButtonConsumerClient isRunningVisible];
```
