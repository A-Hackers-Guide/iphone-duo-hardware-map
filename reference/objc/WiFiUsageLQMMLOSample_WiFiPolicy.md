# `WiFiUsageLQMMLOSample`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiUsageLQMSample`
- 14 instance variables, 15 properties, 27 instance methods, 0 class methods

## Instance variables

```
C _isMLOPreferredLink;
i _band;
Q _duration;
Q _channelWidth;
q _rssi_core0;
q _rssi_core1;
Q _idleTimeMs;
Q _idlePortionOfSamplePercentage;
Q _txFramesTotal;
Q _rxUcastFrames;
Q _txRetriesExhaustedOverTxFrames;
Q _txFailsOverTxFrames;
Q _txRate;
Q _rxRate;
```

## Properties

```
@property (TQ,N,V_duration) duration;
@property (TC,N,V_isMLOPreferredLink) isMLOPreferredLink;
@property (Ti,N,V_band) band;
@property (TQ,N,V_channelWidth) channelWidth;
@property (Tq,R,N,V_rssi_core0) rssi_core0;
@property (Tq,R,N,V_rssi_core1) rssi_core1;
@property (Tq,R,N) diff_rssicore1_rssicore0;
@property (TQ,N,V_idleTimeMs) idleTimeMs;
@property (TQ,N,V_idlePortionOfSamplePercentage) idlePortionOfSamplePercentage;
@property (TQ,N,V_txFramesTotal) txFramesTotal;
@property (TQ,N,V_rxUcastFrames) rxUcastFrames;
@property (TQ,N,V_txRetriesExhaustedOverTxFrames) txRetriesExhaustedOverTxFrames;
@property (TQ,N,V_txFailsOverTxFrames) txFailsOverTxFrames;
@property (TQ,R,N,V_txRate) txRate;
@property (TQ,R,N,V_rxRate) rxRate;
```

## Instance methods

```
-[WiFiUsageLQMMLOSample rxRate];
-[WiFiUsageLQMMLOSample txRate];
-[WiFiUsageLQMMLOSample rssi_core0];
-[WiFiUsageLQMMLOSample rssi_core1];
-[WiFiUsageLQMMLOSample band];
-[WiFiUsageLQMMLOSample duration];
-[WiFiUsageLQMMLOSample setTxFailsOverTxFrames:];
-[WiFiUsageLQMMLOSample txFailsOverTxFrames];
-[WiFiUsageLQMMLOSample channelWidth];
-[WiFiUsageLQMMLOSample asDictionaryInto:];
-[WiFiUsageLQMMLOSample setBand:];
-[WiFiUsageLQMMLOSample setDuration:];
-[WiFiUsageLQMMLOSample diff_rssicore1_rssicore0];
-[WiFiUsageLQMMLOSample setChannelWidth:];
-[WiFiUsageLQMMLOSample idlePortionOfSamplePercentage];
-[WiFiUsageLQMMLOSample idleTimeMs];
-[WiFiUsageLQMMLOSample initWith:andDuration:];
-[WiFiUsageLQMMLOSample isMLOPreferredLink];
-[WiFiUsageLQMMLOSample rxUcastFrames];
-[WiFiUsageLQMMLOSample setIdlePortionOfSamplePercentage:];
-[WiFiUsageLQMMLOSample setIdleTimeMs:];
-[WiFiUsageLQMMLOSample setIsMLOPreferredLink:];
-[WiFiUsageLQMMLOSample setRxUcastFrames:];
-[WiFiUsageLQMMLOSample setTxFramesTotal:];
-[WiFiUsageLQMMLOSample setTxRetriesExhaustedOverTxFrames:];
-[WiFiUsageLQMMLOSample txFramesTotal];
-[WiFiUsageLQMMLOSample txRetriesExhaustedOverTxFrames];
```
