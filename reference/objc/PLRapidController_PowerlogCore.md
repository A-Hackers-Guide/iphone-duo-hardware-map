# `PLRapidController`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 13 properties, 68 instance methods, 15 class methods

## Instance variables

```
q _stage;
d _samplingPercentage;
@"NSString" _taskingRequestReason;
@"NSDate" _logCreationStartDate;
@"NSDate" _logCreationEndDate;
@"NSDate" _logCreationResumeDate;
@"NSString" _mdLogFilePath;
@"NSString" _mdLogCompressedFilePath;
@"NSString" _mssFilePath;
@"NSString" _mssCompressedFilePath;
@"NSString" _failureReason;
@"DRConfigMonitor" _taskingMonitor;
@"NSString" _configUUID;
```

## Properties

```
@property (Tq,V_stage) stage;
@property (Td,V_samplingPercentage) samplingPercentage;
@property (T@"NSString",&,V_taskingRequestReason) taskingRequestReason;
@property (T@"NSDate",&,V_logCreationStartDate) logCreationStartDate;
@property (T@"NSDate",&,V_logCreationEndDate) logCreationEndDate;
@property (T@"NSDate",&,V_logCreationResumeDate) logCreationResumeDate;
@property (T@"NSString",&,V_mdLogFilePath) mdLogFilePath;
@property (T@"NSString",&,V_mdLogCompressedFilePath) mdLogCompressedFilePath;
@property (T@"NSString",&,V_mssFilePath) mssFilePath;
@property (T@"NSString",&,V_mssCompressedFilePath) mssCompressedFilePath;
@property (T@"NSString",&,V_failureReason) failureReason;
@property (T@"DRConfigMonitor",&,V_taskingMonitor) taskingMonitor;
@property (T@"NSString",&,V_configUUID) configUUID;
```

## Class methods

```
+[PLRapidController sharedInstance];
+[PLRapidController cleanup];
+[PLRapidController allTablesInDB:];
+[PLRapidController appsToKeep:];
+[PLRapidController dataCollectionCriterion];
+[PLRapidController deferActivity:];
+[PLRapidController diagnosticLogSubmissionEnabled];
+[PLRapidController dropDataFromDB:withConfig:];
+[PLRapidController dropTablesFromDB:withConfig:];
+[PLRapidController finishActivity:withStatus:];
+[PLRapidController hangTypeFromStr:];
+[PLRapidController offsetTimestampsInDB:withConfig:withBaseTimestamp:];
+[PLRapidController randomBoolWithYesPercentage:];
+[PLRapidController roundDataInDB:withConfig:];
+[PLRapidController trimConditionsForTables:trimDate:];
```

## Instance methods

```
-[PLRapidController setupConnection];
-[PLRapidController init];
-[PLRapidController stage];
-[PLRapidController setStage:];
-[PLRapidController setFailureReason:];
-[PLRapidController failureReason];
-[PLRapidController setMssFilePath:];
-[PLRapidController addMDLogContext:];
-[PLRapidController addMSSContext:];
-[PLRapidController completeTaskingConfig:];
-[PLRapidController configFromMonitor:];
-[PLRapidController configUUID];
-[PLRapidController copyDB];
-[PLRapidController createHangTableInDB:];
-[PLRapidController dropAppVersions:];
-[PLRapidController dropDuplicateRows:];
-[PLRapidController generateContextDictionary:];
-[PLRapidController generateDummyPayload];
-[PLRapidController handleDRConfigUpdate:error:];
-[PLRapidController handleXPCActivityCallback:];
-[PLRapidController initializeSamplingPercentage];
-[PLRapidController initializeTaskingParams];
-[PLRapidController isUploadSizeWithinLimit:];
-[PLRapidController logCreationEndDate];
-[PLRapidController logCreationResumeDate];
-[PLRapidController logCreationStartDate];
-[PLRapidController logGenerationStats];
-[PLRapidController logHangSignposts:toDB:];
-[PLRapidController logSignpostDataToDB:];
-[PLRapidController logToCADataUploadState:];
-[PLRapidController logToCALogGenerationStats:];
-[PLRapidController mdLogCompressedFilePath];
-[PLRapidController mdLogFilePath];
-[PLRapidController mssCompressedFilePath];
-[PLRapidController mssFilePath];
-[PLRapidController packageAllLogs];
-[PLRapidController packageDB:];
-[PLRapidController persistActivityState];
-[PLRapidController prepareMSSLog];
-[PLRapidController preparePerfPowerlog:shouldDefer:];
-[PLRapidController pruneDB:withConfig:];
-[PLRapidController registerDataCollectionActivity];
-[PLRapidController rejectTaskingConfig:];
-[PLRapidController resetActivity];
-[PLRapidController samplingPercentage];
-[PLRapidController setConfigUUID:];
-[PLRapidController setLogCreationEndDate:];
-[PLRapidController setLogCreationResumeDate:];
-[PLRapidController setLogCreationStartDate];
-[PLRapidController setLogCreationStartDate:];
-[PLRapidController setMDLogCompressedFilePath];
-[PLRapidController setMDLogFilePath];
-[PLRapidController setMSSCompressedFilePath];
-[PLRapidController setMSSFilePath];
-[PLRapidController setMdLogCompressedFilePath:];
-[PLRapidController setMdLogFilePath:];
-[PLRapidController setMssCompressedFilePath:];
-[PLRapidController setSamplingPercentage:];
-[PLRapidController setTaskingMonitor:];
-[PLRapidController setTaskingRequestReason:];
-[PLRapidController setupDRTasking];
-[PLRapidController shouldDoRapidCollection];
-[PLRapidController stopDRTasking];
-[PLRapidController taskingMonitor];
-[PLRapidController taskingRequestReason];
-[PLRapidController topAppsRunTime];
-[PLRapidController trimAndFilterDB:withConfig:];
-[PLRapidController uploadLog:];
```
