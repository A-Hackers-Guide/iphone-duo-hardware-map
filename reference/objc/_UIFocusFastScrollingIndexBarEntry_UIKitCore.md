# `_UIFocusFastScrollingIndexBarEntry`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 4 properties, 8 instance methods, 3 class methods

## Instance variables

```
B _isPlaceholder;
B _hasCachedContentOffset;
{CGPoint="x"d"y"d} _cachedContentOffset;
@? _contentOffsetGenerator;
@"NSString" _title;
@"NSIndexPath" _targetFocusedIndexPath;
```

## Properties

```
@property (T@"NSString",R,C,N,V_title) title;
@property (T{CGPoint=dd},R,N) contentOffset;
@property (TB,R,N,GisPlaceholder) placeholder;
@property (T@"NSIndexPath",C,N,V_targetFocusedIndexPath) targetFocusedIndexPath;
```

## Class methods

```
+[_UIFocusFastScrollingIndexBarEntry entryWithTitle:contentOffset:];
+[_UIFocusFastScrollingIndexBarEntry entryWithTitle:generator:];
+[_UIFocusFastScrollingIndexBarEntry placeholderEntryWithEntryBefore:after:];
```

## Instance methods

```
-[_UIFocusFastScrollingIndexBarEntry isPlaceholder];
-[_UIFocusFastScrollingIndexBarEntry contentOffset];
-[_UIFocusFastScrollingIndexBarEntry title];
-[_UIFocusFastScrollingIndexBarEntry description];
-[_UIFocusFastScrollingIndexBarEntry initWithTitle:contentOffset:];
-[_UIFocusFastScrollingIndexBarEntry initWithTitle:generator:];
-[_UIFocusFastScrollingIndexBarEntry setTargetFocusedIndexPath:];
-[_UIFocusFastScrollingIndexBarEntry targetFocusedIndexPath];
```
