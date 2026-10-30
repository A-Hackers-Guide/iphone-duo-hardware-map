# `BLSHDiagnosticsHostPeer`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSDiagnosticsXPCHostInterface`, `BSInvalidatable`
- 9 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<BLSFlipbookDiagnosticsProviding>" _flipbookDiagnosticsProvider;
@"RBSProcessMonitor" _processMonitor;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"BLSDiagnosticFlipbookFrame" _lock_cachedFrameOnGlassNow;
@"BLSDiagnosticFlipbookFrame" _lock_cachedLastCancelledFrame;
i _clientPid;
B _clientIsTaskScheduled;
B _valid;
Q _entitlements;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHDiagnosticsHostPeer frameOnGlassWhenFlipbookLastCancelled];
-[BLSHDiagnosticsHostPeer dealloc];
-[BLSHDiagnosticsHostPeer invalidate];
-[BLSHDiagnosticsHostPeer frameOnGlassNow];
-[BLSHDiagnosticsHostPeer isValid];
-[BLSHDiagnosticsHostPeer description];
-[BLSHDiagnosticsHostPeer allFlipbookFrames];
-[BLSHDiagnosticsHostPeer _lock_validateHostFrame:source:];
-[BLSHDiagnosticsHostPeer genericSurfaceForFrameUUID:reply:name:surfaceFromFrame:];
-[BLSHDiagnosticsHostPeer hostFrameForUUID:];
-[BLSHDiagnosticsHostPeer initWithFlipbookDiagnosticsProvider:peer:];
-[BLSHDiagnosticsHostPeer rawSurfaceForFrameUUID:reply:];
-[BLSHDiagnosticsHostPeer surfaceForFrameUUID:reply:];
```
