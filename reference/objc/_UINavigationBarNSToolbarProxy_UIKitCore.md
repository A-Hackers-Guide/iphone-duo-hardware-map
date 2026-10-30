# `_UINavigationBarNSToolbarProxy`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 10 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"NSString" _title;
@"NSString" _subtitle;
B _isTitleHiddenByCurrentAppearance;
@"NSURL" _representedURL;
@? _representedDragItemsProvider;
@"NSMutableArray" _registeredParticipants;
{?="needsUpdate"b1} _flags;
B _bridgingDisabledForExplicitNSToolbar;
@"UITitlebar" _owningTitlebar;
@"<_UINavigationBarNSToolbarProxyTabBarItemProviding>" _tabBarProvider;
@"_UINavigationBarPalette" _bottomPalette;
```

## Properties

```
@property (TB,N,V_bridgingDisabledForExplicitNSToolbar) bridgingDisabledForExplicitNSToolbar;
@property (T@"UITitlebar",R,W,N,V_owningTitlebar) owningTitlebar;
@property (T@"NSToolbar",R,N) toolbar;
@property (T@"NSString",R,C,N) title;
@property (T@"NSString",R,C,N) subtitle;
@property (TB,R,N) isTitleHiddenByCurrentAppearance;
@property (T@"NSURL",R,N) representedURL;
@property (T@"<_UINavigationBarNSToolbarProxyTabBarItemProviding>",W,N,V_tabBarProvider) tabBarProvider;
@property (T@?,R,C,N) representedDragItemsProvider;
@property (T@"_UINavigationBarPalette",R,N,V_bottomPalette) bottomPalette;
```

## Class methods

```
+[_UINavigationBarNSToolbarProxy _supportsNSToolbarNavigationHosting];
```

## Instance methods

```
-[_UINavigationBarNSToolbarProxy toolbar];
-[_UINavigationBarNSToolbarProxy subtitle];
-[_UINavigationBarNSToolbarProxy dealloc];
-[_UINavigationBarNSToolbarProxy bottomPalette];
-[_UINavigationBarNSToolbarProxy title];
-[_UINavigationBarNSToolbarProxy description];
-[_UINavigationBarNSToolbarProxy _updateIfNecessary];
-[_UINavigationBarNSToolbarProxy bridgingDisabledForExplicitNSToolbar];
-[_UINavigationBarNSToolbarProxy didSetNewToolbar];
-[_UINavigationBarNSToolbarProxy initWithTitlebar:];
-[_UINavigationBarNSToolbarProxy isTitleHiddenByCurrentAppearance];
-[_UINavigationBarNSToolbarProxy owningTitlebar];
-[_UINavigationBarNSToolbarProxy registerToolbarParticipant:];
-[_UINavigationBarNSToolbarProxy representedDragItemsProvider];
-[_UINavigationBarNSToolbarProxy representedURL];
-[_UINavigationBarNSToolbarProxy setBridgingDisabledForExplicitNSToolbar:];
-[_UINavigationBarNSToolbarProxy setTabBarProvider:];
-[_UINavigationBarNSToolbarProxy tabBarProvider];
-[_UINavigationBarNSToolbarProxy unregisterAllParticipants];
-[_UINavigationBarNSToolbarProxy unregisterToolbarParticipant:];
-[_UINavigationBarNSToolbarProxy updateBridgedToolbar];
-[_UINavigationBarNSToolbarProxy willSetNewToolbar];
```
