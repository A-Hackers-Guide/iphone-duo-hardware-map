# `_UIKeyboardInputRehostingSceneHostComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `BSDescriptionStreaming`, `_UIKeyboardInputRehostingSceneHost`, `FBSceneObserver`, `FBSceneComponent`
- 1 instance variables, 7 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",&,N) keyboardNamespaceIdentifier;
@property (T@"UIKBArbiterClientFocusContext",R,N) currentFocusContext;
@property (TB,R,N) keyboardInTrackpadMode;
```

## Instance methods

```
-[_UIKeyboardInputRehostingSceneHostComponent keyboardNamespaceIdentifier];
-[_UIKeyboardInputRehostingSceneHostComponent debugDescription];
-[_UIKeyboardInputRehostingSceneHostComponent removeObserver:];
-[_UIKeyboardInputRehostingSceneHostComponent sceneDidActivate:];
-[_UIKeyboardInputRehostingSceneHostComponent setScene:];
-[_UIKeyboardInputRehostingSceneHostComponent addObserver:];
-[_UIKeyboardInputRehostingSceneHostComponent setKeyboardNamespaceIdentifier:];
-[_UIKeyboardInputRehostingSceneHostComponent description];
-[_UIKeyboardInputRehostingSceneHostComponent appendDescriptionToStream:];
-[_UIKeyboardInputRehostingSceneHostComponent pointIsWithinKeyboardContent:];
-[_UIKeyboardInputRehostingSceneHostComponent currentFocusContext];
-[_UIKeyboardInputRehostingSceneHostComponent keyboardInTrackpadMode];
-[_UIKeyboardInputRehostingSceneHostComponent scene:didUpdateClientSettings:];
```
