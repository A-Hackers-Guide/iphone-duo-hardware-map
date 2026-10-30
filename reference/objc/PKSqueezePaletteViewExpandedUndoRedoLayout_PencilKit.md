# `PKSqueezePaletteViewExpandedUndoRedoLayout`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIHyperInteractorDelegate`, `PKSqueezePaletteViewLayout`
- 21 instance variables, 24 properties, 47 instance methods, 0 class methods

## Instance variables

```
B _isTicksFadedOutAtHead;
B _isTicksFadedOutAtTail;
B _isUpdateUIRunning;
@"PKSqueezePaletteView" _paletteView;
@"PKSqueezePaletteViewExpandedUndoRedoLayoutContext" _context;
q _maxUndoIndex;
q _currentUndoIndex;
q _modelUndoIndex;
q _initialUndoIndex;
d _sliderButtonAngle;
d _initialSliderButtonAngle;
@"UIButtonConfiguration" _originalSliderButtonConfiguration;
@"UIButtonConfiguration" _sliderButtonConfiguration;
@"CAShapeLayer" _ornamentLayer;
@"NSMutableArray" _tickLayers;
@"UIPanGestureRecognizer" _panGestureRecognizer;
@"NSLayoutConstraint" _sliderButtonConstraintCenterX;
@"NSLayoutConstraint" _sliderButtonConstraintCenterY;
@"_UIHyperInteractor" _hyperInteractor;
@"UINotificationFeedbackGenerator" _feedbackGenerator;
Q _senderIDForLastPanGesture;
```

## Properties

```
@property (Tq,V_maxUndoIndex) maxUndoIndex;
@property (Tq,V_currentUndoIndex) currentUndoIndex;
@property (Tq,V_modelUndoIndex) modelUndoIndex;
@property (Tq,V_initialUndoIndex) initialUndoIndex;
@property (Td,N,V_sliderButtonAngle) sliderButtonAngle;
@property (Td,N,V_initialSliderButtonAngle) initialSliderButtonAngle;
@property (T@"UIButtonConfiguration",&,N,V_originalSliderButtonConfiguration) originalSliderButtonConfiguration;
@property (T@"UIButtonConfiguration",&,N,V_sliderButtonConfiguration) sliderButtonConfiguration;
@property (T@"CAShapeLayer",&,N,V_ornamentLayer) ornamentLayer;
@property (T@"NSMutableArray",&,N,V_tickLayers) tickLayers;
@property (T@"UIPanGestureRecognizer",&,N,V_panGestureRecognizer) panGestureRecognizer;
@property (TB,V_isTicksFadedOutAtHead) isTicksFadedOutAtHead;
@property (TB,V_isTicksFadedOutAtTail) isTicksFadedOutAtTail;
@property (TB,V_isUpdateUIRunning) isUpdateUIRunning;
@property (T@"NSLayoutConstraint",&,N,V_sliderButtonConstraintCenterX) sliderButtonConstraintCenterX;
@property (T@"NSLayoutConstraint",&,N,V_sliderButtonConstraintCenterY) sliderButtonConstraintCenterY;
@property (T@"_UIHyperInteractor",&,N,V_hyperInteractor) hyperInteractor;
@property (T@"UINotificationFeedbackGenerator",&,N,V_feedbackGenerator) feedbackGenerator;
@property (TQ,N,V_senderIDForLastPanGesture) senderIDForLastPanGesture;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"PKSqueezePaletteView",W,N,V_paletteView) paletteView;
```

## Instance methods

```
-[PKSqueezePaletteViewExpandedUndoRedoLayout panGestureRecognizer];
-[PKSqueezePaletteViewExpandedUndoRedoLayout setFeedbackGenerator:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout feedbackGenerator];
-[PKSqueezePaletteViewExpandedUndoRedoLayout _hyperInteractorApplyPresentationPoint:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout setPanGestureRecognizer:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout setupUI];
-[PKSqueezePaletteViewExpandedUndoRedoLayout updateUI];
-[PKSqueezePaletteViewExpandedUndoRedoLayout hyperInteractor];
-[PKSqueezePaletteViewExpandedUndoRedoLayout setPaletteView:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout _didTapSliderButton:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout _panGestureHandler:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout currentUndoIndex];
-[PKSqueezePaletteViewExpandedUndoRedoLayout handlePencilInteractionDidTap:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout initialSliderButtonAngle];
-[PKSqueezePaletteViewExpandedUndoRedoLayout initialUndoIndex];
-[PKSqueezePaletteViewExpandedUndoRedoLayout isTicksFadedOutAtHead];
-[PKSqueezePaletteViewExpandedUndoRedoLayout isTicksFadedOutAtTail];
-[PKSqueezePaletteViewExpandedUndoRedoLayout isUpdateUIRunning];
-[PKSqueezePaletteViewExpandedUndoRedoLayout maxUndoIndex];
-[PKSqueezePaletteViewExpandedUndoRedoLayout modelUndoIndex];
-[PKSqueezePaletteViewExpandedUndoRedoLayout originalSliderButtonConfiguration];
-[PKSqueezePaletteViewExpandedUndoRedoLayout ornamentLayer];
-[PKSqueezePaletteViewExpandedUndoRedoLayout paletteView];
-[PKSqueezePaletteViewExpandedUndoRedoLayout senderIDForLastPanGesture];
-[PKSqueezePaletteViewExpandedUndoRedoLayout setCurrentUndoIndex:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout setHyperInteractor:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout setInitialSliderButtonAngle:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout setInitialUndoIndex:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout setIsTicksFadedOutAtHead:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout setIsTicksFadedOutAtTail:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout setIsUpdateUIRunning:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout setMaxUndoIndex:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout setModelUndoIndex:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout setOriginalSliderButtonConfiguration:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout setOrnamentLayer:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout setSenderIDForLastPanGesture:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout setSliderButtonAngle:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout setSliderButtonConfiguration:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout setSliderButtonConstraintCenterX:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout setSliderButtonConstraintCenterY:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout setTickLayers:];
-[PKSqueezePaletteViewExpandedUndoRedoLayout sliderButtonAngle];
-[PKSqueezePaletteViewExpandedUndoRedoLayout sliderButtonConfiguration];
-[PKSqueezePaletteViewExpandedUndoRedoLayout sliderButtonConstraintCenterX];
-[PKSqueezePaletteViewExpandedUndoRedoLayout sliderButtonConstraintCenterY];
-[PKSqueezePaletteViewExpandedUndoRedoLayout tickLayers];
-[PKSqueezePaletteViewExpandedUndoRedoLayout willTransitionToLayout:];
```
