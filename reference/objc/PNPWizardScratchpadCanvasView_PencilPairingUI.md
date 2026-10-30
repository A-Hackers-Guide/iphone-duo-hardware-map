# `PNPWizardScratchpadCanvasView`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 5 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _snapshotImageViews;
@"PKInk" _ink;
@"<PKCanvasViewDelegate>" _canvasViewDelegate;
B _showingSnapshot;
@"PKCanvasView" _canvasView;
```

## Properties

```
@property (TB,N,V_showingSnapshot) showingSnapshot;
@property (T@"<PKCanvasViewDelegate>",W,N) delegate;
@property (T@"PKCanvasView",R,N,V_canvasView) canvasView;
@property (T@"PKInk",&,N) ink;
@property (T@"UIGestureRecognizer",R,N) drawingGestureRecognizer;
```

## Instance methods

```
-[PNPWizardScratchpadCanvasView layoutSubviews];
-[PNPWizardScratchpadCanvasView setDelegate:];
-[PNPWizardScratchpadCanvasView ink];
-[PNPWizardScratchpadCanvasView delegate];
-[PNPWizardScratchpadCanvasView canvasView];
-[PNPWizardScratchpadCanvasView setInk:];
-[PNPWizardScratchpadCanvasView initWithFrame:];
-[PNPWizardScratchpadCanvasView drawingGestureRecognizer];
-[PNPWizardScratchpadCanvasView showingSnapshot];
-[PNPWizardScratchpadCanvasView _playClearAnimationWithImage:];
-[PNPWizardScratchpadCanvasView clearDrawingAnimated];
-[PNPWizardScratchpadCanvasView prepareCanvasView];
-[PNPWizardScratchpadCanvasView setShowingSnapshot:];
```
