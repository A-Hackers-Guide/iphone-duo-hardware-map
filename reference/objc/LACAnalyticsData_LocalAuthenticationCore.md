# `LACAnalyticsData`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACAnalyticsCollecting`
- 2 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"LACBiomeDialogEvent" _biomeDialogEvent;
@"NSNumber" _tccFaceIDResult;
```

## Properties

```
@property (T@"LACBiomeDialogEvent",R,N,V_biomeDialogEvent) biomeDialogEvent;
@property (T@"NSNumber",&,N,V_tccFaceIDResult) tccFaceIDResult;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACAnalyticsData init];
-[LACAnalyticsData authenticationStartedForEvent:];
-[LACAnalyticsData description];
-[LACAnalyticsData tccFaceIDResult];
-[LACAnalyticsData authenticationAction:failing:];
-[LACAnalyticsData authenticationAttemptFailedForEvent:];
-[LACAnalyticsData authenticationSuccessfulForEvent:];
-[LACAnalyticsData biomeDialogEvent];
-[LACAnalyticsData mergeAnalyticsData:];
-[LACAnalyticsData setTccFaceIDResult:];
```
