# `_UIKeyWindowSceneStack`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDebugDescriptionProviding`
- 5 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _recordsByWindowScene;
@"NSMutableOrderedSet" _orderedRecords;
@"UIWindowScene" _keyWindowSceneInStack;
{?="affectsApplicationKeyWindow"b1"hasViewServiceEntitlement"b1} _sceneStackFlags;
@"NSString" _name;
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
-[_UIKeyWindowSceneStack debugDescription];
-[_UIKeyWindowSceneStack succinctDescriptionBuilder];
-[_UIKeyWindowSceneStack init];
-[_UIKeyWindowSceneStack descriptionWithMultilinePrefix:];
-[_UIKeyWindowSceneStack succinctDescription];
-[_UIKeyWindowSceneStack debugDescriptionWithMultilinePrefix:];
-[_UIKeyWindowSceneStack description];
-[_UIKeyWindowSceneStack descriptionBuilderWithMultilinePrefix:];
```
