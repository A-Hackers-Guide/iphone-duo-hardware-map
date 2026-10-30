# `_MapUpdate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 15 properties, 32 instance methods, 6 class methods

## Instance variables

```
B _isSectionUpdate;
B _isInsert;
B _isDelete;
B _isMove;
@"NSIndexPath" _indexPath;
@"NSIndexPath" _moveFromIndexPath;
@"NSIndexPath" _moveToIndexPath;
q _index;
q _section;
q _moveFromSection;
q _moveToSection;
{_NSRange="location"Q"length"Q} _insertRange;
{_NSRange="location"Q"length"Q} _deleteRange;
{_NSRange="location"Q"length"Q} _moveFromRange;
{_NSRange="location"Q"length"Q} _moveToRange;
```

## Properties

```
@property (TB,N,V_isSectionUpdate) isSectionUpdate;
@property (TB,N,V_isInsert) isInsert;
@property (TB,N,V_isDelete) isDelete;
@property (TB,N,V_isMove) isMove;
@property (T@"NSIndexPath",&,N,V_indexPath) indexPath;
@property (T@"NSIndexPath",&,N,V_moveFromIndexPath) moveFromIndexPath;
@property (T@"NSIndexPath",&,N,V_moveToIndexPath) moveToIndexPath;
@property (Tq,N,V_index) index;
@property (Tq,N,V_section) section;
@property (T{_NSRange=QQ},N,V_insertRange) insertRange;
@property (T{_NSRange=QQ},N,V_deleteRange) deleteRange;
@property (Tq,N,V_moveFromSection) moveFromSection;
@property (Tq,N,V_moveToSection) moveToSection;
@property (T{_NSRange=QQ},N,V_moveFromRange) moveFromRange;
@property (T{_NSRange=QQ},N,V_moveToRange) moveToRange;
```

## Class methods

```
+[_MapUpdate itemDeleteItemAtIndexPath:index:];
+[_MapUpdate itemDeleteSection:deleteRange:];
+[_MapUpdate itemInsertItemAtIndexPath:index:];
+[_MapUpdate itemInsertSection:insertRange:];
+[_MapUpdate itemMoveFromIndexIndexPath:toIndexPath:fromIndex:toIndex:];
+[_MapUpdate itemMoveSection:toSection:fromRange:toRange:];
```

## Instance methods

```
-[_MapUpdate setSection:];
-[_MapUpdate section];
-[_MapUpdate indexPath];
-[_MapUpdate index];
-[_MapUpdate isInsert];
-[_MapUpdate setIndex:];
-[_MapUpdate setIsDelete:];
-[_MapUpdate setIndexPath:];
-[_MapUpdate description];
-[_MapUpdate isDelete];
-[_MapUpdate setDeleteRange:];
-[_MapUpdate setMoveToRange:];
-[_MapUpdate isSectionUpdate];
-[_MapUpdate moveFromSection];
-[_MapUpdate moveToIndexPath];
-[_MapUpdate setInsertRange:];
-[_MapUpdate deleteRange];
-[_MapUpdate insertRange];
-[_MapUpdate isMove];
-[_MapUpdate moveFromIndexPath];
-[_MapUpdate moveFromRange];
-[_MapUpdate moveToRange];
-[_MapUpdate moveToSection];
-[_MapUpdate reverseUpdateItem];
-[_MapUpdate setIsInsert:];
-[_MapUpdate setIsMove:];
-[_MapUpdate setIsSectionUpdate:];
-[_MapUpdate setMoveFromIndexPath:];
-[_MapUpdate setMoveFromRange:];
-[_MapUpdate setMoveFromSection:];
-[_MapUpdate setMoveToIndexPath:];
-[_MapUpdate setMoveToSection:];
```
