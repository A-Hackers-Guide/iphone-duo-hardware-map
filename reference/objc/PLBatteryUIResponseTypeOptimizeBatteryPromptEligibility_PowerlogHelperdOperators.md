# `PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLBatteryUIResponseProtocol`
- 5 instance variables, 9 properties, 16 instance methods, 0 class methods

## Instance variables

```
i _criticalDays;
@"PLBatteryUIResponderService" _responderService;
@"NSDate" _start;
@"NSDate" _end;
@"NSArray" _uiLevelEntries;
```

## Properties

```
@property (T@"NSDate",&,V_start) start;
@property (T@"NSDate",&,V_end) end;
@property (T@"NSArray",&,V_uiLevelEntries) uiLevelEntries;
@property (Ti,V_criticalDays) criticalDays;
@property (T@"PLBatteryUIResponderService",&,V_responderService) responderService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility configure:];
-[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility dependencies];
-[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility cleanUp];
-[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility start];
-[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility end];
-[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility coalesce];
-[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility setEnd:];
-[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility result];
-[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility setStart:];
-[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility run];
-[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility criticalDays];
-[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility responderService];
-[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility setCriticalDays:];
-[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility setResponderService:];
-[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility setUiLevelEntries:];
-[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility uiLevelEntries];
```
