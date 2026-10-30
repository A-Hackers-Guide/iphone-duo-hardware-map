# `WiFiUsageParsedBeacon`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 49 instance variables, 49 properties, 113 instance methods, 5 class methods

## Instance variables

```
C _htRxNSS;
C _htTxNSS;
C _vhtRxNSS;
C _vhtTxNSS;
C _heRxNSS;
C _heTxNSS;
B _colocated6Ghz;
B _parsingSuccessful;
C _channel;
C _band;
C _htAMPDUParams;
C _htAntennaSelection;
B _colocated6GhzIsPSC;
B _hasHT;
B _hasVHT;
B _hasHE;
B _hasEHT;
B _hasColocatedMLD2G;
B _hasColocatedMLD5G;
B _hasColocatedMLD6G;
C _ap6gPowerMode;
S _beaconInterval;
S _capabilities;
S _htInfo;
S _htExtendedCapabilities;
S _vhtRxMCSMap;
S _vhtRxMaxRate;
S _vhtTxMCSMap;
S _vhtTxMaxRate;
S _heRxMCSMap80MHz;
S _heTxMCSMap80MHz;
S _heRxMCSMap160MHz;
S _heTxMCSMap160MHz;
S _heRxMCSMap8080MHz;
S _heTxMCSMap8080MHz;
I _htTxBFCapabilities;
I _vhtInfo;
I _shortSSID;
@"NSString" _apName;
@"NSMutableDictionary" _taggedIEList;
@"NSMutableDictionary" _vendorIEList;
@"NSMutableDictionary" _extendedIEList;
@"NSString" _lastParsedOK;
@"NSNumber" _isBeaconAtHeRate;
@"NSString" _bssid;
@"NSData" _htMCSSet;
@"NSData" _heMACInfo;
@"NSData" _hePHYInfo;
@"NSString" _ssid;
```

## Properties

```
@property (T@"NSString",&,N,V_bssid) bssid;
@property (T@"NSString",&,N,V_ssid) ssid;
@property (TI,N,V_shortSSID) shortSSID;
@property (T@"NSString",&,N,V_apName) apName;
@property (T@"NSNumber",N,V_isBeaconAtHeRate) isBeaconAtHeRate;
@property (TS,N,V_beaconInterval) beaconInterval;
@property (TS,N,V_capabilities) capabilities;
@property (TC,N,V_channel) channel;
@property (TC,N,V_band) band;
@property (TB,N,V_colocated6Ghz) colocated6Ghz;
@property (TB,N,V_colocated6GhzIsPSC) colocated6GhzIsPSC;
@property (TB,N,V_hasHT) hasHT;
@property (TS,N,V_htInfo) htInfo;
@property (TC,N,V_htAMPDUParams) htAMPDUParams;
@property (TS,N,V_htExtendedCapabilities) htExtendedCapabilities;
@property (TI,N,V_htTxBFCapabilities) htTxBFCapabilities;
@property (TC,N,V_htAntennaSelection) htAntennaSelection;
@property (TC,N,V_htRxNSS) htRxNSS;
@property (TC,N,V_htTxNSS) htTxNSS;
@property (TB,N,V_hasVHT) hasVHT;
@property (TI,N,V_vhtInfo) vhtInfo;
@property (TS,N,V_vhtRxMCSMap) vhtRxMCSMap;
@property (TS,N,V_vhtRxMaxRate) vhtRxMaxRate;
@property (TS,N,V_vhtTxMCSMap) vhtTxMCSMap;
@property (TS,N,V_vhtTxMaxRate) vhtTxMaxRate;
@property (TC,N,V_vhtRxNSS) vhtRxNSS;
@property (TC,N,V_vhtTxNSS) vhtTxNSS;
@property (TB,N,V_hasHE) hasHE;
@property (T@"NSData",&,N,V_heMACInfo) heMACInfo;
@property (T@"NSData",&,N,V_hePHYInfo) hePHYInfo;
@property (TS,N,V_heRxMCSMap80MHz) heRxMCSMap80MHz;
@property (TS,N,V_heTxMCSMap80MHz) heTxMCSMap80MHz;
@property (TS,N,V_heRxMCSMap160MHz) heRxMCSMap160MHz;
@property (TS,N,V_heTxMCSMap160MHz) heTxMCSMap160MHz;
@property (TS,N,V_heRxMCSMap8080MHz) heRxMCSMap8080MHz;
@property (TS,N,V_heTxMCSMap8080MHz) heTxMCSMap8080MHz;
@property (TC,N,V_heRxNSS) heRxNSS;
@property (TC,N,V_heTxNSS) heTxNSS;
@property (TB,N,V_hasEHT) hasEHT;
@property (TB,N,V_hasColocatedMLD2G) hasColocatedMLD2G;
@property (TB,N,V_hasColocatedMLD5G) hasColocatedMLD5G;
@property (TB,N,V_hasColocatedMLD6G) hasColocatedMLD6G;
@property (TC,N,V_ap6gPowerMode) ap6gPowerMode;
@property (T@"NSMutableDictionary",&,N,V_taggedIEList) taggedIEList;
@property (T@"NSMutableDictionary",&,N,V_vendorIEList) vendorIEList;
@property (T@"NSMutableDictionary",&,N,V_extendedIEList) extendedIEList;
@property (TB,N,V_parsingSuccessful) parsingSuccessful;
@property (T@"NSString",&,N,V_lastParsedOK) lastParsedOK;
@property (T@"NSData",R,N,V_htMCSSet) htMCSSet;
```

## Class methods

```
+[WiFiUsageParsedBeacon defaults];
+[WiFiUsageParsedBeacon config];
+[WiFiUsageParsedBeacon initialize];
+[WiFiUsageParsedBeacon updateConfig];
+[WiFiUsageParsedBeacon isValidIE:ofLen:withIsExtended:];
```

## Instance methods

```
-[WiFiUsageParsedBeacon setChannel:];
-[WiFiUsageParsedBeacon ssid];
-[WiFiUsageParsedBeacon setSsid:];
-[WiFiUsageParsedBeacon channel];
-[WiFiUsageParsedBeacon setShortSSID:];
-[WiFiUsageParsedBeacon band];
-[WiFiUsageParsedBeacon setBssid:];
-[WiFiUsageParsedBeacon shortSSID];
-[WiFiUsageParsedBeacon setBand:];
-[WiFiUsageParsedBeacon capabilities];
-[WiFiUsageParsedBeacon description];
-[WiFiUsageParsedBeacon bssid];
-[WiFiUsageParsedBeacon setCapabilities:];
-[WiFiUsageParsedBeacon dictionaryRepresentation];
-[WiFiUsageParsedBeacon heRxNSS];
-[WiFiUsageParsedBeacon heTxNSS];
-[WiFiUsageParsedBeacon htTxNSS];
-[WiFiUsageParsedBeacon parseHE6GHz:length:endOfBuffer:];
-[WiFiUsageParsedBeacon parseHTCapa:length:endOfBuffer:];
-[WiFiUsageParsedBeacon setVhtTxMCSMap:];
-[WiFiUsageParsedBeacon vhtInfo];
-[WiFiUsageParsedBeacon heRxMCSMap80MHz];
-[WiFiUsageParsedBeacon heTxMCSMap80MHz];
-[WiFiUsageParsedBeacon htRxNSS];
-[WiFiUsageParsedBeacon parseApName:length:endOfBuffer:];
-[WiFiUsageParsedBeacon parseHECapa:length:endOfBuffer:];
-[WiFiUsageParsedBeacon setVhtRxMCSMap:];
-[WiFiUsageParsedBeacon ap6gPowerMode];
-[WiFiUsageParsedBeacon apName];
-[WiFiUsageParsedBeacon beaconInterval];
-[WiFiUsageParsedBeacon colocated6Ghz];
-[WiFiUsageParsedBeacon colocated6GhzIsPSC];
-[WiFiUsageParsedBeacon extendedIEList];
-[WiFiUsageParsedBeacon hasColocatedMLD2G];
-[WiFiUsageParsedBeacon hasColocatedMLD5G];
-[WiFiUsageParsedBeacon hasColocatedMLD6G];
-[WiFiUsageParsedBeacon hasEHT];
-[WiFiUsageParsedBeacon hasHE];
-[WiFiUsageParsedBeacon hasHT];
-[WiFiUsageParsedBeacon hasVHT];
-[WiFiUsageParsedBeacon heMACInfo];
-[WiFiUsageParsedBeacon hePHYInfo];
-[WiFiUsageParsedBeacon heRxMCSMap160MHz];
-[WiFiUsageParsedBeacon heRxMCSMap8080MHz];
-[WiFiUsageParsedBeacon heTxMCSMap160MHz];
-[WiFiUsageParsedBeacon heTxMCSMap8080MHz];
-[WiFiUsageParsedBeacon htAMPDUParams];
-[WiFiUsageParsedBeacon htAntennaSelection];
-[WiFiUsageParsedBeacon htExtendedCapabilities];
-[WiFiUsageParsedBeacon htInfo];
-[WiFiUsageParsedBeacon htMCSSet];
-[WiFiUsageParsedBeacon htTxBFCapabilities];
-[WiFiUsageParsedBeacon initWithBeaconData:andAdditionalMetadata:];
-[WiFiUsageParsedBeacon isBeaconAtHeRate];
-[WiFiUsageParsedBeacon lastParsedOK];
-[WiFiUsageParsedBeacon parseBeaconIE:endOfBuffer:];
-[WiFiUsageParsedBeacon parseDSSS:length:endOfBuffer:];
-[WiFiUsageParsedBeacon parseEHTCapa:length:endOfBuffer:];
-[WiFiUsageParsedBeacon parseExtendedIE:from:length:endOfBuffer:];
-[WiFiUsageParsedBeacon parseHTOp:length:endOfBuffer:];
-[WiFiUsageParsedBeacon parseNormalIE:from:length:endOfBuffer:];
-[WiFiUsageParsedBeacon parseRNR:length:endOfBuffer:];
-[WiFiUsageParsedBeacon parseSSID:length:endOfBuffer:];
-[WiFiUsageParsedBeacon parseVHTCapa:length:endOfBuffer:];
-[WiFiUsageParsedBeacon parsingSuccessful];
-[WiFiUsageParsedBeacon setAp6gPowerMode:];
-[WiFiUsageParsedBeacon setApName:];
-[WiFiUsageParsedBeacon setBeaconInterval:];
-[WiFiUsageParsedBeacon setColocated6Ghz:];
-[WiFiUsageParsedBeacon setColocated6GhzIsPSC:];
-[WiFiUsageParsedBeacon setExtendedIEList:];
-[WiFiUsageParsedBeacon setHasColocatedMLD2G:];
-[WiFiUsageParsedBeacon setHasColocatedMLD5G:];
-[WiFiUsageParsedBeacon setHasColocatedMLD6G:];
-[WiFiUsageParsedBeacon setHasEHT:];
-[WiFiUsageParsedBeacon setHasHE:];
-[WiFiUsageParsedBeacon setHasHT:];
-[WiFiUsageParsedBeacon setHasVHT:];
-[WiFiUsageParsedBeacon setHeMACInfo:];
-[WiFiUsageParsedBeacon setHePHYInfo:];
-[WiFiUsageParsedBeacon setHeRxMCSMap160MHz:];
-[WiFiUsageParsedBeacon setHeRxMCSMap8080MHz:];
-[WiFiUsageParsedBeacon setHeRxMCSMap80MHz:];
-[WiFiUsageParsedBeacon setHeRxNSS:];
-[WiFiUsageParsedBeacon setHeTxMCSMap160MHz:];
-[WiFiUsageParsedBeacon setHeTxMCSMap8080MHz:];
-[WiFiUsageParsedBeacon setHeTxMCSMap80MHz:];
-[WiFiUsageParsedBeacon setHeTxNSS:];
-[WiFiUsageParsedBeacon setHtAMPDUParams:];
-[WiFiUsageParsedBeacon setHtAntennaSelection:];
-[WiFiUsageParsedBeacon setHtExtendedCapabilities:];
-[WiFiUsageParsedBeacon setHtInfo:];
-[WiFiUsageParsedBeacon setHtRxNSS:];
-[WiFiUsageParsedBeacon setHtTxBFCapabilities:];
-[WiFiUsageParsedBeacon setHtTxNSS:];
-[WiFiUsageParsedBeacon setIsBeaconAtHeRate:];
-[WiFiUsageParsedBeacon setLastParsedOK:];
-[WiFiUsageParsedBeacon setParsingSuccessful:];
-[WiFiUsageParsedBeacon setTaggedIEList:];
-[WiFiUsageParsedBeacon setVendorIEList:];
-[WiFiUsageParsedBeacon setVhtInfo:];
-[WiFiUsageParsedBeacon setVhtRxMaxRate:];
-[WiFiUsageParsedBeacon setVhtRxNSS:];
-[WiFiUsageParsedBeacon setVhtTxMaxRate:];
-[WiFiUsageParsedBeacon setVhtTxNSS:];
-[WiFiUsageParsedBeacon taggedIEList];
-[WiFiUsageParsedBeacon vendorIEList];
-[WiFiUsageParsedBeacon vhtRxMCSMap];
-[WiFiUsageParsedBeacon vhtRxMaxRate];
-[WiFiUsageParsedBeacon vhtRxNSS];
-[WiFiUsageParsedBeacon vhtTxMCSMap];
-[WiFiUsageParsedBeacon vhtTxMaxRate];
-[WiFiUsageParsedBeacon vhtTxNSS];
```
