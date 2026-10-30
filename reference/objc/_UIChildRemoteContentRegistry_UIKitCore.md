# `_UIChildRemoteContentRegistry`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSSceneObserver`, `BSDebugDescriptionProviding`
- 4 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"FBSScene" _parentScene;
@"NSHashTable" _childScenes;
@"NSHashTable" _childViewServices;
@"NSMutableDictionary" _enqueuedSettingsAvailabilityBlocks;
```

## Properties

```
@property (T@"NSSet",R,N) childScenes;
@property (T@"NSSet",R,N) childViewServices;
@property (T@"FBSSceneSettings",R,N) parentSettings;
@property (TB,R,N) parentSettingsAvailable;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIChildRemoteContentRegistry addChildScene:];
-[_UIChildRemoteContentRegistry childViewServices];
-[_UIChildRemoteContentRegistry addChildViewService:];
-[_UIChildRemoteContentRegistry debugDescription];
-[_UIChildRemoteContentRegistry succinctDescriptionBuilder];
-[_UIChildRemoteContentRegistry scene:didUpdateSettings:];
-[_UIChildRemoteContentRegistry parentSettings];
-[_UIChildRemoteContentRegistry childScenes];
-[_UIChildRemoteContentRegistry removeChildScene:];
-[_UIChildRemoteContentRegistry initWithParentScene:];
-[_UIChildRemoteContentRegistry descriptionWithMultilinePrefix:];
-[_UIChildRemoteContentRegistry succinctDescription];
-[_UIChildRemoteContentRegistry executeWhenParentSettingsAreAvailable:forChildScene:];
-[_UIChildRemoteContentRegistry debugDescriptionWithMultilinePrefix:];
-[_UIChildRemoteContentRegistry removeChildViewService:];
-[_UIChildRemoteContentRegistry parentSettingsAvailable];
-[_UIChildRemoteContentRegistry description];
-[_UIChildRemoteContentRegistry descriptionBuilderWithMultilinePrefix:];
```
