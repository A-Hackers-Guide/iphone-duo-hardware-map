# `PLStorageOperator`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLOperator`
- 0 instance variables, 0 properties, 14 instance methods, 20 class methods

## Class methods

```
+[PLStorageOperator entryEventIntervalDefinitions];
+[PLStorageOperator entryEventPointDefinitions];
+[PLStorageOperator entryEventForwardDefinitions];
+[PLStorageOperator entryEventNoneDefinitions];
+[PLStorageOperator entryEventPointDefinitionTimeCorrection];
+[PLStorageOperator eventIntervalCacheSizeWithPayload:withEntryDate:];
+[PLStorageOperator entryEventNoneDefinitionAdditionalTablesTurnedOn];
+[PLStorageOperator entryEventPointDefinitionArchive];
+[PLStorageOperator entryEventForwardDefinitionConfiguration];
+[PLStorageOperator entryEventForwardDefinitionActivityStates];
+[PLStorageOperator entryEventForwardDefinitionSubmissionTag];
+[PLStorageOperator eventPointCacheFlushWithPayload:];
+[PLStorageOperator entryEventNoneDefinitionActivity];
+[PLStorageOperator entryEventPointDefinitionPLLog];
+[PLStorageOperator entryEventForwardDefinitionSchemaChange];
+[PLStorageOperator entryEventForwardDefinitionTimeOffset];
+[PLStorageOperator entryEventForwardDefinitionTaskingMode];
+[PLStorageOperator entryEventPointDefinitionOTA];
+[PLStorageOperator entryEventIntervalDefinitionCacheSize];
+[PLStorageOperator entryEventPointDefinitionCacheFlush];
```

## Instance methods

```
-[PLStorageOperator initOperatorDependancies];
-[PLStorageOperator log];
-[PLStorageOperator trimConditionsForEntryKey:forTrimDate:];
-[PLStorageOperator logEventForwardConfiguration:];
-[PLStorageOperator logEventForwardSchemaChange:];
-[PLStorageOperator logEventForwardTaskingMode:];
-[PLStorageOperator logEventForwardTimeOffset:];
-[PLStorageOperator logEventNoneAdditionalTablesTurnedOn:];
-[PLStorageOperator logEventPointArchive:];
-[PLStorageOperator logEventPointCacheFlush:];
-[PLStorageOperator logEventPointOTA:];
-[PLStorageOperator logEventPointPLLog:];
-[PLStorageOperator logEventPointPreUnlock:];
-[PLStorageOperator logEventPointTimeCorrection:];
```
