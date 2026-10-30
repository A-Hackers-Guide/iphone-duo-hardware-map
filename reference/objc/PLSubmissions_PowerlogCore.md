# `PLSubmissions`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 12 properties, 80 instance methods, 1 class methods

## Instance variables

```
B _xpcActivityStarted;
B _taskingStarted;
@"PLStorageOperator" _storageOperator;
@"NSMutableArray" _submissionQueue;
d _lastXPCActivityTimestamp;
d _xpcActivityDelay;
@"PLSQLiteConnection" _connection;
@"NSString" _request;
@"NSString" _filterQuery;
@"NSString" _onDemandTasking;
@"NSNumber" _capValue;
@"DRConfigMonitor" _taskingMonitor;
```

## Properties

```
@property (T@"PLSQLiteConnection",&,V_connection) connection;
@property (T@"NSString",&,V_request) request;
@property (T@"NSString",&,V_filterQuery) filterQuery;
@property (T@"NSString",&,V_onDemandTasking) onDemandTasking;
@property (T@"NSNumber",&,V_capValue) capValue;
@property (T@"DRConfigMonitor",&,V_taskingMonitor) taskingMonitor;
@property (T@"PLStorageOperator",W,V_storageOperator) storageOperator;
@property (TB,V_xpcActivityStarted) xpcActivityStarted;
@property (T@"NSMutableArray",&,V_submissionQueue) submissionQueue;
@property (Td,V_lastXPCActivityTimestamp) lastXPCActivityTimestamp;
@property (Td,V_xpcActivityDelay) xpcActivityDelay;
@property (TB,R,V_taskingStarted) taskingStarted;
```

## Class methods

```
+[PLSubmissions sharedInstance];
```

## Instance methods

```
-[PLSubmissions setSubmissionQueue:];
-[PLSubmissions deferXPCActivity:];
-[PLSubmissions init];
-[PLSubmissions workQueue];
-[PLSubmissions removeFileAtURL:];
-[PLSubmissions request];
-[PLSubmissions connection];
-[PLSubmissions setConnection:];
-[PLSubmissions setStorageOperator:];
-[PLSubmissions setRequest:];
-[PLSubmissions storageOperator];
-[PLSubmissions finishXPCActivity:];
-[PLSubmissions setFilterQuery:];
-[PLSubmissions filterQuery];
-[PLSubmissions submissionQueue];
-[PLSubmissions removeFileAtPath:];
-[PLSubmissions onDemandTasking];
-[PLSubmissions attemptToUnregisterUploadSchedulingActivity];
-[PLSubmissions capValue];
-[PLSubmissions checkTaskingCompletionStatus];
-[PLSubmissions cleanupTemporarySubmissionFilesForTag:];
-[PLSubmissions clearTaskingDRConfig];
-[PLSubmissions configFromMonitor:];
-[PLSubmissions createWatchdogForSubmissionActivity:];
-[PLSubmissions disableHangtracer];
-[PLSubmissions emitBlobDetectedEvent:];
-[PLSubmissions emitBlobVerifiedEvent:];
-[PLSubmissions emitCollisionEvent:];
-[PLSubmissions enableHangtracer];
-[PLSubmissions enqueueFileForUpload:];
-[PLSubmissions enqueueSubmissionRecord:];
-[PLSubmissions fileCleanupWithRecord:];
-[PLSubmissions fullModeSubmissionBehavior];
-[PLSubmissions generateMSSSubmissionWithPayload:];
-[PLSubmissions generateOTASubmissionAndSendTaskingEndSubmission:];
-[PLSubmissions generatePLLSubmissionWithPayload:];
-[PLSubmissions getCurrentDRConfig];
-[PLSubmissions getLastBatteryTimestampSystem];
-[PLSubmissions handleDRConfigUpdate:error:];
-[PLSubmissions handleXPCActivityCallback:];
-[PLSubmissions initSubmissionQueue];
-[PLSubmissions internalSubmissionBehavior];
-[PLSubmissions lastXPCActivityTimestamp];
-[PLSubmissions logOTAStatus:];
-[PLSubmissions logSubmissionStateToAnalytics:];
-[PLSubmissions logTaskingStatus:withAction:];
-[PLSubmissions logTaskingStatus:withAction:withTables:];
-[PLSubmissions logTaskingTablesTurnedOn:];
-[PLSubmissions performSubmission:];
-[PLSubmissions persistSubmissionInfo:];
-[PLSubmissions prepareAndEnqueueSubmissionFilesWithConfig:];
-[PLSubmissions registerUploadSchedulingActivity];
-[PLSubmissions rejectTaskingDRConfig];
-[PLSubmissions sendSubmissionIssueSignature:];
-[PLSubmissions setCapValue:];
-[PLSubmissions setLastXPCActivityTimestamp:];
-[PLSubmissions setOnDemandTasking:];
-[PLSubmissions setTaskingMonitor:];
-[PLSubmissions setXpcActivityDelay:];
-[PLSubmissions setXpcActivityStarted:];
-[PLSubmissions setupDRTasking];
-[PLSubmissions shouldNotifyTaskingReceivedAndCompletedForConfig:];
-[PLSubmissions stopDRTasking];
-[PLSubmissions stopWatchdogForSubmissionActivity:];
-[PLSubmissions submitReasonForToday];
-[PLSubmissions submitRecord:withActivity:];
-[PLSubmissions submitRecordToDiagnosticPipeline:withConfig:];
-[PLSubmissions submitWithTaskingConfig:];
-[PLSubmissions taskingBlobDRExists];
-[PLSubmissions taskingBlobExists];
-[PLSubmissions taskingBlobHasTrialsConfiguration];
-[PLSubmissions taskingBlobLegacyExists];
-[PLSubmissions taskingCleanup];
-[PLSubmissions taskingModeSafeguard];
-[PLSubmissions taskingModeSetup];
-[PLSubmissions taskingMonitor];
-[PLSubmissions taskingStarted];
-[PLSubmissions taskingTypeSpecified];
-[PLSubmissions xpcActivityDelay];
-[PLSubmissions xpcActivityStarted];
```
