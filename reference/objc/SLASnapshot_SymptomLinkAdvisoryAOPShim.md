# `SLASnapshot`

- Image: [`/System/Library/PrivateFrameworks/SymptomLinkAdvisoryAOPShim.framework/SymptomLinkAdvisoryAOPShim`](../userland/System__Library__PrivateFrameworks__SymptomLinkAdvisoryAOPShim.framework__SymptomLinkAdvisoryAOPShim.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 24 instance methods, 0 class methods

## Instance variables

```
C _reportReason;
I _aggregationWindowMs;
@"SLAInterfaceStats" _wifiStats;
@"SLAInterfaceStats" _bluetoothStats;
@"SLAInterfaceStats" _wiredStats;
@"NSNumber" _batteryPercentage;
@"NSNumber" _isPluggedIn;
@"NSNumber" _thermalPressure;
@"NSNumber" _transferActive;
@"NSNumber" _activeTransferEstimatedTotal;
@"NSNumber" _activeTransferRemainingBytes;
```

## Properties

```
@property (TI,N,V_aggregationWindowMs) aggregationWindowMs;
@property (TC,N,V_reportReason) reportReason;
@property (T@"SLAInterfaceStats",&,N,V_wifiStats) wifiStats;
@property (T@"SLAInterfaceStats",&,N,V_bluetoothStats) bluetoothStats;
@property (T@"SLAInterfaceStats",&,N,V_wiredStats) wiredStats;
@property (T@"NSNumber",&,N,V_batteryPercentage) batteryPercentage;
@property (T@"NSNumber",&,N,V_isPluggedIn) isPluggedIn;
@property (T@"NSNumber",&,N,V_thermalPressure) thermalPressure;
@property (T@"NSNumber",&,N,V_transferActive) transferActive;
@property (T@"NSNumber",&,N,V_activeTransferEstimatedTotal) activeTransferEstimatedTotal;
@property (T@"NSNumber",&,N,V_activeTransferRemainingBytes) activeTransferRemainingBytes;
```

## Instance methods

```
-[SLASnapshot thermalPressure];
-[SLASnapshot isPluggedIn];
-[SLASnapshot setThermalPressure:];
-[SLASnapshot init];
-[SLASnapshot setBatteryPercentage:];
-[SLASnapshot batteryPercentage];
-[SLASnapshot reportReason];
-[SLASnapshot setReportReason:];
-[SLASnapshot setIsPluggedIn:];
-[SLASnapshot initWithAggregationWindowMs:reportReason:];
-[SLASnapshot setActiveTransferEstimatedTotal:];
-[SLASnapshot setActiveTransferRemainingBytes:];
-[SLASnapshot setBluetoothStats:];
-[SLASnapshot setTransferActive:];
-[SLASnapshot setWifiStats:];
-[SLASnapshot setWiredStats:];
-[SLASnapshot activeTransferEstimatedTotal];
-[SLASnapshot activeTransferRemainingBytes];
-[SLASnapshot aggregationWindowMs];
-[SLASnapshot bluetoothStats];
-[SLASnapshot setAggregationWindowMs:];
-[SLASnapshot transferActive];
-[SLASnapshot wifiStats];
-[SLASnapshot wiredStats];
```
