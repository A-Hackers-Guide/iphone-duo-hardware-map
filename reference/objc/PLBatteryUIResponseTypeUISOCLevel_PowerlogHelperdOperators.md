# `PLBatteryUIResponseTypeUISOCLevel`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLBatteryUIResponseProtocol`
- 9 instance variables, 13 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"PLBatteryUIResponderService" _responderService;
@"NSDate" _start;
@"NSDate" _end;
d _bucketSize;
@"NSArray" _battEntries;
@"PLEntry" _lastBattEntry;
@"NSArray" _lpmEntries;
@"PLEntry" _lastLPMEntry;
@"NSArray" _resultArray;
```

## Properties

```
@property (T@"NSDate",&,V_start) start;
@property (T@"NSDate",&,V_end) end;
@property (Td,V_bucketSize) bucketSize;
@property (T@"NSArray",&,V_battEntries) battEntries;
@property (T@"PLEntry",&,V_lastBattEntry) lastBattEntry;
@property (T@"NSArray",&,V_lpmEntries) lpmEntries;
@property (T@"PLEntry",&,V_lastLPMEntry) lastLPMEntry;
@property (T@"NSArray",&,V_resultArray) resultArray;
@property (T@"PLBatteryUIResponderService",&,V_responderService) responderService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PLBatteryUIResponseTypeUISOCLevel configure:];
-[PLBatteryUIResponseTypeUISOCLevel dependencies];
-[PLBatteryUIResponseTypeUISOCLevel start];
-[PLBatteryUIResponseTypeUISOCLevel end];
-[PLBatteryUIResponseTypeUISOCLevel coalesce];
-[PLBatteryUIResponseTypeUISOCLevel setEnd:];
-[PLBatteryUIResponseTypeUISOCLevel result];
-[PLBatteryUIResponseTypeUISOCLevel setStart:];
-[PLBatteryUIResponseTypeUISOCLevel run];
-[PLBatteryUIResponseTypeUISOCLevel bucketSize];
-[PLBatteryUIResponseTypeUISOCLevel resultArray];
-[PLBatteryUIResponseTypeUISOCLevel setBattEntries:];
-[PLBatteryUIResponseTypeUISOCLevel setResultArray:];
-[PLBatteryUIResponseTypeUISOCLevel battEntries];
-[PLBatteryUIResponseTypeUISOCLevel dateIntervals:containDate:];
-[PLBatteryUIResponseTypeUISOCLevel entriesInRange:fromEntries:];
-[PLBatteryUIResponseTypeUISOCLevel getLPMIntervalsSpanningRange:];
-[PLBatteryUIResponseTypeUISOCLevel lastBattEntry];
-[PLBatteryUIResponseTypeUISOCLevel lastLPMEntry];
-[PLBatteryUIResponseTypeUISOCLevel lpmEntries];
-[PLBatteryUIResponseTypeUISOCLevel responderService];
-[PLBatteryUIResponseTypeUISOCLevel setBucketSize:];
-[PLBatteryUIResponseTypeUISOCLevel setLastBattEntry:];
-[PLBatteryUIResponseTypeUISOCLevel setLastLPMEntry:];
-[PLBatteryUIResponseTypeUISOCLevel setLpmEntries:];
-[PLBatteryUIResponseTypeUISOCLevel setResponderService:];
```
