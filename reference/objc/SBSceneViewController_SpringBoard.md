# `SBSceneViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBSceneViewPresentationConfiguring`, `SBSceneViewControlling`
- 13 instance variables, 13 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"NSLayoutConstraint" _leftAnchorConstraint;
@"NSLayoutConstraint" _rightAnchorConstraint;
@"NSLayoutConstraint" _topAnchorConstraint;
@"NSLayoutConstraint" _bottomAnchorConstraint;
@"SBSceneHandle" _sceneHandle;
q _displayMode;
q _contentOrientation;
q _containerOrientation;
@"<SBScenePlaceholderContentContext>" _placeholderContentContext;
@"UIView" _customContentView;
@"SBSceneView" _sceneView;
{CGSize="width"d"height"d} _contentReferenceSize;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _sceneViewInsets;
```

## Properties

```
@property (T@"SBSceneView",R,N,G_sceneView,V_sceneView) sceneView;
@property (T{UIEdgeInsets=dddd},N,V_sceneViewInsets) sceneViewInsets;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"SBSceneHandle",R,N,V_sceneHandle) sceneHandle;
@property (Tq,R,N,V_displayMode) displayMode;
@property (T@"<SBScenePlaceholderContentContext>",&,N,V_placeholderContentContext) placeholderContentContext;
@property (T@"UIView",&,N,V_customContentView) customContentView;
@property (T{CGSize=dd},R,N,V_contentReferenceSize) contentReferenceSize;
@property (Tq,R,N,V_contentOrientation) contentOrientation;
@property (Tq,R,N,V_containerOrientation) containerOrientation;
```

## Instance methods

```
-[SBSceneViewController customContentView];
-[SBSceneViewController setCustomContentView:];
-[SBSceneViewController containerOrientation];
-[SBSceneViewController sceneHandle];
-[SBSceneViewController setPlaceholderContentContext:];
-[SBSceneViewController beginInteractiveDisplayModeTransitionToMode:];
-[SBSceneViewController contentOrientation];
-[SBSceneViewController dealloc];
-[SBSceneViewController displayMode];
-[SBSceneViewController containerContentWrapperInterfaceOrientationChangedTo:];
-[SBSceneViewController viewDidLoad];
-[SBSceneViewController initWithSceneHandle:];
-[SBSceneViewController initWithNibName:bundle:];
-[SBSceneViewController setContentReferenceSize:withContentOrientation:andContainerOrientation:];
-[SBSceneViewController invalidate];
-[SBSceneViewController endInteractiveDisplayModeTransitionAtMode:];
-[SBSceneViewController initWithCoder:];
-[SBSceneViewController sceneViewPresentationPriority:];
-[SBSceneViewController setDisplayMode:animationFactory:completion:];
-[SBSceneViewController contentReferenceSize];
-[SBSceneViewController placeholderContentContext];
-[SBSceneViewController updateInteractiveDisplayModeTransitionProgress:];
-[SBSceneViewController sceneViewPresentationIdentifier:];
-[SBSceneViewController sceneViewInsets];
-[SBSceneViewController _sceneView];
-[SBSceneViewController _setSceneView:];
-[SBSceneViewController setSceneViewInsets:];
```
