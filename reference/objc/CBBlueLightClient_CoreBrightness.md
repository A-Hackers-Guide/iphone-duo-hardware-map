# `CBBlueLightClient`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 1 properties, 28 instance methods, 1 class methods

## Instance variables

```
@"BrightnessSystemClient" bsc;
@? clientBlock;
B ownsClient;
B notificationActive;
B rangeSet;
{?="minCCT"f"maxCCT"f"midCCT"f} defaultCctRange;
B rangeOverridden;
{?="minCCT"f"maxCCT"f"midCCT"f} cctRange;
B _supported;
```

## Properties

```
@property (TB,V_supported) supported;
```

## Class methods

```
+[CBBlueLightClient supportsBlueLightReduction];
```

## Instance methods

```
-[CBBlueLightClient supported];
-[CBBlueLightClient setSupported:];
-[CBBlueLightClient init];
-[CBBlueLightClient dealloc];
-[CBBlueLightClient setActive:];
-[CBBlueLightClient setMode:];
-[CBBlueLightClient setEnabled:];
-[CBBlueLightClient setSchedule:];
-[CBBlueLightClient disableNotifications];
-[CBBlueLightClient enableNotifications];
-[CBBlueLightClient getBlueLightStatus:];
-[CBBlueLightClient getCCT:];
-[CBBlueLightClient getCCTRange:];
-[CBBlueLightClient getDefaultCCTRange:];
-[CBBlueLightClient getStrength:];
-[CBBlueLightClient getWarningCCT:];
-[CBBlueLightClient getWarningStrength:];
-[CBBlueLightClient initWithClientObj:];
-[CBBlueLightClient parseStatusDictionary:intoStruct:];
-[CBBlueLightClient setCCT:commit:];
-[CBBlueLightClient setCCT:withPeriod:commit:];
-[CBBlueLightClient setCCTRange:];
-[CBBlueLightClient setEnabled:withOption:];
-[CBBlueLightClient setStatusNotificationBlock:];
-[CBBlueLightClient setStrength:commit:];
-[CBBlueLightClient setStrength:withPeriod:commit:];
-[CBBlueLightClient suspendNotifications:];
-[CBBlueLightClient suspendNotifications:force:];
```
