# `_UILibArchiveAppleDoublePathSet`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSMutableSet" _confirmAppleDoublePaths;
@"NSMutableSet" _pathsWithDotUnderscorePrefixedFilenames;
```

## Class methods

```
+[_UILibArchiveAppleDoublePathSet isPossibleAppleDoubleByApplyingMatchingHeuristicToItem:];
```

## Instance methods

```
-[_UILibArchiveAppleDoublePathSet init];
-[_UILibArchiveAppleDoublePathSet confirmExactAppleDoubleFilesAppearingAfterRealFilesByPrescanningArchivePath:];
-[_UILibArchiveAppleDoublePathSet confirmExactAppleDoubleFilesForItem:];
-[_UILibArchiveAppleDoublePathSet isConfirmedExactAppleDoubleItem:];
-[_UILibArchiveAppleDoublePathSet pathToRealFileIfConfirmedAppleDoubleItem:];
```
