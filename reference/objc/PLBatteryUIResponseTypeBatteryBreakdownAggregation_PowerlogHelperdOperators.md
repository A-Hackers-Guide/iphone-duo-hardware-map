# `PLBatteryUIResponseTypeBatteryBreakdownAggregation`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLBatteryUIResponseTypeBatteryBreakdown`
- 6 instance variables, 6 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _backgroundLocationBreakdown;
@"NSMutableDictionary" _backgroundLocationPluggedInBreakdown;
@"NSMutableDictionary" _backgroundAudioBreakdown;
@"NSMutableDictionary" _backgroundAudioPluggedInBreakdown;
@"NSMutableDictionary" _backgroundLocationAudioBreakdown;
@"NSMutableDictionary" _backgroundLocationAudioPluggedInBreakdown;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_backgroundLocationBreakdown) backgroundLocationBreakdown;
@property (T@"NSMutableDictionary",&,V_backgroundLocationPluggedInBreakdown) backgroundLocationPluggedInBreakdown;
@property (T@"NSMutableDictionary",&,V_backgroundAudioBreakdown) backgroundAudioBreakdown;
@property (T@"NSMutableDictionary",&,V_backgroundAudioPluggedInBreakdown) backgroundAudioPluggedInBreakdown;
@property (T@"NSMutableDictionary",&,V_backgroundLocationAudioBreakdown) backgroundLocationAudioBreakdown;
@property (T@"NSMutableDictionary",&,V_backgroundLocationAudioPluggedInBreakdown) backgroundLocationAudioPluggedInBreakdown;
```

## Instance methods

```
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation adjustRuntimes:];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation initBackgroundLocationAudioTime];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation setBackgroundLocationBreakdown:];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation addFgEnergyForMetrics:qualificationID:rootNodeQualificationEnergy:energyEntry:];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation addRNEForMetrics:rootNodeEnergy:energyEntry:];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation backgroundAudioBreakdown];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation backgroundAudioPluggedInBreakdown];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation backgroundLocationAudioBreakdown];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation backgroundLocationAudioPluggedInBreakdown];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation backgroundLocationBreakdown];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation backgroundLocationPluggedInBreakdown];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation bgLocationAudioTimeApps:];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation bgLocationAudioTimeRuntimes:bundleID:];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation filterEnergyEntries:];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation filterEnergyEntriesWithRuntimes:];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation filterFgBg:filterArray:];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation generateRange:withDataRange:];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation isForegroundOnlyBucket:];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation populateBackgroundLocationAudioTime:bundleID:];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation populateEnergyBucketKeysWithEntries:];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation setBackgroundAudioBreakdown:];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation setBackgroundAudioPluggedInBreakdown:];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation setBackgroundLocationAudioBreakdown:];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation setBackgroundLocationAudioPluggedInBreakdown:];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation setBackgroundLocationPluggedInBreakdown:];
-[PLBatteryUIResponseTypeBatteryBreakdownAggregation shouldShowBreakdown:];
```
