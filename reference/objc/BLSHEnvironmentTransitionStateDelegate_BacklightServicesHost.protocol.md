# `BLSHEnvironmentTransitionStateDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 6 instance methods, 0 class methods

## Properties

```
@property (T@"<BLSHInactiveBudgetPolicing_Private>",R,N) inactiveBudgetPolicy;
@property (T@"<BLSHOSTimerProviding>",R,N) osTimerProvider;
@property (T@"NSString",R,C,N) delegateLoggingName;
```

## Instance methods

```
-[BLSHEnvironmentTransitionStateDelegate delegateLoggingName];
-[BLSHEnvironmentTransitionStateDelegate osTimerProvider];
-[BLSHEnvironmentTransitionStateDelegate inactiveBudgetPolicy];
-[BLSHEnvironmentTransitionStateDelegate transitionState:didBeginUpdateToBacklightState:visualState:];
-[BLSHEnvironmentTransitionStateDelegate transitionState:didCompleteUpdateToBacklightState:visualState:];
-[BLSHEnvironmentTransitionStateDelegate transitionState:didUpdateToDateSpecifier:];
```
