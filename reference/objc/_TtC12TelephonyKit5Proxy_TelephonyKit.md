# `_TtC12TelephonyKit5Proxy`

- Image: [`/System/Library/PrivateFrameworks/TelephonyKit.framework/TelephonyKit`](../userland/System__Library__PrivateFrameworks__TelephonyKit.framework__TelephonyKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtCs12_SwiftObject`
- Protocols: `_TtP12TelephonyKit9XPCClient_`
- 17 instance variables, 0 properties, 12 instance methods, 0 class methods

## Instance variables

```
TelephonyKit.XPCDaemonRole role;
os.OSAllocatedUnfairLock TelephonyKit.XPCDaemonState state;
TelephonyKit.XPCConnection connection;
TelephonyKit.Middleware ? middleware;
_$sScTyyt Swift.Never ? pendingInterruption;
TelephonyKit.PairingParameters ? pairingParameters;
_$sSD -> TelephonyKit.Selection TelephonyKit.Estimation estimations;
_$sSa -> TelephonyKit.TransferResult results;
_$sSh -> TelephonyKit.Selection selfSupportedSelections;
_$sSh -> TelephonyKit.Selection peerSupportedSelections;
_$sSD -> TelephonyKit.Selection _$sSh -> TelephonyKit.UIHint uiHints;
TelephonyKit.XPCDaemonState _$scSg -> stateUpdateHandler;
_$syycSg shutdownHandler;
TelephonyKit.Reason _$scSg -> errorHandler;
Swift.UInt64 _$scSg -> preflightFailureHandler;
_$sySd_SdSgtcSg progressUpdateHandler;
Swift.UInt16 _$scSg -> telemetrySessionIDHandler;
```

## Instance methods

```
-[_TtC12TelephonyKit5Proxy didUpdateProgressWithPercentComplete:estimatedSecondsRemaining:];
-[_TtC12TelephonyKit5Proxy didEstimateWithSelection:estimation:];
-[_TtC12TelephonyKit5Proxy didFailWithReason:];
-[_TtC12TelephonyKit5Proxy didReceiveCodeWithCode:];
-[_TtC12TelephonyKit5Proxy didReceiveSelectionOptionsWithSelfSupportedSelections:peerSupportedSelections:uiHints:];
-[_TtC12TelephonyKit5Proxy didReceiveTransferResultWithResult:];
-[_TtC12TelephonyKit5Proxy didShutdown];
-[_TtC12TelephonyKit5Proxy didUpdateStateWithState:];
-[_TtC12TelephonyKit5Proxy didUpdateTelemetrySessionID:];
-[_TtC12TelephonyKit5Proxy preflightFailedWithAdditionalBytesRequired:];
-[_TtC12TelephonyKit5Proxy processWithData:completionHandler:];
-[_TtC12TelephonyKit5Proxy roleWithCompletionHandler:];
```
