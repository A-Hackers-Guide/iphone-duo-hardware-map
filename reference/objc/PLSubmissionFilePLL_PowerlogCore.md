# `PLSubmissionFilePLL`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLSubmissionFile`
- 1 instance variables, 1 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _isEnergyTasking;
```

## Properties

```
@property (TB,V_isEnergyTasking) isEnergyTasking;
```

## Instance methods

```
-[PLSubmissionFilePLL fileExtension];
-[PLSubmissionFilePLL initWithConfig:];
-[PLSubmissionFilePLL flush];
-[PLSubmissionFilePLL submit];
-[PLSubmissionFilePLL fileType];
-[PLSubmissionFilePLL emitFileExists:];
-[PLSubmissionFilePLL emitCopyResult:];
-[PLSubmissionFilePLL isEnergyTasking];
-[PLSubmissionFilePLL baseCADictionary];
-[PLSubmissionFilePLL copyAndPrepareLog];
-[PLSubmissionFilePLL copyArchiveAtPath:to:];
-[PLSubmissionFilePLL copyLastArchiveToPath:];
-[PLSubmissionFilePLL copyPowerlogToPath:];
-[PLSubmissionFilePLL copyUpgradePowerlogToPath:];
-[PLSubmissionFilePLL declaredRetentionIsExactly24HoursForLegacyEntryKeyConfig:];
-[PLSubmissionFilePLL declaredRetentionIsExactly24HoursForTimeToLiveInDays:];
-[PLSubmissionFilePLL emitDecompressionResult:];
-[PLSubmissionFilePLL emitPreparationResult:];
-[PLSubmissionFilePLL generateSubmissionTagForCurrentLog];
-[PLSubmissionFilePLL logSubmissionSizeToAnalytics:withUncompressedSize:];
-[PLSubmissionFilePLL prepareDatabaseAtPath:];
-[PLSubmissionFilePLL setIsEnergyTasking:];
-[PLSubmissionFilePLL tableHas24HourRetention:];
-[PLSubmissionFilePLL trialsTaskingTrimFiltersForTables:beforeDate:];
-[PLSubmissionFilePLL updateSubmissionTagWithConnection:];
```
