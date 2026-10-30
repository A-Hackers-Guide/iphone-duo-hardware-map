# `BLSBacklightSceneVisualState`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`, `NSCopying`, `NSSecureCoding`
- 6 instance variables, 13 properties, 31 instance methods, 1 class methods

## Instance variables

```
B _dimmed;
B _flipbook;
B _lowPowerRendering;
q _activeAppearance;
q _updateFidelity;
q _adjustedLuminance;
```

## Properties

```
@property (Tq,R,N,V_activeAppearance) activeAppearance;
@property (Tq,R,N,V_updateFidelity) updateFidelity;
@property (Tq,R,N,V_adjustedLuminance) adjustedLuminance;
@property (TB,R,N,GisDimmed,V_dimmed) dimmed;
@property (TB,R,N,GisFlipbook,V_flipbook) flipbook;
@property (TB,R,N) flipbookUsesLowPowerRendering;
@property (TB,R,N,GisLowPowerRendering,V_lowPowerRendering) lowPowerRendering;
@property (Tq,R,N) grantedFidelity;
@property (Tq,R,N) expectedFidelity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSBacklightSceneVisualState supportsSecureCoding];
```

## Instance methods

```
-[BLSBacklightSceneVisualState flipbookUsesLowPowerRendering];
-[BLSBacklightSceneVisualState bls_loggingString];
-[BLSBacklightSceneVisualState updateFidelity];
-[BLSBacklightSceneVisualState bls_shortLoggingString];
-[BLSBacklightSceneVisualState isFlipbook];
-[BLSBacklightSceneVisualState initWithActiveAppearance:updateFidelity:adjustedLuminance:dimmed:flipbook:];
-[BLSBacklightSceneVisualState init];
-[BLSBacklightSceneVisualState initWithXPCDictionary:];
-[BLSBacklightSceneVisualState isDimmed];
-[BLSBacklightSceneVisualState activeAppearance];
-[BLSBacklightSceneVisualState isEqualToVisualStateIgnoringFlipbookAndLowPowerRendering:];
-[BLSBacklightSceneVisualState adjustedLuminance];
-[BLSBacklightSceneVisualState isLowPowerRendering];
-[BLSBacklightSceneVisualState isEssentiallyEqualToVisualState:];
-[BLSBacklightSceneVisualState newVisualStateWithUpdateFidelity:];
-[BLSBacklightSceneVisualState encodeWithXPCDictionary:];
-[BLSBacklightSceneVisualState expectedFidelity];
-[BLSBacklightSceneVisualState newVisualStateWithUpdateFidelity:flipbook:lowPowerRendering:];
-[BLSBacklightSceneVisualState isEqualToVisualStateIgnoringFlipbook:];
-[BLSBacklightSceneVisualState encodeWithCoder:];
-[BLSBacklightSceneVisualState initWithActiveAppearance:updateFidelity:adjustedLuminance:dimmed:];
-[BLSBacklightSceneVisualState hash];
-[BLSBacklightSceneVisualState isEqualAppearanceToVisualState:];
-[BLSBacklightSceneVisualState description];
-[BLSBacklightSceneVisualState newVisualStateWithFlipbookUsesLowPowerRendering:];
-[BLSBacklightSceneVisualState initWithCoder:];
-[BLSBacklightSceneVisualState initWithActiveAppearance:updateFidelity:adjustedLuminance:];
-[BLSBacklightSceneVisualState copyWithZone:];
-[BLSBacklightSceneVisualState grantedFidelity];
-[BLSBacklightSceneVisualState isEqual:];
-[BLSBacklightSceneVisualState initWithActiveAppearance:updateFidelity:adjustedLuminance:dimmed:flipbook:lowPowerRendering:];
```
