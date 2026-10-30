# `PLMetricsFormatterJSON`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 22 instance variables, 1 properties, 40 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" allMetrics;
@"NSMutableArray" metricArray;
@"NSArray" appTimeMapping;
@"NSArray" appBGTimeMapping;
@"NSArray" appBGTimeUpMapping;
@"NSArray" appTimeUnpluggedMapping;
@"NSArray" appTimeLocationActivityMapping;
@"NSArray" appTimeCellularConditionMapping;
@"NSArray" appNetworkIOWifiMapping;
@"NSArray" appNetworkIOCellularMapping;
@"NSArray" appDisplayAPLMapping;
@"NSArray" appDisplayXAPLMapping;
@"NSMutableArray" appEnergyFGMapping;
@"NSMutableArray" appEnergyBGMapping;
@"NSMutableArray" appEnergyTotalMapping;
@"NSMutableArray" appEnergyBGAudioMapping;
@"NSMutableArray" appEnergyBGLocationMapping;
@"NSArray" diskIOMapping;
@"NSArray" memoryMapping;
@"NSArray" storageConsumptionMapping;
[1024c] tmpFilePath;
@"NSDate" _logFileTimeStamp;
```

## Properties

```
@property (T@"NSDate",&,V_logFileTimeStamp) logFileTimeStamp;
```

## Class methods

```
+[PLMetricsFormatterJSON pruneDictionary:withAllowlist:];
```

## Instance methods

```
-[PLMetricsFormatterJSON init];
-[PLMetricsFormatterJSON test];
-[PLMetricsFormatterJSON sanitizeDictionary:];
-[PLMetricsFormatterJSON getOSVersion];
-[PLMetricsFormatterJSON addStorageConsumption:userData:];
-[PLMetricsFormatterJSON addAllMetrics:signpostData:];
-[PLMetricsFormatterJSON addAppEnergy:userData:];
-[PLMetricsFormatterJSON addAppMemoryKeys:userData:];
-[PLMetricsFormatterJSON addAppMetaData:userData:];
-[PLMetricsFormatterJSON addAppMetric:];
-[PLMetricsFormatterJSON addAppPerformanceKeysActivations:activationData:];
-[PLMetricsFormatterJSON addAppPerformanceKeysExits:processExitData:];
-[PLMetricsFormatterJSON addAppPerformanceKeysGlitch:scrollGlitchData:];
-[PLMetricsFormatterJSON addAppPerformanceKeysHang:userData:hangTimeData:];
-[PLMetricsFormatterJSON addAppPerformanceKeysLaunch:userData:launchTimeData:];
-[PLMetricsFormatterJSON addAppPerformanceKeysResume:userData:resumeTimeData:];
-[PLMetricsFormatterJSON addAppTime:userData:];
-[PLMetricsFormatterJSON addDiskIO:userData:];
-[PLMetricsFormatterJSON addDisplayAPL:userData:forIndex:];
-[PLMetricsFormatterJSON addGlobalMetaData:];
-[PLMetricsFormatterJSON addNetworkIO:userData:];
-[PLMetricsFormatterJSON addPerformanceMetrics:userData:signpostData:];
-[PLMetricsFormatterJSON addPowerMetrics:userData:];
-[PLMetricsFormatterJSON addSubKeys:extractFromHere:deviceFirstLevelMetric:firstLevelKey:secondLevelKey:subKeyMap:];
-[PLMetricsFormatterJSON addSubKeysThirdLevel:extractFromHere:deviceFirstLevelMetric:firstLevelKey:secondLevelKey:thirdLevelKey:subKeyMap:];
-[PLMetricsFormatterJSON checkKeyExistence:secondLevel:dictToCheck:];
-[PLMetricsFormatterJSON createHeaderForSessionsFile];
-[PLMetricsFormatterJSON customRound:precision:];
-[PLMetricsFormatterJSON getCurrentTimeFormatted:];
-[PLMetricsFormatterJSON getFileHandle];
-[PLMetricsFormatterJSON logFileTimeStamp];
-[PLMetricsFormatterJSON metricsToStringAsJSON];
-[PLMetricsFormatterJSON moveLogFile];
-[PLMetricsFormatterJSON printAllMetricsToConsole];
-[PLMetricsFormatterJSON pruneJSONData];
-[PLMetricsFormatterJSON roundArrayValuesToNearestX:precision:];
-[PLMetricsFormatterJSON sendAppMetricToCoreAnalytics:];
-[PLMetricsFormatterJSON setLogFileTimeStamp:];
-[PLMetricsFormatterJSON testAllMetrics];
-[PLMetricsFormatterJSON writeSessionFile];
```
