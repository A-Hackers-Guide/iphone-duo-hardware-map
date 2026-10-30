# `CWFDiagnosticReporter`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"SDRDiagnosticReporter" _ABCReporter;
```

## Class methods

```
+[CWFDiagnosticReporter sharedWiFiDiagnosticReporter];
```

## Instance methods

```
-[CWFDiagnosticReporter init];
-[CWFDiagnosticReporter initABCReporter];
-[CWFDiagnosticReporter removeRequestedBlockOnWiFiABCSignature:];
-[CWFDiagnosticReporter requestWiFiToBlockABCSignatureUntil:signature:];
-[CWFDiagnosticReporter submitWiFiDiagnosticReportType:reason:subtypeContext:];
```
