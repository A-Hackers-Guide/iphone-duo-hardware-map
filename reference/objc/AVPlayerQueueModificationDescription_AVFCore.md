# `AVPlayerQueueModificationDescription`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 3 class methods

## Instance variables

```
q _modificationType;
@"AVPlayerItem" _item;
@"AVPlayerItem" _afterItem;
@"NSArray" _items;
```

## Properties

```
@property (Tq,R,N,V_modificationType) modificationType;
@property (T@"AVPlayerItem",R,N,V_item) item;
@property (T@"AVPlayerItem",R,N,V_afterItem) afterItem;
@property (T@"NSArray",R,N,V_items) items;
```

## Class methods

```
+[AVPlayerQueueModificationDescription modificationForInsertingItem:afterItem:];
+[AVPlayerQueueModificationDescription modificationForRemovingAllItems:];
+[AVPlayerQueueModificationDescription modificationForRemovingItem:];
```

## Instance methods

```
-[AVPlayerQueueModificationDescription init];
-[AVPlayerQueueModificationDescription dealloc];
-[AVPlayerQueueModificationDescription items];
-[AVPlayerQueueModificationDescription item];
-[AVPlayerQueueModificationDescription initWithModificationType:items:];
-[AVPlayerQueueModificationDescription afterItem];
-[AVPlayerQueueModificationDescription initWithModificationType:item:afterItem:];
-[AVPlayerQueueModificationDescription modificationType];
```
