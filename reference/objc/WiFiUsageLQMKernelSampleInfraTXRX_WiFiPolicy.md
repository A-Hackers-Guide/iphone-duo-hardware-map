# `WiFiUsageLQMKernelSampleInfraTXRX`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiUsageLQMSample`
- 36 instance variables, 36 properties, 73 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _timestamp;
d _duration;
Q _decodingAttempts;
Q _rxStartOverDecodingAttemptsPercentage;
Q _rxBadPlcpOverDecodingAttemptsPercentage;
Q _rxCrsGlitchOverDecodingAttemptsPercentage;
Q _rxDecodingErrorsOverRxStart;
Q _rxUcastOverRxStart;
Q _rxBeaconOverRxStart;
Q _rxFrmTooLongOverDecodingErrors;
Q _rxFrmTooShrtOverDecodingErrors;
Q _rxAnyErrOverDecodingErrors;
Q _rxBadFCSOverDecodingErrors;
Q _rxResponseTimeoutOverDecodingErrors;
Q _rxNoDelimOverDecodingErrors;
Q _rxFifo0OvflOverDecodingErrors;
Q _rxFifo1OvflOverDecodingErrors;
Q _rxUcastDataPercentage;
Q _rxUcastMgmtPercentage;
Q _rxUcastCtrlPercentage;
Q _rxUcastRTSOverRxCtrlFrmsPercentage;
Q _rxUcastCTSOverRxCtrlFrmsPercentage;
Q _rxBACKOverRxCtrlFrmsPercentage;
Q _rxUcastACKOverRxCtrlFrmsPercentage;
Q _rxBeaconMbss;
Q _rxBeaconObss;
Q _txAllFrm;
Q _txPhyErrorOverTxAllFrmPercentage;
Q _txAMPDUOverTxAllFrmPercentage;
Q _txUcastOverTxAllFrmPercentage;
Q _txCtrlFrms;
Q _txRTSOverTxCtrlFrmsPercentage;
Q _txCTSOverTxCtrlFrmsPercentage;
Q _txBACKOverTxCtrlFrmsPercentage;
Q _txACKOverTxCtrlFrmsPercentage;
Q _txRTSFailOvertxRTS;
```

## Properties

```
@property (T@"NSDate",&,N,V_timestamp) timestamp;
@property (TQ,N,V_decodingAttempts) decodingAttempts;
@property (TQ,N,V_rxStartOverDecodingAttemptsPercentage) rxStartOverDecodingAttemptsPercentage;
@property (TQ,N,V_rxBadPlcpOverDecodingAttemptsPercentage) rxBadPlcpOverDecodingAttemptsPercentage;
@property (TQ,N,V_rxCrsGlitchOverDecodingAttemptsPercentage) rxCrsGlitchOverDecodingAttemptsPercentage;
@property (TQ,N,V_rxDecodingErrorsOverRxStart) rxDecodingErrorsOverRxStart;
@property (TQ,N,V_rxUcastOverRxStart) rxUcastOverRxStart;
@property (TQ,N,V_rxBeaconOverRxStart) rxBeaconOverRxStart;
@property (TQ,N,V_rxFrmTooLongOverDecodingErrors) rxFrmTooLongOverDecodingErrors;
@property (TQ,N,V_rxFrmTooShrtOverDecodingErrors) rxFrmTooShrtOverDecodingErrors;
@property (TQ,N,V_rxAnyErrOverDecodingErrors) rxAnyErrOverDecodingErrors;
@property (TQ,N,V_rxBadFCSOverDecodingErrors) rxBadFCSOverDecodingErrors;
@property (TQ,N,V_rxResponseTimeoutOverDecodingErrors) rxResponseTimeoutOverDecodingErrors;
@property (TQ,N,V_rxNoDelimOverDecodingErrors) rxNoDelimOverDecodingErrors;
@property (TQ,N,V_rxFifo0OvflOverDecodingErrors) rxFifo0OvflOverDecodingErrors;
@property (TQ,N,V_rxFifo1OvflOverDecodingErrors) rxFifo1OvflOverDecodingErrors;
@property (TQ,N,V_rxUcastDataPercentage) rxUcastDataPercentage;
@property (TQ,N,V_rxUcastMgmtPercentage) rxUcastMgmtPercentage;
@property (TQ,N,V_rxUcastCtrlPercentage) rxUcastCtrlPercentage;
@property (TQ,N,V_rxUcastRTSOverRxCtrlFrmsPercentage) rxUcastRTSOverRxCtrlFrmsPercentage;
@property (TQ,N,V_rxUcastCTSOverRxCtrlFrmsPercentage) rxUcastCTSOverRxCtrlFrmsPercentage;
@property (TQ,N,V_rxBACKOverRxCtrlFrmsPercentage) rxBACKOverRxCtrlFrmsPercentage;
@property (TQ,N,V_rxUcastACKOverRxCtrlFrmsPercentage) rxUcastACKOverRxCtrlFrmsPercentage;
@property (TQ,N,V_rxBeaconMbss) rxBeaconMbss;
@property (TQ,N,V_rxBeaconObss) rxBeaconObss;
@property (TQ,N,V_txAllFrm) txAllFrm;
@property (TQ,N,V_txPhyErrorOverTxAllFrmPercentage) txPhyErrorOverTxAllFrmPercentage;
@property (TQ,N,V_txAMPDUOverTxAllFrmPercentage) txAMPDUOverTxAllFrmPercentage;
@property (TQ,N,V_txUcastOverTxAllFrmPercentage) txUcastOverTxAllFrmPercentage;
@property (TQ,N,V_txCtrlFrms) txCtrlFrms;
@property (TQ,N,V_txRTSOverTxCtrlFrmsPercentage) txRTSOverTxCtrlFrmsPercentage;
@property (TQ,N,V_txCTSOverTxCtrlFrmsPercentage) txCTSOverTxCtrlFrmsPercentage;
@property (TQ,N,V_txBACKOverTxCtrlFrmsPercentage) txBACKOverTxCtrlFrmsPercentage;
@property (TQ,N,V_txACKOverTxCtrlFrmsPercentage) txACKOverTxCtrlFrmsPercentage;
@property (TQ,N,V_txRTSFailOvertxRTS) txRTSFailOvertxRTS;
@property (Td,N,V_duration) duration;
```

## Class methods

```
+[WiFiUsageLQMKernelSampleInfraTXRX sampleWithStruct:WithReferenceDate:AsNsec:];
```

## Instance methods

```
-[WiFiUsageLQMKernelSampleInfraTXRX setTimestamp:];
-[WiFiUsageLQMKernelSampleInfraTXRX decodingAttempts];
-[WiFiUsageLQMKernelSampleInfraTXRX timestamp];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxStartOverDecodingAttemptsPercentage:];
-[WiFiUsageLQMKernelSampleInfraTXRX duration];
-[WiFiUsageLQMKernelSampleInfraTXRX setTxRTSFailOvertxRTS:];
-[WiFiUsageLQMKernelSampleInfraTXRX rxBadPlcpOverDecodingAttemptsPercentage];
-[WiFiUsageLQMKernelSampleInfraTXRX rxStartOverDecodingAttemptsPercentage];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxCrsGlitchOverDecodingAttemptsPercentage:];
-[WiFiUsageLQMKernelSampleInfraTXRX setDecodingAttempts:];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxBadPlcpOverDecodingAttemptsPercentage:];
-[WiFiUsageLQMKernelSampleInfraTXRX setDuration:];
-[WiFiUsageLQMKernelSampleInfraTXRX rxCrsGlitchOverDecodingAttemptsPercentage];
-[WiFiUsageLQMKernelSampleInfraTXRX txRTSFailOvertxRTS];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxDecodingErrorsOverRxStart:];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxNoDelimOverDecodingErrors:];
-[WiFiUsageLQMKernelSampleInfraTXRX initWithStruct:WithReferenceDate:AsNsec:];
-[WiFiUsageLQMKernelSampleInfraTXRX rxAnyErrOverDecodingErrors];
-[WiFiUsageLQMKernelSampleInfraTXRX rxBACKOverRxCtrlFrmsPercentage];
-[WiFiUsageLQMKernelSampleInfraTXRX rxBadFCSOverDecodingErrors];
-[WiFiUsageLQMKernelSampleInfraTXRX rxBeaconMbss];
-[WiFiUsageLQMKernelSampleInfraTXRX rxBeaconObss];
-[WiFiUsageLQMKernelSampleInfraTXRX rxBeaconOverRxStart];
-[WiFiUsageLQMKernelSampleInfraTXRX rxDecodingErrorsOverRxStart];
-[WiFiUsageLQMKernelSampleInfraTXRX rxFifo0OvflOverDecodingErrors];
-[WiFiUsageLQMKernelSampleInfraTXRX rxFifo1OvflOverDecodingErrors];
-[WiFiUsageLQMKernelSampleInfraTXRX rxFrmTooLongOverDecodingErrors];
-[WiFiUsageLQMKernelSampleInfraTXRX rxFrmTooShrtOverDecodingErrors];
-[WiFiUsageLQMKernelSampleInfraTXRX rxNoDelimOverDecodingErrors];
-[WiFiUsageLQMKernelSampleInfraTXRX rxResponseTimeoutOverDecodingErrors];
-[WiFiUsageLQMKernelSampleInfraTXRX rxUcastACKOverRxCtrlFrmsPercentage];
-[WiFiUsageLQMKernelSampleInfraTXRX rxUcastCTSOverRxCtrlFrmsPercentage];
-[WiFiUsageLQMKernelSampleInfraTXRX rxUcastCtrlPercentage];
-[WiFiUsageLQMKernelSampleInfraTXRX rxUcastDataPercentage];
-[WiFiUsageLQMKernelSampleInfraTXRX rxUcastMgmtPercentage];
-[WiFiUsageLQMKernelSampleInfraTXRX rxUcastOverRxStart];
-[WiFiUsageLQMKernelSampleInfraTXRX rxUcastRTSOverRxCtrlFrmsPercentage];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxAnyErrOverDecodingErrors:];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxBACKOverRxCtrlFrmsPercentage:];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxBadFCSOverDecodingErrors:];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxBeaconMbss:];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxBeaconObss:];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxBeaconOverRxStart:];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxFifo0OvflOverDecodingErrors:];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxFifo1OvflOverDecodingErrors:];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxFrmTooLongOverDecodingErrors:];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxFrmTooShrtOverDecodingErrors:];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxResponseTimeoutOverDecodingErrors:];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxUcastACKOverRxCtrlFrmsPercentage:];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxUcastCTSOverRxCtrlFrmsPercentage:];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxUcastCtrlPercentage:];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxUcastDataPercentage:];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxUcastMgmtPercentage:];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxUcastOverRxStart:];
-[WiFiUsageLQMKernelSampleInfraTXRX setRxUcastRTSOverRxCtrlFrmsPercentage:];
-[WiFiUsageLQMKernelSampleInfraTXRX setTxACKOverTxCtrlFrmsPercentage:];
-[WiFiUsageLQMKernelSampleInfraTXRX setTxAMPDUOverTxAllFrmPercentage:];
-[WiFiUsageLQMKernelSampleInfraTXRX setTxAllFrm:];
-[WiFiUsageLQMKernelSampleInfraTXRX setTxBACKOverTxCtrlFrmsPercentage:];
-[WiFiUsageLQMKernelSampleInfraTXRX setTxCTSOverTxCtrlFrmsPercentage:];
-[WiFiUsageLQMKernelSampleInfraTXRX setTxCtrlFrms:];
-[WiFiUsageLQMKernelSampleInfraTXRX setTxPhyErrorOverTxAllFrmPercentage:];
-[WiFiUsageLQMKernelSampleInfraTXRX setTxRTSOverTxCtrlFrmsPercentage:];
-[WiFiUsageLQMKernelSampleInfraTXRX setTxUcastOverTxAllFrmPercentage:];
-[WiFiUsageLQMKernelSampleInfraTXRX txACKOverTxCtrlFrmsPercentage];
-[WiFiUsageLQMKernelSampleInfraTXRX txAMPDUOverTxAllFrmPercentage];
-[WiFiUsageLQMKernelSampleInfraTXRX txAllFrm];
-[WiFiUsageLQMKernelSampleInfraTXRX txBACKOverTxCtrlFrmsPercentage];
-[WiFiUsageLQMKernelSampleInfraTXRX txCTSOverTxCtrlFrmsPercentage];
-[WiFiUsageLQMKernelSampleInfraTXRX txCtrlFrms];
-[WiFiUsageLQMKernelSampleInfraTXRX txPhyErrorOverTxAllFrmPercentage];
-[WiFiUsageLQMKernelSampleInfraTXRX txRTSOverTxCtrlFrmsPercentage];
-[WiFiUsageLQMKernelSampleInfraTXRX txUcastOverTxAllFrmPercentage];
```
