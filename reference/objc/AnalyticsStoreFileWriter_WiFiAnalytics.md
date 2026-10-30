# `AnalyticsStoreFileWriter`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 23 instance methods, 3 class methods

## Instance variables

```
@"NSDateFormatter" _dateFormatter;
@"WAPersistentContainer" _persistentContainer;
```

## Properties

```
@property (T@"WAPersistentContainer",&,N,V_persistentContainer) persistentContainer;
```

## Class methods

```
+[AnalyticsStoreFileWriter writeData:toFile:];
+[AnalyticsStoreFileWriter analyticsStoreFileWriterDirectory];
+[AnalyticsStoreFileWriter writeObj:toJSONFile:];
```

## Instance methods

```
-[AnalyticsStoreFileWriter moc];
-[AnalyticsStoreFileWriter setPersistentContainer:];
-[AnalyticsStoreFileWriter persistentContainer];
-[AnalyticsStoreFileWriter initWithPersistentContainer:];
-[AnalyticsStoreFileWriter mom];
-[AnalyticsStoreFileWriter analyticsStoreFileWriterFilePath];
-[AnalyticsStoreFileWriter batchedWriteAnalyticsStoreToCSVFilesWithBatchSize:maxAge:];
-[AnalyticsStoreFileWriter batchedWriteAnalyticsStoreToFile:maxAge:];
-[AnalyticsStoreFileWriter batchedWriteAnalyticsStoreToFileWithBatchSize:maxAge:];
-[AnalyticsStoreFileWriter exportEntityToCSV:batchSize:maxAge:toURL:fileDate:];
-[AnalyticsStoreFileWriter initDateFormatter];
-[AnalyticsStoreFileWriter relationshipKeyPathsForPrefetching:];
-[AnalyticsStoreFileWriter stringifyManagedObjectsArray:titleString:dataStringsArray:onMoc:];
-[AnalyticsStoreFileWriter stringifyObjectWithPadding:padding:padToLength:];
-[AnalyticsStoreFileWriter stringifyRelationship:name:onMoc:];
-[AnalyticsStoreFileWriter stringifyValueArray:];
-[AnalyticsStoreFileWriter writeAnalyticsStoreToFile];
-[AnalyticsStoreFileWriter writeArrayToJSONFile:];
-[AnalyticsStoreFileWriter writeAttributes:fromObject:ofEntity:withWriter:];
-[AnalyticsStoreFileWriter writeDeploymentGraphToFile];
-[AnalyticsStoreFileWriter writeDictionaryToJSONFile:network:];
-[AnalyticsStoreFileWriter writeRelationships:fromObject:ofEntity:with:];
-[AnalyticsStoreFileWriter writeRelationshipsHeaders:ofEntity:with:];
```
