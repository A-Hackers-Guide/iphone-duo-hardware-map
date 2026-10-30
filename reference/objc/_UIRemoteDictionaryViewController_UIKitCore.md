# `_UIRemoteDictionaryViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewController`
- 3 instance variables, 2 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _availableDictionaries;
@"_UIDictionaryManager" _dictionaryAssetManager;
@"NSMutableDictionary" _downloadingAssets;
```

## Properties

```
@property (T@"_UIDictionaryManager",&,N,V_dictionaryAssetManager) dictionaryAssetManager;
@property (T@"NSMutableDictionary",&,N,V_downloadingAssets) downloadingAssets;
```

## Instance methods

```
-[_UIRemoteDictionaryViewController tableView:shouldHighlightRowAtIndexPath:];
-[_UIRemoteDictionaryViewController tableView:numberOfRowsInSection:];
-[_UIRemoteDictionaryViewController tableView:commitEditingStyle:forRowAtIndexPath:];
-[_UIRemoteDictionaryViewController tableView:cellForRowAtIndexPath:];
-[_UIRemoteDictionaryViewController viewDidLoad];
-[_UIRemoteDictionaryViewController initWithStyle:];
-[_UIRemoteDictionaryViewController _downloadButton];
-[_UIRemoteDictionaryViewController _handleDownloadButton:];
-[_UIRemoteDictionaryViewController _startDownloadForDictionary:];
-[_UIRemoteDictionaryViewController dictionaryAssetManager];
-[_UIRemoteDictionaryViewController downloadingAssets];
-[_UIRemoteDictionaryViewController setDictionaryAssetManager:];
-[_UIRemoteDictionaryViewController setDownloadingAssets:];
-[_UIRemoteDictionaryViewController tableView:canEditRowAtIndexPath:];
```
