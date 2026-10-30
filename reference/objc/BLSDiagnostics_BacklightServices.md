# `BLSDiagnostics`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSDiagnosticFlipbookFrameSurfaceProvider`, `BLSFlipbookDiagnosticsProviding`, `BSInvalidatable`
- 2 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"BSServiceDispatchQueue" _callbackQueue;
@"BSServiceInitiatingConnection" _connection;
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
-[BLSDiagnostics frameOnGlassWhenFlipbookLastCancelled];
-[BLSDiagnostics init];
-[BLSDiagnostics invalidate];
-[BLSDiagnostics frameWithUUID:];
-[BLSDiagnostics frameOnGlassNow];
-[BLSDiagnostics allFlipbookFrames];
-[BLSDiagnostics rawSurfaceForFrame:];
-[BLSDiagnostics surfaceForFrame:];
```
