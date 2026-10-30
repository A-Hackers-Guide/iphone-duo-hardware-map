# `SBWindowDragInteraction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIDragInteraction`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"UIGestureRecognizer" _gestureRecognizer;
@"<SBAppPlatterDragSourceViewProviding>" _sourceViewProvider;
@"NSString" _sceneIdentifier;
@"NSString" _bundleIdentifier;
```

## Properties

```
@property (T@"UIGestureRecognizer",R,W,N,V_gestureRecognizer) gestureRecognizer;
@property (T@"<SBAppPlatterDragSourceViewProviding>",W,N,V_sourceViewProvider) sourceViewProvider;
@property (T@"NSString",&,N,V_sceneIdentifier) sceneIdentifier;
@property (T@"NSString",&,N,V_bundleIdentifier) bundleIdentifier;
```

## Instance methods

```
-[SBWindowDragInteraction _locationInView:];
-[SBWindowDragInteraction gestureRecognizer];
-[SBWindowDragInteraction bundleIdentifier];
-[SBWindowDragInteraction setSceneIdentifier:];
-[SBWindowDragInteraction sceneIdentifier];
-[SBWindowDragInteraction setSourceViewProvider:];
-[SBWindowDragInteraction initWithDelegate:gestureRecognizer:];
-[SBWindowDragInteraction setBundleIdentifier:];
-[SBWindowDragInteraction sourceViewProvider];
```
