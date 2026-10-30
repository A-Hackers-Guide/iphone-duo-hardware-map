# `_UISceneMultiNamespaceWorkspace`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneWorkspaceObserver`, `BSDescriptionStreaming`, `BSInvalidatable`
- 5 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _invalidated;
@"NSString" _identifier;
@"NSMutableDictionary" _namespaceMap;
@"FBSceneWorkspace" _workspace;
@"<_UISceneMultiNamespaceWorkspaceDelegate>" _delegate;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISceneMultiNamespaceWorkspace debugDescription];
-[_UISceneMultiNamespaceWorkspace init];
-[_UISceneMultiNamespaceWorkspace workspace:willRemoveScene:];
-[_UISceneMultiNamespaceWorkspace dealloc];
-[_UISceneMultiNamespaceWorkspace workspace:didAddScene:];
-[_UISceneMultiNamespaceWorkspace invalidate];
-[_UISceneMultiNamespaceWorkspace description];
-[_UISceneMultiNamespaceWorkspace appendDescriptionToStream:];
-[_UISceneMultiNamespaceWorkspace _scenesMatching:];
```
