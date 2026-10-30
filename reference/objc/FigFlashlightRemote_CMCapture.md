# `FigFlashlightRemote`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigFlashlight`
- 3 instance variables, 0 properties, 15 instance methods, 1 class methods

## Instance variables

```
Q _objectID;
B _connectionDied;
@"NSString" _loggingPrefix;
```

## Class methods

```
+[FigFlashlightRemote initialize];
```

## Instance methods

```
-[FigFlashlightRemote powerOn];
-[FigFlashlightRemote isAvailable];
-[FigFlashlightRemote debugDescription];
-[FigFlashlightRemote dealloc];
-[FigFlashlightRemote level];
-[FigFlashlightRemote setLevel:];
-[FigFlashlightRemote setLowCurrentTorchEnabled:];
-[FigFlashlightRemote isOverheated];
-[FigFlashlightRemote beamWidth];
-[FigFlashlightRemote setBeamWidth:];
-[FigFlashlightRemote initWithInitialAvailableOut:overheatedOut:levelOut:beamWidthOut:];
-[FigFlashlightRemote notifyForCurrentState];
-[FigFlashlightRemote powerOff];
-[FigFlashlightRemote _newBasicMessageWithOpcode:];
-[FigFlashlightRemote _sendBasicMessageWithOpcode:replyOut:];
```
