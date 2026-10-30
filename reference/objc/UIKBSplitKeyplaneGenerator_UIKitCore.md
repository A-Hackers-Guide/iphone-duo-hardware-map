# `UIKBSplitKeyplaneGenerator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _rows;
@"NSDictionary" _splitLayoutHints;
@"UIKBTree" _sourceKeyboard;
@"UIKBTree" _sourceKeyplane;
{CGSize="width"d"height"d} _splitKeySizeFactor;
{CGSize="width"d"height"d} _keyboardSize;
d _leftSideWidestRow;
d _rightSideWidestRow;
q _keyboardType;
@"UIKeyboardSliceSet" _sliceSet;
@"UIKeyboardTransitionSlice" _leftSlice;
@"UIKeyboardTransitionSlice" _rightSlice;
```

## Instance methods

```
-[UIKBSplitKeyplaneGenerator init];
-[UIKBSplitKeyplaneGenerator keysOrderedByPosition];
-[UIKBSplitKeyplaneGenerator addKey:withShape:forRow:attribs:left:force:isDefaultWidth:];
-[UIKBSplitKeyplaneGenerator addSliceStart:end:startToken:endToken:left:normalization:isDefaultWidth:row:];
-[UIKBSplitKeyplaneGenerator alignSpaceKeyEdges];
-[UIKBSplitKeyplaneGenerator commitUncommittedSlices];
-[UIKBSplitKeyplaneGenerator finalizeSplitKeyplane];
-[UIKBSplitKeyplaneGenerator generateRivenKeyplaneFromKeyplane:forKeyboard:];
-[UIKBSplitKeyplaneGenerator hintsForRow:];
-[UIKBSplitKeyplaneGenerator initializeGeneratorForKeyplane:name:];
-[UIKBSplitKeyplaneGenerator organizeKeyplaneIntoRows];
-[UIKBSplitKeyplaneGenerator splitRow:];
-[UIKBSplitKeyplaneGenerator splitSpaceKey:leftSpace:left:right:];
```
