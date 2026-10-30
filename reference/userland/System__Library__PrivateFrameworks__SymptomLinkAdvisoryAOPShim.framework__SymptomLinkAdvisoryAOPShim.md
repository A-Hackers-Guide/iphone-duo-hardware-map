# `/System/Library/PrivateFrameworks/SymptomLinkAdvisoryAOPShim.framework/SymptomLinkAdvisoryAOPShim`

iOS 27.2 dyld shared cache image. Version `251.40.7.0.0`. **[DSC]**

## Linked libraries (7)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/Security.framework/Security`

## Objective-C: 4 classes, 0 protocols, 79 methods, 31 properties

### Class pages

Every class and protocol, with its methods: [`SLAInterfaceStats`](../objc/SLAInterfaceStats_SymptomLinkAdvisoryAOPShim.md), [`SLASnapshot`](../objc/SLASnapshot_SymptomLinkAdvisoryAOPShim.md), [`SLATelemetrySnapshot`](../objc/SLATelemetrySnapshot_SymptomLinkAdvisoryAOPShim.md), [`SymptomLinkAdvisoryAOPShim`](../objc/SymptomLinkAdvisoryAOPShim_SymptomLinkAdvisoryAOPShim.md)

### Classes

`SLAInterfaceStats`, `SLASnapshot`, `SLATelemetrySnapshot`, `SymptomLinkAdvisoryAOPShim`

### Properties

```
@property (TQ,N,V_txBytes) txBytes;
@property (TQ,N,V_rxBytes) rxBytes;
@property (TS,N,V_activeFlowCount) activeFlowCount;
@property (T@"NSNumber",&,N,V_avgRTTMs) avgRTTMs;
@property (T@"NSNumber",&,N,V_minRTTMs) minRTTMs;
@property (T@"NSNumber",&,N,V_maxRTTVarianceMs) maxRTTVarianceMs;
@property (TQ,N,V_retransmittedBytes) retransmittedBytes;
@property (TQ,N,V_duplicateBytes) duplicateBytes;
@property (TQ,N,V_outOfOrderBytes) outOfOrderBytes;
@property (TS,N,V_connProbeFailureCount) connProbeFailureCount;
@property (TS,N,V_readProbeFailureCount) readProbeFailureCount;
@property (TS,N,V_writeProbeFailureCount) writeProbeFailureCount;
@property (TI,N,V_aggregationWindowMs) aggregationWindowMs;
@property (TC,N,V_reportReason) reportReason;
@property (T@"SLAInterfaceStats",&,N,V_wifiStats) wifiStats;
@property (T@"SLAInterfaceStats",&,N,V_bluetoothStats) bluetoothStats;
@property (T@"SLAInterfaceStats",&,N,V_wiredStats) wiredStats;
@property (T@"NSNumber",&,N,V_batteryPercentage) batteryPercentage;
@property (T@"NSNumber",&,N,V_isPluggedIn) isPluggedIn;
@property (T@"NSNumber",&,N,V_thermalPressure) thermalPressure;
@property (T@"NSNumber",&,N,V_transferActive) transferActive;
@property (T@"NSNumber",&,N,V_activeTransferEstimatedTotal) activeTransferEstimatedTotal;
@property (T@"NSNumber",&,N,V_activeTransferRemainingBytes) activeTransferRemainingBytes;
@property (TI,N,V_periodDurationSec) periodDurationSec;
@property (TI,N,V_snapshotsProcessed) snapshotsProcessed;
@property (TI,N,V_recommendationChanges) recommendationChanges;
@property (TI,N,V_frictionEventsWiFi) frictionEventsWiFi;
@property (TI,N,V_frictionEventsBT) frictionEventsBT;
@property (TI,N,V_stallEventsWiFi) stallEventsWiFi;
@property (TI,N,V_stallEventsBT) stallEventsBT;
@property (TI,N,V_liveLinkAdvisories) liveLinkAdvisories;
```

## Strings (42)

```
Client missing required entitlement
RPC interface close failed: %d
3
TB_ASSERT: (server->gettelemetry != ((void*)0)) && \"implementation for GetTelemetry is not present\"
/Library/Caches/com.apple.xbs/236004E1-A52B-48CC-92D8-0A3096B3CEC6/TemporaryDirectory.BreRZD/Binaries/RTKitNet_AP_Libraries/install/TempContent/Objects/RtKitNet.build/SymptomLinkAdvisoryAOPShim.build/DerivedSources/autolinkupgrade.c
TB_FATAL: unrecognized selector: %llu
rev
%s-%s-%s
ALUminium service not found
com.apple.aop2.ulpn.aluminium.ap.client
v40@?0{aluminium_aluminiumtelemetrysnapshot_s=IIIIIIII}8
com.apple.symptoms.linkAdvisory.ULPN
Battery percentage must be 0-100
aop_framework
autolinkupgrade.c
TB_ASSERT: (err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \"unexpected tb_error_t returned\"
com.apple.aop2.ulpn.aluminium
TB_ASSERT: (server->reportsnapshot != ((void*)0)) && \"implementation for ReportSnapshot is not present\"
TB_FATAL: unrecognized selector: %llu (%s:%d)\n
^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[97c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16
TB_FATAL: invalid value: unexpected case value, %llx
Tightbeam init failed: %u
v12@?0i8
Tightbeam call failed: %u
TB_ASSERT: (server->enable != ((void*)0)) && \"implementation for Enable is not present\"
TB_ASSERT: (cmp.encoded) && \"completion block must be called before returning\"
com.apple.symptoms.linkAdvisory
Missing entitlement: com.apple.symptoms.linkAdvisory.ULPN
v8@?0
Service not initialized
Report reason must be 0-3
I40@?0{aluminium_aluminiumtelemetrysnapshot_s=IIIIIIII}8
fwd
IONameMatch
RPC interface open failed: %d
Snapshot cannot be nil
I12@?0i8
ALUminium enable/disable failed
Thermal pressure level must be 0-5
TB_FATAL: invalid value: unexpected case value, %llx (%s:%d)\n
ALUminium reportSnapshot failed
AFKEndpointInterface
```
