# `PLEntry`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 9 instance variables, 19 properties, 66 instance methods, 9 class methods

## Instance variables

```
B _existsInDB;
B _isErrorEntry;
B _writeToDB;
@"NSMutableDictionary" _dictionary;
@"NSDictionary" _entryDefinition;
@"NSDate" _entryDate;
@"NSString" _entryKey;
q _entryID;
@"NSObject<OS_dispatch_semaphore>" _sem;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_dictionary) dictionary;
@property (T@"NSObject<OS_dispatch_semaphore>",&,N,V_sem) sem;
@property (T@"NSMutableArray",R) keys;
@property (T@"NSMutableArray",R,GallValues) values;
@property (TB,R) hasDynamicKeys;
@property (TB,R) hasArrayKeys;
@property (TB,R) hasDMAKeys;
@property (T@"NSArray",R) definedKeys;
@property (T@"NSArray",R) dynamicKeys;
@property (T@"NSArray",R) arrayKeys;
@property (T@"NSArray",R) DMAKeys;
@property (TB,V_existsInDB) existsInDB;
@property (TB,V_isErrorEntry) isErrorEntry;
@property (TB,V_writeToDB) writeToDB;
@property (T@"NSDictionary",&,N,V_entryDefinition) entryDefinition;
@property (T@"NSDate",&,N,V_entryDate) entryDate;
@property (T@"NSString",&,N,V_entryKey) entryKey;
@property (T@,R) subEntryKey;
@property (Tq,N,V_entryID) entryID;
```

## Class methods

```
+[PLEntry load];
+[PLEntry entryKey];
+[PLEntry registerEntry:];
+[PLEntry classForEntryKey:];
+[PLEntry dataFormatForMetric:auxiliaryMetrics:];
+[PLEntry entryWithEntryKey:withData:];
+[PLEntry entryWithEntryKey:withRawData:];
+[PLEntry summarizeAggregateEntries:];
+[PLEntry summarizeAggregateEntries:withPrimaryKeys:];
```

## Instance methods

```
-[PLEntry setDictionary:];
-[PLEntry debugDescription];
-[PLEntry entryKey];
-[PLEntry compare:];
-[PLEntry init];
-[PLEntry serialized];
-[PLEntry dictionary];
-[PLEntry initEntryWithRawData:];
-[PLEntry setEntryKey:];
-[PLEntry objectForKeyedSubscript:];
-[PLEntry serializedForJSON];
-[PLEntry objectForKey:];
-[PLEntry entryID];
-[PLEntry keys];
-[PLEntry allValues];
-[PLEntry entryDate];
-[PLEntry setEntryDate:];
-[PLEntry description];
-[PLEntry setObject:forKey:];
-[PLEntry filterEntryLogging];
-[PLEntry setEntryID:];
-[PLEntry removeObjectForKey:];
-[PLEntry copyWithZone:];
-[PLEntry setObject:forKeyedSubscript:];
-[PLEntry compare:options:];
-[PLEntry sem];
-[PLEntry setSem:];
-[PLEntry DMAKeys];
-[PLEntry entryDefinition];
-[PLEntry formaterForKey:];
-[PLEntry descriptionRespectingAllowlist:];
-[PLEntry loadDynamicKeys];
-[PLEntry setObjectsUsingMetricsFromData:];
-[PLEntry arrayKeys];
-[PLEntry checkOverridesEntryDateWithNowDate:];
-[PLEntry definedKeys];
-[PLEntry definitionForKey:];
-[PLEntry dynamicKeys];
-[PLEntry existsInDB];
-[PLEntry hasAppIdentifierKeys];
-[PLEntry hasArrayKeys];
-[PLEntry hasDMAKeys];
-[PLEntry hasDynamicKeys];
-[PLEntry initEntryWithData:];
-[PLEntry initWithEntryDate:];
-[PLEntry initWithEntryKey:];
-[PLEntry initWithEntryKey:withData:];
-[PLEntry initWithEntryKey:withDate:];
-[PLEntry initWithEntryKey:withDate:capacity:];
-[PLEntry initWithEntryKey:withRawData:];
-[PLEntry isErrorEntry];
-[PLEntry isKeyAggregateValue:];
-[PLEntry isKeyDynamic:];
-[PLEntry isPPSEnabled];
-[PLEntry keyValuePathForKey:];
-[PLEntry setDynamicObjectsFromRawData:];
-[PLEntry setEntryDefinition:];
-[PLEntry setExistsInDB:];
-[PLEntry setIsErrorEntry:];
-[PLEntry setObjectsFromData:];
-[PLEntry setObjectsFromRawData:];
-[PLEntry setWriteToDB:];
-[PLEntry staticArraySizeForKey:];
-[PLEntry subEntryKey];
-[PLEntry unitForKey:];
-[PLEntry writeToDB];
```
