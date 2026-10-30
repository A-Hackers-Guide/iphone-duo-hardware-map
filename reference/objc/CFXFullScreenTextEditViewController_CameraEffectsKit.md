# `CFXFullScreenTextEditViewController`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `CFXEffectEditorViewDelegate`
- 11 instance variables, 15 properties, 67 instance methods, 6 class methods

## Instance variables

```
B _effectWasRemoved;
B _isRunningAnimation;
B _insertingEffect;
@"CFXEffect" _textEffect;
@"CFXEffect" _workingEffect;
@"CFXEffectEditorView" _effectEditor;
@"<CFXFullScreenTextEditViewControllerDelegate>" _delegate;
@"UIView" _dimmingView;
@"JFXOverlayEffectDebugViewOptions" _debugOptions;
@"UIView" _debugView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _effectEditorFrameRelativeToScreen;
```

## Properties

```
@property (T@"CFXEffect",&,N,V_workingEffect) workingEffect;
@property (T@"CFXEffectEditorView",&,N,V_effectEditor) effectEditor;
@property (T@"<CFXFullScreenTextEditViewControllerDelegate>",R,W,N,V_delegate) delegate;
@property (TB,N,V_effectWasRemoved) effectWasRemoved;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_effectEditorFrameRelativeToScreen) effectEditorFrameRelativeToScreen;
@property (T@"UIView",&,N,V_dimmingView) dimmingView;
@property (TB,N,V_isRunningAnimation) isRunningAnimation;
@property (TB,N,V_insertingEffect) insertingEffect;
@property (T@"JFXOverlayEffectDebugViewOptions",&,N,V_debugOptions) debugOptions;
@property (T@"UIView",&,N,V_debugView) debugView;
@property (T@"CFXEffect",R,N,V_textEffect) textEffect;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CFXFullScreenTextEditViewController resign];
+[CFXFullScreenTextEditViewController CFX_fadeTimingParameters];
+[CFXFullScreenTextEditViewController isFullScreenTextEditorPresented];
+[CFXFullScreenTextEditViewController displayFullScreenTextEditorForEffect:inViewController:delegate:cameraViewWindowFrame:insertingEffect:];
+[CFXFullScreenTextEditViewController notifyCameraViewWindowFrameChanged:];
+[CFXFullScreenTextEditViewController removeFullScreenTextEditor];
```

## Instance methods

```
-[CFXFullScreenTextEditViewController keyboardDidHide:];
-[CFXFullScreenTextEditViewController dimmingView];
-[CFXFullScreenTextEditViewController viewWillDisappear:];
-[CFXFullScreenTextEditViewController debugView];
-[CFXFullScreenTextEditViewController setDebugView:];
-[CFXFullScreenTextEditViewController debugOptions];
-[CFXFullScreenTextEditViewController dealloc];
-[CFXFullScreenTextEditViewController viewDidLoad];
-[CFXFullScreenTextEditViewController setDimmingView:];
-[CFXFullScreenTextEditViewController viewDidAppear:];
-[CFXFullScreenTextEditViewController setDebugOptions:];
-[CFXFullScreenTextEditViewController delegate];
-[CFXFullScreenTextEditViewController effectEditorView:didRemoveEffect:];
-[CFXFullScreenTextEditViewController effectEditorView:effectAtPoint:];
-[CFXFullScreenTextEditViewController CFX_animateWithDuration:animatingIn:completion:];
-[CFXFullScreenTextEditViewController effectEditorView:didTransformEffect:transform:relativeToBounds:];
-[CFXFullScreenTextEditViewController effectEditorView:textForEffect:];
-[CFXFullScreenTextEditViewController insertingEffect];
-[CFXFullScreenTextEditViewController configureWorkingEffect];
-[CFXFullScreenTextEditViewController didTappedEmptyDimmedArea:];
-[CFXFullScreenTextEditViewController effectEditor];
-[CFXFullScreenTextEditViewController effectEditorFrameRelativeToScreen];
-[CFXFullScreenTextEditViewController effectEditorView:applyAnimationTransformsToEffect:transforms:];
-[CFXFullScreenTextEditViewController effectEditorView:beginEditingAnimationFromFrameForEffect:relativeToBounds:];
-[CFXFullScreenTextEditViewController effectEditorView:beginEditingAnimationToFrameForEffect:relativeToBounds:];
-[CFXFullScreenTextEditViewController effectEditorView:calculateAnimatedFaceTrackingTransformWithCurrentFaceTrackingDataFromTrackingType:interpolatedWithFaceTrackingTransform:toTrackingType:atAnimationProgress:];
-[CFXFullScreenTextEditViewController effectEditorView:didBeginEditingTextForEffect:];
-[CFXFullScreenTextEditViewController effectEditorView:didCompleteBeginEditingAnimationForEffect:];
-[CFXFullScreenTextEditViewController effectEditorView:didCompleteEndEditingAnimationForEffect:completion:];
-[CFXFullScreenTextEditViewController effectEditorView:didEditTextForEffect:newText:];
-[CFXFullScreenTextEditViewController effectEditorView:didEndEditingTextForEffect:wasCancelled:];
-[CFXFullScreenTextEditViewController effectEditorView:didStartBeginEditingAnimationForEffect:completion:];
-[CFXFullScreenTextEditViewController effectEditorView:didStartEndEditingAnimationForEffect:];
-[CFXFullScreenTextEditViewController effectEditorView:durationForBeginEditingAnimationForEffect:];
-[CFXFullScreenTextEditViewController effectEditorView:durationForEndEditingAnimationForEffect:];
-[CFXFullScreenTextEditViewController effectEditorView:endEditingAnimationFromFrameForEffect:relativeToBounds:];
-[CFXFullScreenTextEditViewController effectEditorView:endEditingAnimationToFrameForEffect:relativeToBounds:];
-[CFXFullScreenTextEditViewController effectEditorView:frameForEffect:relativeToBounds:];
-[CFXFullScreenTextEditViewController effectEditorView:hitAreaBoundingFrameForEffect:adjustForMinimumSize:relativeToBounds:];
-[CFXFullScreenTextEditViewController effectEditorView:isEffectAtPoint:effect:];
-[CFXFullScreenTextEditViewController effectEditorView:isFaceTrackingDataAvailableForEffect:];
-[CFXFullScreenTextEditViewController effectEditorView:isFaceTrackingEffect:];
-[CFXFullScreenTextEditViewController effectEditorView:maximumTextLengthForEffect:];
-[CFXFullScreenTextEditViewController effectEditorView:overlayEffectFrameForEffect:relativeToBounds:];
-[CFXFullScreenTextEditViewController effectEditorView:removeButtonPositionForEffect:relativeToBounds:];
-[CFXFullScreenTextEditViewController effectEditorView:shouldDisableEditingAnimationForEffect:];
-[CFXFullScreenTextEditViewController effectEditorView:shouldEditTextForEffect:];
-[CFXFullScreenTextEditViewController effectEditorView:spacingBetweenCenterPointOfEffect:point:relativeToBounds:];
-[CFXFullScreenTextEditViewController effectEditorView:textEditingPropertiesForEffect:relativeToBounds:];
-[CFXFullScreenTextEditViewController effectEditorView:willBeginAnimationAfterEditingEffect:];
-[CFXFullScreenTextEditViewController effectEditorView:willBeginAnimationBeforeEditingEffect:];
-[CFXFullScreenTextEditViewController effectEditorViewDidBeginEditing:];
-[CFXFullScreenTextEditViewController effectEditorViewDidEndEditing:];
-[CFXFullScreenTextEditViewController effectEditorViewShouldPreviewEditEffect:];
-[CFXFullScreenTextEditViewController effectWasRemoved];
-[CFXFullScreenTextEditViewController initWithTextEffect:CGSize:insertingEffect:delegate:];
-[CFXFullScreenTextEditViewController isRunningAnimation];
-[CFXFullScreenTextEditViewController removeButtonRelativeBoundsIsViewSpace];
-[CFXFullScreenTextEditViewController scaleTextToFitTextEditingBounds:];
-[CFXFullScreenTextEditViewController setEffectEditor:];
-[CFXFullScreenTextEditViewController setEffectEditorFrameRelativeToScreen:];
-[CFXFullScreenTextEditViewController setEffectWasRemoved:];
-[CFXFullScreenTextEditViewController setInsertingEffect:];
-[CFXFullScreenTextEditViewController setIsRunningAnimation:];
-[CFXFullScreenTextEditViewController setWorkingEffect:];
-[CFXFullScreenTextEditViewController textEffect];
-[CFXFullScreenTextEditViewController workingEffect];
```
