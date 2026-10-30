# `SBAppSwitcherModel`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBRecentAppLayoutsDelegate`
- 4 instance variables, 5 properties, 31 instance methods, 1 class methods

## Instance variables

```
@"SBRecentAppLayouts" _recents;
@ _recentsChangedNotificationObserver;
@"NSArray" _appLayoutsSnapshot;
@"<SBAppSwitcherModelDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBAppSwitcherModelDelegate>",R,W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBAppSwitcherModel appSwitcherHeaderIconImageDescriptorName];
```

## Instance methods

```
-[SBAppSwitcherModel addAppLayout:atIndex:];
-[SBAppSwitcherModel initWithDelegate:];
-[SBAppSwitcherModel remove:];
-[SBAppSwitcherModel dealloc];
-[SBAppSwitcherModel displayItemLayoutAttributesProvider];
-[SBAppSwitcherModel addToFront:];
-[SBAppSwitcherModel delegate];
-[SBAppSwitcherModel removeAppLayouts:];
-[SBAppSwitcherModel recentDisplayItemsForBundleIdentifier:includingHiddenAppLayouts:];
-[SBAppSwitcherModel addAppLayout:afterAppLayout:];
-[SBAppSwitcherModel replaceAppLayout:withAppLayout:];
-[SBAppSwitcherModel hide:];
-[SBAppSwitcherModel recentAppLayouts:shouldAllowMultipleDisplayItemsForApplication:];
-[SBAppSwitcherModel _makeRecentAppLayoutsController];
-[SBAppSwitcherModel _adjustedIndexForVisibleAppLayoutAtIndex:];
-[SBAppSwitcherModel appLayoutContainingDisplayItem:includingHiddenAppLayouts:];
-[SBAppSwitcherModel appLayoutsForBundleIdentifier:includingHiddenAppLayouts:];
-[SBAppSwitcherModel appLayoutsIncludingHiddenAppLayouts:];
-[SBAppSwitcherModel appSwitcherDefaultsForRecentAppLayouts:];
-[SBAppSwitcherModel applicationControllerForRecentAppLayouts:];
-[SBAppSwitcherModel applicationPlaceholderControllerForRecentAppLayouts:];
-[SBAppSwitcherModel clearAppLayoutsSnapshot];
-[SBAppSwitcherModel iconRepositoryForRecentAppLayouts:];
-[SBAppSwitcherModel indexOfDisplayItem:visible:];
-[SBAppSwitcherModel recentAppLayouts:didMoveAppLayoutToFront:];
-[SBAppSwitcherModel recentAppLayouts:didRemoveAppLayoutForFallingOffList:];
-[SBAppSwitcherModel recentAppLayouts:willAddAppLayout:replacingAppLayouts:removingAppLayouts:];
-[SBAppSwitcherModel recentAppLayouts:willReplaceAppLayout:proposedReplacementAppLayout:];
-[SBAppSwitcherModel restoreAppLayoutsSnapshot];
-[SBAppSwitcherModel sceneManagerForRecentAppLayouts:];
-[SBAppSwitcherModel takeAppLayoutsSnapshot];
```
