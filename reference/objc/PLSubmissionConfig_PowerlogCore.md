# `PLSubmissionConfig`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 45 instance variables, 54 properties, 134 instance methods, 5 class methods

## Instance variables

```
Q _submittedFilesMask;
B _isDRTasking;
B _enableDPUpload;
B _signpostDisable;
B _seed;
B _internal;
s _submitReasonType;
@"NSUUID" _configUUID;
@"NSDate" _configDateReceived;
@"NSDate" _configDateApplied;
@"NSString" _request;
@"NSString" _ondemand;
@"NSNumber" _capSize;
@"NSNumber" _mssCycleInterval;
@"NSDictionary" _plTaskingTables;
@"NSDictionary" _ppsTaskingTables;
@"NSDictionary" _hashEntries;
@"NSArray" _removeEntries;
@"NSArray" _trimmingQueries;
@"NSString" _taskingType;
@"NSDictionary" _defaultTaskingTypeParameters;
@"NSDictionary" _perModelTaskingTypeParameters;
@"NSArray" _taskingTrials;
@"NSNumber" _taskingTrialsPercentage;
@"NSNumber" _taskingBaselinePercentage;
@"NSArray" _taskingTableGroups;
@"NSDictionary" _perModelTrialsPercentages;
@"NSArray" _enrolledTrialNamespaces;
@"NSArray" _taskingFiles;
@"NSDictionary" _signpostAllowlist;
@"NSDate" _startDate;
@"NSDate" _endDate;
@"NSDate" _lastBatteryTimestampSystem;
@"NSNumber" _cacheSize;
@"NSString" _tagUUID;
@"NSArray" _builds;
@"NSString" _deviceModel;
@"NSString" _filePath;
@"NSDictionary" _ckTagConfig;
@"NSString" _blobFailureReason;
d _dice;
@"NSString" _taskingBuild;
@"NSString" _taskingPopulation;
@"NSString" _taskingDeviceModels;
@"NSDictionary" _taskingPercentage;
```

## Properties

```
@property (Td,V_dice) dice;
@property (T@"NSString",&,V_taskingBuild) taskingBuild;
@property (T@"NSString",&,V_taskingPopulation) taskingPopulation;
@property (T@"NSString",&,V_taskingDeviceModels) taskingDeviceModels;
@property (T@"NSDictionary",&,V_taskingPercentage) taskingPercentage;
@property (TB,V_isDRTasking) isDRTasking;
@property (T@"NSUUID",&,V_configUUID) configUUID;
@property (T@"NSDate",&,V_configDateReceived) configDateReceived;
@property (T@"NSDate",&,V_configDateApplied) configDateApplied;
@property (T@"NSString",&,V_request) request;
@property (T@"NSString",&,V_ondemand) ondemand;
@property (T@"NSNumber",&,V_capSize) capSize;
@property (T@"NSNumber",&,V_mssCycleInterval) mssCycleInterval;
@property (T@"NSDictionary",&,V_plTaskingTables) plTaskingTables;
@property (T@"NSDictionary",&,V_ppsTaskingTables) ppsTaskingTables;
@property (T@"NSDictionary",&,V_hashEntries) hashEntries;
@property (T@"NSArray",&,V_removeEntries) removeEntries;
@property (T@"NSArray",&,V_trimmingQueries) trimmingQueries;
@property (T@"NSString",&,V_taskingType) taskingType;
@property (T@"NSDictionary",&,V_defaultTaskingTypeParameters) defaultTaskingTypeParameters;
@property (T@"NSDictionary",&,V_perModelTaskingTypeParameters) perModelTaskingTypeParameters;
@property (T@"NSArray",&,V_taskingTrials) taskingTrials;
@property (T@"NSNumber",&,V_taskingTrialsPercentage) taskingTrialsPercentage;
@property (T@"NSNumber",&,V_taskingBaselinePercentage) taskingBaselinePercentage;
@property (T@"NSArray",&,V_taskingTableGroups) taskingTableGroups;
@property (T@"NSDictionary",&,V_perModelTrialsPercentages) perModelTrialsPercentages;
@property (T@"NSArray",&,V_enrolledTrialNamespaces) enrolledTrialNamespaces;
@property (T@"NSArray",&,V_taskingFiles) taskingFiles;
@property (TB,R) hasFileToSubmit;
@property (TB,R) submitPLL;
@property (TB,R) submitPLLUpgrade;
@property (TB,R) submitMSS;
@property (TB,R) submitSP;
@property (TB,R) submitBDC;
@property (TB,R) submitCE;
@property (TB,R) submitXC;
@property (TB,R) submitBG;
@property (TQ,R) submittedFilesMask;
@property (TB,V_enableDPUpload) enableDPUpload;
@property (TB,V_signpostDisable) signpostDisable;
@property (T@"NSDictionary",&,V_signpostAllowlist) signpostAllowlist;
@property (T@"NSDate",&,V_startDate) startDate;
@property (T@"NSDate",&,V_endDate) endDate;
@property (T@"NSDate",&,V_lastBatteryTimestampSystem) lastBatteryTimestampSystem;
@property (T@"NSNumber",&,V_cacheSize) cacheSize;
@property (Ts,V_submitReasonType) submitReasonType;
@property (T@"NSString",&,V_tagUUID) tagUUID;
@property (TB,V_seed) seed;
@property (TB,V_internal) internal;
@property (T@"NSArray",&,V_builds) builds;
@property (T@"NSString",&,V_deviceModel) deviceModel;
@property (T@"NSString",&,V_filePath) filePath;
@property (T@"NSDictionary",&,V_ckTagConfig) ckTagConfig;
@property (T@"NSString",&,V_blobFailureReason) blobFailureReason;
```

## Class methods

```
+[PLSubmissionConfig clearTaskingDefaults];
+[PLSubmissionConfig getDateMarkerFromSystemDate:];
+[PLSubmissionConfig internalSubmissionBehavior];
+[PLSubmissionConfig submitTaskingDefaultsCheckStateToCA:];
+[PLSubmissionConfig taskingTableGroups];
```

## Instance methods

```
-[PLSubmissionConfig startDate];
-[PLSubmissionConfig seed];
-[PLSubmissionConfig deviceModel];
-[PLSubmissionConfig setStartDate:];
-[PLSubmissionConfig cacheSize];
-[PLSubmissionConfig endDate];
-[PLSubmissionConfig request];
-[PLSubmissionConfig setEndDate:];
-[PLSubmissionConfig setCacheSize:];
-[PLSubmissionConfig setInternal:];
-[PLSubmissionConfig filePath];
-[PLSubmissionConfig setRequest:];
-[PLSubmissionConfig internal];
-[PLSubmissionConfig copyWithZone:];
-[PLSubmissionConfig setFilePath:];
-[PLSubmissionConfig initWithPayload:];
-[PLSubmissionConfig setSeed:];
-[PLSubmissionConfig setDeviceModel:];
-[PLSubmissionConfig contextDictionary];
-[PLSubmissionConfig builds];
-[PLSubmissionConfig setBuilds:];
-[PLSubmissionConfig capSize];
-[PLSubmissionConfig emitSubmitEvent];
-[PLSubmissionConfig plTaskingTables];
-[PLSubmissionConfig setCkTagConfig:];
-[PLSubmissionConfig setHashEntries:];
-[PLSubmissionConfig setIsDRTasking:];
-[PLSubmissionConfig tagUUID];
-[PLSubmissionConfig emitQueryEvent:];
-[PLSubmissionConfig enrolledTrialsFromTaskingTrials];
-[PLSubmissionConfig hasFileToSubmit];
-[PLSubmissionConfig setTaskingType:];
-[PLSubmissionConfig signpostDisable];
-[PLSubmissionConfig trimmingQueries];
-[PLSubmissionConfig blobFailureReason];
-[PLSubmissionConfig ckTagConfig];
-[PLSubmissionConfig conditionCheckForAppIntents];
-[PLSubmissionConfig conditionCheckForEnergy];
-[PLSubmissionConfig conditionCheckForTaskingType:];
-[PLSubmissionConfig configDateApplied];
-[PLSubmissionConfig configDateReceived];
-[PLSubmissionConfig configUUID];
-[PLSubmissionConfig defaultTaskingTypeParameters];
-[PLSubmissionConfig dice];
-[PLSubmissionConfig emitTaskingTypeSpecifiedEvent];
-[PLSubmissionConfig emitTrialsTaskingDecisionEvent:enrolledTrials:appliedPercentage:];
-[PLSubmissionConfig enableDPUpload];
-[PLSubmissionConfig enrolledTrialNamespaces];
-[PLSubmissionConfig getDateMarker];
-[PLSubmissionConfig getDateMarkerLegacy];
-[PLSubmissionConfig getSubmitReasonTypeToCAFieldValue];
-[PLSubmissionConfig getSubmitReasonTypeToDefaultsKey];
-[PLSubmissionConfig getSubmitReasonTypeToFlushReason];
-[PLSubmissionConfig getSubmitReasonTypeToReasonLog];
-[PLSubmissionConfig getSubmitReasonTypeToStorageEventOTAType];
-[PLSubmissionConfig hashEntries];
-[PLSubmissionConfig initTagInfoForReasonType:withStartDate:withEndDate:];
-[PLSubmissionConfig initWithReasonType:];
-[PLSubmissionConfig initWithReasonType:DRConfig:];
-[PLSubmissionConfig initializeFilesToBeSubmitted];
-[PLSubmissionConfig isDRTasking];
-[PLSubmissionConfig isValidSubmissionFilesMask];
-[PLSubmissionConfig isValidTaskingBlob];
-[PLSubmissionConfig lastBatteryTimestampSystem];
-[PLSubmissionConfig lookupTableGroup:];
-[PLSubmissionConfig mssCycleInterval];
-[PLSubmissionConfig ondemand];
-[PLSubmissionConfig perModelTaskingTypeParameters];
-[PLSubmissionConfig perModelTrialsPercentages];
-[PLSubmissionConfig ppsTaskingTables];
-[PLSubmissionConfig readTaskingDefaults];
-[PLSubmissionConfig readTaskingPayloadOverride:];
-[PLSubmissionConfig removeEntries];
-[PLSubmissionConfig resolveTaskingTables];
-[PLSubmissionConfig setBlobFailureReason:];
-[PLSubmissionConfig setCapSize:];
-[PLSubmissionConfig setConfigDateApplied:];
-[PLSubmissionConfig setConfigDateReceived:];
-[PLSubmissionConfig setConfigUUID:];
-[PLSubmissionConfig setDefaultTaskingTypeParameters:];
-[PLSubmissionConfig setDice:];
-[PLSubmissionConfig setEnableDPUpload:];
-[PLSubmissionConfig setEnrolledTrialNamespaces:];
-[PLSubmissionConfig setLastBatteryTimestampSystem:];
-[PLSubmissionConfig setMssCycleInterval:];
-[PLSubmissionConfig setOndemand:];
-[PLSubmissionConfig setPerModelTaskingTypeParameters:];
-[PLSubmissionConfig setPerModelTrialsPercentages:];
-[PLSubmissionConfig setPlTaskingTables:];
-[PLSubmissionConfig setPpsTaskingTables:];
-[PLSubmissionConfig setRemoveEntries:];
-[PLSubmissionConfig setSignpostAllowlist:];
-[PLSubmissionConfig setSignpostDisable:];
-[PLSubmissionConfig setSubmitReasonType:];
-[PLSubmissionConfig setSubmittedFilesMask:];
-[PLSubmissionConfig setTagUUID:];
-[PLSubmissionConfig setTaskingBaselinePercentage:];
-[PLSubmissionConfig setTaskingBuild:];
-[PLSubmissionConfig setTaskingDeviceModels:];
-[PLSubmissionConfig setTaskingFiles:];
-[PLSubmissionConfig setTaskingPercentage:];
-[PLSubmissionConfig setTaskingPopulation:];
-[PLSubmissionConfig setTaskingTableGroups:];
-[PLSubmissionConfig setTaskingTrials:];
-[PLSubmissionConfig setTaskingTrialsPercentage:];
-[PLSubmissionConfig setTrimmingQueries:];
-[PLSubmissionConfig shouldStartTaskingToday];
-[PLSubmissionConfig shouldStartTrialsTaskingToday:];
-[PLSubmissionConfig shouldSubmitToday];
-[PLSubmissionConfig signpostAllowlist];
-[PLSubmissionConfig splitBySubmissionType];
-[PLSubmissionConfig submissionCategory];
-[PLSubmissionConfig submissionMaskToString];
-[PLSubmissionConfig submitBDC];
-[PLSubmissionConfig submitBG];
-[PLSubmissionConfig submitCE];
-[PLSubmissionConfig submitFileStatsToAnalytics];
-[PLSubmissionConfig submitMSS];
-[PLSubmissionConfig submitPLL];
-[PLSubmissionConfig submitPLLUpgrade];
-[PLSubmissionConfig submitReasonType];
-[PLSubmissionConfig submitSP];
-[PLSubmissionConfig submitXC];
-[PLSubmissionConfig submittedFilesMask];
-[PLSubmissionConfig taskingBaselinePercentage];
-[PLSubmissionConfig taskingBuild];
-[PLSubmissionConfig taskingDeviceModels];
-[PLSubmissionConfig taskingFiles];
-[PLSubmissionConfig taskingPercentage];
-[PLSubmissionConfig taskingPopulation];
-[PLSubmissionConfig taskingTableGroups];
-[PLSubmissionConfig taskingTrials];
-[PLSubmissionConfig taskingTrialsPercentage];
-[PLSubmissionConfig taskingType];
```
