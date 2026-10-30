# `PLArchiveEntry`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLEntry`
- 2 instance variables, 17 properties, 27 instance methods, 3 class methods

## Instance variables

```
B _systemTimeOffsetModified;
@"NSString" _crPath;
```

## Properties

```
@property (T@"NSString",R,N) path;
@property (T@"NSString",R,N) compressedPath;
@property (T@"NSString",R,N,V_crPath) crPath;
@property (T@"NSString",R,N) name;
@property (T@"NSDate",R) startDate;
@property (T@"NSDate",R) endDate;
@property (T@"NSString",R) uuid;
@property (Td,N) systemTimeOffset;
@property (TB,R,V_systemTimeOffsetModified) systemTimeOffsetModified;
@property (TB,R) fullMode;
@property (Tq,N) stage;
@property (TQ,N) numAttempts;
@property (T@"NSDate",&,N) syncedOffDate;
@property (T@"NSDate",&,N) removedDate;
@property (Tq,N) mainDBSizeAtStart;
@property (TB,R,N) syncedOff;
@property (TB,R,N) removed;
```

## Class methods

```
+[PLArchiveEntry load];
+[PLArchiveEntry storageQueue];
+[PLArchiveEntry entryKey];
```

## Instance methods

```
-[PLArchiveEntry startDate];
-[PLArchiveEntry uuid];
-[PLArchiveEntry stage];
-[PLArchiveEntry endDate];
-[PLArchiveEntry initEntryWithRawData:];
-[PLArchiveEntry fullMode];
-[PLArchiveEntry setStage:];
-[PLArchiveEntry log];
-[PLArchiveEntry name];
-[PLArchiveEntry path];
-[PLArchiveEntry initWithMetadata:];
-[PLArchiveEntry removed];
-[PLArchiveEntry setNumAttempts:];
-[PLArchiveEntry numAttempts];
-[PLArchiveEntry setRemovedDate:];
-[PLArchiveEntry compressedPath];
-[PLArchiveEntry crPath];
-[PLArchiveEntry initWithStartDate:endDate:andUUID:];
-[PLArchiveEntry mainDBSizeAtStart];
-[PLArchiveEntry removedDate];
-[PLArchiveEntry setMainDBSizeAtStart:];
-[PLArchiveEntry setSyncedOffDate:];
-[PLArchiveEntry setSystemTimeOffset:];
-[PLArchiveEntry syncedOff];
-[PLArchiveEntry syncedOffDate];
-[PLArchiveEntry systemTimeOffset];
-[PLArchiveEntry systemTimeOffsetModified];
```
