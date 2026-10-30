# `PLACDiagnosticsService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- 10 instance variables, 10 properties, 38 instance methods, 9 class methods

## Instance variables

```
I _attemptNumber;
@"PLXPCListenerOperatorComposition" _diagnosticsTriggerListener;
@"PLXPCResponderOperatorComposition" _acDiagnosticsMarkResponder;
@"PLXPCResponderOperatorComposition" _acDiagnosticsClearResponder;
@"PLXPCResponderOperatorComposition" _acDiagnosticsSetSerialResponder;
@"PLXPCResponderOperatorComposition" _acDiagnosticsCheckResponder;
@"PLXPCResponderOperatorComposition" _acDiagnosticsStatusResponder;
@"NSObject<OS_dispatch_source>" _periodicCheckTimer;
@"_TtC21PowerlogLiteOperators19ACDiagnosticsClient" _admissionClient;
@"NSDate" _candidateMarkedDate;
```

## Properties

```
@property (T@"PLXPCListenerOperatorComposition",&,V_diagnosticsTriggerListener) diagnosticsTriggerListener;
@property (T@"PLXPCResponderOperatorComposition",&,V_acDiagnosticsMarkResponder) acDiagnosticsMarkResponder;
@property (T@"PLXPCResponderOperatorComposition",&,V_acDiagnosticsClearResponder) acDiagnosticsClearResponder;
@property (T@"PLXPCResponderOperatorComposition",&,V_acDiagnosticsSetSerialResponder) acDiagnosticsSetSerialResponder;
@property (T@"PLXPCResponderOperatorComposition",&,V_acDiagnosticsCheckResponder) acDiagnosticsCheckResponder;
@property (T@"PLXPCResponderOperatorComposition",&,V_acDiagnosticsStatusResponder) acDiagnosticsStatusResponder;
@property (T@"NSObject<OS_dispatch_source>",&,V_periodicCheckTimer) periodicCheckTimer;
@property (T@"_TtC21PowerlogLiteOperators19ACDiagnosticsClient",&,V_admissionClient) admissionClient;
@property (T@"NSDate",&,V_candidateMarkedDate) candidateMarkedDate;
@property (TI,V_attemptNumber) attemptNumber;
```

## Class methods

```
+[PLACDiagnosticsService load];
+[PLACDiagnosticsService archiveFolder:];
+[PLACDiagnosticsService compressPowerlogsInFolder:];
+[PLACDiagnosticsService copyPowerlogArchivesToPath:];
+[PLACDiagnosticsService createFileWithEncryptedMetadata:temporaryPath:];
+[PLACDiagnosticsService createTagJsonFileWithResponseDictionary:temporaryPath:];
+[PLACDiagnosticsService createTempFolder];
+[PLACDiagnosticsService generatePowerlogForUploadAtTemporaryPath:];
+[PLACDiagnosticsService serializedJSONStringWithDictionary:];
```

## Instance methods

```
-[PLACDiagnosticsService init];
-[PLACDiagnosticsService initOperatorDependancies];
-[PLACDiagnosticsService setAttemptNumber:];
-[PLACDiagnosticsService attemptNumber];
-[PLACDiagnosticsService admissionClient];
-[PLACDiagnosticsService setAcDiagnosticsClearResponder:];
-[PLACDiagnosticsService acDiagnosticsSetSerialResponder];
-[PLACDiagnosticsService setAcDiagnosticsCheckResponder:];
-[PLACDiagnosticsService setupDiagnosticsTriggerListener];
-[PLACDiagnosticsService acDiagnosticsCheckResponder];
-[PLACDiagnosticsService acDiagnosticsClearResponder];
-[PLACDiagnosticsService acDiagnosticsMarkResponder];
-[PLACDiagnosticsService acDiagnosticsStatusResponder];
-[PLACDiagnosticsService candidateMarkedDate];
-[PLACDiagnosticsService clearCandidateStatus];
-[PLACDiagnosticsService diagnosticsTriggerListener];
-[PLACDiagnosticsService getCandidateIDWithCandidateInfo:];
-[PLACDiagnosticsService getCandidateInfo];
-[PLACDiagnosticsService getCandidateTimestampWithCandidateInfo:];
-[PLACDiagnosticsService handleAdmissionGranted:candidateID:timestamp:];
-[PLACDiagnosticsService handleDiagnosticsTrigger:];
-[PLACDiagnosticsService initOperatorDependanciesForTestingWithSerialNumber:];
-[PLACDiagnosticsService isCandidateExpired];
-[PLACDiagnosticsService markCandidateForTestingWithTimestamp:];
-[PLACDiagnosticsService performAdmissionCheck];
-[PLACDiagnosticsService performAdmissionCheckWithCompletion:];
-[PLACDiagnosticsService periodicCheckTimer];
-[PLACDiagnosticsService resumePeriodicCheckingIfNeeded];
-[PLACDiagnosticsService setAcDiagnosticsMarkResponder:];
-[PLACDiagnosticsService setAcDiagnosticsSetSerialResponder:];
-[PLACDiagnosticsService setAcDiagnosticsStatusResponder:];
-[PLACDiagnosticsService setAdmissionClient:];
-[PLACDiagnosticsService setCandidateMarkedDate:];
-[PLACDiagnosticsService setDiagnosticsTriggerListener:];
-[PLACDiagnosticsService setPeriodicCheckTimer:];
-[PLACDiagnosticsService setupACDiagnosticsXPCHandlersForTesting];
-[PLACDiagnosticsService startPeriodicChecking];
-[PLACDiagnosticsService stopPeriodicChecking];
```
