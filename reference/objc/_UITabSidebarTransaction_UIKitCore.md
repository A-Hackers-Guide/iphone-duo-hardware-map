# `_UITabSidebarTransaction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _committed;
@"UITabBarControllerSidebar" _sidebar;
@"NSMutableDictionary" _tabsByIdentifier;
@"NSMutableSet" _tabsBecomingVisible;
@"NSMutableSet" _tabsBecomingHidden;
@"NSMutableDictionary" _updatedDisplayOrderForGroup;
```

## Properties

```
@property (T@"UITabBarControllerSidebar",R,W,N,V_sidebar) sidebar;
@property (T@"NSMutableDictionary",R,N,V_tabsByIdentifier) tabsByIdentifier;
@property (TB,N,GisCommitted,V_committed) committed;
@property (T@"NSMutableSet",&,N,V_tabsBecomingVisible) tabsBecomingVisible;
@property (T@"NSMutableSet",&,N,V_tabsBecomingHidden) tabsBecomingHidden;
@property (T@"NSMutableDictionary",&,N,V_updatedDisplayOrderForGroup) updatedDisplayOrderForGroup;
```

## Instance methods

```
-[_UITabSidebarTransaction sidebar];
-[_UITabSidebarTransaction isTabHidden:];
-[_UITabSidebarTransaction setCommitted:];
-[_UITabSidebarTransaction commit];
-[_UITabSidebarTransaction isCommitted];
-[_UITabSidebarTransaction _commit];
-[_UITabSidebarTransaction setUpdatedDisplayOrderForGroup:];
-[_UITabSidebarTransaction _ancestorIdentifierForDescendant:parent:];
-[_UITabSidebarTransaction _mutableDisplayOrderForGroupIdentifier:];
-[_UITabSidebarTransaction _resetDisplayOrderForGroup:];
-[_UITabSidebarTransaction currentDisplayOrderForGroupWithIdentifier:];
-[_UITabSidebarTransaction initWithTabs:sidebar:];
-[_UITabSidebarTransaction replaceTab:forIdentifier:];
-[_UITabSidebarTransaction resetCustomizationForTabs:];
-[_UITabSidebarTransaction setTabsBecomingHidden:];
-[_UITabSidebarTransaction setTabsBecomingVisible:];
-[_UITabSidebarTransaction tabsBecomingHidden];
-[_UITabSidebarTransaction tabsBecomingVisible];
-[_UITabSidebarTransaction tabsByIdentifier];
-[_UITabSidebarTransaction updateTab:toHidden:];
-[_UITabSidebarTransaction updateTabs:];
-[_UITabSidebarTransaction updateUsingTransaction:];
-[_UITabSidebarTransaction updatedDisplayOrderForGroup];
```
