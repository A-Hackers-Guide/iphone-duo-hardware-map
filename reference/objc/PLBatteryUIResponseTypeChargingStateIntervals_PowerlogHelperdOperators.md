# `PLBatteryUIResponseTypeChargingStateIntervals`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLBatteryUIResponseProtocol`
- 13 instance variables, 17 properties, 55 instance methods, 0 class methods

## Instance variables

```
B _useBattUIforEC;
B _shouldSnapInterval;
@"PLBatteryUIResponderService" _responderService;
@"NSDate" _start;
@"NSDate" _end;
d _bucketSize;
@"PLEntry" _lastBattEntry;
@"NSMutableDictionary" _chargingStateIntervalsDict;
@"NSDictionary" _resultDict;
@"NSMutableArray" _dailyChargingStateIntervalsDict;
@"NSMutableArray" _dailyLastBattEntry;
@"NSMutableArray" _resultArray;
{_PLTimeIntervalRange="location"d"length"d} _range;
```

## Properties

```
@property (T@"NSDate",&,V_start) start;
@property (T@"NSDate",&,V_end) end;
@property (T{_PLTimeIntervalRange=dd},V_range) range;
@property (T@"PLEntry",&,V_lastBattEntry) lastBattEntry;
@property (T@"NSMutableDictionary",&,V_chargingStateIntervalsDict) chargingStateIntervalsDict;
@property (T@"NSDictionary",&,V_resultDict) resultDict;
@property (TB,V_useBattUIforEC) useBattUIforEC;
@property (T@"NSMutableArray",&,V_dailyChargingStateIntervalsDict) dailyChargingStateIntervalsDict;
@property (T@"NSMutableArray",&,V_dailyLastBattEntry) dailyLastBattEntry;
@property (T@"NSMutableArray",&,V_resultArray) resultArray;
@property (TB,V_shouldSnapInterval) shouldSnapInterval;
@property (T@"PLBatteryUIResponderService",&,V_responderService) responderService;
@property (Td,V_bucketSize) bucketSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PLBatteryUIResponseTypeChargingStateIntervals configure:];
-[PLBatteryUIResponseTypeChargingStateIntervals dependencies];
-[PLBatteryUIResponseTypeChargingStateIntervals range];
-[PLBatteryUIResponseTypeChargingStateIntervals start];
-[PLBatteryUIResponseTypeChargingStateIntervals end];
-[PLBatteryUIResponseTypeChargingStateIntervals setRange:];
-[PLBatteryUIResponseTypeChargingStateIntervals coalesce];
-[PLBatteryUIResponseTypeChargingStateIntervals setEnd:];
-[PLBatteryUIResponseTypeChargingStateIntervals result];
-[PLBatteryUIResponseTypeChargingStateIntervals setStart:];
-[PLBatteryUIResponseTypeChargingStateIntervals run];
-[PLBatteryUIResponseTypeChargingStateIntervals bucketSize];
-[PLBatteryUIResponseTypeChargingStateIntervals resultArray];
-[PLBatteryUIResponseTypeChargingStateIntervals constructSlowChargingIntervals:];
-[PLBatteryUIResponseTypeChargingStateIntervals enforceGraphIntervalPrecedence:];
-[PLBatteryUIResponseTypeChargingStateIntervals dailyChargingStateIntervalsDict];
-[PLBatteryUIResponseTypeChargingStateIntervals setResultArray:];
-[PLBatteryUIResponseTypeChargingStateIntervals chargingStateIntervalsDict];
-[PLBatteryUIResponseTypeChargingStateIntervals constructIntervalTuplesFromBattEntries:lastBattEntry:startOfRange:endOfRange:];
-[PLBatteryUIResponseTypeChargingStateIntervals constructIntervalTuplesFromEntries:startOfRange:endOfRange:];
-[PLBatteryUIResponseTypeChargingStateIntervals constructIntervalTuplesFromEntries:startOfRange:endOfRange:allowOverflow:];
-[PLBatteryUIResponseTypeChargingStateIntervals dailyLastBattEntry];
-[PLBatteryUIResponseTypeChargingStateIntervals differenceBetweenSetAndIntersectingSet:intervalSetB:];
-[PLBatteryUIResponseTypeChargingStateIntervals filterIntervals:withThreshold:];
-[PLBatteryUIResponseTypeChargingStateIntervals filterThreshold:];
-[PLBatteryUIResponseTypeChargingStateIntervals getApplicableSlowChargingIntervalsGivenECIntervals:slowChargingIntervals:];
-[PLBatteryUIResponseTypeChargingStateIntervals getBattUIEntriesWithKey:inRange:];
-[PLBatteryUIResponseTypeChargingStateIntervals getChargingStateIntervals:forGraphIntervalType:];
-[PLBatteryUIResponseTypeChargingStateIntervals getChargingStateIntervalsDictWithRange:addToDailyArrays:];
-[PLBatteryUIResponseTypeChargingStateIntervals intersectionOfTwoSets:intervalSetB:];
-[PLBatteryUIResponseTypeChargingStateIntervals intersectionOfTwoSetsWithMergeThreshold:intervalSetA:intervalSetB:];
-[PLBatteryUIResponseTypeChargingStateIntervals isChargingSpeedIntervalType:];
-[PLBatteryUIResponseTypeChargingStateIntervals isPausedChargingIntervalType:];
-[PLBatteryUIResponseTypeChargingStateIntervals isStoppedChargingIntervalType:];
-[PLBatteryUIResponseTypeChargingStateIntervals lastBattEntry];
-[PLBatteryUIResponseTypeChargingStateIntervals mapChargingStateIntervalsToGraphIntervals:];
-[PLBatteryUIResponseTypeChargingStateIntervals mergeAllChargingIntervals:];
-[PLBatteryUIResponseTypeChargingStateIntervals mergeIntervals:withTolerance:];
-[PLBatteryUIResponseTypeChargingStateIntervals organizeStateIntervalsWithRange:lastBattUIEntry:chargingIntervalsDict:addToDailyArrays:];
-[PLBatteryUIResponseTypeChargingStateIntervals responderService];
-[PLBatteryUIResponseTypeChargingStateIntervals resultDict];
-[PLBatteryUIResponseTypeChargingStateIntervals setBucketSize:];
-[PLBatteryUIResponseTypeChargingStateIntervals setChargingStateIntervalsDict:];
-[PLBatteryUIResponseTypeChargingStateIntervals setDailyChargingStateIntervalsDict:];
-[PLBatteryUIResponseTypeChargingStateIntervals setDailyLastBattEntry:];
-[PLBatteryUIResponseTypeChargingStateIntervals setLastBattEntry:];
-[PLBatteryUIResponseTypeChargingStateIntervals setResponderService:];
-[PLBatteryUIResponseTypeChargingStateIntervals setResultDict:];
-[PLBatteryUIResponseTypeChargingStateIntervals setShouldSnapInterval:];
-[PLBatteryUIResponseTypeChargingStateIntervals setUseBattUIforEC:];
-[PLBatteryUIResponseTypeChargingStateIntervals shouldSnapInterval];
-[PLBatteryUIResponseTypeChargingStateIntervals snapIntervals:];
-[PLBatteryUIResponseTypeChargingStateIntervals sortIntervals:];
-[PLBatteryUIResponseTypeChargingStateIntervals unionBetweenSetAndIntersectingSet:intervalSetB:];
-[PLBatteryUIResponseTypeChargingStateIntervals useBattUIforEC];
```
