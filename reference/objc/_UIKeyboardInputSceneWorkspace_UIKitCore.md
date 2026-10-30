# `_UIKeyboardInputSceneWorkspace`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneMultiNamespaceWorkspaceDelegate`, `FBSceneWorkspaceDelegate`, `FBSceneWorkspaceObserver`, `FBSceneObserver`, `BSDescriptionStreaming`
- 5 instance variables, 4 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"_UISceneMultiNamespaceWorkspace" _workspace;
@"NSMutableDictionary" _namespaceControllerMap;
@"NSMutableDictionary" _hostingCompoundAssertions;
@"NSMutableDictionary" _hostingAssertions;
B _invalidated;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIKeyboardInputSceneWorkspace sharedInstance];
```

## Instance methods

```
-[_UIKeyboardInputSceneWorkspace workspace:clientDidConnectWithHandshake:];
-[_UIKeyboardInputSceneWorkspace multiNamespaceWorkspace:namespaceForScene:];
-[_UIKeyboardInputSceneWorkspace workspace:didReceiveSceneRequestWithOptions:fromProcess:completion:];
-[_UIKeyboardInputSceneWorkspace sceneWillDeactivate:withContext:];
-[_UIKeyboardInputSceneWorkspace debugDescription];
-[_UIKeyboardInputSceneWorkspace rehostingScene:didUpdateNamespaceIdentifierFrom:to:];
-[_UIKeyboardInputSceneWorkspace init];
-[_UIKeyboardInputSceneWorkspace multiNamespaceWorkspace:willInvalidateNamespace:];
-[_UIKeyboardInputSceneWorkspace workspace:willRemoveScene:];
-[_UIKeyboardInputSceneWorkspace workspace:didAddScene:];
-[_UIKeyboardInputSceneWorkspace acquireHostingAssertionForScene:withReason:];
-[_UIKeyboardInputSceneWorkspace keyboardSceneForPairedIdentityToken:];
-[_UIKeyboardInputSceneWorkspace description];
-[_UIKeyboardInputSceneWorkspace appendDescriptionToStream:];
-[_UIKeyboardInputSceneWorkspace rehostingSceneDidDisconnect:];
-[_UIKeyboardInputSceneWorkspace rehostingSceneDidConnect:];
-[_UIKeyboardInputSceneWorkspace scene:didUpdateClientSettings:];
-[_UIKeyboardInputSceneWorkspace multiNamespaceWorkspace:didMoveScene:fromNamespace:toNamespace:];
```
