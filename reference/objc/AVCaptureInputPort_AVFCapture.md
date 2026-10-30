# `AVCaptureInputPort`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 7 properties, 27 instance methods, 3 class methods

## Instance variables

```
@"AVCaptureInputPortInternal" _internal;
```

## Properties

```
@property (T@"AVCaptureInput",R,N) input;
@property (T@"NSString",R,N) mediaType;
@property (T^{opaqueCMFormatDescription=},R,N) formatDescription;
@property (TB,N,GisEnabled) enabled;
@property (T^{OpaqueCMClock=},R,N) clock;
@property (T@"NSString",R,N) sourceDeviceType;
@property (Tq,R,N) sourceDevicePosition;
```

## Class methods

```
+[AVCaptureInputPort initialize];
+[AVCaptureInputPort portWithInput:mediaType:formatDescription:enabled:sourceDeviceType:sourceDevicePosition:];
+[AVCaptureInputPort automaticallyNotifiesObserversOfClock];
```

## Instance methods

```
-[AVCaptureInputPort formatDescription];
-[AVCaptureInputPort clock];
-[AVCaptureInputPort _updateCenterStageUnavailableReasonsWithDevice:deviceInput:];
-[AVCaptureInputPort input];
-[AVCaptureInputPort sourcesFromConstituentDevice];
-[AVCaptureInputPort changeSeed];
-[AVCaptureInputPort valueForUndefinedKey:];
-[AVCaptureInputPort _updateBackgroundBlurUnavailableReasonsWithDevice:deviceInput:];
-[AVCaptureInputPort _updateStudioLightingUnavailableReasonsWithDevice:deviceInput:];
-[AVCaptureInputPort _updateRingLightUnavailableReasonsWithDevice:deviceInput:];
-[AVCaptureInputPort _updateRingLightSupportedWithDevice:];
-[AVCaptureInputPort _setFormatDescription:];
-[AVCaptureInputPort dealloc];
-[AVCaptureInputPort setOwner:];
-[AVCaptureInputPort _updateReactionEffectsUnavailableReasonsWithDevice:deviceInput:];
-[AVCaptureInputPort sourceID];
-[AVCaptureInputPort bumpChangeSeed];
-[AVCaptureInputPort isEnabled];
-[AVCaptureInputPort sourceDeviceType];
-[AVCaptureInputPort _setClock:];
-[AVCaptureInputPort setEnabled:];
-[AVCaptureInputPort _updateBackgroundReplacementUnavailableReasonsWithDevice:deviceInput:];
-[AVCaptureInputPort description];
-[AVCaptureInputPort mediaType];
-[AVCaptureInputPort _initWithInput:mediaType:formatDescription:enabled:sourceDeviceType:sourceDevicePosition:];
-[AVCaptureInputPort figCaptureSourceConfigurationForSessionPreset:];
-[AVCaptureInputPort sourceDevicePosition];
```
