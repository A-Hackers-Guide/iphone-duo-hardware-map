# `WiFiAnalyticsAWDWiFiNWActivityBtCoex`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 19 instance variables, 36 properties, 80 instance methods, 0 class methods

## Instance variables

```
I _a2dpdeny;
I _a2dpgrant;
I _aptxafterpm;
I _audiodeny;
I _audiogrant;
I _btabort;
@"WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason" _btrequestReason;
I _cts;
I _duration;
I _grant;
I _pm;
I _psnullretrycount;
I _request;
I _sniffdeny;
I _sniffgrant;
I _ucodehighlatency;
I _wlanrxpreempt;
I _wlantxpreempt;
{?="a2dpdeny"b1"a2dpgrant"b1"aptxafterpm"b1"audiodeny"b1"audiogrant"b1"btabort"b1"cts"b1"duration"b1"grant"b1"pm"b1"psnullretrycount"b1"request"b1"sniffdeny"b1"sniffgrant"b1"ucodehighlatency"b1"wlanrxpreempt"b1"wlantxpreempt"b1} _has;
```

## Properties

```
@property (TB,N) hasRequest;
@property (TI,N,V_request) request;
@property (TB,N) hasGrant;
@property (TI,N,V_grant) grant;
@property (TB,N) hasDuration;
@property (TI,N,V_duration) duration;
@property (TB,N) hasBtabort;
@property (TI,N,V_btabort) btabort;
@property (TB,N) hasPsnullretrycount;
@property (TI,N,V_psnullretrycount) psnullretrycount;
@property (TB,N) hasUcodehighlatency;
@property (TI,N,V_ucodehighlatency) ucodehighlatency;
@property (TB,N) hasCts;
@property (TI,N,V_cts) cts;
@property (TB,N) hasPm;
@property (TI,N,V_pm) pm;
@property (TB,N) hasWlantxpreempt;
@property (TI,N,V_wlantxpreempt) wlantxpreempt;
@property (TB,N) hasWlanrxpreempt;
@property (TI,N,V_wlanrxpreempt) wlanrxpreempt;
@property (TB,N) hasAptxafterpm;
@property (TI,N,V_aptxafterpm) aptxafterpm;
@property (TB,N) hasAudiogrant;
@property (TI,N,V_audiogrant) audiogrant;
@property (TB,N) hasAudiodeny;
@property (TI,N,V_audiodeny) audiodeny;
@property (TB,N) hasA2dpgrant;
@property (TI,N,V_a2dpgrant) a2dpgrant;
@property (TB,N) hasA2dpdeny;
@property (TI,N,V_a2dpdeny) a2dpdeny;
@property (TB,N) hasSniffgrant;
@property (TI,N,V_sniffgrant) sniffgrant;
@property (TB,N) hasSniffdeny;
@property (TI,N,V_sniffdeny) sniffdeny;
@property (TB,R,N) hasBtrequestReason;
@property (T@"WiFiAnalyticsAWDWiFiNWActivityBtCoexReqestReason",&,N,V_btrequestReason) btrequestReason;
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex hasRequest];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex hasWlantxpreempt];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex hasBtabort];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setHasWlanrxpreempt:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setUcodehighlatency:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex grant];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setA2dpgrant:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex hasA2dpgrant];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex writeTo:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex a2dpgrant];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex pm];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex audiodeny];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex wlantxpreempt];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setHasA2dpgrant:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex hasPm];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex mergeFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex hasDuration];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex hasAptxafterpm];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setHasGrant:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex hasPsnullretrycount];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setAudiodeny:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setHasWlantxpreempt:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex cts];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setGrant:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex sniffdeny];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex audiogrant];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex duration];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex request];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setHasDuration:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex aptxafterpm];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setA2dpdeny:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setHasCts:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex a2dpdeny];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setHasA2dpdeny:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setHasRequest:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setPm:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setHasPm:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setAudiogrant:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setHasSniffgrant:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setCts:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex wlanrxpreempt];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setBtrequestReason:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex psnullretrycount];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setWlanrxpreempt:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setHasPsnullretrycount:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex hash];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex copyTo:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setAptxafterpm:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex hasGrant];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex hasUcodehighlatency];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex description];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex hasSniffgrant];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setHasAptxafterpm:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setHasAudiogrant:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex hasAudiodeny];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex hasBtrequestReason];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setRequest:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex ucodehighlatency];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setDuration:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex readFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setHasSniffdeny:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex copyWithZone:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex hasSniffdeny];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setSniffdeny:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setPsnullretrycount:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex isEqual:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex btrequestReason];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex btabort];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setSniffgrant:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex hasAudiogrant];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setHasAudiodeny:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setHasBtabort:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex hasA2dpdeny];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex sniffgrant];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setWlantxpreempt:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setHasUcodehighlatency:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex setBtabort:];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex hasCts];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiNWActivityBtCoex hasWlanrxpreempt];
```
