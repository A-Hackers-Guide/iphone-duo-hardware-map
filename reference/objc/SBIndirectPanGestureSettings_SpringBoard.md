# `SBIndirectPanGestureSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 6 instance variables, 6 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _shouldRequirePointerEventMovement;
d _trackpadHysteresis;
d _mouseHysteresis;
d _mouseActivationDistance;
d _orthogonalTranslationAdjustmentFactor;
d _dockProgressThresholdForPresentingDock;
```

## Properties

```
@property (Td,N,V_trackpadHysteresis) trackpadHysteresis;
@property (Td,N,V_mouseHysteresis) mouseHysteresis;
@property (Td,N,V_mouseActivationDistance) mouseActivationDistance;
@property (Td,N,V_orthogonalTranslationAdjustmentFactor) orthogonalTranslationAdjustmentFactor;
@property (Td,N,V_dockProgressThresholdForPresentingDock) dockProgressThresholdForPresentingDock;
@property (TB,N,V_shouldRequirePointerEventMovement) shouldRequirePointerEventMovement;
```

## Class methods

```
+[SBIndirectPanGestureSettings settingsControllerModule];
```

## Instance methods

```
-[SBIndirectPanGestureSettings trackpadHysteresis];
-[SBIndirectPanGestureSettings setShouldRequirePointerEventMovement:];
-[SBIndirectPanGestureSettings setDefaultValues];
-[SBIndirectPanGestureSettings setMouseHysteresis:];
-[SBIndirectPanGestureSettings mouseHysteresis];
-[SBIndirectPanGestureSettings setTrackpadHysteresis:];
-[SBIndirectPanGestureSettings shouldRequirePointerEventMovement];
-[SBIndirectPanGestureSettings dockProgressThresholdForPresentingDock];
-[SBIndirectPanGestureSettings mouseActivationDistance];
-[SBIndirectPanGestureSettings orthogonalTranslationAdjustmentFactor];
-[SBIndirectPanGestureSettings setDockProgressThresholdForPresentingDock:];
-[SBIndirectPanGestureSettings setMouseActivationDistance:];
-[SBIndirectPanGestureSettings setOrthogonalTranslationAdjustmentFactor:];
```
