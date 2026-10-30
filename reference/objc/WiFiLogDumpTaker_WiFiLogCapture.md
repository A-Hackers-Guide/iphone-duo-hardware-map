# `WiFiLogDumpTaker`

- Image: [`/System/Library/PrivateFrameworks/WiFiLogCapture.framework/WiFiLogCapture`](../userland/System__Library__PrivateFrameworks__WiFiLogCapture.framework__WiFiLogCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" event_queue;
@"NSObject<OS_xpc_object>" xpc_connection;
B _didLastCaptureFallback;
```

## Properties

```
@property (TB,R,N,V_didLastCaptureFallback) didLastCaptureFallback;
```

## Instance methods

```
-[WiFiLogDumpTaker init];
-[WiFiLogDumpTaker handleConnection:];
-[WiFiLogDumpTaker XPCConnection:];
-[WiFiLogDumpTaker didLastCaptureFallback];
-[WiFiLogDumpTaker takeWiFiCoreCaptureDumpWithReason:callback:];
-[WiFiLogDumpTaker takeWiFiDiagnosticsDumpWithPath:reason:callback:];
-[WiFiLogDumpTaker takeWiFiDiagnosticsDumpWithPath:reason:shouldTryFallback:callback:];
-[WiFiLogDumpTaker takeWiFiDiagnosticsDumpWithPathAndReason:::];
```
