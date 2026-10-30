# `PLBasebandEurekaMessage`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLBasebandMessage`
- 6 instance variables, 7 properties, 58 instance methods, 0 class methods

## Instance variables

```
C _skip;
^{_PLBasebandEventHeader={_PLBasebandMessageHeader=C}I[8C]C} _header;
@"NSData" _payload;
^{_PLBasebandSystemSelectionEvent=S} _ssevent;
* _ssaction;
* _ssstate;
```

## Properties

```
@property (T^{_PLBasebandEventHeader={_PLBasebandMessageHeader=C}I[8C]C},V_header) header;
@property (T@"NSData",&,V_payload) payload;
@property (T^{_PLBasebandSystemSelectionEvent=S},V_ssevent) ssevent;
@property (T*,V_ssaction) ssaction;
@property (T*,V_ssstate) ssstate;
@property (TC,V_skip) skip;
@property (TI,R) eventCode;
```

## Instance methods

```
-[PLBasebandEurekaMessage header];
-[PLBasebandEurekaMessage setHeader:];
-[PLBasebandEurekaMessage payload];
-[PLBasebandEurekaMessage setPayload:];
-[PLBasebandEurekaMessage parseData:];
-[PLBasebandEurekaMessage initWithData:];
-[PLBasebandEurekaMessage skip];
-[PLBasebandEurekaMessage setSkip:];
-[PLBasebandEurekaMessage payloadString];
-[PLBasebandEurekaMessage eventCode];
-[PLBasebandEurekaMessage eventStringOOS:];
-[PLBasebandEurekaMessage ssevent];
-[PLBasebandEurekaMessage stateStringACC:];
-[PLBasebandEurekaMessage stateStringLTE:];
-[PLBasebandEurekaMessage callTypeString:];
-[PLBasebandEurekaMessage cdmaExitString:];
-[PLBasebandEurekaMessage eventStringACC:];
-[PLBasebandEurekaMessage smgmmEventType:];
-[PLBasebandEurekaMessage ssstate];
-[PLBasebandEurekaMessage stateStringGSM:];
-[PLBasebandEurekaMessage stateStringOOS:];
-[PLBasebandEurekaMessage actionSystemSelection];
-[PLBasebandEurekaMessage cellUpdateCause:];
-[PLBasebandEurekaMessage cellularSystemStringSystemSelection:];
-[PLBasebandEurekaMessage convertCMCallConnectPayloadToDictionary:];
-[PLBasebandEurekaMessage convertCMCallConnectV2PayloadToDictionary:];
-[PLBasebandEurekaMessage convertCMCallOrigPayloadToDictionary:];
-[PLBasebandEurekaMessage convertCMCallOrigV2PayloadToDictionary:];
-[PLBasebandEurekaMessage estCauseLTE:];
-[PLBasebandEurekaMessage establishmentCauseStringWCDMA:];
-[PLBasebandEurekaMessage eventSystemSelection];
-[PLBasebandEurekaMessage iratHOStringLTE:];
-[PLBasebandEurekaMessage iratStringLTE:];
-[PLBasebandEurekaMessage logWithLogger:];
-[PLBasebandEurekaMessage pagingCauseWCDMA:];
-[PLBasebandEurekaMessage pagingTypeWCDMA:];
-[PLBasebandEurekaMessage procedureStringPSSI:];
-[PLBasebandEurekaMessage ratStringPSSI:];
-[PLBasebandEurekaMessage relCauseLTE:];
-[PLBasebandEurekaMessage releaseCauseStringWCDMA:];
-[PLBasebandEurekaMessage scanTypeStartWCDMA:];
-[PLBasebandEurekaMessage scanTypeStopWCDMA:];
-[PLBasebandEurekaMessage searchPhaseStringPSSI:];
-[PLBasebandEurekaMessage setSsaction:];
-[PLBasebandEurekaMessage setSsevent:];
-[PLBasebandEurekaMessage setSsstate:];
-[PLBasebandEurekaMessage soCallTypeString:];
-[PLBasebandEurekaMessage ssaction];
-[PLBasebandEurekaMessage stateStringHSDPA:];
-[PLBasebandEurekaMessage stateStringHSPAPLUS_DC:];
-[PLBasebandEurekaMessage stateStringHSUPA:];
-[PLBasebandEurekaMessage stateStringMotion:];
-[PLBasebandEurekaMessage stateStringUTRANL1:];
-[PLBasebandEurekaMessage stateStringWCDMA:];
-[PLBasebandEurekaMessage stateSystemSelection];
-[PLBasebandEurekaMessage stringForUnknownBytes:];
-[PLBasebandEurekaMessage termStringSystemSelection:];
-[PLBasebandEurekaMessage tooShortErrorString];
```
