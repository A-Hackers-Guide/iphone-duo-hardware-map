# `LACDTOTelemetryReporting` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 18 instance methods, 0 class methods

## Instance methods

```
-[LACDTOTelemetryReporting sendAutoEnablementCheckResult:liveness:];
-[LACDTOTelemetryReporting sendCollapseEvaluationResult:mechanism:];
-[LACDTOTelemetryReporting sendEnvironmentUpdateDidFinish];
-[LACDTOTelemetryReporting sendEnvironmentUpdateWillStart];
-[LACDTOTelemetryReporting sendFeatureEnablementResult:strictModeEnabled:extendedPolicyProtectionEnabled:source:isAutoEnablement:success:liveness:];
-[LACDTOTelemetryReporting sendLocationStatePolicyResult:policy:];
-[LACDTOTelemetryReporting sendLocationStatusQueryDidFinish];
-[LACDTOTelemetryReporting sendLocationStatusQueryWillStart];
-[LACDTOTelemetryReporting sendLostModeQueryDidFinish];
-[LACDTOTelemetryReporting sendLostModeQueryResult:lost:confirmed:durationMs:];
-[LACDTOTelemetryReporting sendLostModeQueryWillStart];
-[LACDTOTelemetryReporting sendLostModeStateResult:time:];
-[LACDTOTelemetryReporting sendRatchetConfigAnomaly:secondsSinceBoot:];
-[LACDTOTelemetryReporting sendRatchetEvaluationResult:ratchetOperationAbandoned:ratchetStateBefore:ratchetStateAfter:];
-[LACDTOTelemetryReporting sendRepairStatusQueryDidFinish];
-[LACDTOTelemetryReporting sendRepairStatusQueryWillStart];
-[LACDTOTelemetryReporting sendSecurityDelayEvent:];
-[LACDTOTelemetryReporting sendSecurityDelayUIEvent:];
```
