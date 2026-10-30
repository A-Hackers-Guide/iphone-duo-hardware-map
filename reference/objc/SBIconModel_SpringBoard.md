# `SBIconModel`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBHIconModel`
- 3 instance variables, 1 properties, 21 instance methods, 8 class methods

## Instance variables

```
B _iconsHaveBeenLoadedOnce;
B _createsIconsForInternalApps;
@"NSOrderedSet" _cachedFlattenedForecastedDesiredIconState;
```

## Properties

```
@property (T@"NSOrderedSet",C,N,V_cachedFlattenedForecastedDesiredIconState) cachedFlattenedForecastedDesiredIconState;
```

## Class methods

```
+[SBIconModel applicationIconClass];
+[SBIconModel bookmarkClass];
+[SBIconModel bookmarkIconClass];
+[SBIconModel currentLocaleDidChangeNotificationName];
+[SBIconModel migratedIdentifierForLeafIdentifier:];
+[SBIconModel osMigrationHomeScreenLayoutItemForIcon:atIconIndex:inList:withIdentifier:gridCellInfo:];
+[SBIconModel osMigrationHomeScreenLayoutItemForLeafItem:withIdentifier:atIconIndex:gridCellInfo:];
+[SBIconModel osMigrationHomeScreenLeafItemForIcon:inList:];
```

## Instance methods

```
-[SBIconModel importOSMigrationHomeScreenLayout:];
-[SBIconModel osMigrationHomeScreenLayoutForRootFolder:];
-[SBIconModel isIconVisible:];
-[SBIconModel clearDesiredIconStateWithOptions:];
-[SBIconModel insertOSMigrationHomeScreenLayoutItem:intoListAtIndex:inFolder:rootFolder:referenceGridSize:subsequentListSlide:];
-[SBIconModel iconForOSMigrationHomeScreenLeafItem:];
-[SBIconModel loadAllIcons];
-[SBIconModel insertOSMigrationHomeScreenLayoutItems:intoListAtIndex:inFolder:rootFolder:referenceGridSize:];
-[SBIconModel shouldAvoidCreatingIconForApplication:];
-[SBIconModel modernizeRootArchive:];
-[SBIconModel bookmarkIconForWebClipIdentifier:];
-[SBIconModel exportFlattenedState:includeMissingIcons:];
-[SBIconModel exportPendingState:includeMissingIcons:];
-[SBIconModel exportedOSMigrationHomeScreenLayout];
-[SBIconModel exportedOSMigrationDefaultHomeScreenLayout];
-[SBIconModel cachedFlattenedForecastedDesiredIconState];
-[SBIconModel applicationIconForBundleIdentifier:];
-[SBIconModel shouldAvoidPlacingIconOnFirstPage:];
-[SBIconModel exportState:];
-[SBIconModel setCachedFlattenedForecastedDesiredIconState:];
-[SBIconModel importState:];
```
