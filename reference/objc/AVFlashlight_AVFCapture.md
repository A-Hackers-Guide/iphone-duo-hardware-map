# `AVFlashlight`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 7 properties, 17 instance methods, 2 class methods

## Instance variables

```
@"AVFlashlightInternal" _internal;
```

## Properties

```
@property (TB,R,N,GisAvailable) available;
@property (TB,R,N,GisOverheated) overheated;
@property (Tf,R,N) flashlightLevel;
@property (TB,R,N) beamWidthControlSupported;
@property (Tf,R,N) minBeamWidth;
@property (Tf,R,N) maxBeamWidth;
@property (Tf,N) beamWidth;
```

## Class methods

```
+[AVFlashlight initialize];
+[AVFlashlight hasFlashlight];
```

## Instance methods

```
-[AVFlashlight isAvailable];
-[AVFlashlight _handleNotification:payload:];
-[AVFlashlight init];
-[AVFlashlight dealloc];
-[AVFlashlight isOverheated];
-[AVFlashlight beamWidth];
-[AVFlashlight setBeamWidth:];
-[AVFlashlight flashlightLevel];
-[AVFlashlight _reconnectToServer];
-[AVFlashlight _setupFlashlightPreservingState:];
-[AVFlashlight _teardownFlashlight];
-[AVFlashlight beamWidthControlSupported];
-[AVFlashlight maxBeamWidth];
-[AVFlashlight minBeamWidth];
-[AVFlashlight setFlashlightLevel:withError:];
-[AVFlashlight turnPowerOff];
-[AVFlashlight turnPowerOnWithError:];
```
