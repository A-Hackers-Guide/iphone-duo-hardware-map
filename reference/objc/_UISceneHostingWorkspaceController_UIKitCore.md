# `_UISceneHostingWorkspaceController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `FBSceneWorkspaceDelegate`
- 1 instance variables, 4 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"FBSceneWorkspace" _sceneWorkspace;
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
+[_UISceneHostingWorkspaceController sharedInstance];
```

## Instance methods

```
-[_UISceneHostingWorkspaceController debugDescription];
-[_UISceneHostingWorkspaceController init];
-[_UISceneHostingWorkspaceController workspace:willRemoveScene:];
-[_UISceneHostingWorkspaceController workspace:didAddScene:];
-[_UISceneHostingWorkspaceController succinctDescription];
-[_UISceneHostingWorkspaceController description];
-[_UISceneHostingWorkspaceController appendDescriptionToStream:];
```
