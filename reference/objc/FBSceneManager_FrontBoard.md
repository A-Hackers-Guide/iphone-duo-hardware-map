# `FBSceneManager`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 29 instance methods, 6 class methods

## Instance variables

```
@"FBSceneWorkspace" _workspace;
B _invalidated;
```

## Properties

```
@property (TB,N,S_setSuppressConnectionHandshakes:) _suppressConnectionHandshakes;
@property (T@"<FBSceneManagerDelegate>",W,N) delegate;
```

## Class methods

```
+[FBSceneManager sharedInstance];
+[FBSceneManager keyboardScene];
+[FBSceneManager setKeyboardScene:];
+[FBSceneManager observeKeyboardSceneAvailability:];
+[FBSceneManager _clearKeyboardScene];
+[FBSceneManager synchronizeChanges:];
```

## Instance methods

```
-[FBSceneManager enumerateScenesWithBlock:];
-[FBSceneManager debugDescription];
-[FBSceneManager removeObserver:];
-[FBSceneManager init];
-[FBSceneManager _invalidate];
-[FBSceneManager add:];
-[FBSceneManager remove:];
-[FBSceneManager dealloc];
-[FBSceneManager sceneWithIdentifier:];
-[FBSceneManager addObserver:];
-[FBSceneManager setDelegate:];
-[FBSceneManager sceneFromIdentityToken:];
-[FBSceneManager delegate];
-[FBSceneManager description];
-[FBSceneManager createScene:];
-[FBSceneManager sceneFromIdentityTokenStringRepresentation:];
-[FBSceneManager createSceneFromRemnant:withSettings:transitionContext:];
-[FBSceneManager scenesPassingTest:];
-[FBSceneManager _createSceneWithDefinition:settings:initialClientSettings:transitionContext:fromRemnant:usingClientProvider:completion:];
-[FBSceneManager _initWithProcessManager:];
-[FBSceneManager _isSameAsWorkspace:];
-[FBSceneManager _setSuppressConnectionHandshakes:];
-[FBSceneManager _suppressConnectionHandshakes];
-[FBSceneManager createLegacySceneFromRemnant:withSettings:transitionContext:];
-[FBSceneManager createSceneWithDefinition:];
-[FBSceneManager createSceneWithDefinition:initialParameters:];
-[FBSceneManager createSceneWithIdentifier:parameters:clientProvider:transitionContext:];
-[FBSceneManager destroyScene:withTransitionContext:];
-[FBSceneManager newSceneIdentityTokenForIdentity:];
```
