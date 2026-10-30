# `PKPaletteViewInteraction`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIEditingOverlayInteractionWithView`, `PKPaletteHostingWindowScene`, `UIKeyboardSceneDelegateVisibilityObserver`, `_UISceneComponentProviding`, `PKPaletteTapToRadarCommandDelegate`, `PKTextEffectsWindowObserverDelegate`, `UIInteraction`
- 13 instance variables, 20 properties, 58 instance methods, 4 class methods

## Instance variables

```
@"UIScene" _scene;
@"<PKPaletteViewInteractionDelegate>" _delegate;
@"PKPaletteHostView" _paletteHostView;
@"PKDrawingPaletteView" _paletteView;
@"UIWindowScene" _windowScene;
@"PKTextEffectsWindowObserver" _textEffectsWindowObserver;
@"UIView" _view;
@"NSLayoutConstraint" _paletteHostViewWidthConstraint;
@"NSLayoutConstraint" _paletteHostViewHeightConstraint;
@"NSLayoutConstraint" _paletteHostViewTopConstraint;
@"NSLayoutConstraint" _paletteHostViewLeftConstraint;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sceneBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _textEffectsWindowFrame;
```

## Properties

```
@property (T@"UIWindowScene",W,N,V_windowScene) windowScene;
@property (T@"PKTextEffectsWindowObserver",&,N,V_textEffectsWindowObserver) textEffectsWindowObserver;
@property (T@"PKPaletteHostView",&,N,V_paletteHostView) paletteHostView;
@property (T@"PKDrawingPaletteView",&,N,V_paletteView) paletteView;
@property (T@"UIView",W,N,V_view) view;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_sceneBounds) sceneBounds;
@property (T@"NSLayoutConstraint",&,N,V_paletteHostViewWidthConstraint) paletteHostViewWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_paletteHostViewHeightConstraint) paletteHostViewHeightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_paletteHostViewTopConstraint) paletteHostViewTopConstraint;
@property (T@"NSLayoutConstraint",&,N,V_paletteHostViewLeftConstraint) paletteHostViewLeftConstraint;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_textEffectsWindowFrame) textEffectsWindowFrame;
@property (TB,R,N,GisActive) active;
@property (T@"<PKPaletteViewInteractionDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisPaletteVisible) paletteVisible;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) paletteHostingWindowSceneBounds;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIScene",W,N,G_scene,S_setScene:) _scene;
```

## Class methods

```
+[PKPaletteViewInteraction isHostedWindow:];
+[PKPaletteViewInteraction existingPaletteViewInteractionForWindowScene:];
+[PKPaletteViewInteraction paletteViewInteractionForCanvas:];
+[PKPaletteViewInteraction paletteViewInteractionForWindow:windowScene:];
```

## Instance methods

```
-[PKPaletteViewInteraction setWindowScene:];
-[PKPaletteViewInteraction _scene];
-[PKPaletteViewInteraction _sceneWillInvalidate:];
-[PKPaletteViewInteraction setView:];
-[PKPaletteViewInteraction initWithScene:];
-[PKPaletteViewInteraction editingOverlayContainerDidChangeToSceneBounds:];
-[PKPaletteViewInteraction view];
-[PKPaletteViewInteraction setDelegate:];
-[PKPaletteViewInteraction hostingWindow];
-[PKPaletteViewInteraction willMoveToView:];
-[PKPaletteViewInteraction delegate];
-[PKPaletteViewInteraction _setScene:];
-[PKPaletteViewInteraction isActive];
-[PKPaletteViewInteraction windowScene];
-[PKPaletteViewInteraction didMoveToView:];
-[PKPaletteViewInteraction initWithWindowSize:];
-[PKPaletteViewInteraction keyboardSceneDelegate:inputViewSetVisibilityDidChange:includedReset:];
-[PKPaletteViewInteraction sceneBounds];
-[PKPaletteViewInteraction paletteHostView];
-[PKPaletteViewInteraction paletteHostingWindowSceneBounds];
-[PKPaletteViewInteraction paletteHostViewHeightConstraint];
-[PKPaletteViewInteraction setPaletteView:];
-[PKPaletteViewInteraction setSceneBounds:];
-[PKPaletteViewInteraction _isCompactHostedWindow];
-[PKPaletteViewInteraction _sceneBoundsForUpdateWithFollowsHostingWindowOut:];
-[PKPaletteViewInteraction _sceneDidActivateNotification:];
-[PKPaletteViewInteraction _sceneWillEnterForegroundNotification:];
-[PKPaletteViewInteraction _setPaletteVisible:animated:completion:];
-[PKPaletteViewInteraction _shouldDeferPaletteVisibilityUpdate];
-[PKPaletteViewInteraction _traitCollectionForHostingWindow];
-[PKPaletteViewInteraction _updateForRotation:];
-[PKPaletteViewInteraction _updateForWillRotate:];
-[PKPaletteViewInteraction _updatePalettePopoverWithUIStyle:];
-[PKPaletteViewInteraction _updatePaletteTraitCollection:];
-[PKPaletteViewInteraction _updatePaletteUserInterfaceStyle:];
-[PKPaletteViewInteraction _updateSceneBounds];
-[PKPaletteViewInteraction _updateTraitCollection];
-[PKPaletteViewInteraction _updateUIWithSceneBounds:];
-[PKPaletteViewInteraction _viewControllerForPalette];
-[PKPaletteViewInteraction hidePaletteViewAnimated:completion:];
-[PKPaletteViewInteraction isPaletteVisible];
-[PKPaletteViewInteraction paletteHostViewLeftConstraint];
-[PKPaletteViewInteraction paletteHostViewTopConstraint];
-[PKPaletteViewInteraction paletteHostViewWidthConstraint];
-[PKPaletteViewInteraction paletteTapToRadarCommandConfiguration:];
-[PKPaletteViewInteraction paletteView];
-[PKPaletteViewInteraction setPaletteHostView:];
-[PKPaletteViewInteraction setPaletteHostViewHeightConstraint:];
-[PKPaletteViewInteraction setPaletteHostViewLeftConstraint:];
-[PKPaletteViewInteraction setPaletteHostViewTopConstraint:];
-[PKPaletteViewInteraction setPaletteHostViewWidthConstraint:];
-[PKPaletteViewInteraction setTextEffectsWindowFrame:];
-[PKPaletteViewInteraction setTextEffectsWindowObserver:];
-[PKPaletteViewInteraction showPaletteViewAnimated:completion:];
-[PKPaletteViewInteraction textEffectsWindowDidChangeKeyWindowBounds:];
-[PKPaletteViewInteraction textEffectsWindowDidChangeKeyWindowUserInterfaceStyle:];
-[PKPaletteViewInteraction textEffectsWindowFrame];
-[PKPaletteViewInteraction textEffectsWindowObserver];
```
