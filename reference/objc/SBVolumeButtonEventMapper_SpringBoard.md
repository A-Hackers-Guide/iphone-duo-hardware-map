# `SBVolumeButtonEventMapper`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBUIActiveOrientationObserver`
- 4 instance variables, 8 properties, 18 instance methods, 7 class methods

## Instance variables

```
B _volumeButtonRemappingEnabled;
q _effectiveInterfaceOrientation;
Q _buttonsEdge;
q _layoutDirection;
```

## Properties

```
@property (TQ,N,V_buttonsEdge) buttonsEdge;
@property (Tq,N,V_effectiveInterfaceOrientation) effectiveInterfaceOrientation;
@property (Tq,N,V_layoutDirection) layoutDirection;
@property (TB,N,GisVolumeButtonRemappingEnabled,V_volumeButtonRemappingEnabled) volumeButtonRemappingEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBVolumeButtonEventMapper _shouldInvertVolumeButtonsForLTRRightEdgePadInInterfaceOrientation:];
+[SBVolumeButtonEventMapper _shouldInvertVolumeButtonsForLTRTopEdgePadInInterfaceOrientation:];
+[SBVolumeButtonEventMapper _shouldInvertVolumeButtonsForRTLRightEdgePadInInterfaceOrientation:];
+[SBVolumeButtonEventMapper _shouldInvertVolumeButtonsForRTLTopEdgePadInInterfaceOrientation:];
+[SBVolumeButtonEventMapper isVolumeButtonRemappingSupported];
+[SBVolumeButtonEventMapper isVolumeDownEnabledForScreenshots];
+[SBVolumeButtonEventMapper shouldInvertVolumeButtonsOnEdge:forInterfaceOrientation:userInterfaceLayoutDirection:];
```

## Instance methods

```
-[SBVolumeButtonEventMapper activeInterfaceOrientationDidChangeToOrientation:willAnimateWithDuration:fromOrientation:];
-[SBVolumeButtonEventMapper init];
-[SBVolumeButtonEventMapper setLayoutDirection:];
-[SBVolumeButtonEventMapper dealloc];
-[SBVolumeButtonEventMapper layoutDirection];
-[SBVolumeButtonEventMapper activeInterfaceOrientationWillChangeToOrientation:];
-[SBVolumeButtonEventMapper effectiveInterfaceOrientation];
-[SBVolumeButtonEventMapper setButtonsEdge:];
-[SBVolumeButtonEventMapper _hardwareDefaultsChanged];
-[SBVolumeButtonEventMapper _resetEffectiveInterfaceOrientation];
-[SBVolumeButtonEventMapper buttonsEdge];
-[SBVolumeButtonEventMapper isPreventingEffectiveInterfaceOrientationChanges];
-[SBVolumeButtonEventMapper isVolumeButtonEventInvertible:withPressType:];
-[SBVolumeButtonEventMapper isVolumeButtonRemappingEnabled];
-[SBVolumeButtonEventMapper physicalButtonKindForDeliveredPressType:event:];
-[SBVolumeButtonEventMapper setEffectiveInterfaceOrientation:];
-[SBVolumeButtonEventMapper setVolumeButtonRemappingEnabled:];
-[SBVolumeButtonEventMapper shouldInvertVolumeButtonsForEvent:withPressType:];
```
