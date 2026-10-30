# `CMHistoricalDataStore`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 30 instance methods, 0 class methods

## Instance variables

```
^{sqlite3=} fDb;
@"CMHistoricalFetchToken" fToken;
@"NSObject<OS_dispatch_queue>" fInternalQueue;
{unique_ptr<CLConnectionClient, std::default_delete<CLConnectionClient>>=""{?="__ptr_"^{CLConnectionClient}}} fLocationdConnection;
@"NSDictionary" fConfiguration;
```

## Instance methods

```
-[CMHistoricalDataStore init];
-[CMHistoricalDataStore dealloc];
-[CMHistoricalDataStore _setConfiguration:];
-[CMHistoricalDataStore resetToken];
-[CMHistoricalDataStore _cacheTableNamesForToken:];
-[CMHistoricalDataStore cacheAllRecordIds];
-[CMHistoricalDataStore cardioTableNames];
-[CMHistoricalDataStore closeDBConnection];
-[CMHistoricalDataStore coldDBPath];
-[CMHistoricalDataStore fetchCardioSamplesFrom:to:queryToken:withHandler:];
-[CMHistoricalDataStore fetchMobilitySamplesFrom:to:queryToken:withHandler:];
-[CMHistoricalDataStore getFirstRecordIdForTable:];
-[CMHistoricalDataStore getLastRecordIdForTable:];
-[CMHistoricalDataStore getPageSize];
-[CMHistoricalDataStore getRecordIdForTable:ascending:];
-[CMHistoricalDataStore initializeWithToken:type:start:end:];
-[CMHistoricalDataStore isDbOpenAndValid];
-[CMHistoricalDataStore markCursorDone];
-[CMHistoricalDataStore mobilityTableNames];
-[CMHistoricalDataStore nextHistoricalFetchWithCount:withHandler:];
-[CMHistoricalDataStore parseCardioTypeFromSql:datatype:];
-[CMHistoricalDataStore parseMobilityTypeFromSql:dataype:];
-[CMHistoricalDataStore populateArray:fromSql:query:];
-[CMHistoricalDataStore queryConfigurationFromDaemon];
-[CMHistoricalDataStore tableNameForCardioType:];
-[CMHistoricalDataStore tableNameForCurrentType:];
-[CMHistoricalDataStore tableNameForMobilityType:];
-[CMHistoricalDataStore tableNameFromToken];
-[CMHistoricalDataStore tableNames];
-[CMHistoricalDataStore tokenSanityChecks];
```
