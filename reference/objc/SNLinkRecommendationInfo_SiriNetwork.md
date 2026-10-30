# `SNLinkRecommendationInfo`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 16 properties, 32 instance methods, 0 class methods

## Instance variables

```
B _btPreference;
B _wifiPreference;
Q _btRSSI;
q _wifiRSSI;
q _wifiSNR;
q _beaconPER;
q _nwType;
q _wifiCCA;
q _lsmRecommendationBe;
q _expectedThroughputVIBE;
q _packetLifetimeVIBE;
q _packetLossRateVIBE;
q _btRetransmissionRateTx;
q _btRetransmissionRateRx;
q _btTech;
d _timeTaken;
```

## Properties

```
@property (TB,N,V_btPreference) btPreference;
@property (TB,N,V_wifiPreference) wifiPreference;
@property (TQ,N,V_btRSSI) btRSSI;
@property (Tq,N,V_wifiRSSI) wifiRSSI;
@property (Tq,N,V_wifiSNR) wifiSNR;
@property (Tq,N,V_beaconPER) beaconPER;
@property (Tq,N,V_nwType) nwType;
@property (Tq,N,V_wifiCCA) wifiCCA;
@property (Tq,N,V_lsmRecommendationBe) lsmRecommendationBe;
@property (Tq,N,V_expectedThroughputVIBE) expectedThroughputVIBE;
@property (Tq,N,V_packetLifetimeVIBE) packetLifetimeVIBE;
@property (Tq,N,V_packetLossRateVIBE) packetLossRateVIBE;
@property (Tq,N,V_btRetransmissionRateTx) btRetransmissionRateTx;
@property (Tq,N,V_btRetransmissionRateRx) btRetransmissionRateRx;
@property (Tq,N,V_btTech) btTech;
@property (Td,N,V_timeTaken) timeTaken;
```

## Instance methods

```
-[SNLinkRecommendationInfo setWifiRSSI:];
-[SNLinkRecommendationInfo wifiRSSI];
-[SNLinkRecommendationInfo wifiSNR];
-[SNLinkRecommendationInfo setWifiSNR:];
-[SNLinkRecommendationInfo timeTaken];
-[SNLinkRecommendationInfo setTimeTaken:];
-[SNLinkRecommendationInfo btPreference];
-[SNLinkRecommendationInfo wifiPreference];
-[SNLinkRecommendationInfo wifiCCA];
-[SNLinkRecommendationInfo beaconPER];
-[SNLinkRecommendationInfo btRSSI];
-[SNLinkRecommendationInfo btRetransmissionRateRx];
-[SNLinkRecommendationInfo btRetransmissionRateTx];
-[SNLinkRecommendationInfo btTech];
-[SNLinkRecommendationInfo expectedThroughputVIBE];
-[SNLinkRecommendationInfo lsmRecommendationBe];
-[SNLinkRecommendationInfo nwType];
-[SNLinkRecommendationInfo packetLifetimeVIBE];
-[SNLinkRecommendationInfo packetLossRateVIBE];
-[SNLinkRecommendationInfo setBeaconPER:];
-[SNLinkRecommendationInfo setBtPreference:];
-[SNLinkRecommendationInfo setBtRSSI:];
-[SNLinkRecommendationInfo setBtRetransmissionRateRx:];
-[SNLinkRecommendationInfo setBtRetransmissionRateTx:];
-[SNLinkRecommendationInfo setBtTech:];
-[SNLinkRecommendationInfo setExpectedThroughputVIBE:];
-[SNLinkRecommendationInfo setLsmRecommendationBe:];
-[SNLinkRecommendationInfo setNwType:];
-[SNLinkRecommendationInfo setPacketLifetimeVIBE:];
-[SNLinkRecommendationInfo setPacketLossRateVIBE:];
-[SNLinkRecommendationInfo setWifiCCA:];
-[SNLinkRecommendationInfo setWifiPreference:];
```
