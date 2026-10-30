# `SBMenuBarHelpMenuProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITextFieldDelegate`
- 7 instance variables, 12 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _searchTextFieldUsedOnce;
@"<SBMenuBarHelpMenuProviderDelegate>" _delegate;
@"UIMenu" _searchableMenu;
@"UIContextMenuInteraction" _contextMenuInteraction;
@"SBMenuBarHelpSearchField" _searchFieldContainer;
@"UIMenu" _emptySearchMenuToRestore;
@"UIMenu" _searchTextFieldMenu;
```

## Properties

```
@property (T@"SBMenuBarHelpSearchField",&,N,V_searchFieldContainer) searchFieldContainer;
@property (T@"UIMenu",&,N,V_emptySearchMenuToRestore) emptySearchMenuToRestore;
@property (T@"UIMenu",&,N,V_searchTextFieldMenu) searchTextFieldMenu;
@property (TB,N,V_searchTextFieldUsedOnce) searchTextFieldUsedOnce;
@property (T@"<SBMenuBarHelpMenuProviderDelegate>",W,N,V_delegate) delegate;
@property (T@"UITextField",R,N) searchTextField;
@property (T@"UIMenu",&,N,V_searchableMenu) searchableMenu;
@property (T@"UIContextMenuInteraction",&,N,V_contextMenuInteraction) contextMenuInteraction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBMenuBarHelpMenuProvider searchFieldContainer];
-[SBMenuBarHelpMenuProvider setContextMenuInteraction:];
-[SBMenuBarHelpMenuProvider setDelegate:];
-[SBMenuBarHelpMenuProvider searchTextField];
-[SBMenuBarHelpMenuProvider contextMenuInteraction];
-[SBMenuBarHelpMenuProvider delegate];
-[SBMenuBarHelpMenuProvider setSearchFieldContainer:];
-[SBMenuBarHelpMenuProvider _demoMenuProvider];
-[SBMenuBarHelpMenuProvider _searchTextDidChange:];
-[SBMenuBarHelpMenuProvider emptySearchMenuToRestore];
-[SBMenuBarHelpMenuProvider searchTextFieldMenu];
-[SBMenuBarHelpMenuProvider searchTextFieldUsedOnce];
-[SBMenuBarHelpMenuProvider searchableMenu];
-[SBMenuBarHelpMenuProvider setEmptySearchMenuToRestore:];
-[SBMenuBarHelpMenuProvider setSearchTextFieldMenu:];
-[SBMenuBarHelpMenuProvider setSearchTextFieldUsedOnce:];
-[SBMenuBarHelpMenuProvider setSearchableMenu:];
-[SBMenuBarHelpMenuProvider systemHelpMenusForScene:];
-[SBMenuBarHelpMenuProvider userGuideMenuForBundleId:];
```
