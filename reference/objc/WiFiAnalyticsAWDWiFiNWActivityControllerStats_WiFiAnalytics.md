# `WiFiAnalyticsAWDWiFiNWActivityControllerStats`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 23 instance variables, 41 properties, 95 instance methods, 3 class methods

## Instance variables

```
Q _commandsIssued;
@"WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics" _aggregateMetrics;
I _backoffStuck;
@"WiFiAnalyticsAWDWiFiNWActivityBtCoex" _btCoex;
I _ccCaptureDriverLogs;
I _channel;
I _channelBandwidth;
I _channelsVisited0;
I _channelsVisited1;
I _commanderHalted;
I _controllerResets;
@"WiFiAnalyticsAWDWiFiNWActivityImpedingFunctions" _impedingFunctions;
I _iorSuccess;
I _iorWA;
@"WiFiAnalyticsAWDWiFiNWActivityOMI" _omi;
@"WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation" _phyrate;
@"WiFiAnalyticsAWDWiFiNWActivityPowerPStats" _powerActivity;
@"WiFiAnalyticsAWDWiFiNWActivityRuUsage" _ruUsage;
@"NSMutableArray" _rxmdpuLosts;
@"NSMutableArray" _rxmpduWMEs;
@"WiFiAnalyticsAWDWiFiNWActivityScanActivity" _scanActivity;
@"NSMutableArray" _txmpduWMEs;
{?="commandsIssued"b1"backoffStuck"b1"ccCaptureDriverLogs"b1"channel"b1"channelBandwidth"b1"channelsVisited0"b1"channelsVisited1"b1"commanderHalted"b1"controllerResets"b1"iorSuccess"b1"iorWA"b1} _has;
```

## Properties

```
@property (TB,N) hasControllerResets;
@property (TI,N,V_controllerResets) controllerResets;
@property (TB,N) hasBackoffStuck;
@property (TI,N,V_backoffStuck) backoffStuck;
@property (TB,R,N) hasScanActivity;
@property (T@"WiFiAnalyticsAWDWiFiNWActivityScanActivity",&,N,V_scanActivity) scanActivity;
@property (TB,R,N) hasPowerActivity;
@property (T@"WiFiAnalyticsAWDWiFiNWActivityPowerPStats",&,N,V_powerActivity) powerActivity;
@property (TB,R,N) hasImpedingFunctions;
@property (T@"WiFiAnalyticsAWDWiFiNWActivityImpedingFunctions",&,N,V_impedingFunctions) impedingFunctions;
@property (TB,R,N) hasAggregateMetrics;
@property (T@"WiFiAnalyticsAWDWiFiNWActivityAggregateMetrics",&,N,V_aggregateMetrics) aggregateMetrics;
@property (TB,R,N) hasBtCoex;
@property (T@"WiFiAnalyticsAWDWiFiNWActivityBtCoex",&,N,V_btCoex) btCoex;
@property (TB,N) hasChannelsVisited0;
@property (TI,N,V_channelsVisited0) channelsVisited0;
@property (TB,N) hasChannelsVisited1;
@property (TI,N,V_channelsVisited1) channelsVisited1;
@property (TB,R,N) hasPhyrate;
@property (T@"WiFiAnalyticsAWDWiFiNWActivityRateAndAggregation",&,N,V_phyrate) phyrate;
@property (TB,N) hasChannel;
@property (TI,N,V_channel) channel;
@property (TB,N) hasChannelBandwidth;
@property (TI,N,V_channelBandwidth) channelBandwidth;
@property (TB,N) hasCcCaptureDriverLogs;
@property (TI,N,V_ccCaptureDriverLogs) ccCaptureDriverLogs;
@property (TB,N) hasCommandsIssued;
@property (TQ,N,V_commandsIssued) commandsIssued;
@property (TB,N) hasCommanderHalted;
@property (TI,N,V_commanderHalted) commanderHalted;
@property (TB,N) hasIorSuccess;
@property (TI,N,V_iorSuccess) iorSuccess;
@property (TB,N) hasIorWA;
@property (TI,N,V_iorWA) iorWA;
@property (T@"NSMutableArray",&,N,V_txmpduWMEs) txmpduWMEs;
@property (T@"NSMutableArray",&,N,V_rxmpduWMEs) rxmpduWMEs;
@property (T@"NSMutableArray",&,N,V_rxmdpuLosts) rxmdpuLosts;
@property (TB,R,N) hasOmi;
@property (T@"WiFiAnalyticsAWDWiFiNWActivityOMI",&,N,V_omi) omi;
@property (TB,R,N) hasRuUsage;
@property (T@"WiFiAnalyticsAWDWiFiNWActivityRuUsage",&,N,V_ruUsage) ruUsage;
```

## Class methods

```
+[WiFiAnalyticsAWDWiFiNWActivityControllerStats rxmdpuLostType];
+[WiFiAnalyticsAWDWiFiNWActivityControllerStats rxmpduWMEType];
+[WiFiAnalyticsAWDWiFiNWActivityControllerStats txmpduWMEType];
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setRuUsage:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setPhyrate:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setChannel:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats channel];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats writeTo:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setImpedingFunctions:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats hasBackoffStuck];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats hasImpedingFunctions];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setHasIorWA:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats aggregateMetrics];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats hasPhyrate];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats rxmdpuLosts];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats ccCaptureDriverLogs];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats hasChannel];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats rxmpduWMEAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats addTxmpduWME:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats omi];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats btCoex];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats hasCommandsIssued];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats txmpduWMEs];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats hasChannelBandwidth];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats mergeFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setCommanderHalted:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setHasChannel:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats rxmdpuLostsCount];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats clearRxmpduWMEs];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats addRxmpduWME:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats powerActivity];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats impedingFunctions];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats channelsVisited0];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setCcCaptureDriverLogs:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats hasRuUsage];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats iorWA];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats rxmpduWMEs];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats hasControllerResets];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats phyrate];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setBackoffStuck:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats hasScanActivity];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setChannelsVisited1:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats hasCommanderHalted];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats hasBtCoex];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats ruUsage];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setHasIorSuccess:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats rxmpduWMEsCount];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats hasCcCaptureDriverLogs];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setIorWA:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setOmi:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats hasAggregateMetrics];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setHasBackoffStuck:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats commandsIssued];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setHasChannelsVisited1:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats channelsVisited1];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats backoffStuck];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setCommandsIssued:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats hasPowerActivity];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats hasChannelsVisited0];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats iorSuccess];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats hash];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setAggregateMetrics:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats copyTo:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setChannelBandwidth:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats description];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setControllerResets:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setIorSuccess:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setHasChannelBandwidth:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats hasChannelsVisited1];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setRxmdpuLosts:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats rxmdpuLostAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setHasCommanderHalted:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setHasCommandsIssued:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats readFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats copyWithZone:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats scanActivity];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats hasIorWA];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setTxmpduWMEs:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats hasIorSuccess];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setHasChannelsVisited0:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setScanActivity:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats isEqual:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats commanderHalted];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setRxmpduWMEs:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats controllerResets];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats txmpduWMEAtIndex:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setPowerActivity:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats clearTxmpduWMEs];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats channelBandwidth];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats hasOmi];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setChannelsVisited0:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setBtCoex:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats txmpduWMEsCount];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats clearRxmdpuLosts];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setHasControllerResets:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats addRxmdpuLost:];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiNWActivityControllerStats setHasCcCaptureDriverLogs:];
```
