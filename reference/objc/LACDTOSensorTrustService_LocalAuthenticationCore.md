# `LACDTOSensorTrustService`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOSensorTrustService`
- 7 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _replyQueue;
@"<LACUserInterfaceController>" _uiController;
@"<LACDTOKVStore>" _store;
@"<LACDTOFeatureStateProviding>" _featureStateProvider;
@"<LACFlagsProvider>" _flags;
@"<LACDTOSensorTrustStateProvider>" _trustStateProvider;
@"<LACDTOTelemetryReporting>" _telemetry;
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
-[LACDTOSensorTrustService _repairStateProvider];
-[LACDTOSensorTrustService _trustStore];
-[LACDTOSensorTrustService _trustVerifier];
-[LACDTOSensorTrustService _uiPresenter];
-[LACDTOSensorTrustService evaluationProcessor];
-[LACDTOSensorTrustService initWithReplyQueue:uiController:store:featureStateProvider:telemetry:];
-[LACDTOSensorTrustService trustStateProvider];
```
