# `ANFetchFirmwareVersionTask`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ANTask`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _crashData;
@"CLFindMyAccessoryFirmwareVersion" _firmwareVersion;
@"ANNordicCrashEvent" _nordicCrash;
```

## Properties

```
@property (T@"ANNordicCrashEvent",&,V_nordicCrash) nordicCrash;
@property (T@"CLFindMyAccessoryFirmwareVersion",&,V_firmwareVersion) firmwareVersion;
@property (T@"NSArray",R) roseCrashes;
```

## Instance methods

```
-[ANFetchFirmwareVersionTask firmwareVersion];
-[ANFetchFirmwareVersionTask setFirmwareVersion:];
-[ANFetchFirmwareVersionTask dealloc];
-[ANFetchFirmwareVersionTask description];
-[ANFetchFirmwareVersionTask timeoutSeconds];
-[ANFetchFirmwareVersionTask setNordicCrash:];
-[ANFetchFirmwareVersionTask appendNordicCrashData:];
-[ANFetchFirmwareVersionTask appendRoseCrashData:];
-[ANFetchFirmwareVersionTask initWithIncludeCrashLogs:];
-[ANFetchFirmwareVersionTask nordicCrash];
-[ANFetchFirmwareVersionTask roseCrashes];
```
