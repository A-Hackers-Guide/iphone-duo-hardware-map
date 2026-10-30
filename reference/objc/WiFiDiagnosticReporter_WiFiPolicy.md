# `WiFiDiagnosticReporter`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"SDRDiagnosticReporter" _ABCReporter;
```

## Class methods

```
+[WiFiDiagnosticReporter sharedWiFiDiagnosticReporter];
```

## Instance methods

```
-[WiFiDiagnosticReporter init];
-[WiFiDiagnosticReporter initABCReporter];
-[WiFiDiagnosticReporter isWiFiABCSignatureUnblocked:];
-[WiFiDiagnosticReporter submitWiFiWatchdogReason:subtypeContext:];
```
