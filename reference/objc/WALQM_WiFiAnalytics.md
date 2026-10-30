# `WALQM`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 21 properties, 43 instance methods, 1 class methods

## Instance variables

```
B _isAnyAppInFg;
B _isFTactive;
B _isTimeSensitiveAppRunning;
s _band;
Q _channel;
q _rssi;
q _noise;
q _snr;
Q _ccaTotal;
Q _ccaSelf;
Q _ccaOther;
Q _ccaInterference;
Q _beaconPER;
Q _rxFrames;
Q _rxRetryFrames;
Q _txFrames;
Q _txReTrans;
Q _txFail;
Q _txRate;
Q _rxRate;
Q _duration;
```

## Properties

```
@property (TQ,V_channel) channel;
@property (Ts,V_band) band;
@property (Tq,V_rssi) rssi;
@property (Tq,V_noise) noise;
@property (Tq,V_snr) snr;
@property (TQ,V_ccaTotal) ccaTotal;
@property (TQ,V_ccaSelf) ccaSelf;
@property (TQ,V_ccaOther) ccaOther;
@property (TQ,V_ccaInterference) ccaInterference;
@property (TQ,V_beaconPER) beaconPER;
@property (TQ,V_rxFrames) rxFrames;
@property (TQ,V_rxRetryFrames) rxRetryFrames;
@property (TQ,V_txFrames) txFrames;
@property (TQ,V_txReTrans) txReTrans;
@property (TQ,V_txFail) txFail;
@property (TQ,V_txRate) txRate;
@property (TQ,V_rxRate) rxRate;
@property (TQ,V_duration) duration;
@property (TB,V_isAnyAppInFg) isAnyAppInFg;
@property (TB,V_isFTactive) isFTactive;
@property (TB,V_isTimeSensitiveAppRunning) isTimeSensitiveAppRunning;
```

## Class methods

```
+[WALQM waLQMonChannel:band:rssi:noise:snr:totalCCA:selfCca:otherCca:interference:beaconPer:rxFrames:rxRetryFrames:txFrames:txRetries:txFail:txRate:rxRate:isAnyAppInFG:isFTactive:isTimeSensitiveAppRunning:duration:];
```

## Instance methods

```
-[WALQM rssi];
-[WALQM setSnr:];
-[WALQM setChannel:];
-[WALQM setNoise:];
-[WALQM rxRate];
-[WALQM channel];
-[WALQM snr];
-[WALQM txRate];
-[WALQM setTxRate:];
-[WALQM noise];
-[WALQM setIsFTactive:];
-[WALQM setTxFrames:];
-[WALQM setRssi:];
-[WALQM setRxFrames:];
-[WALQM band];
-[WALQM setRxRate:];
-[WALQM ccaTotal];
-[WALQM isFTactive];
-[WALQM duration];
-[WALQM rxFrames];
-[WALQM txFrames];
-[WALQM setBand:];
-[WALQM setIsTimeSensitiveAppRunning:];
-[WALQM description];
-[WALQM setDuration:];
-[WALQM isTimeSensitiveAppRunning];
-[WALQM setCcaTotal:];
-[WALQM beaconPER];
-[WALQM setBeaconPER:];
-[WALQM ccaSelf];
-[WALQM ccaInterference];
-[WALQM ccaOther];
-[WALQM isAnyAppInFg];
-[WALQM rxRetryFrames];
-[WALQM setCcaInterference:];
-[WALQM setCcaOther:];
-[WALQM setCcaSelf:];
-[WALQM setIsAnyAppInFg:];
-[WALQM setRxRetryFrames:];
-[WALQM setTxFail:];
-[WALQM setTxReTrans:];
-[WALQM txFail];
-[WALQM txReTrans];
```
