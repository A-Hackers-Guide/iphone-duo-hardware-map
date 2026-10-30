# `_UIWorkspaceSceneRequestOptionsFactory`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 9 instance methods, 3 class methods

## Instance variables

```
@"NSMutableDictionary" _buildersByRole;
@"NSDictionary" _defaultBuildersByRole;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_buildersByRole) buildersByRole;
@property (T@"NSDictionary",&,N,V_defaultBuildersByRole) defaultBuildersByRole;
```

## Class methods

```
+[_UIWorkspaceSceneRequestOptionsFactory _createDefaultBuilders];
+[_UIWorkspaceSceneRequestOptionsFactory _defaultBuilderProviders];
+[_UIWorkspaceSceneRequestOptionsFactory sharedFactory];
```

## Instance methods

```
-[_UIWorkspaceSceneRequestOptionsFactory _init];
-[_UIWorkspaceSceneRequestOptionsFactory _effectiveBuilderForRole:];
-[_UIWorkspaceSceneRequestOptionsFactory _registerBuilder:forRole:];
-[_UIWorkspaceSceneRequestOptionsFactory buildWorkspaceRequestOptionsForRequest:withContinuation:];
-[_UIWorkspaceSceneRequestOptionsFactory buildersByRole];
-[_UIWorkspaceSceneRequestOptionsFactory customEndpointForRequest:];
-[_UIWorkspaceSceneRequestOptionsFactory defaultBuildersByRole];
-[_UIWorkspaceSceneRequestOptionsFactory setBuildersByRole:];
-[_UIWorkspaceSceneRequestOptionsFactory setDefaultBuildersByRole:];
```
