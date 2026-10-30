# `WiFiAnalyticsAWDWiFiDPSActiveProbeStats`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 10 instance variables, 18 properties, 45 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _rttGatewayBE;
I _rttGatewayBK;
I _rttGatewayVI;
I _rttGatewayVO;
I _rttPrimaryDnsBE;
I _rttPrimaryDnsBK;
I _rttPrimaryDnsVI;
I _rttPrimaryDnsVO;
{?="timestamp"b1"rttGatewayBE"b1"rttGatewayBK"b1"rttGatewayVI"b1"rttGatewayVO"b1"rttPrimaryDnsBE"b1"rttPrimaryDnsBK"b1"rttPrimaryDnsVI"b1"rttPrimaryDnsVO"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasRttGatewayBE;
@property (TI,N,V_rttGatewayBE) rttGatewayBE;
@property (TB,N) hasRttGatewayBK;
@property (TI,N,V_rttGatewayBK) rttGatewayBK;
@property (TB,N) hasRttGatewayVO;
@property (TI,N,V_rttGatewayVO) rttGatewayVO;
@property (TB,N) hasRttGatewayVI;
@property (TI,N,V_rttGatewayVI) rttGatewayVI;
@property (TB,N) hasRttPrimaryDnsBE;
@property (TI,N,V_rttPrimaryDnsBE) rttPrimaryDnsBE;
@property (TB,N) hasRttPrimaryDnsBK;
@property (TI,N,V_rttPrimaryDnsBK) rttPrimaryDnsBK;
@property (TB,N) hasRttPrimaryDnsVO;
@property (TI,N,V_rttPrimaryDnsVO) rttPrimaryDnsVO;
@property (TB,N) hasRttPrimaryDnsVI;
@property (TI,N,V_rttPrimaryDnsVI) rttPrimaryDnsVI;
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats hasTimestamp];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats setHasTimestamp:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats setTimestamp:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats writeTo:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats mergeFrom:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats timestamp];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats hash];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats copyTo:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats description];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats readFrom:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats copyWithZone:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats isEqual:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats hasRttGatewayBE];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats hasRttGatewayVI];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats rttPrimaryDnsBK];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats rttPrimaryDnsVO];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats hasRttGatewayBK];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats hasRttGatewayVO];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats rttPrimaryDnsBE];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats rttPrimaryDnsVI];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats hasRttPrimaryDnsBE];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats hasRttPrimaryDnsBK];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats hasRttPrimaryDnsVI];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats hasRttPrimaryDnsVO];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats rttGatewayBE];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats rttGatewayBK];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats rttGatewayVI];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats rttGatewayVO];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats setHasRttGatewayBE:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats setHasRttGatewayBK:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats setHasRttGatewayVI:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats setHasRttGatewayVO:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats setHasRttPrimaryDnsBE:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats setHasRttPrimaryDnsBK:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats setHasRttPrimaryDnsVI:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats setHasRttPrimaryDnsVO:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats setRttGatewayBE:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats setRttGatewayBK:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats setRttGatewayVI:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats setRttGatewayVO:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats setRttPrimaryDnsBE:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats setRttPrimaryDnsBK:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats setRttPrimaryDnsVI:];
-[WiFiAnalyticsAWDWiFiDPSActiveProbeStats setRttPrimaryDnsVO:];
```
