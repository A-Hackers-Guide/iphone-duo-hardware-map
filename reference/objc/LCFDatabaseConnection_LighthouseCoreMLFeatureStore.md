# `LCFDatabaseConnection`

- Image: [`/System/Library/PrivateFrameworks/LighthouseCoreMLFeatureStore.framework/LighthouseCoreMLFeatureStore`](../userland/System__Library__PrivateFrameworks__LighthouseCoreMLFeatureStore.framework__LighthouseCoreMLFeatureStore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSURL" _databaseBaseURL;
@"NSString" _databaseName;
@"NSString" _databaseNamePath;
@"NSString" _tableName;
@"LCFDatabaseColumnConnection" _dbColumnConnection;
```

## Properties

```
@property (T@"NSURL",R,N,V_databaseBaseURL) databaseBaseURL;
@property (T@"NSString",R,N,V_databaseName) databaseName;
@property (T@"NSString",R,N,V_databaseNamePath) databaseNamePath;
@property (T@"NSString",R,N,V_tableName) tableName;
@property (T@"LCFDatabaseColumnConnection",R,N,V_dbColumnConnection) dbColumnConnection;
```

## Instance methods

```
-[LCFDatabaseConnection databaseName];
-[LCFDatabaseConnection tableName];
-[LCFDatabaseConnection addColumn:];
-[LCFDatabaseConnection getColumns];
-[LCFDatabaseConnection databaseBaseURL];
-[LCFDatabaseConnection databaseNamePath];
-[LCFDatabaseConnection dbColumnConnection];
-[LCFDatabaseConnection doQueryEachStep:statementStepHandler:];
-[LCFDatabaseConnection doQueryExec:];
-[LCFDatabaseConnection dumpDatabase];
-[LCFDatabaseConnection ensureDatabaseTable];
-[LCFDatabaseConnection init:databaseName:tableName:];
-[LCFDatabaseConnection isDoubleArray:];
-[LCFDatabaseConnection pruneFrom:endDate:];
-[LCFDatabaseConnection query:startDate:endDate:reversed:];
-[LCFDatabaseConnection writeFeatures:];
```
