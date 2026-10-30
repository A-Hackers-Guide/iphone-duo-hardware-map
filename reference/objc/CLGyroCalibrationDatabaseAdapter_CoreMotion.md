# `CLGyroCalibrationDatabaseAdapter`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CLNotifierServiceAdapter`
- Protocols: `CLGyroCalibrationDatabaseProtocol`
- 0 instance variables, 5 properties, 19 instance methods, 4 class methods

## Properties

```
@property (TB,N) valid;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CLGyroCalibrationDatabaseAdapter becameFatallyBlocked:index:];
+[CLGyroCalibrationDatabaseAdapter isSupported];
+[CLGyroCalibrationDatabaseAdapter performSyncOnSilo:invoker:];
+[CLGyroCalibrationDatabaseAdapter getSilo];
```

## Instance methods

```
-[CLGyroCalibrationDatabaseAdapter init];
-[CLGyroCalibrationDatabaseAdapter adaptee];
-[CLGyroCalibrationDatabaseAdapter syncgetBiasFit:];
-[CLGyroCalibrationDatabaseAdapter beginService];
-[CLGyroCalibrationDatabaseAdapter doAsync:];
-[CLGyroCalibrationDatabaseAdapter doAsync:withReply:];
-[CLGyroCalibrationDatabaseAdapter dumpDatabase:onCompletion:];
-[CLGyroCalibrationDatabaseAdapter endService];
-[CLGyroCalibrationDatabaseAdapter getBiasFitWithReply:];
-[CLGyroCalibrationDatabaseAdapter startFactoryGYTT];
-[CLGyroCalibrationDatabaseAdapter syncgetDoSync:];
-[CLGyroCalibrationDatabaseAdapter syncgetGyroStatsWithBias:slope:l2Error:isDynamic:deltaBias:deltaSlope:deltaError:isDeltaDynamic:];
-[CLGyroCalibrationDatabaseAdapter syncgetInsertWithBias:variance:temperature:timestamp:];
-[CLGyroCalibrationDatabaseAdapter syncgetLastMiniCalibration];
-[CLGyroCalibrationDatabaseAdapter syncgetMaxDynamicTemperature];
-[CLGyroCalibrationDatabaseAdapter syncgetNonFactoryRoundCount];
-[CLGyroCalibrationDatabaseAdapter syncgetNumTemperatures];
-[CLGyroCalibrationDatabaseAdapter syncgetSupportsMiniCalibration];
-[CLGyroCalibrationDatabaseAdapter syncgetWipeDatabase];
```
