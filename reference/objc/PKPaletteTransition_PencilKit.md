# `PKPaletteTransition`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 10 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"<PKPaletteTransitionDelegate>" _delegate;
q _initialVisualState;
q _targetVisualState;
q _intermediateVisualState;
q _pointingDirection;
@"NSArray" __remainingTransitionStages;
@"UIViewFloatAnimatableProperty" _rotationAngleAnimatableProperty;
@"UIViewFloatAnimatableProperty" _expandedToCollapsedAnimatableProperty;
```

## Properties

```
@property (Tq,N,S_setTargetVisualState:,V_targetVisualState) targetVisualState;
@property (Tq,N,S_setIntermediateVisualState:,V_intermediateVisualState) intermediateVisualState;
@property (Tq,N,S_setPointingDirection:,V_pointingDirection) pointingDirection;
@property (T@"NSArray",&,N,V__remainingTransitionStages) _remainingTransitionStages;
@property (T@"UIViewFloatAnimatableProperty",&,N,V_rotationAngleAnimatableProperty) rotationAngleAnimatableProperty;
@property (T@"UIViewFloatAnimatableProperty",&,N,V_expandedToCollapsedAnimatableProperty) expandedToCollapsedAnimatableProperty;
@property (T@"<PKPaletteTransitionDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisTransitionInProgress) transitionInProgress;
@property (Tq,R,N,V_initialVisualState) initialVisualState;
@property (Td,R,N) expandedToCollapsedRatio;
```

## Instance methods

```
-[PKPaletteTransition targetVisualState];
-[PKPaletteTransition setDelegate:];
-[PKPaletteTransition isTransitionInProgress];
-[PKPaletteTransition delegate];
-[PKPaletteTransition rotationAngleAnimatableProperty];
-[PKPaletteTransition _canMoveToNextTransitionStage];
-[PKPaletteTransition _currentStage];
-[PKPaletteTransition _handleExpandedToCollapsedAnimatablePropertyPresentationValueChanged];
-[PKPaletteTransition _handleRotationAnimatablePropertyPresentationValueChanged];
-[PKPaletteTransition _moveToNextTransitionStageIfReady];
-[PKPaletteTransition _remainingTransitionStages];
-[PKPaletteTransition _setIntermediateVisualState:];
-[PKPaletteTransition _setPointingDirection:];
-[PKPaletteTransition _setTargetVisualState:];
-[PKPaletteTransition expandedToCollapsedAnimatableProperty];
-[PKPaletteTransition expandedToCollapsedRatio];
-[PKPaletteTransition initWithInitialVisualState:];
-[PKPaletteTransition initialVisualState];
-[PKPaletteTransition intermediateVisualState];
-[PKPaletteTransition paletteDidBeginResizingAnimation];
-[PKPaletteTransition paletteDidBeginRotationAnimation];
-[PKPaletteTransition pointingDirection];
-[PKPaletteTransition setExpandedToCollapsedAnimatableProperty:];
-[PKPaletteTransition setRotationAngleAnimatableProperty:];
-[PKPaletteTransition set_remainingTransitionStages:];
-[PKPaletteTransition transitionToVisualState:];
```
