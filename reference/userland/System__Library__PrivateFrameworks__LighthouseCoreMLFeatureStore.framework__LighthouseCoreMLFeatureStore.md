# `/System/Library/PrivateFrameworks/LighthouseCoreMLFeatureStore.framework/LighthouseCoreMLFeatureStore`

iOS 27.2 dyld shared cache image. Version `3.0.0.0.0`. **[DSC]**

## Linked libraries (9)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/Frameworks/CoreML.framework/CoreML`
- `/System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics`
- `/usr/lib/libsqlite3.dylib`

## Objective-C: 24 classes, 2 protocols, 181 methods, 94 properties

### Class pages

Every class and protocol, with its methods: [`LCFBiomeManager`](../objc/LCFBiomeManager_LighthouseCoreMLFeatureStore.md), [`LCFCoreMLBatchProvider`](../objc/LCFCoreMLBatchProvider_LighthouseCoreMLFeatureStore.md), [`LCFCoreMLFeatureProvider`](../objc/LCFCoreMLFeatureProvider_LighthouseCoreMLFeatureStore.md), [`LCFCoreMLFeatureProviderUtils`](../objc/LCFCoreMLFeatureProviderUtils_LighthouseCoreMLFeatureStore.md), [`LCFDatabaseColumn`](../objc/LCFDatabaseColumn_LighthouseCoreMLFeatureStore.md), [`LCFDatabaseColumnConnection`](../objc/LCFDatabaseColumnConnection_LighthouseCoreMLFeatureStore.md), [`LCFDatabaseConnection`](../objc/LCFDatabaseConnection_LighthouseCoreMLFeatureStore.md), [`LCFELBatchProviderInfo`](../objc/LCFELBatchProviderInfo_LighthouseCoreMLFeatureStore.md), [`LCFELChangePointDetectionEvent`](../objc/LCFELChangePointDetectionEvent_LighthouseCoreMLFeatureStore.md), [`LCFELChangepointDetectionAnalysisResult`](../objc/LCFELChangepointDetectionAnalysisResult_LighthouseCoreMLFeatureStore.md), [`LCFELCoreAnalyticsHandler`](../objc/LCFELCoreAnalyticsHandler_LighthouseCoreMLFeatureStore.md), [`LCFELEventLogging`](../objc/LCFELEventLogging_LighthouseCoreMLFeatureStore.md), [`LCFELFeatureImportanceAnalysisResult`](../objc/LCFELFeatureImportanceAnalysisResult_LighthouseCoreMLFeatureStore.md), [`LCFELFeatureImportanceEvent`](../objc/LCFELFeatureImportanceEvent_LighthouseCoreMLFeatureStore.md), [`LCFELFeatureValueStatistic`](../objc/LCFELFeatureValueStatistic_LighthouseCoreMLFeatureStore.md), [`LCFELModelTrainingEvent`](../objc/LCFELModelTrainingEvent_LighthouseCoreMLFeatureStore.md), [`LCFELShadowEvaluationEvent`](../objc/LCFELShadowEvaluationEvent_LighthouseCoreMLFeatureStore.md), [`LCFELShadowEvaluationPrediction`](../objc/LCFELShadowEvaluationPrediction_LighthouseCoreMLFeatureStore.md), [`LCFFeatureConverter`](../objc/LCFFeatureConverter_LighthouseCoreMLFeatureStore.md), [`LCFFeatureSet`](../objc/LCFFeatureSet_LighthouseCoreMLFeatureStore.md), [`LCFFeatureStore`](../objc/LCFFeatureStore_LighthouseCoreMLFeatureStore.md), [`LCFFeatureStoreContextId`](../objc/LCFFeatureStoreContextId_LighthouseCoreMLFeatureStore.md), [`LCFFeatureValue`](../objc/LCFFeatureValue_LighthouseCoreMLFeatureStore.md), [`LCFFetureValueNameType`](../objc/LCFFetureValueNameType_LighthouseCoreMLFeatureStore.md), [`MLBatchProvider`](../objc/MLBatchProvider_LighthouseCoreMLFeatureStore.protocol.md), [`MLFeatureProvider`](../objc/MLFeatureProvider_LighthouseCoreMLFeatureStore.protocol.md)

### Classes

`LCFBiomeManager`, `LCFCoreMLBatchProvider`, `LCFCoreMLFeatureProvider`, `LCFCoreMLFeatureProviderUtils`, `LCFDatabaseColumn`, `LCFDatabaseColumnConnection`, `LCFDatabaseConnection`, `LCFELBatchProviderInfo`, `LCFELChangePointDetectionEvent`, `LCFELChangepointDetectionAnalysisResult`, `LCFELCoreAnalyticsHandler`, `LCFELEventLogging`, `LCFELFeatureImportanceAnalysisResult`, `LCFELFeatureImportanceEvent`, `LCFELFeatureValueStatistic`, `LCFELModelTrainingEvent`, `LCFELShadowEvaluationEvent`, `LCFELShadowEvaluationPrediction`, `LCFFeatureConverter`, `LCFFeatureSet`, `LCFFeatureStore`, `LCFFeatureStoreContextId`, `LCFFeatureValue`, `LCFFetureValueNameType`

### Protocols

`MLBatchProvider`, `MLFeatureProvider`

### Properties

```
@property (Tq,R,N) count;
@property (T@"NSSet",R,N) featureNames;
@property (T@"BMStream",R,N,V_biomeStream) biomeStream;
@property (T@"BMSource",&,N,V_biomeSource) biomeSource;
@property (T@"NSString",R,N,V_featureStoreKey) featureStoreKey;
@property (T@"NSDate",R,N,V_timeFirst) timeFirst;
@property (T@"NSDate",R,N,V_timeLast) timeLast;
@property (Tq,R,N,V_count) count;
@property (T@"NSArray",R,N,V_featureProviders) featureProviders;
@property (T@"NSString",R,N,V_featureStoreKey) featureStoreKey;
@property (T@"NSDate",R,N,V_timestamp) timestamp;
@property (T@"NSDictionary",R,N,V_featureValues) featureValues;
@property (T@"NSSet",R,N,V_featureNames) featureNames;
@property (T@"NSString",R,N,V_name) name;
@property (T@"NSString",R,N,V_typeDb) typeDb;
@property (Tq,R,N,V_type) type;
@property (T@"NSURL",R,N,V_databaseBaseURL) databaseBaseURL;
@property (T@"NSString",R,N,V_databaseName) databaseName;
@property (T@"NSString",R,N,V_databaseNamePath) databaseNamePath;
@property (T@"NSString",R,N,V_tableName) tableName;
@property (T@"NSArray",&,N,V_nameTypesCache) nameTypesCache;
@property (T@"NSURL",R,N,V_databaseBaseURL) databaseBaseURL;
@property (T@"NSString",R,N,V_databaseName) databaseName;
@property (T@"NSString",R,N,V_databaseNamePath) databaseNamePath;
@property (T@"NSString",R,N,V_tableName) tableName;
@property (T@"LCFDatabaseColumnConnection",R,N,V_dbColumnConnection) dbColumnConnection;
@property (T@"NSUUID",R,N,V_contextId) contextId;
@property (T@"NSUUID",R,N,V_eventId) eventId;
@property (T@"NSString",R,N,V_featureStoreKey) featureStoreKey;
@property (T@"NSNumber",R,N,V_timeRange) timeRange;
@property (T@"NSNumber",R,N,V_featureCount) featureCount;
@property (T@"NSDictionary",R,N,V_totalFeatureStatistics) totalFeatureStatistics;
@property (T@"NSArray",R,N,V_positiveFeatureStatistics) positiveFeatureStatistics;
@property (T@"NSArray",R,N,V_negativeFeatureStatistics) negativeFeatureStatistics;
@property (T@"NSUUID",R,N,V_contextId) contextId;
@property (T@"NSUUID",R,N,V_eventId) eventId;
@property (T@"LCFELBatchProviderInfo",R,N,V_inputBachProviderInfo) inputBachProviderInfo;
@property (T@"NSArray",R,N,V_results) results;
@property (T@"NSNumber",R,N,V_succeeded) succeeded;
@property (T@"NSError",R,N,V_analysisError) analysisError;
@property (T@"NSString",R,N,V_featureName) featureName;
@property (T@"NSNumber",R,N,V_featureCount) featureCount;
@property (T@"NSNumber",R,N,V_detectedChangePointCount) detectedChangePointCount;
@property (T@"NSArray",R,N,V_changepointTimestamps) changepointTimestamps;
@property (T@"NSString",R,N,V_featureName) featureName;
@property (T@"NSNumber",R,N,V_featureCount) featureCount;
@property (T@"NSNumber",R,N,V_correlationCoefficient) correlationCoefficient;
@property (T@"NSNumber",R,N,V_featureImportance) featureImportance;
@property (T@"NSUUID",R,N,V_contextId) contextId;
@property (T@"NSUUID",R,N,V_eventId) eventId;
@property (T@"LCFELBatchProviderInfo",R,N,V_inputBachProviderInfo) inputBachProviderInfo;
@property (T@"NSString",R,N,V_targetLabelFeatureName) targetLabelFeatureName;
@property (T@"NSArray",R,N,V_results) results;
@property (T@"NSNumber",R,N,V_succeeded) succeeded;
@property (T@"NSError",R,N,V_analysisError) analysisError;
@property (T@"NSString",R,N,V_featureName) featureName;
@property (T@"NSNumber",R,N,V_count) count;
@property (T@"NSNumber",R,N,V_mean) mean;
@property (T@"NSNumber",R,N,V_stddev) stddev;
@property (T@"NSUUID",R,N,V_contextId) contextId;
@property (T@"NSUUID",R,N,V_eventId) eventId;
@property (T@"NSString",R,N,V_modelName) modelName;
@property (T@"LCFELBatchProviderInfo",R,N,V_bachProviderInfo) bachProviderInfo;
@property (T@"NSNumber",R,N,V_succeeded) succeeded;
@property (T@"NSError",R,N,V_trainingError) trainingError;
@property (T@"NSUUID",R,N,V_contextId) contextId;
@property (T@"NSUUID",R,N,V_eventId) eventId;
@property (T@"NSString",R,N,V_modelName) modelName;
@property (T@"LCFELBatchProviderInfo",R,N,V_inputBachProviderInfo) inputBachProviderInfo;
@property (T@"NSArray",R,N,V_evaluatedPredictions) evaluatedPredictions;
@property (T@"NSNumber",R,N,V_accuracy) accuracy;
@property (T@"NSNumber",R,N,V_succeeded) succeeded;
@property (T@"NSError",R,N,V_evaluationError) evaluationError;
@property (T@"NSDate",R,N,V_timestampOfInputFeatureSet) timestampOfInputFeatureSet;
@property (T@"NSNumber",R,N,V_predictedClass) predictedClass;
@property (T@"NSNumber",R,N,V_probability) probability;
@property (T@"NSString",R,N,V_itemIdentifier) itemIdentifier;
@property (T@"NSNumber",R,N,V_featureVersion) featureVersion;
@property (T@"NSDate",R,N,V_timestamp) timestamp;
@property (T@"NSDictionary",R,N,V_featureValues) featureValues;
@property (T@"LCFBiomeManager",R,N,V_biomeManagerLabeledDataStore) biomeManagerLabeledDataStore;
@property (T@"LCFDatabaseConnection",R,N,V_dbFeatureStore) dbFeatureStore;
@property (TB,R,N,V_useSqlite) useSqlite;
@property (T@"NSString",R,N,V_featureStoreKey) featureStoreKey;
@property (Tq,R,N,V_type) type;
@property (T@"NSString",R,N) valueInString;
@property (T@"NSNumber",R,N,V_intValue) intValue;
@property (T@"NSNumber",R,N,V_doubleValue) doubleValue;
@property (T@"NSString",R,N,V_stringValue) stringValue;
@property (T@"NSNumber",R,N,V_boolValue) boolValue;
@property (T@"NSNumber",R,N,V_timeBucketValue) timeBucketValue;
@property (T@"NSArray",R,N,V_doubleArray) doubleArray;
@property (T@"NSString",R,N,V_featureName) featureName;
@property (Tq,R,N,V_featureValueType) featureValueType;
```

## Strings (97)

```
featureStat_mean
featureStat_stddev
correlationCoefficient
com.apple.LighthouseCoreMLFoundations.LCFELChangePointDetectionEvent
FLOAT
BEGIN
sampleType
featureStore
INTEGER
v16@?0^v8
-[LCFDatabaseConnection doQueryEachStep:statementStepHandler:]
classProbability
_configurationInfo
CREATE TABLE IF NOT EXISTS %@ (ID INTEGER PRIMARY KEY AUTOINCREMENT, %@ TEXT, %@ FLOAT, %@ FLOAT)
%@ order by %@ desc
com.apple.LighthouseCoreMLFoundations.LCFELFeatureValueStatistic
accuracy
featureImportance
changePoints_count
SELECT * FROM %@
v16@?0@\"BPSCompletion\"8
modelName
com.apple.LighthouseCoreMLFoundations.LCFELShadowEvaluationEvent
FeatureStore
false
INSERT INTO %@ (ColumnName, Type) VALUES('%@', %@)
featureValueStatisticId
usageType
_isPositiveLabeled
LCFDatabaseConnection.m
changePoints
_labelingEvidence
_sharingEventUID
_lcf_featureVersion
targetLabelFeatureName
featureCount
featureName
succeeded
errorDomain
'%@'
BOOL
BiomeManager
i
TEXT
DatabaseColumnConnection
_lcf_timestamp
_labelingPolicyVersion
COMMIT
pragma table_info(%@)
v16@?0^{sqlite3_stmt=}8
errorCodeEnum
com.apple.LighthouseCoreMLFeatureStore
alter table %@ ADD COLUMN %@ %@;
%@ %@ >= %@ 
%@ order by %@ asc
ID
null
faetureStoreKey
v8@?0
v24@?0r^v8q16
INSERT INTO %@ (%@) VALUES(%@)
,
com.apple.LighthouseCoreMLFoundations.LCFELModelTrainingEvent
SELECT %@ FROM %@
CREATE TABLE IF NOT EXISTS %@ (ID INTEGER PRIMARY KEY AUTOINCREMENT, ColumnName TEXT, Type INTEGER)
v16@?0@\"BMStoreEvent\"8
_lcf_itemIdentifier
%@ where 
%@ %@ <= %@ 
DELETE FROM %@
LCFDatabaseColumnConnection.m
eventId
timeRange
com.apple.LighthouseCoreMLFoundations.LCFELFeatureImportanceEvent
%@ and 
SELECT * FROM %@ limit 10
featureStat_count
DatabaseConnection
_Columns
-[LCFDatabaseColumnConnection doQueryEachStep:statementStepHandler:]
contextId
q
%@
normalizedName (%@) could not construct a featurevalue
Wrong feature value type is assigned featureName:%@ columnInDb.type:%ld featureValueType: %ld
database %@
_biomeSource already exists.
prune is called on biome stream mode.
sqlite3_open succeeded %@
Wrong type is asked %@ %ld %ld
Completed.
could not find all needed features.
sqlite3_open failed %@
featureProvider could not be construcd
sqlite3_exec failed %@
sqlite3_exec no column found - %@ 
Reading Biome events from %f to %f.
```
