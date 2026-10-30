# `_UINavigationItemRenameHandler`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 27 instance methods, 5 class methods

## Instance variables

```
@"UINavigationItem" _associatedItem;
@? _shouldBeginRenamingHandler;
@? _willBeginRenamingHandler;
@? _didEndRenamingHandler;
@? _willBeginRenamingWithRangeHandler;
@? _shouldEndRenamingHandler;
@? _fileURLForRenaming;
@? _fileRenameDidFail;
@? _fileRenameDidEnd;
```

## Properties

```
@property (T@"UINavigationItem",W,N,V_associatedItem) associatedItem;
@property (T@?,C,N,V_shouldBeginRenamingHandler) shouldBeginRenamingHandler;
@property (T@?,C,N,V_willBeginRenamingHandler) willBeginRenamingHandler;
@property (T@?,C,N,V_didEndRenamingHandler) didEndRenamingHandler;
@property (T@?,C,N,V_willBeginRenamingWithRangeHandler) willBeginRenamingWithRangeHandler;
@property (T@?,C,N,V_shouldEndRenamingHandler) shouldEndRenamingHandler;
@property (T@?,C,N,V_fileURLForRenaming) fileURLForRenaming;
@property (T@?,C,N,V_fileRenameDidFail) fileRenameDidFail;
@property (T@?,C,N,V_fileRenameDidEnd) fileRenameDidEnd;
```

## Class methods

```
+[_UINavigationItemRenameHandler defaultNavigationItem:didEndRenamingWithTitle:];
+[_UINavigationItemRenameHandler defaultNavigationItem:shouldEndRenamingWithTitle:];
+[_UINavigationItemRenameHandler defaultNavigationItem:willBeginRenamingWithSuggestedTitle:selectedRange:];
+[_UINavigationItemRenameHandler defaultNavigationItemShouldBeginRenaming:forValidDelegate:];
+[_UINavigationItemRenameHandler handlerWithDidEndRenamingHandler:];
```

## Instance methods

```
-[_UINavigationItemRenameHandler init];
-[_UINavigationItemRenameHandler _canRename];
-[_UINavigationItemRenameHandler _didEndRenamingWithTitle:];
-[_UINavigationItemRenameHandler _fileRenameDidEndWithFinalURL:];
-[_UINavigationItemRenameHandler _fileRenameDidFailWithError:];
-[_UINavigationItemRenameHandler _fileURLForRenaming];
-[_UINavigationItemRenameHandler _shouldEndRenamingWithTitle:];
-[_UINavigationItemRenameHandler _willBeginRenamingWithTitle:selectedRange:];
-[_UINavigationItemRenameHandler associatedItem];
-[_UINavigationItemRenameHandler didEndRenamingHandler];
-[_UINavigationItemRenameHandler fileRenameDidEnd];
-[_UINavigationItemRenameHandler fileRenameDidFail];
-[_UINavigationItemRenameHandler fileURLForRenaming];
-[_UINavigationItemRenameHandler initWithDidEndRenamingHandler:];
-[_UINavigationItemRenameHandler setAssociatedItem:];
-[_UINavigationItemRenameHandler setDidEndRenamingHandler:];
-[_UINavigationItemRenameHandler setFileRenameDidEnd:];
-[_UINavigationItemRenameHandler setFileRenameDidFail:];
-[_UINavigationItemRenameHandler setFileURLForRenaming:];
-[_UINavigationItemRenameHandler setShouldBeginRenamingHandler:];
-[_UINavigationItemRenameHandler setShouldEndRenamingHandler:];
-[_UINavigationItemRenameHandler setWillBeginRenamingHandler:];
-[_UINavigationItemRenameHandler setWillBeginRenamingWithRangeHandler:];
-[_UINavigationItemRenameHandler shouldBeginRenamingHandler];
-[_UINavigationItemRenameHandler shouldEndRenamingHandler];
-[_UINavigationItemRenameHandler willBeginRenamingHandler];
-[_UINavigationItemRenameHandler willBeginRenamingWithRangeHandler];
```
