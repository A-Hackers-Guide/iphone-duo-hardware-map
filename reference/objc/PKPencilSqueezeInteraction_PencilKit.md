# `PKPencilSqueezeInteraction`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKTextEffectsWindowObserverDelegate`, `PKPencilSqueezeControllerDelegate`, `UIInteraction`
- 5 instance variables, 7 properties, 24 instance methods, 3 class methods

## Instance variables

```
@"PKPencilSqueezeController" _squeezeController;
@"PKTextEffectsWindowObserver" _textEffectsWindowObserver;
d _paletteViewDismissedTimestamp;
@"UIView" _view;
@"<PKPencilSqueezeInteractionDelegate>" __delegate;
```

## Properties

```
@property (T@"<PKPencilSqueezeInteractionDelegate>",W,N,V__delegate) _delegate;
@property (TB,R,N) _paletteViewVisible;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,W,N,V_view) view;
```

## Class methods

```
+[PKPencilSqueezeInteraction _existingInteractionForWindowScene:];
+[PKPencilSqueezeInteraction _perSceneInteractions];
+[PKPencilSqueezeInteraction _postPencilSettingsDidChangeRemoteNotification];
```

## Instance methods

```
-[PKPencilSqueezeInteraction init];
-[PKPencilSqueezeInteraction dealloc];
-[PKPencilSqueezeInteraction editingOverlayContainerDidChangeToSceneBounds:];
-[PKPencilSqueezeInteraction _delegate];
-[PKPencilSqueezeInteraction view];
-[PKPencilSqueezeInteraction willMoveToView:];
-[PKPencilSqueezeInteraction set_delegate:];
-[PKPencilSqueezeInteraction _updateUserInterfaceStyle];
-[PKPencilSqueezeInteraction didMoveToView:];
-[PKPencilSqueezeInteraction _cancelShowToolPicker];
-[PKPencilSqueezeInteraction _handleRemotePencilSettingDidChangeNotification];
-[PKPencilSqueezeInteraction _isPointInsidePaletteView:fromView:withEvent:];
-[PKPencilSqueezeInteraction _isUndoRedoPalette];
-[PKPencilSqueezeInteraction _paletteViewFrameForHoverLocation:inView:];
-[PKPencilSqueezeInteraction _paletteViewVisible];
-[PKPencilSqueezeInteraction _performSqueezeAction];
-[PKPencilSqueezeInteraction _setMiniPaletteVisible:hoverLocation:inView:];
-[PKPencilSqueezeInteraction _tiledCanvasViewShouldDiscardTapStroke:];
-[PKPencilSqueezeInteraction pencilSqueezeControllerCanShowPaletteView:];
-[PKPencilSqueezeInteraction pencilSqueezeControllerDidChangePaletteViewVisibility:];
-[PKPencilSqueezeInteraction pencilSqueezeControllerWillChangePaletteViewVisibility:toVisible:];
-[PKPencilSqueezeInteraction textEffectsWindowDidChangeKeyWindowBounds:];
-[PKPencilSqueezeInteraction textEffectsWindowDidChangeKeyWindowUserInterfaceStyle:];
-[PKPencilSqueezeInteraction textEffectsWindowDidChangeWindowBounds:];
```
