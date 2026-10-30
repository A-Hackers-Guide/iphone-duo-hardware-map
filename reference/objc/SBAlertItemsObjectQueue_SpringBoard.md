# `SBAlertItemsObjectQueue`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `NSFastEnumeration`
- 1 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSMutableOrderedSet" _objects;
```

## Properties

```
@property (T@"NSMutableOrderedSet",&,N,V_objects) objects;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAlertItemsObjectQueue succinctDescriptionBuilder];
-[SBAlertItemsObjectQueue init];
-[SBAlertItemsObjectQueue appendObject:];
-[SBAlertItemsObjectQueue descriptionWithMultilinePrefix:];
-[SBAlertItemsObjectQueue succinctDescription];
-[SBAlertItemsObjectQueue countByEnumeratingWithState:objects:count:];
-[SBAlertItemsObjectQueue setObjects:];
-[SBAlertItemsObjectQueue removeObject:];
-[SBAlertItemsObjectQueue containsObject:];
-[SBAlertItemsObjectQueue objects];
-[SBAlertItemsObjectQueue descriptionBuilderWithMultilinePrefix:];
-[SBAlertItemsObjectQueue dequeueAllObjects];
-[SBAlertItemsObjectQueue objectsOfClass:];
-[SBAlertItemsObjectQueue hasObject];
-[SBAlertItemsObjectQueue hasObjectOfClass:];
-[SBAlertItemsObjectQueue prependObject:];
```
