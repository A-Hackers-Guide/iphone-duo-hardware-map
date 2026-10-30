# `CTDeviceDataUsage`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 7 properties, 32 instance methods, 1 class methods

## Instance variables

```
Q _periods;
@"NSMutableDictionary" _apps;
@"NSMutableDictionary" _uninstalledApps;
@"NSMutableDictionary" _proxiedOnlyApps;
@"NSMutableDictionary" _systemServices;
@"NSMutableDictionary" _hiddenApps;
@"NSArray" _wifiAssist;
```

## Properties

```
@property (TQ,V_periods) periods;
@property (T@"NSMutableDictionary",&,V_apps) apps;
@property (T@"NSMutableDictionary",&,V_uninstalledApps) uninstalledApps;
@property (T@"NSMutableDictionary",&,V_proxiedOnlyApps) proxiedOnlyApps;
@property (T@"NSMutableDictionary",&,V_systemServices) systemServices;
@property (T@"NSMutableDictionary",&,V_hiddenApps) hiddenApps;
@property (T@"NSArray",&,V_wifiAssist) wifiAssist;
```

## Class methods

```
+[CTDeviceDataUsage supportsSecureCoding];
```

## Instance methods

```
-[CTDeviceDataUsage encodeWithCoder:];
-[CTDeviceDataUsage description];
-[CTDeviceDataUsage initWithCoder:];
-[CTDeviceDataUsage apps];
-[CTDeviceDataUsage setApps:];
-[CTDeviceDataUsage copyWithZone:];
-[CTDeviceDataUsage periods];
-[CTDeviceDataUsage proxiedOnlyApps];
-[CTDeviceDataUsage uninstalledApps];
-[CTDeviceDataUsage appDataUsageForPeriod:];
-[CTDeviceDataUsage dataUsage:forPeriod:];
-[CTDeviceDataUsage hiddenAppDataUsageForPeriod:];
-[CTDeviceDataUsage hiddenApps];
-[CTDeviceDataUsage proxiedOnlyAppDataUsageForPeriod:];
-[CTDeviceDataUsage setHiddenApps:];
-[CTDeviceDataUsage setPeriods:];
-[CTDeviceDataUsage setProxiedOnlyApps:];
-[CTDeviceDataUsage setSystemServices:];
-[CTDeviceDataUsage setUninstalledApps:];
-[CTDeviceDataUsage setWifiAssist:];
-[CTDeviceDataUsage systemServiceDataUsageForPeriod:];
-[CTDeviceDataUsage systemServices];
-[CTDeviceDataUsage totalAppDataUsedForPeriod:];
-[CTDeviceDataUsage totalDataUsage:forPeriod:];
-[CTDeviceDataUsage totalDataUsedForPeriod:];
-[CTDeviceDataUsage totalHiddenAppDataUsedForPeriod:];
-[CTDeviceDataUsage totalProxiedOnlyAppDataUsedForPeriod:];
-[CTDeviceDataUsage totalSystemServiceDataUsedForPeriod:];
-[CTDeviceDataUsage totalUninstalledAppDataUsedForPeriod:];
-[CTDeviceDataUsage totalWifiAssistUsageForPeriod:];
-[CTDeviceDataUsage uninstalledAppDataUsageForPeriod:];
-[CTDeviceDataUsage wifiAssist];
```
