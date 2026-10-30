# `UIKBSplitRow`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 6 properties, 17 instance methods, 0 class methods

## Instance variables

```
C _rowIndex;
d _rowOffset;
d _rowWidth;
{CGSize="width"d"height"d} _defaultKeySize;
@"NSMutableArray" _keys;
@"NSMutableArray" _vacancies;
@"NSDictionary" _hints;
@"UIKBTree" _keylistLeft;
@"UIKBTree" _geolistLeft;
@"UIKBTree" _attrlistLeft;
@"UIKBTree" _keylistRight;
@"UIKBTree" _geolistRight;
@"UIKBTree" _attrlistRight;
```

## Properties

```
@property (TC,N,V_rowIndex) rowIndex;
@property (Td,V_rowOffset) rowOffset;
@property (Td,V_rowWidth) rowWidth;
@property (T{CGSize=dd},V_defaultKeySize) defaultKeySize;
@property (T@"NSMutableArray",R,V_keys) keys;
@property (T@"NSDictionary",&,V_hints) hints;
```

## Instance methods

```
-[UIKBSplitRow addKey:];
-[UIKBSplitRow init];
-[UIKBSplitRow dealloc];
-[UIKBSplitRow keyAtIndex:];
-[UIKBSplitRow keys];
-[UIKBSplitRow description];
-[UIKBSplitRow rowIndex];
-[UIKBSplitRow setRowIndex:];
-[UIKBSplitRow defaultKeySize];
-[UIKBSplitRow hints];
-[UIKBSplitRow listOfType:left:];
-[UIKBSplitRow rowOffset];
-[UIKBSplitRow rowWidth];
-[UIKBSplitRow setDefaultKeySize:];
-[UIKBSplitRow setHints:];
-[UIKBSplitRow setRowOffset:];
-[UIKBSplitRow setRowWidth:];
```
