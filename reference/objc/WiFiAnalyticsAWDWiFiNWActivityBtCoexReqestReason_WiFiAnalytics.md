# `WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 15 instance variables, 28 properties, 65 instance methods, 0 class methods

## Instance variables

```
I _a2dp;
I _acl;
I _ble;
I _blescan;
I _esco;
I _inquiry;
I _inquiryscan;
I _mss;
I _other;
I _page;
I _pagescan;
I _park;
I _sco;
I _sniff;
{?="a2dp"b1"acl"b1"ble"b1"blescan"b1"esco"b1"inquiry"b1"inquiryscan"b1"mss"b1"other"b1"page"b1"pagescan"b1"park"b1"sco"b1"sniff"b1} _has;
```

## Properties

```
@property (TB,N) hasAcl;
@property (TI,N,V_acl) acl;
@property (TB,N) hasSco;
@property (TI,N,V_sco) sco;
@property (TB,N) hasEsco;
@property (TI,N,V_esco) esco;
@property (TB,N) hasA2dp;
@property (TI,N,V_a2dp) a2dp;
@property (TB,N) hasSniff;
@property (TI,N,V_sniff) sniff;
@property (TB,N) hasPagescan;
@property (TI,N,V_pagescan) pagescan;
@property (TB,N) hasInquiryscan;
@property (TI,N,V_inquiryscan) inquiryscan;
@property (TB,N) hasPage;
@property (TI,N,V_page) page;
@property (TB,N) hasInquiry;
@property (TI,N,V_inquiry) inquiry;
@property (TB,N) hasMss;
@property (TI,N,V_mss) mss;
@property (TB,N) hasPark;
@property (TI,N,V_park) park;
@property (TB,N) hasBle;
@property (TI,N,V_ble) ble;
@property (TB,N) hasBlescan;
@property (TI,N,V_blescan) blescan;
@property (TB,N) hasOther;
@property (TI,N,V_other) other;
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason ble];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason esco];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason other];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setHasBle:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason acl];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setAcl:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setHasSco:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason hasMss];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setPagescan:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setHasInquiryscan:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setHasPark:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason writeTo:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setEsco:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setBlescan:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setHasBlescan:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason hasPage];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason hasA2dp];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setHasInquiry:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason hasInquiry];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setHasPagescan:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setBle:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason mergeFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setHasEsco:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setHasAcl:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setInquiry:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setHasA2dp:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setPage:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setInquiryscan:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason hasEsco];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason hasPagescan];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason sco];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason park];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason hasInquiryscan];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason blescan];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setPark:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason a2dp];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason page];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason hasBlescan];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason hasSco];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setSniff:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason hasBle];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason hash];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason copyTo:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason inquiryscan];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason description];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason hasOther];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason inquiry];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason mss];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason sniff];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setMss:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setHasOther:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setHasSniff:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setHasPage:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setOther:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason readFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason hasPark];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason pagescan];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason copyWithZone:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason hasAcl];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setA2dp:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setSco:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason isEqual:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason hasSniff];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason setHasMss:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason dictionaryRepresentation];
```
