# `PLBatteryUIResponseTypeIOSUISOCDrain`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLBatteryUIResponseProtocol`
- 9 instance variables, 13 properties, 28 instance methods, 0 class methods

## Instance variables

```
B _isDynamicEnd;
@"PLBatteryUIResponderService" _responderService;
@"NSDate" _start;
@"NSDate" _end;
d _bucketSize;
@"NSArray" _uiLevelEntries;
d _dynamicEndOffset;
@"NSArray" _resultArray;
@"NSArray" _dynamicResultArray;
```

## Properties

```
@property (T@"NSDate",&,V_start) start;
@property (T@"NSDate",&,V_end) end;
@property (Td,V_bucketSize) bucketSize;
@property (T@"NSArray",&,V_uiLevelEntries) uiLevelEntries;
@property (TB,V_isDynamicEnd) isDynamicEnd;
@property (Td,V_dynamicEndOffset) dynamicEndOffset;
@property (T@"NSArray",&,V_resultArray) resultArray;
@property (T@"NSArray",&,V_dynamicResultArray) dynamicResultArray;
@property (T@"PLBatteryUIResponderService",&,V_responderService) responderService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PLBatteryUIResponseTypeIOSUISOCDrain configure:];
-[PLBatteryUIResponseTypeIOSUISOCDrain dependencies];
-[PLBatteryUIResponseTypeIOSUISOCDrain start];
-[PLBatteryUIResponseTypeIOSUISOCDrain end];
-[PLBatteryUIResponseTypeIOSUISOCDrain coalesce];
-[PLBatteryUIResponseTypeIOSUISOCDrain setEnd:];
-[PLBatteryUIResponseTypeIOSUISOCDrain result];
-[PLBatteryUIResponseTypeIOSUISOCDrain setStart:];
-[PLBatteryUIResponseTypeIOSUISOCDrain run];
-[PLBatteryUIResponseTypeIOSUISOCDrain bucketSize];
-[PLBatteryUIResponseTypeIOSUISOCDrain resultArray];
-[PLBatteryUIResponseTypeIOSUISOCDrain drainForInterval:start:max:end:];
-[PLBatteryUIResponseTypeIOSUISOCDrain setResultArray:];
-[PLBatteryUIResponseTypeIOSUISOCDrain updateInterval:level:timestamp:];
-[PLBatteryUIResponseTypeIOSUISOCDrain dynamicEndOffset];
-[PLBatteryUIResponseTypeIOSUISOCDrain dynamicResultArray];
-[PLBatteryUIResponseTypeIOSUISOCDrain finalizeInterval:uiDrainTotal:dynamicDrainTotal:dynamicCutoff:includeDynamic:];
-[PLBatteryUIResponseTypeIOSUISOCDrain initializeInterval:isCharging:level:timestamp:];
-[PLBatteryUIResponseTypeIOSUISOCDrain isDynamicEnd];
-[PLBatteryUIResponseTypeIOSUISOCDrain processBucketAtIndex:bucketStart:bucketEnd:levelIndex:uiDrain:dynamicDrain:];
-[PLBatteryUIResponseTypeIOSUISOCDrain responderService];
-[PLBatteryUIResponseTypeIOSUISOCDrain setBucketSize:];
-[PLBatteryUIResponseTypeIOSUISOCDrain setDynamicEndOffset:];
-[PLBatteryUIResponseTypeIOSUISOCDrain setDynamicResultArray:];
-[PLBatteryUIResponseTypeIOSUISOCDrain setIsDynamicEnd:];
-[PLBatteryUIResponseTypeIOSUISOCDrain setResponderService:];
-[PLBatteryUIResponseTypeIOSUISOCDrain setUiLevelEntries:];
-[PLBatteryUIResponseTypeIOSUISOCDrain uiLevelEntries];
```
