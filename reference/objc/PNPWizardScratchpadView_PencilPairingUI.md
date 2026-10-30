# `PNPWizardScratchpadView`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PKCanvasViewDelegate`, `PNPPencilInteractionEventDestination`
- 17 instance variables, 9 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"UIView" _backgroundView;
@"PNPWizardScratchpadCanvasView" _canvasView;
@"PNPWizardScratchpadCanvasView" _fingerDrawingCanvasView;
@"CAShapeLayer" _frameLayer;
@"PNPWizardInkWeightControl" _inkWeightControl;
B _inkWeightControlVisible;
q _selectedInkIndex;
q _previousMarkingToolIndex;
@"NSMutableArray" _inkViews;
@"NSArray" _colors;
@"UIView" _toolsBackgroundPillView;
@"PNPWizardScratchpadToast" _toastView;
@"NSTimer" _showToastTimer;
B _showingToast;
B _isDrawing;
Q _step;
@"<PNPWizardScratchpadViewDelegate>" _delegate;
```

## Properties

```
@property (TB,N,V_showingToast) showingToast;
@property (TB,N,V_isDrawing) isDrawing;
@property (TQ,N,V_step) step;
@property (T@"<PNPWizardScratchpadViewDelegate>",W,N,V_delegate) delegate;
@property (T{CGPoint=dd},R,N) pointForFirstTool;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PNPWizardScratchpadView step];
-[PNPWizardScratchpadView setStep:];
-[PNPWizardScratchpadView layoutSubviews];
-[PNPWizardScratchpadView isDrawing];
-[PNPWizardScratchpadView hitTest:withEvent:];
-[PNPWizardScratchpadView setDelegate:];
-[PNPWizardScratchpadView delegate];
-[PNPWizardScratchpadView initWithFrame:];
-[PNPWizardScratchpadView setIsDrawing:];
-[PNPWizardScratchpadView viewWillMoveToSuperview:];
-[PNPWizardScratchpadView _canvasViewWillBeginDrawing:];
-[PNPWizardScratchpadView canvasViewDidBeginDrawing:];
-[PNPWizardScratchpadView canvasViewDidEndDrawing:];
-[PNPWizardScratchpadView _initializeToastViewIfNecessary];
-[PNPWizardScratchpadView _animateAdjustmentSliderAppearance:];
-[PNPWizardScratchpadView _animateInkChange:];
-[PNPWizardScratchpadView _animateLayoutChange:];
-[PNPWizardScratchpadView _deselectAllInks];
-[PNPWizardScratchpadView _dismissToastNotification];
-[PNPWizardScratchpadView _inkViewPressed:];
-[PNPWizardScratchpadView _selectInkAtIndex:];
-[PNPWizardScratchpadView _selectedInk];
-[PNPWizardScratchpadView _selectedInkView];
-[PNPWizardScratchpadView _showToastNotificationAndAnimateStrokeAway];
-[PNPWizardScratchpadView _showToastNotificationWithInitialAnimation];
-[PNPWizardScratchpadView _triggerShowToastTimer];
-[PNPWizardScratchpadView _viewIsPartOfStylusCanvasView:];
-[PNPWizardScratchpadView clearCanvas];
-[PNPWizardScratchpadView eventSource:hadPencilDoubleTapped:];
-[PNPWizardScratchpadView pointForFirstTool];
-[PNPWizardScratchpadView prepareCanvasViews];
-[PNPWizardScratchpadView setShowingToast:];
-[PNPWizardScratchpadView showingToast];
```
