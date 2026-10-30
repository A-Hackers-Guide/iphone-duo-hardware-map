# `BKSMousePointerDevicePreferences`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `BSProtobufSerializable`
- 9 instance variables, 13 properties, 27 instance methods, 3 class methods

## Instance variables

```
B _enableNaturalScrolling;
B _enableTapToClick;
B _enableTwoFingerSecondaryClick;
f _pointerAccelerationFactor;
f _scrollAccelerationFactor;
q _clickHapticStrength;
q _doubleTapDragMode;
q _buttonConfigurationForHardwareButtonMice;
q _buttonConfigurationForVirtualButtonMice;
```

## Properties

```
@property (Tf,N,V_pointerAccelerationFactor) pointerAccelerationFactor;
@property (Tf,N,V_scrollAccelerationFactor) scrollAccelerationFactor;
@property (TB,N,V_enableNaturalScrolling) enableNaturalScrolling;
@property (TB,N,V_enableTapToClick) enableTapToClick;
@property (TB,N,V_enableTwoFingerSecondaryClick) enableTwoFingerSecondaryClick;
@property (Tq,N,V_clickHapticStrength) clickHapticStrength;
@property (Tq,N,V_doubleTapDragMode) doubleTapDragMode;
@property (Tq,N,V_buttonConfigurationForHardwareButtonMice) buttonConfigurationForHardwareButtonMice;
@property (Tq,N,V_buttonConfigurationForVirtualButtonMice) buttonConfigurationForVirtualButtonMice;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSMousePointerDevicePreferences supportsSecureCoding];
+[BKSMousePointerDevicePreferences protobufSchema];
+[BKSMousePointerDevicePreferences defaultPreferencesForHardwareType:];
```

## Instance methods

```
-[BKSMousePointerDevicePreferences didFinishProtobufDecodingWithError:];
-[BKSMousePointerDevicePreferences setClickHapticStrength:];
-[BKSMousePointerDevicePreferences enableTwoFingerSecondaryClick];
-[BKSMousePointerDevicePreferences initForProtobufDecoding];
-[BKSMousePointerDevicePreferences init];
-[BKSMousePointerDevicePreferences buttonConfigurationForHardwareButtonMice];
-[BKSMousePointerDevicePreferences setEnableNaturalScrolling:];
-[BKSMousePointerDevicePreferences enableTapToClick];
-[BKSMousePointerDevicePreferences doubleTapDragMode];
-[BKSMousePointerDevicePreferences setEnableTwoFingerSecondaryClick:];
-[BKSMousePointerDevicePreferences setPointerAccelerationFactor:];
-[BKSMousePointerDevicePreferences setEnableTapToClick:];
-[BKSMousePointerDevicePreferences clickHapticStrength];
-[BKSMousePointerDevicePreferences encodeWithCoder:];
-[BKSMousePointerDevicePreferences hash];
-[BKSMousePointerDevicePreferences description];
-[BKSMousePointerDevicePreferences initWithCoder:];
-[BKSMousePointerDevicePreferences pointerAccelerationFactor];
-[BKSMousePointerDevicePreferences enableNaturalScrolling];
-[BKSMousePointerDevicePreferences isEqual:];
-[BKSMousePointerDevicePreferences setButtonConfigurationForVirtualButtonMice:];
-[BKSMousePointerDevicePreferences scrollAccelerationFactor];
-[BKSMousePointerDevicePreferences setButtonConfigurationForHardwareButtonMice:];
-[BKSMousePointerDevicePreferences setDoubleTapDragMode:];
-[BKSMousePointerDevicePreferences setScrollAccelerationFactor:];
-[BKSMousePointerDevicePreferences buttonConfigurationForVirtualButtonMice];
-[BKSMousePointerDevicePreferences _fixMissingButtonConfigurations];
```
