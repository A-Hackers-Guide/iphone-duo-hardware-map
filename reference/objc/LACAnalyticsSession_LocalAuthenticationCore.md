# `LACAnalyticsSession`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACAnalyticsCollecting`
- 5 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _evaluationAnalytics;
B _finished;
@"LACAnalyticsData" _analyticsData;
@"NSString" _dialogID;
@"NSString" _bundleID;
```

## Properties

```
@property (T@"LACAnalyticsData",R,N,V_analyticsData) analyticsData;
@property (T@"NSString",R,N,V_dialogID) dialogID;
@property (T@"NSString",R,N,V_bundleID) bundleID;
@property (TB,R,N,V_finished) finished;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACAnalyticsSession finished];
-[LACAnalyticsSession finish];
-[LACAnalyticsSession analyticsData];
-[LACAnalyticsSession dealloc];
-[LACAnalyticsSession authenticationStartedForEvent:];
-[LACAnalyticsSession description];
-[LACAnalyticsSession bundleID];
-[LACAnalyticsSession dialogID];
-[LACAnalyticsSession authenticationAction:failing:];
-[LACAnalyticsSession authenticationAttemptFailedForEvent:];
-[LACAnalyticsSession authenticationSuccessfulForEvent:];
-[LACAnalyticsSession initWithDialogID:bundleID:];
-[LACAnalyticsSession mergeEvaluationAnalytics:];
-[LACAnalyticsSession trackEvaluationAnalytics:];
-[LACAnalyticsSession untrackEvaluationAnalytics:];
```
