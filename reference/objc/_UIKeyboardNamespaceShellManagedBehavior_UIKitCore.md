# `_UIKeyboardNamespaceShellManagedBehavior`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneObserver`, `FBSSceneObserver`, `_UIKeyboardNamespaceBehavior`
- 3 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"_UIKeyboardWorkspaceNamespaceController" _namespaceController;
@"FBSSceneSettings" _cachedRehostingSceneSettings;
@"FBSDisplayConfiguration" _derivedDisplayConfiguration;
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
-[_UIKeyboardNamespaceShellManagedBehavior namespaceController:didUpdateHosting:forScene:];
-[_UIKeyboardNamespaceShellManagedBehavior namespaceController:didAddScene:];
-[_UIKeyboardNamespaceShellManagedBehavior scene:didUpdateSettings:];
-[_UIKeyboardNamespaceShellManagedBehavior namespaceController:willUpdateRehostingScene:];
-[_UIKeyboardNamespaceShellManagedBehavior initWithNamespaceController:];
-[_UIKeyboardNamespaceShellManagedBehavior namespaceController:willRemoveScene:];
-[_UIKeyboardNamespaceShellManagedBehavior scene:didUpdateClientSettings:];
```
