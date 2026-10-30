# `LCFDatabaseColumnConnection`

- Image: [`/System/Library/PrivateFrameworks/LighthouseCoreMLFeatureStore.framework/LighthouseCoreMLFeatureStore`](../userland/System__Library__PrivateFrameworks__LighthouseCoreMLFeatureStore.framework__LighthouseCoreMLFeatureStore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSURL" _databaseBaseURL;
@"NSString" _databaseName;
@"NSString" _databaseNamePath;
@"NSString" _tableName;
@"NSArray" _nameTypesCache;
```

## Properties

```
@property (T@"NSURL",R,N,V_databaseBaseURL) databaseBaseURL;
@property (T@"NSString",R,N,V_databaseName) databaseName;
@property (T@"NSString",R,N,V_databaseNamePath) databaseNamePath;
@property (T@"NSString",R,N,V_tableName) tableName;
@property (T@"NSArray",&,N,V_nameTypesCache) nameTypesCache;
```

## Instance methods

```
-[LCFDatabaseColumnConnection databaseName];
-[LCFDatabaseColumnConnection query];
-[LCFDatabaseColumnConnection tableName];
-[LCFDatabaseColumnConnection databaseBaseURL];
-[LCFDatabaseColumnConnection writeFeatures:featureValueType:];
-[LCFDatabaseColumnConnection databaseNamePath];
-[LCFDatabaseColumnConnection doQueryEachStep:statementStepHandler:];
-[LCFDatabaseColumnConnection doQueryExec:];
-[LCFDatabaseColumnConnection dumpDatabase];
-[LCFDatabaseColumnConnection ensureDatabaseTable];
-[LCFDatabaseColumnConnection init:databaseName:tableName:];
-[LCFDatabaseColumnConnection nameTypesCache];
-[LCFDatabaseColumnConnection setNameTypesCache:];
```
