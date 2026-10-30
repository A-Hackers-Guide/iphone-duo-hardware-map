# `LACDTOTelemetryReporter`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOTelemetryReporting`
- 1 instance variables, 4 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"<LACAnalyticsReporting>" _analyticsReporter;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LACDTOTelemetryReporter sharedInstance];
```

## Instance methods

```
-[LACDTOTelemetryReporter sendAutoEnablementCheckResult:liveness:];
-[LACDTOTelemetryReporter sendCollapseEvaluationResult:mechanism:];
-[LACDTOTelemetryReporter sendEnvironmentUpdateDidFinish];
-[LACDTOTelemetryReporter sendEnvironmentUpdateWillStart];
-[LACDTOTelemetryReporter sendFeatureEnablementResult:strictModeEnabled:extendedPolicyProtectionEnabled:source:isAutoEnablement:success:liveness:];
-[LACDTOTelemetryReporter sendLocationStatePolicyResult:policy:];
-[LACDTOTelemetryReporter sendLocationStatusQueryDidFinish];
-[LACDTOTelemetryReporter sendLocationStatusQueryWillStart];
-[LACDTOTelemetryReporter sendLostModeQueryDidFinish];
-[LACDTOTelemetryReporter sendLostModeQueryResult:lost:confirmed:durationMs:];
-[LACDTOTelemetryReporter sendLostModeQueryWillStart];
-[LACDTOTelemetryReporter sendLostModeStateResult:time:];
-[LACDTOTelemetryReporter sendRatchetConfigAnomaly:secondsSinceBoot:];
-[LACDTOTelemetryReporter sendRatchetEvaluationResult:ratchetOperationAbandoned:ratchetStateBefore:ratchetStateAfter:];
-[LACDTOTelemetryReporter sendRepairStatusQueryDidFinish];
-[LACDTOTelemetryReporter sendRepairStatusQueryWillStart];
-[LACDTOTelemetryReporter sendSecurityDelayEvent:];
-[LACDTOTelemetryReporter sendSecurityDelayUIEvent:];
```
