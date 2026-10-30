# `CTDataStatus`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 15 instance variables, 23 properties, 43 instance methods, 1 class methods

## Instance variables

```
B _attached;
B _dataSim;
B _roamAllowed;
B _dataPlanSignalingReductionOverride;
B _cellularDataPossible;
B _inHomeCountry;
i _indicator;
i _indicatorOverride;
i _radioTechnology;
i _dataMode;
i _dataBearerTechnology;
I _dataBearerSoMask;
I _activeContexts;
I _totalActiveContexts;
i _reason;
```

## Properties

```
@property (TB,R,N) newRadioCoverage;
@property (TB,R,N) newRadioSaCoverage;
@property (TB,R,N) newRadioNsaCoverage;
@property (TB,R,N) newRadioDataBearer;
@property (TB,R,N) newRadioSaDataBearer;
@property (TB,R,N) newRadioNsaDataBearer;
@property (TB,R,N) newRadioMmWaveDataBearer;
@property (TB,R,N) newRadioSub6DataBearer;
@property (TB,N,V_attached) attached;
@property (TB,N,V_dataSim) dataSim;
@property (Ti,N,V_indicator) indicator;
@property (Ti,N,V_indicatorOverride) indicatorOverride;
@property (TB,N,V_roamAllowed) roamAllowed;
@property (Ti,N,V_radioTechnology) radioTechnology;
@property (Ti,N,V_dataMode) dataMode;
@property (Ti,N,V_dataBearerTechnology) dataBearerTechnology;
@property (TI,N,V_dataBearerSoMask) dataBearerSoMask;
@property (TB,N,V_dataPlanSignalingReductionOverride) dataPlanSignalingReductionOverride;
@property (TB,N,V_cellularDataPossible) cellularDataPossible;
@property (TI,N,V_activeContexts) activeContexts;
@property (TI,N,V_totalActiveContexts) totalActiveContexts;
@property (TB,N,V_inHomeCountry) inHomeCountry;
@property (Ti,N,V_reason) reason;
```

## Class methods

```
+[CTDataStatus supportsSecureCoding];
```

## Instance methods

```
-[CTDataStatus radioTechnology];
-[CTDataStatus activeContexts];
-[CTDataStatus setActiveContexts:];
-[CTDataStatus setReason:];
-[CTDataStatus indicator];
-[CTDataStatus roamAllowed];
-[CTDataStatus setCellularDataPossible:];
-[CTDataStatus cellularDataPossible];
-[CTDataStatus encodeWithCoder:];
-[CTDataStatus setInHomeCountry:];
-[CTDataStatus dataMode];
-[CTDataStatus description];
-[CTDataStatus initWithCoder:];
-[CTDataStatus newRadioCoverage];
-[CTDataStatus reason];
-[CTDataStatus setRoamAllowed:];
-[CTDataStatus copyWithZone:];
-[CTDataStatus setDataMode:];
-[CTDataStatus setRadioTechnology:];
-[CTDataStatus inHomeCountry];
-[CTDataStatus setAttached:];
-[CTDataStatus attached];
-[CTDataStatus setIndicator:];
-[CTDataStatus dataBearerSoMask];
-[CTDataStatus dataSim];
-[CTDataStatus copyBasic];
-[CTDataStatus dataBearerTechnology];
-[CTDataStatus dataPlanSignalingReductionOverride];
-[CTDataStatus indicatorOverride];
-[CTDataStatus newRadioDataBearer];
-[CTDataStatus newRadioMmWaveDataBearer];
-[CTDataStatus newRadioNsaCoverage];
-[CTDataStatus newRadioNsaDataBearer];
-[CTDataStatus newRadioSaCoverage];
-[CTDataStatus newRadioSaDataBearer];
-[CTDataStatus newRadioSub6DataBearer];
-[CTDataStatus setDataBearerSoMask:];
-[CTDataStatus setDataBearerTechnology:];
-[CTDataStatus setDataPlanSignalingReductionOverride:];
-[CTDataStatus setDataSim:];
-[CTDataStatus setIndicatorOverride:];
-[CTDataStatus setTotalActiveContexts:];
-[CTDataStatus totalActiveContexts];
```
