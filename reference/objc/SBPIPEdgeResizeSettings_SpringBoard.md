# `SBPIPEdgeResizeSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 7 instance variables, 7 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _disableCornerResizeForButtons;
B _blurNoteWhileResizing;
@"SBPIPEdgeResizeAnchorPointSettings" _anchorPointSettings;
d _liveResizePointerInteractionRegionOuterLength;
d _liveResizePointerInteractionRegionInnerLength;
d _liveResizePointerInteractionRegionCornerLength;
d _hysteresis;
```

## Properties

```
@property (T@"SBPIPEdgeResizeAnchorPointSettings",&,N,V_anchorPointSettings) anchorPointSettings;
@property (TB,N,V_disableCornerResizeForButtons) disableCornerResizeForButtons;
@property (TB,N,V_blurNoteWhileResizing) blurNoteWhileResizing;
@property (Td,N,V_liveResizePointerInteractionRegionOuterLength) liveResizePointerInteractionRegionOuterLength;
@property (Td,N,V_liveResizePointerInteractionRegionInnerLength) liveResizePointerInteractionRegionInnerLength;
@property (Td,N,V_liveResizePointerInteractionRegionCornerLength) liveResizePointerInteractionRegionCornerLength;
@property (Td,N,V_hysteresis) hysteresis;
```

## Class methods

```
+[SBPIPEdgeResizeSettings settingsControllerModule];
```

## Instance methods

```
-[SBPIPEdgeResizeSettings setHysteresis:];
-[SBPIPEdgeResizeSettings hysteresis];
-[SBPIPEdgeResizeSettings liveResizePointerInteractionRegionOuterLength];
-[SBPIPEdgeResizeSettings setLiveResizePointerInteractionRegionInnerLength:];
-[SBPIPEdgeResizeSettings setLiveResizePointerInteractionRegionOuterLength:];
-[SBPIPEdgeResizeSettings setDefaultValues];
-[SBPIPEdgeResizeSettings liveResizePointerInteractionRegionInnerLength];
-[SBPIPEdgeResizeSettings anchorPointSettings];
-[SBPIPEdgeResizeSettings blurNoteWhileResizing];
-[SBPIPEdgeResizeSettings disableCornerResizeForButtons];
-[SBPIPEdgeResizeSettings liveResizePointerInteractionRegionCornerLength];
-[SBPIPEdgeResizeSettings setAnchorPointSettings:];
-[SBPIPEdgeResizeSettings setBlurNoteWhileResizing:];
-[SBPIPEdgeResizeSettings setDisableCornerResizeForButtons:];
-[SBPIPEdgeResizeSettings setLiveResizePointerInteractionRegionCornerLength:];
```
