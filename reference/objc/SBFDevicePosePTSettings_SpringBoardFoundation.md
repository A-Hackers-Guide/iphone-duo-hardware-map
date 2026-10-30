# `SBFDevicePosePTSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 16 instance variables, 16 properties, 33 instance methods, 1 class methods

## Instance variables

```
B _continuousFoldTransitionEnabled;
d _partiallyOpenToOpenFlatBoundary;
d _openTransitionBeginBoundary;
d _closeTransitionBeginBoundary;
d _transitionAutoCompleteDuration;
d _swapDegreesForContinuousLiveStyle;
d _swapDegreesForContinuousSnapshotStyleWhenOpening;
d _swapDegreesForContinuousSnapshotStyleWhenClosing;
d _swapDegreesForFadeInFadeOutStyle;
d _autocompleteMinDelay;
d _autocompleteMaxDelay;
d _displayPrewarmDuration;
d _velocitySmoothingFactor;
d _likelyToOpenVelocityDegreesPerSecond;
d _enterFoldAvoidancePredictionWindow;
d _sustainFoldAvoidancePredictionWindow;
```

## Properties

```
@property (TB,N,V_continuousFoldTransitionEnabled) continuousFoldTransitionEnabled;
@property (Td,N,V_partiallyOpenToOpenFlatBoundary) partiallyOpenToOpenFlatBoundary;
@property (Td,N,V_openTransitionBeginBoundary) openTransitionBeginBoundary;
@property (Td,N,V_closeTransitionBeginBoundary) closeTransitionBeginBoundary;
@property (Td,N,V_transitionAutoCompleteDuration) transitionAutoCompleteDuration;
@property (Td,N,V_swapDegreesForContinuousLiveStyle) swapDegreesForContinuousLiveStyle;
@property (Td,N,V_swapDegreesForContinuousSnapshotStyleWhenOpening) swapDegreesForContinuousSnapshotStyleWhenOpening;
@property (Td,N,V_swapDegreesForContinuousSnapshotStyleWhenClosing) swapDegreesForContinuousSnapshotStyleWhenClosing;
@property (Td,N,V_swapDegreesForFadeInFadeOutStyle) swapDegreesForFadeInFadeOutStyle;
@property (Td,N,V_autocompleteMinDelay) autocompleteMinDelay;
@property (Td,N,V_autocompleteMaxDelay) autocompleteMaxDelay;
@property (Td,N,V_displayPrewarmDuration) displayPrewarmDuration;
@property (Td,N,V_velocitySmoothingFactor) velocitySmoothingFactor;
@property (Td,N,V_likelyToOpenVelocityDegreesPerSecond) likelyToOpenVelocityDegreesPerSecond;
@property (Td,N,V_enterFoldAvoidancePredictionWindow) enterFoldAvoidancePredictionWindow;
@property (Td,N,V_sustainFoldAvoidancePredictionWindow) sustainFoldAvoidancePredictionWindow;
```

## Class methods

```
+[SBFDevicePosePTSettings settingsControllerModule];
```

## Instance methods

```
-[SBFDevicePosePTSettings setDefaultValues];
-[SBFDevicePosePTSettings partiallyOpenToOpenFlatBoundary];
-[SBFDevicePosePTSettings setOpenTransitionBeginBoundary:];
-[SBFDevicePosePTSettings continuousFoldTransitionEnabled];
-[SBFDevicePosePTSettings autocompleteMaxDelay];
-[SBFDevicePosePTSettings autocompleteMinDelay];
-[SBFDevicePosePTSettings closeTransitionBeginBoundary];
-[SBFDevicePosePTSettings displayPrewarmDuration];
-[SBFDevicePosePTSettings enterFoldAvoidancePredictionWindow];
-[SBFDevicePosePTSettings likelyToOpenVelocityDegreesPerSecond];
-[SBFDevicePosePTSettings openTransitionBeginBoundary];
-[SBFDevicePosePTSettings setAutocompleteMaxDelay:];
-[SBFDevicePosePTSettings setAutocompleteMinDelay:];
-[SBFDevicePosePTSettings setCloseTransitionBeginBoundary:];
-[SBFDevicePosePTSettings setContinuousFoldTransitionEnabled:];
-[SBFDevicePosePTSettings setDisplayPrewarmDuration:];
-[SBFDevicePosePTSettings setEnterFoldAvoidancePredictionWindow:];
-[SBFDevicePosePTSettings setLikelyToOpenVelocityDegreesPerSecond:];
-[SBFDevicePosePTSettings setPartiallyOpenToOpenFlatBoundary:];
-[SBFDevicePosePTSettings setSustainFoldAvoidancePredictionWindow:];
-[SBFDevicePosePTSettings setSwapDegreesForContinuousLiveStyle:];
-[SBFDevicePosePTSettings setSwapDegreesForContinuousSnapshotStyleWhenClosing:];
-[SBFDevicePosePTSettings setSwapDegreesForContinuousSnapshotStyleWhenOpening:];
-[SBFDevicePosePTSettings setSwapDegreesForFadeInFadeOutStyle:];
-[SBFDevicePosePTSettings setTransitionAutoCompleteDuration:];
-[SBFDevicePosePTSettings setVelocitySmoothingFactor:];
-[SBFDevicePosePTSettings sustainFoldAvoidancePredictionWindow];
-[SBFDevicePosePTSettings swapDegreesForContinuousLiveStyle];
-[SBFDevicePosePTSettings swapDegreesForContinuousSnapshotStyleWhenClosing];
-[SBFDevicePosePTSettings swapDegreesForContinuousSnapshotStyleWhenOpening];
-[SBFDevicePosePTSettings swapDegreesForFadeInFadeOutStyle];
-[SBFDevicePosePTSettings transitionAutoCompleteDuration];
-[SBFDevicePosePTSettings velocitySmoothingFactor];
```
