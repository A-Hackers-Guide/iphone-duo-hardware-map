# `UISSlotMachine`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UISSlotMachineProtocol`
- 9 instance variables, 5 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"<UISSlotDrawer>" _slotDrawer;
Q _slotDrawerMethod;
Q _options;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _cachedContentsLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _layerContextLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _LRUTagsByClassLock;
@"NSMutableDictionary" _cachedContents;
@"CAContext" _layerContext;
@"NSMapTable" _LRUTagsByClass;
```

## Properties

```
@property (T@"NSSet",R,N) allTags;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISSlotMachine allowedLocalizations];
```

## Instance methods

```
-[UISSlotMachine getRemoteContentForLayerContextWithId:style:tag:reply:];
-[UISSlotMachine allTags];
-[UISSlotMachine _getRemoteContentForLayerContextWithId:style:tag:forceSync:reply:];
-[UISSlotMachine initWithSlotDrawer:options:];
-[UISSlotMachine remoteContentForLayerContextWithId:style:tag:];
-[UISSlotMachine removeContentForStyle:tag:];
-[UISSlotMachine removeContentsForTag:];
```
