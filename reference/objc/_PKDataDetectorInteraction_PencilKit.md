# `_PKDataDetectorInteraction`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIContextMenuInteractionDelegate_ForWebKitOnly`, `_PKDataDetectorControllerDelegate`, `UIInteraction`
- 10 instance variables, 13 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"PKRecognitionController" _recognitionController;
B _enabled;
@"_PKDataDetectorController" _dataDetectorController;
@"UIContextMenuInteraction" _menuInteraction;
@"UITapGestureRecognizer" _tapGestureRecognizer;
@"UIView" _view;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sourceRect;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _drawingTransform;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _highlightTransform;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _highlightPreviewTransform;
```

## Properties

```
@property (T@"UIView",W,N,V_view) view;
@property (T@"_PKDataDetectorController",R,N,V_dataDetectorController) dataDetectorController;
@property (T@"UIContextMenuInteraction",R,N,V_menuInteraction) menuInteraction;
@property (T@"UITapGestureRecognizer",R,N,V_tapGestureRecognizer) tapGestureRecognizer;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (T{CGAffineTransform=dddddd},N,V_drawingTransform) drawingTransform;
@property (T{CGAffineTransform=dddddd},N,V_highlightTransform) highlightTransform;
@property (T{CGAffineTransform=dddddd},N,V_highlightPreviewTransform) highlightPreviewTransform;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_sourceRect) sourceRect;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_PKDataDetectorInteraction setSourceRect:];
-[_PKDataDetectorInteraction tapGestureRecognizer];
-[_PKDataDetectorInteraction sourceRect];
-[_PKDataDetectorInteraction contextMenuInteraction:configurationForMenuAtLocation:];
-[_PKDataDetectorInteraction tapHandler:];
-[_PKDataDetectorInteraction menuInteraction];
-[_PKDataDetectorInteraction setView:];
-[_PKDataDetectorInteraction contextMenuInteraction:configuration:highlightPreviewForItemWithIdentifier:];
-[_PKDataDetectorInteraction isEnabled];
-[_PKDataDetectorInteraction view];
-[_PKDataDetectorInteraction setEnabled:];
-[_PKDataDetectorInteraction willMoveToView:];
-[_PKDataDetectorInteraction contextMenuInteraction:willPerformPreviewActionForMenuWithConfiguration:animator:];
-[_PKDataDetectorInteraction itemWithIdentifier:];
-[_PKDataDetectorInteraction didMoveToView:];
-[_PKDataDetectorInteraction _contextMenuInteraction:overrideSuggestedActionsForConfiguration:];
-[_PKDataDetectorInteraction handleTapAtPoint:];
-[_PKDataDetectorInteraction dataDetectorController];
-[_PKDataDetectorInteraction dataDetectorHitTest:];
-[_PKDataDetectorInteraction drawingTransform];
-[_PKDataDetectorInteraction highlightPreviewTransform];
-[_PKDataDetectorInteraction highlightTransform];
-[_PKDataDetectorInteraction initWithRecognitionController:];
-[_PKDataDetectorInteraction setDrawingTransform:];
-[_PKDataDetectorInteraction setHighlightPreviewTransform:];
-[_PKDataDetectorInteraction setHighlightTransform:];
```
